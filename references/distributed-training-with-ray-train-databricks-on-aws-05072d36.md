---
title: Distributed training with Ray Train | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/ray-train-distributed
ingestedAt: "2026-06-18T08:08:11.292Z"
---

This example runs distributed data-parallel fine-tuning with [Ray Train](https://docs.ray.io/en/latest/train/train.html)'s `TorchTrainer` across 8 H100 GPUs on a single node. A bootstrap script starts a Ray cluster on the node, then the Ray Train driver launches one worker per GPU, wraps the model in DDP, and shards the dataset across workers automatically.

It fine-tunes a public model ([Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B)), so it runs as-is without a Hugging Face token.

The workload does the following:

*   Uploads the local project with `code_source: snapshot`.
*   Starts a Ray head with all 8 GPUs, then runs the Ray Train driver.
*   Uses `ray.train.torch.prepare_model` and `prepare_data_loader` to handle DDP wrapping, device placement, and distributed sampling.
*   Logs metrics to MLflow.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   The `air` CLI installed and authenticated. See [Install the AI Runtime CLI](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation).

## Project layout[​](#project-layout "Direct link to Project layout")

Create a directory with the following files.

Text

    ray_train_distributed/├── train.yaml          # air workload config (inline dependencies + Ray bootstrap)└── train_ray.py        # Ray Train TorchTrainer driver + per-worker training

## Step 1: Write the workload YAML[​](#step-1-write-the-workload-yaml "Direct link to Step 1: Write the workload YAML")

`train.yaml` requests a single `GPU_8xH100` node. Dependencies are declared inline under `environment` (with the client image `version`), and the `command` starts a Ray cluster on the node then runs the driver, so the workload does not need a separate dependency file or launcher script:

YAML

    experiment_name: air-ray-train-distributedenvironment:  version: '4'  dependencies:    - ray[default,train]>=2.30    - transformers>=4.45    - datasets>=3.0    - huggingface_hub>=0.34    # The base image ships fsspec 2023.5.0, which is too old for modern    # huggingface_hub and breaks dataset/model downloads. Pin a newer fsspec.    - fsspec>=2024.6.1# 8 H100 on a single node. Ray Train launches one worker per GPU.compute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: .command: |  cd $CODE_SOURCE_PATH  RAY_HEAD_PORT=6379  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}  if [ "${NODE_RANK:-0}" = "0" ]; then    echo "NODE_RANK=0: starting Ray head with $GPUS_PER_NODE GPU(s)..."    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0    python train_ray.py    ray stop  else    echo "NODE_RANK=$NODE_RANK: connecting to Ray head at $MASTER_ADDR:$RAY_HEAD_PORT..."    for i in $(seq 1 12); do      if ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block 2>/dev/null; then        break      fi      echo "Attempt $i failed, retrying in 5s..."      sleep 5    done  fimax_retries: 0timeout_minutes: 90env_variables:  NCCL_SOCKET_IFNAME: eth0

The inline `command` starts a Ray head with all GPUs on the node, runs the driver with `python train_ray.py`, then stops the cluster. It also includes a worker branch that joins the head, so the same command keeps working if you scale the job to multiple nodes.

## Step 2: Define the Ray Train driver[​](#step-2-define-the-ray-train-driver "Direct link to Step 2: Define the Ray Train driver")

`train_ray.py` defines a `train_func` that runs on every worker and a `main` that configures the `TorchTrainer` to use all GPUs in the cluster. `prepare_model` wraps the model in DDP and moves it to the worker's GPU. `prepare_data_loader` adds a distributed sampler:

Python

    def train_func(config: dict):    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)    model.config.use_cache = False    model = prepare_model(model)              # DDP wrap + device placement    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)    loader = prepare_data_loader(loader)      # distributed sampler + GPU transfer    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"])    ...    ray.train.report({"loss": out.loss.item(), "step": step})def main():    ray.init(address="auto")    total_gpus = int(ray.cluster_resources().get("GPU", 0))    trainer = TorchTrainer(        train_func,        train_loop_config={"lr": 2e-5, "batch_size": 4, "max_steps": 100},        scaling_config=ScalingConfig(num_workers=total_gpus, use_gpu=True),    )    trainer.fit()

