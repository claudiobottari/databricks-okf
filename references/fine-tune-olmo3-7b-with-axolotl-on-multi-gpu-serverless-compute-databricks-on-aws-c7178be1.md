---
title: Fine-tune Olmo3 7B with Axolotl on multi-GPU serverless compute | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-olmo3-7b-lora-axolotl
ingestedAt: "2026-06-18T08:09:01.392Z"
---

This notebook demonstrates how to fine-tune the [Olmo3 7B Instruct model](https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT) using [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) on Databricks serverless GPU compute. Axolotl provides a high-performance framework for LLM post-training with QLoRA (Quantized Low-Rank Adaptation), enabling efficient fine-tuning on multi-GPU infrastructure. The trained model is logged to MLflow and registered in Unity Catalog for deployment.

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires serverless GPU compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**
2.  On the right side, click the environment button
3.  Select **8xH100** as the **Accelerator**
4.  Select **AI v5** as your environment, then click **Apply**

## Install required dependencies[​](#install-required-dependencies "Direct link to Install required dependencies")

Installs Axolotl with Flash Attention support and compatible versions of trl and optimization libraries. The `cut-cross-entropy` package provides memory-efficient loss computation for large language models.

Python

    %pip install --no-build-isolation "axolotl[flash-attn]==0.13.1"%pip install "trl==0.27.1"%pip install "torchao==0.16.0"%pip install "cut-cross-entropy[transformers] @ git+https://github.com/axolotl-ai-cloud/ml-cross-entropy.git@f4b5712"dbutils.library.restartPython()

## Retrieve HuggingFace token[​](#retrieve-huggingface-token "Direct link to Retrieve HuggingFace token")

Retrieves the HuggingFace authentication token from Databricks secrets. This token is required to download the Olmo3 7B base model from the HuggingFace Hub.

Python

    HF_TOKEN = dbutils.secrets.get(scope="sgc-nightly-notebook", key="hf_token")

## Configure training parameters[​](#configure-training-parameters "Direct link to Configure training parameters")

