---
title: Fine-tune Llama 3.1 8B using Mosaic LLM Foundry on Databricks Serverless GPU | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-llama3-8b-llmfoundry
ingestedAt: "2026-06-18T08:08:59.746Z"
---

This notebook demonstrates how to fine-tune a Llama 3.1 8B model using [Mosaic LLM Foundry](https://github.com/mosaicml/llm-foundry) on Databricks Serverless GPU. LLM Foundry is a codebase for training, fine-tuning, evaluating, and deploying large language models with support for distributed training strategies.

The notebook uses:

*   **Mosaic LLM Foundry**: A framework for training and fine-tuning LLMs with built-in support for FSDP, efficient data loading, and MLflow integration
*   **FSDP (Fully Sharded Data Parallel)**: Distributes model parameters, gradients, and optimizer states across GPUs
*   **Databricks Serverless GPU**: Runs distributed training on connected serverless GPU compute
*   **Unity Catalog**: Stores model checkpoints and registers trained models
*   **MLflow**: Tracks experiments and logs training metrics

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires serverless GPU compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**
2.  Open the **Environment** side panel on the right side of the notebook
3.  Set **Accelerator** to **8xH100**
4.  Select the **Standard** base environment and set **Environment version** to **5**, which contains the libraries needed to run this example
5.  Select **Apply** and click **Confirm** to apply this environment to your notebook

## Install required libraries[​](#install-required-libraries "Direct link to Install required libraries")

Install Mosaic LLM Foundry and its dependencies for distributed training. The prebuilt `flash-attn` wheel is installed **first** so that `pip` reuses it instead of compiling flash-attention from source (which is slow) when it resolves `llm-foundry[gpu]`:

*   `flash-attn`: Optimized attention implementation, installed from a prebuilt wheel
*   `llm-foundry`: Core framework for LLM training and fine-tuning
*   `hf_transfer`: Faster model downloads from Hugging Face
*   `yamlmagic`: Enables YAML configuration in notebook cells

Python

    %pip install --no-deps "https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu12torch2.6cxx11abiFALSE-cp312-cp312-linux_x86_64.whl"%pip install llm-foundry[gpu]==0.20.0%pip install hf_transfer%pip install git+https://github.com/josejg/yamlmagic.git

## Restart the Python environment[​](#restart-the-python-environment "Direct link to Restart the Python environment")

Restart the Python kernel to ensure the newly installed packages are available.

Python

    dbutils.library.restartPython()

## Configure Unity Catalog paths for model storage[​](#configure-unity-catalog-paths-for-model-storage "Direct link to Configure Unity Catalog paths for model storage")

Set up Unity Catalog locations for storing model checkpoints and registering the trained model. The configuration uses query parameters that can be customized without editing the code.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "llama3_1-8b")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")MLFLOW_EXPERIMENT_NAME = '/Workspace/Shared/llm-foundry-sgc' # TODO: update this nameprint(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"EXPERIMENT_NAME: {MLFLOW_EXPERIMENT_NAME}")# Model selection - Choose based on your compute constraintsOUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}" # Save checkpoint to UC Volumeprint(f"OUTPUT_DIR: {OUTPUT_DIR}")

## Define training configuration using YAML[​](#define-training-configuration-using-yaml "Direct link to Define training configuration using YAML")

Load the fine-tuning configuration from YAML format. The configuration specifies:

*   Model architecture and pretrained weights (Llama 3.1 8B)
*   FSDP settings for distributed training
*   Training hyperparameters (learning rate, batch size, optimizer)
*   Dataset configuration (mosaicml/dolly\_hhrlhf)
*   MLflow logging and model checkpointing
*   Callbacks for monitoring and optimization