The complete script is listed in [Full training script](#full-training-script) at the end of this page.

## Step 3: Submit the run[​](#step-3-submit-the-run "Direct link to Step 3: Submit the run")

Bash

    air run -f train.yaml --dry-runair run -f train.yaml --watch

## Step 4: Inspect the run[​](#step-4-inspect-the-run "Direct link to Step 4: Inspect the run")

Bash

    air get run <run-id>air logs <run-id>

The Ray head and the driver both run on node 0, so logs stream from a single node.

## Where results land[​](#where-results-land "Direct link to Where results land")

Metrics reported with `ray.train.report` and logged with MLflow appear in the MLflow experiment named in `experiment_name`, viewable in the workspace MLflow UI.

## Full training script[​](#full-training-script "Direct link to Full training script")

The complete `train_ray.py` for copy-paste:

Python

    #!/usr/bin/env python3"""Distributed data-parallel fine-tuning with Ray Train on a single 8x H100 node.The workload `command` starts a Ray head with 8 GPUs and runs this script. Ray Train'sTorchTrainer launches one worker per GPU (8 total), wraps the model in DDP, shardsthe dataset across workers, and aggregates metrics. Each worker runs `train_func`.Uses a public model (no Hugging Face token required) so the example runs as-is."""import osimport mlflowimport rayimport ray.trainimport torchfrom datasets import load_datasetfrom ray.train import RunConfig, ScalingConfigfrom ray.train.torch import TorchTrainer, prepare_data_loader, prepare_modelfrom torch.utils.data import DataLoaderfrom transformers import AutoModelForCausalLM, AutoTokenizerMODEL_NAME = "Qwen/Qwen2.5-3B"DATASET_NAME = "tatsu-lab/alpaca"MAX_SEQ_LEN = 1024def build_dataset(tokenizer):    raw = load_dataset(DATASET_NAME, split="train[:8000]")    def format_example(row):        prompt = f"### Instruction:\n{row['instruction']}\n\n"        if row.get("input"):            prompt += f"### Input:\n{row['input']}\n\n"        text = f"{prompt}### Response:\n{row['output']}{tokenizer.eos_token}"        out = tokenizer(text, truncation=True, max_length=MAX_SEQ_LEN, padding="max_length")        out["labels"] = out["input_ids"].copy()        return out    return raw.map(format_example, remove_columns=raw.column_names)def train_func(config: dict):    """Runs on every Ray Train worker (one per GPU)."""    rank = ray.train.get_context().get_world_rank()    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)    if tokenizer.pad_token is None:        tokenizer.pad_token = tokenizer.eos_token    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)    model.config.use_cache = False    # prepare_model moves the model to this worker's GPU and wraps it in DDP.    model = prepare_model(model)    dataset = build_dataset(tokenizer).with_format("torch")    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)    # prepare_data_loader injects a DistributedSampler and moves batches to the GPU.    loader = prepare_data_loader(loader)    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"])    # AI Runtime injects MLFLOW_RUN_ID and configures the databricks tracking URI on    # the node, so logging works without DATABRICKS_HOST/TOKEN. Gate on MLFLOW_RUN_ID    # so the script also runs cleanly off-platform (e.g. locally) where it is unset.    use_mlflow = rank == 0 and bool(os.environ.get("MLFLOW_RUN_ID"))    if use_mlflow:        mlflow.start_run(run_id=os.environ.get("MLFLOW_RUN_ID"))        mlflow.log_params({"model": MODEL_NAME, "lr": config["lr"], "batch_size": config["batch_size"]})    model.train()    step = 0    for batch in loader:        out = model(            input_ids=batch["input_ids"],            attention_mask=batch["attention_mask"],            labels=batch["labels"],        )        out.loss.backward()        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)        optimizer.step()        optimizer.zero_grad()        step += 1        ray.train.report({"loss": out.loss.item(), "step": step})        if use_mlflow:            mlflow.log_metric("train_loss", out.loss.item(), step=step)        if step >= config["max_steps"]:            break    if use_mlflow:        mlflow.end_run()def main():    ray.init(address="auto")    total_gpus = int(ray.cluster_resources().get("GPU", 0))    print(f"Ray cluster ready: {total_gpus} GPU(s)", flush=True)    trainer = TorchTrainer(        train_func,        train_loop_config={"lr": 2e-5, "batch_size": 4, "max_steps": 100},        scaling_config=ScalingConfig(num_workers=total_gpus, use_gpu=True),        run_config=RunConfig(storage_path="/tmp/ray_results", name="qwen-sft"),    )    result = trainer.fit()    print(f"Training finished. Final metrics: {result.metrics}", flush=True)    ray.shutdown()if __name__ == "__main__":    main()

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Multi-node LLM fine-tuning with FSDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/multinode-llm-sft)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