Sets up the Axolotl training configuration based on the [olmo3-7b-qlora.yaml](https://github.com/axolotl-ai-cloud/axolotl/blob/main/examples/olmo3/olmo3-7b-qlora.yaml) example. Key modifications include:

*   MLflow integration for experiment tracking
*   Unity Catalog volume path for checkpoint storage
*   SDPA (Scaled Dot Product Attention) instead of Flash Attention for broader GPU compatibility

### Define Unity Catalog paths[​](#define-unity-catalog-paths "Direct link to Define Unity Catalog paths")

Creates widgets to specify the Unity Catalog location for storing model checkpoints. The output directory combines the catalog, schema, volume, and model name into a fully qualified path.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_volume", "checkpoints")dbutils.widgets.text("model", "openai/gpt-oss-20b")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_VOLUME = dbutils.widgets.get("uc_volume")UC_MODEL_NAME = dbutils.widgets.get("model")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"print(f"OUTPUT_DIR: {OUTPUT_DIR}")

### Disable telemetry[​](#disable-telemetry "Direct link to Disable telemetry")

Disables Axolotl's usage tracking by setting the environment variable.

Python

    import osos.environ['AXOLOTL_DO_NOT_TRACK'] = '1'

### Create Axolotl configuration[​](#create-axolotl-configuration "Direct link to Create Axolotl configuration")

Defines the complete training configuration using Axolotl's `DictDefault` format. This includes model settings (QLoRA with 4-bit quantization), dataset configuration (Alpaca format), LoRA hyperparameters (rank 32, alpha 16), training parameters (1 epoch, batch size 2, gradient accumulation 4), and MLflow integration for experiment tracking.

Python

    from axolotl.cli.config import load_cfgfrom axolotl.utils.dict import DictDefault# Config is based on with some changes to fit GPU types# https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/examples/olmo3/olmo3-7b-qlora.yaml# Axolotl provides full control and transparency over model and training configurationconfig = DictDefault(    base_model="allenai/Olmo-3-7B-Instruct-SFT",    plugins=[        "axolotl.integrations.cut_cross_entropy.CutCrossEntropyPlugin"    ],    load_in_8bit=False,    load_in_4bit=True,    datasets=[        {            "path": "fozziethebeat/alpaca_messages_2k_test",            "type": "chat_template"        }    ],    dataset_prepared_path="last_run_prepared",    val_set_size=0.1,    output_dir=OUTPUT_DIR,    adapter="qlora",    lora_model_dir=None,    sequence_len=2048,    sample_packing=True,    lora_r=32,    lora_alpha=16,    lora_dropout=0.05,    lora_target_linear=True,    lora_target_modules=[        "gate_proj",        "down_proj",        "up_proj",        "q_proj",        "v_proj",        "k_proj",        "o_proj"    ],    wandb_project=None,    wandb_entity=None,    wandb_watch=None,    wandb_name=None,    wandb_log_model=None,    gradient_accumulation_steps=4,    micro_batch_size=2,    num_epochs=1,    optimizer="adamw_bnb_8bit",    lr_scheduler="cosine",    learning_rate=0.0002,    bf16="auto",    tf32=False,    gradient_checkpointing=True,    resume_from_checkpoint=None,    logging_steps=1,    flash_attention=False,    warmup_ratio=0.1,    evals_per_epoch=1,    saves_per_epoch=1,    # Eval dataset is too small    eval_sample_packing=False,    # Write metrics to MLflow    use_mlflow=True,    mlflow_tracking_uri="databricks",    mlflow_run_name="olmo3-7b-qlora-axolotl",    hf_mlflow_log_artifacts=False,    wandb_mode="disabled",    attn_implementation="sdpa",    sdpa_attention=True,    save_first_step=True,    device_map=None,)

### Configure PyTorch CUDA memory allocation[​](#configure-pytorch-cuda-memory-allocation "Direct link to Configure PyTorch CUDA memory allocation")

Optimizes GPU memory management for efficient training on multi-GPU setups.

Python

    from axolotl.utils import set_pytorch_cuda_alloc_confset_pytorch_cuda_alloc_conf()

## Run distributed training on serverless GPU compute[​](#run-distributed-training-on-serverless-gpu-compute "Direct link to Run distributed training on serverless GPU compute")

Uses the `@distributed` decorator from the serverless GPU API to distribute the Axolotl training job across 8 H100 GPUs. The decorator handles multi-GPU orchestration, allowing the training function to run in a distributed environment without manual cluster setup.

Python

    from serverless_gpu.launcher import distributedfrom serverless_gpu.compute import GPUType@distributed(gpus=8, gpu_type=GPUType.H100)def run_train(cfg: DictDefault):    import os    os.environ['HF_TOKEN'] = HF_TOKEN    from axolotl.common.datasets import load_datasets    # Load, parse and tokenize the datasets to be formatted with qwen3 chat template    # Drop long samples from the dataset that overflow the max sequence length    # validates the configuration    cfg = load_cfg(cfg)    dataset_meta = load_datasets(cfg=cfg)    from axolotl.train import train    # just train the first 16 steps for demo.    # This is sufficient to align the model as we've used packing to maximize the trainable samples per step.    cfg.max_steps = 16    model, tokenizer, trainer = train(cfg=cfg, dataset_meta=dataset_meta)    import mlflow    mlflow_run_id = None    if mlflow.last_active_run() is not None:        mlflow_run_id = mlflow.last_active_run().info.run_id    return mlflow_run_id

Python

    result = run_train.distributed(config)

### Execute the training job[​](#execute-the-training-job "Direct link to Execute the training job")

Launches the distributed training job. The function loads the dataset, validates the configuration, trains the model for 16 steps, and returns the MLflow run ID for tracking.

Python

    run_id = result[0]print(run_id)

Retrieves the MLflow run ID from the training results for model registration and experiment tracking.

## Register the fine-tuned model to Unity Catalog[​](#register-the-fine-tuned-model-to-unity-catalog "Direct link to Register the fine-tuned model to Unity Catalog")

Loads the trained LoRA adapter, merges it with the base model, and registers the combined model to Unity Catalog via MLflow. This makes the model available for deployment and inference.

**Note:** This step requires H100 GPU compute to load the model checkpoint. Running on smaller GPUs may result in CUDA out-of-memory errors.

Python

    from transformers import AutoTokenizer, AutoModelForCausalLM, pipelinefrom peft import PeftModelimport mlflowimport torchHF_MODEL_NAME = "allenai/Olmo-3-7B-Instruct-SFT"torch.cuda.empty_cache()# Load the trained model for registrationprint("Loading LoRA model for registration...")# For LoRA models, we need both base model and adapterbase_model = AutoModelForCausalLM.from_pretrained(    HF_MODEL_NAME,    trust_remote_code=True)# Load tokenizertokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)adapter_dir = OUTPUT_DIRpeft_model = PeftModel.from_pretrained(base_model, adapter_dir)# Merge LoRA into base and drop PEFT wrappersmerged_model = peft_model.merge_and_unload()merged_model.generation_config.temperature = Nonemerged_model.generation_config.top_p = None# Create Unity Catalog model namefull_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"print(f"Registering model as: {full_model_name}")text_gen_pipe = pipeline(    task="text-generation",    model=merged_model,    tokenizer=tokenizer,)input_example = ["Hello, world!"]with mlflow.start_run(run_id=run_id):    model_info = mlflow.transformers.log_model(        transformers_model=text_gen_pipe,        name="model",        input_example=input_example,        registered_model_name=full_model_name,    )print(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")print(f"✓ MLflow model URI: {model_info.model_uri}")print(f"✓ Model version: {model_info.registered_model_version}")print(f"\n📦 Model Registration Complete!")print(f"Unity Catalog Path: {full_model_name}")print(f"Optimization: Cut Cross Entropy + QLoRA")

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Fine-tune Olmo3 7B with Axolotl on multi-GPU serverless compute
