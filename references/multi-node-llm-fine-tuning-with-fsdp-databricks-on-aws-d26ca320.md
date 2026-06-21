---
title: Multi-node LLM fine-tuning with FSDP | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/multinode-llm-sft
ingestedAt: "2026-06-18T08:08:09.111Z"
---

This example runs supervised fine-tuning (SFT) of [Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) across 16 H100 GPUs spread over 2 nodes using `torchrun` and PyTorch [Fully Sharded Data Parallel (FSDP)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html). FSDP shards model parameters, gradients, and optimizer states across all 16 ranks so the 8B-parameter model and its optimizer state fit comfortably in GPU memory.

The workload does the following:

*   Uploads the local project with `code_source: snapshot`.
*   Launches one process per GPU with `torchrun`, using the rendezvous environment variables that AI Runtime sets on each node.
*   Reads a gated model from Hugging Face using a Databricks secret.
*   Logs metrics to MLflow and writes the consolidated checkpoint to a Unity Catalog volume.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   The `air` CLI installed and authenticated. See [Install the AI Runtime CLI](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation).
*   A Unity Catalog volume you can write to for the output checkpoint.
*   Access to the gated model on Hugging Face, plus an access token stored as a Databricks secret (see below).

### Get access to the model on Hugging Face[​](#get-access-to-the-model-on-hugging-face "Direct link to Get access to the model on Hugging Face")

Llama-3.1-8B is a gated model, so you must request access and provide a token to download it:

