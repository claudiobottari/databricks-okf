---
title: Distributed fine-tuning of Qwen2-0.5B with LoRA | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-distributed-finetune-qwen2-0.5b
ingestedAt: "2026-06-18T08:08:46.321Z"
---

This notebook demonstrates how to efficiently fine-tune the Qwen2-0.5B large language model using parameter-efficient techniques on Serverless GPU Compute. You'll learn how to:

*   Apply **LoRA (Low-Rank Adaptation)** to reduce trainable parameters by ~99% while maintaining model quality
*   Use **Liger Kernels** for memory-efficient training with optimized Triton kernels
*   Leverage **TRL (Transformer Reinforcement Learning)** for supervised fine-tuning
*   Register the fine-tuned model in Unity Catalog for governance and deployment

**Key concepts:**

*   [LoRA](https://arxiv.org/abs/2106.09685): A technique that freezes the base model and trains small adapter layers, dramatically reducing memory requirements and training time
*   [Liger Kernels](https://github.com/linkedin/Liger-Kernel): GPU-optimized kernels that reduce memory usage by up to 80% through fused operations
*   [TRL](https://huggingface.co/docs/trl): A library for training language models with reinforcement learning and supervised fine-tuning
*   [Serverless GPU Compute](https://docs.databricks.com/aws/en/compute/gpu): Databricks managed compute that automatically scales GPU resources

## LoRA vs full fine-tuning decision matrix[​](#lora-vs-full-fine-tuning-decision-matrix "Direct link to LoRA vs full fine-tuning decision matrix")

[LoRA (Low-Rank Adaptation)](https://arxiv.org/abs/2106.09685) freezes the base model and trains only small adapter layers, reducing trainable parameters by ~99%. This makes training faster and more memory-efficient.

## Liger Kernel benefits[​](#liger-kernel-benefits "Direct link to Liger Kernel benefits")

[Liger Kernels](https://github.com/linkedin/Liger-Kernel) are GPU-optimized operations that fuse multiple steps into single kernels, reducing memory transfers and improving efficiency. The [technical paper](https://arxiv.org/pdf/2410.10989) provides detailed benchmarks showing significant performance improvements.

*   **Fused operations**: Combines operations (e.g., linear + loss) to reduce memory overhead by up to 80%
*   **Triton kernels**: Custom GPU kernels optimized for transformer operations (RMSNorm, RoPE, SwiGLU, CrossEntropy)
*   **Memory efficiency**: Allows larger batch sizes or models that wouldn't otherwise fit in GPU memory
*   **Single GPU optimization**: Particularly effective for A10/A100 single-GPU training scenarios

This notebook uses the [TRL library](https://huggingface.co/docs/trl) to simplify the training configuration and automatically apply these optimizations.

## Connect to Serverless GPU Compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to Serverless GPU Compute")

This notebook requires Serverless GPU Compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**
2.  On the right side, click the environment button
3.  Select **8xH100** as the **Accelerator**
4.  Choose **AI v5** from the base environment
5.  Click **Apply**

The training function will automatically provision 8 H100 GPUs for distributed training.

## Install required libraries[​](#install-required-libraries "Direct link to Install required libraries")

The Databricks AI v5 environment already includes most of the libraries required for this example (such as `trl`, `peft`, `transformers`, `hf_transfer`, and `mlflow`). The next cell installs `liger-kernel`, which is not yet part of the environment.

The `%restart_python` command restarts the Python interpreter to ensure the newly installed package is properly loaded.

Python

    %pip install liger-kernel==0.8.0%restart_python

## Configuration setup[​](#configuration-setup "Direct link to Configuration setup")

### Unity Catalog integration[​](#unity-catalog-integration "Direct link to Unity Catalog integration")

The next cell configures where your fine-tuned model will be stored and registered:

*   **Catalog & Schema**: Organize models within your Unity Catalog namespace (default: `main.default`)
*   **Model Name**: The registered model name in Unity Catalog for governance and deployment
*   **Volume**: Unity Catalog volume for storing model checkpoints during training

These widgets allow you to customize the storage location without editing code. The model will be registered as `{catalog}.{schema}.{model_name}` for easy access and version control.

### Training hyperparameters[​](#training-hyperparameters "Direct link to Training hyperparameters")

The cell also defines key training parameters:

*   **Model & Dataset**: Qwen2-0.5B with Capybara conversational dataset
*   **Batch Size (8)**: Number of examples per GPU per training step
*   **Gradient Accumulation (4)**: Accumulates gradients over 4 batches for effective batch size of 32
*   **Learning Rate (1e-4)**: Conservative rate, automatically scaled 10x higher for LoRA training
*   **Epochs (1)**: Single pass through the dataset to prevent overfitting
*   **Logging & Checkpointing**: Saves progress every 100 steps, logs metrics every 25 steps

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "qwen2_liger_lora_assistant")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")# MLflow and Unity Catalog configuration# Model selection - Choose based on your compute constraintsMODEL_NAME = "Qwen/Qwen2-0.5B"DATASET_NAME = "trl-lib/Capybara"OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/qwen2-0.5b-lora"# Training hyperparametersBATCH_SIZE = 8GRADIENT_ACCUMULATION_STEPS = 4LEARNING_RATE = 1e-4NUM_EPOCHS = 1EVAL_STEPS = 100LOGGING_STEPS = 25SAVE_STEPS = 100

## LoRA configuration[​](#lora-configuration "Direct link to LoRA configuration")

The next cell configures LoRA (Low-Rank Adaptation) parameters that control how the model is fine-tuned. LoRA freezes the base model weights and trains only small adapter matrices, dramatically reducing memory requirements.

### Parameter selection[​](#parameter-selection "Direct link to Parameter selection")

*   **Rank (r=8)**: Provides good balance of performance vs parameters
*   **Alpha (32)**: Scaling factor, typically 2-4x the rank
*   **Dropout (0.1)**: Regularization to prevent overfitting

### Target modules for Qwen2[​](#target-modules-for-qwen2 "Direct link to Target modules for Qwen2")

This example targets all key transformation layers:

*   **Attention**: `q_proj`, `k_proj`, `v_proj`, `o_proj`
*   **MLP**: `gate_proj`, `up_proj`, `down_proj`

Python

    LORA_R = 8LORA_ALPHA = 32LORA_DROPOUT = 0.1LORA_TARGET_MODULES = [    "q_proj", "k_proj", "v_proj", "o_proj",    "gate_proj", "up_proj", "down_proj"]

## Define the training function[​](#define-the-training-function "Direct link to Define the training function")

The next cell creates the distributed training function that will run across multiple GPUs. Here's what it does:

### Distributed training setup[​](#distributed-training-setup "Direct link to Distributed training setup")

The `@distributed` decorator configures Serverless GPU Compute:

*   **8 GPUs**: Distributes training across 8 H100 GPUs for faster training
*   **Automatic orchestration**: Handles GPU provisioning, data distribution, and synchronization

### Training workflow[​](#training-workflow "Direct link to Training workflow")

The function executes these steps:

1.  **Load dataset**: Downloads and prepares the Capybara conversational dataset
2.  **Initialize model**: Loads Qwen2-0.5B and tokenizer with chat formatting
3.  **Apply LoRA**: Attaches adapter layers to reduce trainable parameters by ~99%
4.  **Configure training**: Sets up batch size, learning rate, and Liger kernel optimizations
5.  **Train model**: Runs the training loop with automatic checkpointing and logging
6.  **Save artifacts**: Stores LoRA adapters and tokenizer to Unity Catalog volume
7.  **Return MLflow run ID**: Provides the run ID for model registration

### Key optimizations enabled[​](#key-optimizations-enabled "Direct link to Key optimizations enabled")

*   **Liger Kernels**: Fused GPU operations reduce memory usage by up to 80%
*   **Mixed precision (FP16)**: Faster computation with lower memory footprint
*   **Gradient checkpointing**: Trades computation for memory to fit larger batches
*   **Gradient accumulation**: Simulates larger batch sizes for stable training

Python

    from serverless_gpu import distributedfrom serverless_gpu import runtime as rt@distributed(gpus=8, gpu_type="H100")def run_train(use_lora=True):    import logging    from datasets import load_dataset    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer    from peft import LoraConfig, TaskType, get_peft_model    from trl import (        SFTConfig,        SFTTrainer,        setup_chat_format    )    import json    import os    import mlflow    dataset = load_dataset(DATASET_NAME)    logging.info(f"✓ Dataset loaded: {dataset}")    if "test" not in dataset:        logging.info("Creating validation split from training data...")        dataset = dataset["train"].train_test_split(test_size=0.1, seed=42)        logging.info("✓ Data split: 90% train, 10% validation")    # model and tokenizer initialization    model = AutoModelForCausalLM.from_pretrained(        MODEL_NAME,        trust_remote_code=True,    )    tokenizer = AutoTokenizer.from_pretrained(        MODEL_NAME,        trust_remote_code=True,        use_fast=True    )    # Chat template formatting for conversational fine-tuning    if tokenizer.chat_template is None:        logging.info("Adding chat template for proper conversation formatting...")        model, tokenizer = setup_chat_format(model, tokenizer, format="chatml")        logging.info("✓ ChatML format applied for structured conversations")    if tokenizer.pad_token is None:        tokenizer.pad_token = tokenizer.eos_token        logging.info("✓ Padding token set to EOS token")    logging.info("✓ Model and tokenizer loaded successfully")    # PEFT    peft_config = None    if use_lora:        try:            logging.info("Configuring LoRA for parameter-efficient fine-tuning...")            peft_config = LoraConfig(                task_type=TaskType.CAUSAL_LM,                inference_mode=False,                r=LORA_R,                lora_alpha=LORA_ALPHA,                lora_dropout=LORA_DROPOUT,                target_modules=LORA_TARGET_MODULES,                bias="none",                use_rslora=False,                modules_to_save=None,            )            logging.info(f"LoRA configuration: rank={LORA_R}, alpha={LORA_ALPHA}, dropout={LORA_DROPOUT}")            logging.info(f"Target modules: {', '.join(LORA_TARGET_MODULES)}")            original_params = model.num_parameters()            model = get_peft_model(model, peft_config)            trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)            total_params = sum(p.numel() for p in model.parameters())            efficiency_ratio = 100 * trainable_params / total_params            logging.info(f"✓ LoRA applied successfully:")            logging.info(f"  • Original parameters: {original_params:,}")            logging.info(f"  • Trainable parameters: {trainable_params:,}")            logging.info(f"  • Training efficiency: {efficiency_ratio:.2f}% of parameters")            logging.info(f"  • Memory savings: ~{100-efficiency_ratio:.1f}% reduction in gradient memory")        except Exception as e:            logging.info(f"✗ LoRA configuration failed: {e}")            logging.info("Falling back to full fine-tuning...")            peft_config = None    else:        logging.info("Full fine-tuning mode selected")        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)        logging.info(f"Trainable parameters: {trainable_params:,} (100% of model)")    # Learning rate adjustment for LoRA    adjusted_lr = LEARNING_RATE * 10 if use_lora else LEARNING_RATE    logging.info(f"Learning rate: {adjusted_lr} ({'LoRA-adjusted' if use_lora else 'standard'})")    training_args_dict = {        "output_dir": OUTPUT_DIR,        "per_device_train_batch_size": BATCH_SIZE,        "per_device_eval_batch_size": BATCH_SIZE,        "gradient_accumulation_steps": GRADIENT_ACCUMULATION_STEPS,        "learning_rate": adjusted_lr,        "num_train_epochs": NUM_EPOCHS,        "eval_steps": EVAL_STEPS,        "logging_steps": LOGGING_STEPS,        "save_steps": SAVE_STEPS,        "save_total_limit": 2,        "report_to": "mlflow",        "run_name": f"{MODEL_NAME}_fine-tuning",        "warmup_steps": 50,        "weight_decay": 0.01,        "metric_for_best_model": "eval_loss",        "greater_is_better": False,        "dataloader_pin_memory": False,        "remove_unused_columns": False,        "use_liger_kernel": True,  # Enable Liger kernel optimizations        "fp16": True,  # Mixed precision training        "gradient_checkpointing": True,        "gradient_checkpointing_kwargs": {"use_reentrant": False}, # Required for LORA with DDP    }    logging.info("✓ Liger kernel optimizations enabled")    training_args = SFTConfig(**training_args_dict)    trainer = SFTTrainer(        model=model,        args=training_args,        train_dataset=dataset["train"],        eval_dataset=dataset["test"],        processing_class=tokenizer,        peft_config=peft_config,    )    logging.info("\n" + "="*50)    logging.info("STARTING TRAINING")    logging.info("="*50)    logging.info("🚀 Training with Liger kernels for memory-efficient single GPU training")    if use_lora:        logging.info("🎯 Using LoRA for parameter-efficient fine-tuning")    trainer.train()    logging.info("\n✓ Training completed successfully!")    if rt.get_global_rank() == 0:        logging.info("\nSaving trained model...")        logging.info("Saving LoRA adapter weights...")        trainer.save_model(training_args.output_dir)        logging.info("✓ LoRA adapters saved - use with base model for inference")        tokenizer.save_pretrained(training_args.output_dir)        logging.info("✓ Tokenizer saved with model")        logging.info(f"\n🎉 All artifacts saved to: {training_args.output_dir}")    mlflow_run_id = None    if mlflow.last_active_run() is not None:        mlflow_run_id = mlflow.last_active_run().info.run_id    return mlflow_run_id

## Run the distributed training[​](#run-the-distributed-training "Direct link to Run the distributed training")

This cell executes the training function on 8 H100 GPUs. The `distributed()` method handles:

*   Provisioning Serverless GPU Compute resources
*   Distributing the training workload across multiple GPUs
*   Collecting the MLflow run ID for model registration

Training typically takes 15-30 minutes depending on dataset size and compute availability.

Python

    mlflow_run_id = run_train.distributed(use_lora=True)[0]print(mlflow_run_id)

## MLflow and Unity Catalog registration[​](#mlflow-and-unity-catalog-registration "Direct link to MLflow and Unity Catalog registration")

### Model registration strategy[​](#model-registration-strategy "Direct link to Model registration strategy")

*   **MLflow Tracking**: Log model artifacts and metadata
*   **Unity Catalog**: Register model for governance and deployment
*   **Model Versioning**: Automatic versioning for model lifecycle management
*   **Metadata**: Complete model information for reproducibility

Python

    print("\nRegistering model with MLflow and Unity Catalog...")from transformers import AutoTokenizer, AutoModelForCausalLMfrom peft import PeftModelimport mlflowtry:    # Load the trained model for registration    print("Loading LoRA model for registration...")    # For LoRA models, we need both base model and adapter    base_model = AutoModelForCausalLM.from_pretrained(        MODEL_NAME,        trust_remote_code=True    )    # Load tokenizer    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)    adapter_dir = OUTPUT_DIR    peft_model = PeftModel.from_pretrained(base_model, adapter_dir)    # Merge LoRA into base and drop PEFT wrappers    merged_model = peft_model.merge_and_unload()    components = {        "model": merged_model,        "tokenizer": tokenizer,    }    # Create Unity Catalog model name    full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"    print(f"Registering model as: {full_model_name}")    # Start MLflow run and log model    task = "llm/v1/chat"    model_type = "LoRA"    with mlflow.start_run(run_id=mlflow_run_id):        model_info = mlflow.transformers.log_model(            transformers_model=components,            artifact_path="model",            task=task,            registered_model_name=full_model_name,            metadata={                "task": task,                "pretrained_model_name": MODEL_NAME,                "databricks_model_family": "QwenForCausalLM",            },        )    print(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")    print(f"✓ MLflow model URI: {model_info.model_uri}")    # Print deployment information    print(f"\n📦 Model Registration Complete!")    print(f"Unity Catalog Path: {full_model_name}")    print(f"Model Type: {model_type}")    print(f"Optimization: Liger Kernels + LoRA")except Exception as e:    print(f"✗ Model registration failed: {e}")    print("Model is still saved locally and can be registered manually")    print(f"Local model path: {OUTPUT_DIR}")

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've fine-tuned and registered your model, you can:

*   **Deploy the model**: [Serve models with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
*   **Learn more about distributed training**: [Multi-GPU distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   **Optimize Serverless GPU Compute usage**: [Best practices for Serverless GPU Compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   **Troubleshoot issues**: [Troubleshoot issues on Serverless GPU Compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed fine-tuning of Qwen2-0.5B with LoRA