Python

    %%yaml configseed: 17model:  name: hf_causal_lm  pretrained: true  init_device: mixed  use_auth_token: true  use_flash_attention_2: true  pretrained_model_name_or_path: meta-llama/Llama-3.1-8Bloggers:  mlflow:    resume: true    tracking_uri: databricks    rename_metrics:      time/token: time/num_tokens      lr-DecoupledLionW/group0: learning_rate    log_system_metrics: true    experiment_name: "mlflow_experiment_name"    run_name: llama3_8b-finetune    model_registry_uri: databricks-uc    model_registry_prefix: main.linyuancallbacks:  lr_monitor: {}  run_timeout:    timeout: 7200  scheduled_gc:    batch_interval: 1000  speed_monitor:    window_size: 10  memory_monitor: {}  runtime_estimator: {}  hf_checkpointer:    save_folder: "dbfs:/Volumes/main/sgc/checkpoints/llama3_1-8b-hf"    save_interval: "1ep"    precision: "bfloat16"    overwrite: true    mlflow_registered_model_name: "main.sgc.llama3_1_8b_full_ft"    mlflow_logging_config:      task: "llm/v1/completions"      metadata:        pretrained_model_name: "meta-llama/Llama-3.1-8B-Instruct"optimizer:  lr: 5.0e-07  name: decoupled_lionw  betas:  - 0.9  - 0.95  weight_decay: 0precision: amp_bf16scheduler:  name: linear_decay_with_warmup  alpha_f: 0  t_warmup: 10batokenizer:  name: meta-llama/Llama-3.1-8B  kwargs:    model_max_length: 1024algorithms:  gradient_clipping:    clipping_type: norm    clipping_threshold: 1autoresume: falselog_config: falsefsdp_config:  verbose: false  mixed_precision: PURE  state_dict_type: sharded  limit_all_gathers: true  sharding_strategy: FULL_SHARD  activation_cpu_offload: false  activation_checkpointing: true  activation_checkpointing_reentrant: falsemax_seq_len: 1024save_folder: "output_folder"dist_timeout: 600max_duration: 20baprogress_bar: falsetrain_loader:  name: finetuning  dataset:    split: test    hf_name: mosaicml/dolly_hhrlhf    shuffle: true    safe_load: true    max_seq_len: 1024    packing_ratio: auto    target_prompts: none    target_responses: all    allow_pad_trimming: false    decoder_only_format: true  timeout: 0  drop_last: false  pin_memory: true  num_workers: 8  prefetch_factor: 2  persistent_workers: trueeval_interval: 1save_interval: 1hlog_to_console: truesave_overwrite: truepython_log_level: debugsave_weights_only: falseconsole_log_interval: 10badevice_eval_batch_size: 1global_train_batch_size: 32device_train_microbatch_size: 1save_num_checkpoints_to_keep: 1

Python

    config["loggers"]["mlflow"]["experiment_name"] = MLFLOW_EXPERIMENT_NAMEconfig["save_folder"] = OUTPUT_DIRconfig["callbacks"]["hf_checkpointer"]["save_folder"] = OUTPUT_DIRconfig["callbacks"]["hf_checkpointer"]["mlflow_registered_model_name"] = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"

## Define the distributed training function[​](#define-the-distributed-training-function "Direct link to Define the distributed training function")

This cell defines the training function that will run on 8 H100 GPUs using the `@distributed` decorator. The function:

*   Configures the Hugging Face token for model access
*   Enables fast model downloads with `hf_transfer`
*   Calls the LLM Foundry `train()` function with the YAML configuration
*   Returns the MLflow run ID for tracking the experiment

The `@distributed` decorator runs the function on the connected serverless GPU compute and handles distributed training orchestration.

Python

    from serverless_gpu import distributedfrom llmfoundry.command_utils.train import trainfrom omegaconf import DictConfigimport mlflowfrom huggingface_hub import constantsHF_TOKEN = dbutils.secrets.get(scope="sgc-nightly-notebook", key="hf_token")@distributed(gpus=8, gpu_type='H100')def run_llm_foundry():    import os    import logging    os.environ["HUGGING_FACE_HUB_TOKEN"] = HF_TOKEN    constants.HF_HUB_ENABLE_HF_TRANSFER = True    train(DictConfig(config))    logging.info("\n✓ Training completed successfully!")    mlflow_run_id = None    if mlflow.last_active_run() is not None:        mlflow_run_id = mlflow.last_active_run().info.run_id    return mlflow_run_id

## Run the distributed training job[​](#run-the-distributed-training-job "Direct link to Run the distributed training job")

Execute the training function on 8 H100 GPUs. The function returns the MLflow run ID, which can be used to track metrics, view logs, and access the trained model in the MLflow UI.

Python

    mlflow_run_id = run_llm_foundry.distributed()[0]print(mlflow_run_id)

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Mosaic LLM Foundry documentation](https://github.com/mosaicml/llm-foundry)
*   [Unity Catalog model registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Fine-tune Llama 3.1 8B using Mosaic LLM Foundry on Databricks Serverless GPU