1.  Open the model page at [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) and accept the license to request access. Wait until access is granted.
2.  Create a [Hugging Face access token](https://huggingface.co/docs/hub/en/security-tokens) with **read** permission.

### Store the token as a Databricks secret[​](#store-the-token-as-a-databricks-secret "Direct link to Store the token as a Databricks secret")

The workload reads the token from a [Databricks secret](https://docs.databricks.com/aws/en/security/secrets/) instead of hard-coding it. Create a secret scope and add your token:

Bash

    databricks secrets create-scope my_scopedatabricks secrets put-secret my_scope hf_token

`train.yaml` references it as `my_scope/hf_token`. Replace the scope and key with your own.

## Project layout[​](#project-layout "Direct link to Project layout")

Create a directory with the following files.

Text

    multinode_llm_sft/├── train.yaml          # air workload config (inline dependencies + torchrun launcher)└── train.py            # FSDP fine-tuning script

## Step 1: Write the workload YAML[​](#step-1-write-the-workload-yaml "Direct link to Step 1: Write the workload YAML")

`train.yaml` requests 16 GPUs as two `GPU_8xH100` nodes, mounts the Hugging Face token as a secret, and passes hyperparameters to the script through the `parameters` block. Dependencies are declared inline under `environment` (with the client image `version`). The `torch` package ships in the AI Runtime base image, so only the extras are listed:

YAML

    experiment_name: air-multinode-llama-sftenvironment:  version: '4'  dependencies:    - transformers>=4.45    - datasets>=3.0    - huggingface_hub>=0.34    - accelerate>=0.34    # The base image ships fsspec 2023.5.0, which is too old for modern    # huggingface_hub and breaks dataset/model downloads. Pin a newer fsspec.    - fsspec>=2024.6.1# 16 GPUs across 2 nodes (GPU_8xH100 = 8 H100 per node).compute:  num_accelerators: 16  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: .command: |  cd $CODE_SOURCE_PATH  # air sets NUM_NODES, NODE_RANK, LOCAL_WORLD_SIZE, MASTER_ADDR, and MASTER_PORT on each node.  torchrun \    --nnodes="$NUM_NODES" \    --node_rank="$NODE_RANK" \    --nproc_per_node="${LOCAL_WORLD_SIZE:-8}" \    --master_addr="$MASTER_ADDR" \    --master_port="$MASTER_PORT" \    train.py# Pin NCCL control-plane traffic to eth0 so cross-node rendezvous works.env_variables:  NCCL_SOCKET_IFNAME: eth0  HF_HOME: /tmp/hf# Gated model download needs a Hugging Face token. Replace with your own# Databricks secret in the form "scope/key".secrets:  HF_TOKEN: 'my_scope/hf_token'max_retries: 1timeout_minutes: 120# Surfaced to train.py via HYPERPARAMETERS_PATH.parameters:  model_name: meta-llama/Llama-3.1-8B  dataset_name: tatsu-lab/alpaca  max_seq_len: 1024  per_device_batch_size: 4  gradient_accumulation_steps: 2  learning_rate: 0.00002  max_steps: 100  output_dir: /Volumes/main/default/air_checkpoints/llama31-8b-sft

AI Runtime runs `command` once per node and sets the rendezvous environment variables (`NUM_NODES`, `NODE_RANK`, `LOCAL_WORLD_SIZE`, `MASTER_ADDR`, and `MASTER_PORT`) on each node. `torchrun` reads them to launch one process per GPU, so the inline command is the whole launcher. No separate launcher script is needed.

## Step 2: Write the FSDP training script[​](#step-2-write-the-fsdp-training-script "Direct link to Step 2: Write the FSDP training script")

`train.py` initializes the process group, wraps each transformer block in FSDP, trains on a tokenized instruction dataset, and saves a consolidated checkpoint from rank 0. The key pieces:

Python

    # Shard each transformer block independently so no single GPU holds the full model.auto_wrap_policy = functools.partial(    transformer_auto_wrap_policy, transformer_layer_cls={LlamaDecoderLayer})model = FSDP(    model,    auto_wrap_policy=auto_wrap_policy,    sharding_strategy=ShardingStrategy.FULL_SHARD,    mixed_precision=MixedPrecision(        param_dtype=torch.bfloat16,        reduce_dtype=torch.bfloat16,        buffer_dtype=torch.bfloat16,    ),    device_id=local_rank,    use_orig_params=True,)

Rank 0 gathers the full state dict (offloaded to CPU) and writes it to the Unity Catalog volume:

Python

    save_policy = FullStateDictConfig(offload_to_cpu=True, rank0_only=True)with FSDP.state_dict_type(model, StateDictType.FULL_STATE_DICT, save_policy):    cpu_state = model.state_dict()if rank == 0:    model.module.save_pretrained(output_dir, state_dict=cpu_state)    tokenizer.save_pretrained(output_dir)

The complete script is listed in [Full training script](#full-training-script) at the end of this page.

## Step 3: Submit the run[​](#step-3-submit-the-run "Direct link to Step 3: Submit the run")

Validate the config, then submit and watch logs:

Bash

    air run -f train.yaml --dry-runair run -f train.yaml --watch

## Step 4: Inspect the run[​](#step-4-inspect-the-run "Direct link to Step 4: Inspect the run")

Distributed runs span multiple nodes. Use `--node` to read logs from a specific node:

Bash

    air get run <run-id>air logs <run-id> --node 0air logs <run-id> --node 1

## Where results land[​](#where-results-land "Direct link to Where results land")

*   **Metrics and parameters**: Logged to the MLflow experiment named in `experiment_name`. View them in the workspace MLflow UI.
*   **Fine-tuned checkpoint**: Written to the Unity Catalog volume in `parameters.output_dir`.

## Full training script[​](#full-training-script "Direct link to Full training script")

The complete `train.py` for copy-paste:

Python

    #!/usr/bin/env python3"""Multi-node FSDP supervised fine-tuning of Llama-3.1-8B.Launched via ``torchrun`` from the workload YAML ``command`` across 2 nodes x 8 H100 (16 ranks). Each rankowns one GPU. The model is sharded with PyTorch FSDP (full shard + bf16), trained onan instruction dataset, and the consolidated checkpoint is written to a Unity CatalogVolume by rank 0. Metrics are logged to MLflow.Hyperparameters are read from the YAML block passed by ``air`` via HYPERPARAMETERS_PATH."""import functoolsimport osimport mlflowimport torchimport torch.distributed as distimport yamlfrom datasets import load_datasetfrom torch.distributed.fsdp import FullStateDictConfig, FullyShardedDataParallel as FSDPfrom torch.distributed.fsdp import MixedPrecision, ShardingStrategy, StateDictTypefrom torch.distributed.fsdp.wrap import transformer_auto_wrap_policyfrom torch.utils.data import DataLoader, DistributedSamplerfrom transformers import AutoModelForCausalLM, AutoTokenizerfrom transformers.models.llama.modeling_llama import LlamaDecoderLayerdef load_params() -> dict:    """Read the hyperparameters block that `air` materializes from the YAML `parameters:`."""    path = os.environ.get("HYPERPARAMETERS_PATH")    if path and os.path.exists(path):        with open(path) as f:            return yaml.safe_load(f) or {}    return {}def build_dataset(tokenizer, dataset_name: str, max_seq_len: int):    """Tokenize an instruction dataset into fixed-length causal-LM examples."""    raw = load_dataset(dataset_name, split="train")    def format_example(row):        instruction = row.get("instruction", "")        context = row.get("input", "")        response = row.get("output", "")        prompt = f"### Instruction:\n{instruction}\n\n"        if context:            prompt += f"### Input:\n{context}\n\n"        text = f"{prompt}### Response:\n{response}{tokenizer.eos_token}"        out = tokenizer(text, truncation=True, max_length=max_seq_len, padding="max_length")        out["labels"] = out["input_ids"].copy()        return out    cols = raw.column_names    tokenized = raw.map(format_example, remove_columns=cols)    # Emit torch tensors so the default DataLoader collate stacks them into [B, L] batches.    tokenized.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])    return tokenizeddef main():    rank = int(os.environ["RANK"])    local_rank = int(os.environ["LOCAL_RANK"])    world_size = int(os.environ["WORLD_SIZE"])    dist.init_process_group(backend="nccl")    torch.cuda.set_device(local_rank)    device = torch.device(f"cuda:{local_rank}")    p = load_params()    model_name = p.get("model_name", "meta-llama/Llama-3.1-8B")    dataset_name = p.get("dataset_name", "tatsu-lab/alpaca")    max_seq_len = int(p.get("max_seq_len", 1024))    batch_size = int(p.get("per_device_batch_size", 4))    grad_accum = int(p.get("gradient_accumulation_steps", 2))    lr = float(p.get("learning_rate", 2e-5))    max_steps = int(p.get("max_steps", 100))    output_dir = p.get("output_dir", "/tmp/llama-sft")    if rank == 0:        print(f"World size={world_size} | model={model_name} | dataset={dataset_name}", flush=True)    # --- Model & data --------------------------------------------------------    tokenizer = AutoTokenizer.from_pretrained(model_name)    if tokenizer.pad_token is None:        tokenizer.pad_token = tokenizer.eos_token    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)    model.config.use_cache = False  # incompatible with gradient checkpointing / FSDP training    model.gradient_checkpointing_enable()    # Shard each transformer block independently so no single GPU holds the full model.    auto_wrap_policy = functools.partial(transformer_auto_wrap_policy, transformer_layer_cls={LlamaDecoderLayer})    model = FSDP(        model,        auto_wrap_policy=auto_wrap_policy,        sharding_strategy=ShardingStrategy.FULL_SHARD,        mixed_precision=MixedPrecision(            param_dtype=torch.bfloat16,            reduce_dtype=torch.bfloat16,            buffer_dtype=torch.bfloat16,        ),        device_id=local_rank,        use_orig_params=True,    )    dataset = build_dataset(tokenizer, dataset_name, max_seq_len)    sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank, shuffle=True)    loader = DataLoader(dataset, batch_size=batch_size, sampler=sampler, drop_last=True)    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)    # --- MLflow (rank 0 only) ------------------------------------------------    # AI Runtime injects MLFLOW_RUN_ID and configures the databricks tracking URI on    # the node, so logging works without DATABRICKS_HOST/TOKEN. Gate on MLFLOW_RUN_ID    # so the script also runs cleanly off-platform (e.g. locally) where it is unset.    use_mlflow = rank == 0 and bool(os.environ.get("MLFLOW_RUN_ID"))    if use_mlflow:        mlflow.start_run(run_id=os.environ.get("MLFLOW_RUN_ID"))        mlflow.log_params({"model_name": model_name, "lr": lr, "batch_size": batch_size, "world_size": world_size})    # --- Training loop -------------------------------------------------------    model.train()    sampler.set_epoch(0)    step = 0    optimizer.zero_grad()    for micro_step, batch in enumerate(loader):        input_ids = batch["input_ids"].to(device)        attention_mask = batch["attention_mask"].to(device)        labels = batch["labels"].to(device)        out = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)        (out.loss / grad_accum).backward()        if (micro_step + 1) % grad_accum == 0:            model.clip_grad_norm_(1.0)            optimizer.step()            optimizer.zero_grad()            step += 1            if rank == 0:                print(f"step={step}/{max_steps} loss={out.loss.item():.4f}", flush=True)                if use_mlflow:                    mlflow.log_metric("train_loss", out.loss.item(), step=step)            if step >= max_steps:                break    # --- Save consolidated checkpoint to the UC Volume (rank 0) --------------    save_policy = FullStateDictConfig(offload_to_cpu=True, rank0_only=True)    with FSDP.state_dict_type(model, StateDictType.FULL_STATE_DICT, save_policy):        cpu_state = model.state_dict()    if rank == 0:        os.makedirs(output_dir, exist_ok=True)        model.module.save_pretrained(output_dir, state_dict=cpu_state)        tokenizer.save_pretrained(output_dir)        print(f"Saved checkpoint to {output_dir}", flush=True)        if use_mlflow:            mlflow.end_run()    dist.barrier()    dist.destroy_process_group()if __name__ == "__main__":    main()

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Distributed training with Ray Train](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/ray-train-distributed)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
