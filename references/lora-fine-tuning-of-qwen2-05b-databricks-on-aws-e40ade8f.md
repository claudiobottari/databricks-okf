---
title: LoRA fine-tuning of Qwen2-0.5B | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-finetune-qwen2-0.5b
ingestedAt: "2026-06-18T08:08:56.004Z"
---

This notebook demonstrates how to efficiently fine-tune the Qwen2-0.5B large language model using parameter-efficient techniques. You'll learn how to:

*   Apply **LoRA (Low-Rank Adaptation)** to reduce trainable parameters by ~99% while maintaining model quality
*   Use **Liger Kernels** for memory-efficient training with optimized Triton kernels
*   Leverage **TRL (Transformer Reinforcement Learning)** for supervised fine-tuning
*   Register the fine-tuned model in Unity Catalog for governance and deployment

**Key concepts:**

*   [LoRA](https://arxiv.org/abs/2106.09685): A technique that freezes the base model and trains small adapter layers, dramatically reducing memory requirements and training time
*   [Liger Kernels](https://github.com/linkedin/Liger-Kernel): GPU-optimized kernels that reduce memory usage by up to 80% through fused operations
*   [TRL](https://huggingface.co/docs/trl): A library for training language models with reinforcement learning and supervised fine-tuning

## LoRA vs full fine-tuning decision matrix[​](#lora-vs-full-fine-tuning-decision-matrix "Direct link to LoRA vs full fine-tuning decision matrix")

[LoRA (Low-Rank Adaptation)](https://arxiv.org/abs/2106.09685) freezes the base model and trains only small adapter layers, reducing trainable parameters by ~99%. This makes training faster and more memory-efficient.

## Liger Kernel benefits[​](#liger-kernel-benefits "Direct link to Liger Kernel benefits")

[Liger Kernels](https://github.com/linkedin/Liger-Kernel) are GPU-optimized operations that fuse multiple steps into single kernels, reducing memory transfers and improving efficiency. The [technical paper](https://arxiv.org/pdf/2410.10989) provides detailed benchmarks showing significant performance improvements.

*   **Fused operations**: Combines operations (e.g., linear + loss) to reduce memory overhead by up to 80%
*   **Triton kernels**: Custom GPU kernels optimized for transformer operations (RMSNorm, RoPE, SwiGLU, CrossEntropy)
*   **Memory efficiency**: Allows larger batch sizes or models that wouldn't otherwise fit in GPU memory
*   **Single GPU optimization**: Particularly effective for A10/A100 single-GPU training scenarios

This notebook uses the [TRL library](https://huggingface.co/docs/trl) to simplify the training configuration and automatically apply these optimizations.

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

To connect to serverless GPU compute:

1.  Click the **Connect** drop-down menu in the notebook and select **Serverless GPU**.
2.  Open the **Environment** panel and choose **AI v5** as the base environment.
3.  Click **Apply**.

For more information, see the [GPU compute documentation](https://docs.databricks.com/compute/gpu.html).

## Install required libraries[​](#install-required-libraries "Direct link to Install required libraries")

The Databricks AI v5 environment already includes most of the libraries required for this example (such as `trl`, `peft`, `transformers`, and `hf_transfer`). The next cell installs `liger-kernel`, which is not yet part of the environment.

The `%restart_python` command restarts the Python interpreter to ensure the newly installed package is properly loaded.

Python

    %pip install liger-kernel==0.8.0%restart_python

## Import libraries[​](#import-libraries "Direct link to Import libraries")

The next cell imports the required libraries for model training, dataset handling, and MLflow tracking.

Python

    from datasets import load_datasetfrom transformers import AutoModelForCausalLM, AutoTokenizerfrom peft import LoraConfig, TaskType, get_peft_modelfrom trl import (    SFTConfig,    SFTTrainer,    setup_chat_format)import osimport mlflow

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
*   **Max steps (200)**: Caps training at 200 steps for a fast demonstration run
*   **Logging & Checkpointing**: Saves progress every 100 steps, logs metrics every 25 steps

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "qwen2_liger_lora_assistant")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")# MLflow and Unity Catalog configuration# Model selection - Choose based on your compute constraintsMODEL_NAME = "Qwen/Qwen2-0.5B"DATASET_NAME = "trl-lib/Capybara"OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"# Training hyperparametersBATCH_SIZE = 8GRADIENT_ACCUMULATION_STEPS = 4LEARNING_RATE = 1e-4MAX_STEPS = 200EVAL_STEPS = 100LOGGING_STEPS = 25SAVE_STEPS = 100

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

## Liger Kernel optimization[​](#liger-kernel-optimization "Direct link to Liger Kernel optimization")

### Memory and performance optimization[​](#memory-and-performance-optimization "Direct link to Memory and performance optimization")

[Liger Kernels](https://github.com/linkedin/Liger-Kernel) provide significant memory and performance improvements through:

*   **Fused linear operations**: Combines linear layers with losses
*   **Optimized kernels**: RMSNorm, RoPE, SwiGLU, CrossEntropy optimizations
*   **Memory reduction**: Up to 80% memory savings on fused operations
*   **Single GPU focus**: Optimized for A10 single-GPU training

For more details, see the [Efficient Triton Kernels paper](https://arxiv.org/pdf/2410.10989).

## Load and prepare dataset[​](#load-and-prepare-dataset "Direct link to Load and prepare dataset")

The next cell loads the training dataset and prepares it for fine-tuning:

*   **Dataset**: [trl-lib/Capybara](https://huggingface.co/datasets/trl-lib/Capybara) - high-quality conversational data optimized for instruction following
*   **Train/validation split**: Creates a 90/10 split if no test set exists
*   **Data validation**: Ensures proper formatting for conversational fine-tuning

Python

    dataset = load_dataset(DATASET_NAME)print(f"✓ Dataset loaded: {dataset}")if "test" not in dataset:    print("Creating validation split from training data...")    dataset = dataset["train"].train_test_split(test_size=0.1, seed=42)    print("✓ Data split: 90% train, 10% validation")

## Initialize model and tokenizer[​](#initialize-model-and-tokenizer "Direct link to Initialize model and tokenizer")

The next cell loads the base model and tokenizer, then configures them for conversational fine-tuning:

*   **Model loading**: Downloads Qwen2-0.5B from Hugging Face
*   **Tokenizer setup**: Configures fast tokenizer with proper padding
*   **Chat formatting**: Applies ChatML format for structured conversations
*   **Token configuration**: Sets padding token to EOS token for proper sequence handling

Python

    model = AutoModelForCausalLM.from_pretrained(    MODEL_NAME,    trust_remote_code=True,)tokenizer = AutoTokenizer.from_pretrained(    MODEL_NAME,    trust_remote_code=True,    use_fast=True)# Chat template formatting for conversational fine-tuningif tokenizer.chat_template is None:    print("Adding chat template for proper conversation formatting...")    model, tokenizer = setup_chat_format(model, tokenizer, format="chatml")    print("✓ ChatML format applied for structured conversations")if tokenizer.pad_token is None:    tokenizer.pad_token = tokenizer.eos_token    print("✓ Padding token set to EOS token")print("✓ Model and tokenizer loaded successfully")

## Apply LoRA adapters[​](#apply-lora-adapters "Direct link to Apply LoRA adapters")

The next cell applies LoRA (Low-Rank Adaptation) to the model:

*   **Configuration**: Sets up LoRA with rank=8, alpha=32, dropout=0.1
*   **Target modules**: Applies adapters to attention and MLP layers
*   **Parameter efficiency**: Reduces trainable parameters to ~1% of the original model
*   **Memory savings**: Dramatically reduces gradient memory requirements
*   **Fallback**: Automatically falls back to full fine-tuning if LoRA configuration fails

Python

    peft_config = Nonetry:    print("Configuring LoRA for parameter-efficient fine-tuning...")    peft_config = LoraConfig(        task_type=TaskType.CAUSAL_LM,        inference_mode=False,        r=LORA_R,        lora_alpha=LORA_ALPHA,        lora_dropout=LORA_DROPOUT,        target_modules=LORA_TARGET_MODULES,        bias="none",        use_rslora=False,        modules_to_save=None,    )    print(f"LoRA configuration: rank={LORA_R}, alpha={LORA_ALPHA}, dropout={LORA_DROPOUT}")    print(f"Target modules: {', '.join(LORA_TARGET_MODULES)}")    original_params = model.num_parameters()    model = get_peft_model(model, peft_config)    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)    total_params = sum(p.numel() for p in model.parameters())    efficiency_ratio = 100 * trainable_params / total_params    print(f"✓ LoRA applied successfully:")    print(f"  • Original parameters: {original_params:,}")    print(f"  • Trainable parameters: {trainable_params:,}")    print(f"  • Training efficiency: {efficiency_ratio:.2f}% of parameters")    print(f"  • Memory savings: ~{100-efficiency_ratio:.1f}% reduction in gradient memory")except Exception as e:    print(f"✗ LoRA configuration failed: {e}")    print("Falling back to full fine-tuning...")    USE_LORA = False    peft_config = None

## Train the model[​](#train-the-model "Direct link to Train the model")

The next cell configures and executes the training process:

### Training configuration[​](#training-configuration "Direct link to Training configuration")

*   **Learning rate adjustment**: Scales learning rate 10x higher for LoRA (as recommended in the [LoRA paper](https://arxiv.org/abs/2106.09685))
*   **Batch configuration**: 8 samples per device with 4 gradient accumulation steps (effective batch size: 32)
*   **Optimization**: Warmup steps, weight decay, and best model selection based on evaluation loss
*   **Logging**: Reports metrics to MLflow for experiment tracking

### Key optimizations enabled[​](#key-optimizations-enabled "Direct link to Key optimizations enabled")

*   **Liger Kernels**: Fused GPU operations reduce memory usage by up to 80%
*   **Mixed precision (FP16)**: Faster computation with lower memory footprint
*   **Gradient accumulation**: Simulates larger batch sizes for stable training
*   **Checkpointing**: Saves model every 100 steps with limit of 2 checkpoints

The training loop will log progress every 25 steps and evaluate every 100 steps.

Python

    with mlflow.start_run(run_name=f"{MODEL_NAME}_fine-tuning", log_system_metrics=True):    try:        # Learning rate adjustment for LoRA        adjusted_lr = LEARNING_RATE * 10        print(f"Learning rate: {adjusted_lr}")        training_args_dict = {            "output_dir": OUTPUT_DIR,            "per_device_train_batch_size": BATCH_SIZE,            "per_device_eval_batch_size": BATCH_SIZE,            "gradient_accumulation_steps": GRADIENT_ACCUMULATION_STEPS,            "learning_rate": adjusted_lr,            "max_steps": MAX_STEPS,            "eval_steps": EVAL_STEPS,            "logging_steps": LOGGING_STEPS,            "save_steps": SAVE_STEPS,            "save_total_limit": 2,            "report_to": "mlflow", # Log to MLflow            "warmup_steps": 50,            "weight_decay": 0.01,            "metric_for_best_model": "eval_loss",            "greater_is_better": False,            "dataloader_pin_memory": False,            "remove_unused_columns": False,            "use_liger_kernel": True,  # Enable Liger kernel optimizations            "fp16": True,  # Mixed precision training        }        print("✓ Liger kernel optimizations enabled")        training_args = SFTConfig(**training_args_dict)        trainer = SFTTrainer(            model=model,            args=training_args,            train_dataset=dataset["train"],            eval_dataset=dataset["test"],            processing_class=tokenizer,            peft_config=peft_config,        )        print("\n" + "="*50)        print("STARTING TRAINING")        print("="*50)        print("🚀 Training with Liger kernels for memory-efficient single GPU training")        print("🎯 Using LoRA for parameter-efficient fine-tuning")        trainer.train()        print("\n✓ Training completed successfully!")    except Exception as e:        print(f"✗ Training failed: {e}")        raise

## Save model artifacts[​](#save-model-artifacts "Direct link to Save model artifacts")

The next cell saves the trained model and tokenizer to the Unity Catalog volume:

*   **LoRA adapters**: Saves only the trained adapter weights (much smaller than full model)
*   **Tokenizer**: Saves tokenizer configuration for inference
*   **Storage location**: Saves to `/Volumes/{catalog}/{schema}/{volume}/{model_name}`
*   **Reusability**: Adapters can be loaded with the base model for inference

Python

    try:    print("\nSaving trained model...")    print("Saving LoRA adapter weights...")    trainer.save_model(training_args.output_dir)    print("✓ LoRA adapters saved - use with base model for inference")    tokenizer.save_pretrained(training_args.output_dir)    print("✓ Tokenizer saved with model")    print(f"\n🎉 All artifacts saved to: {training_args.output_dir}")except Exception as e:    print(f"✗ Model saving failed: {e}")    raise

## Register model in Unity Catalog[​](#register-model-in-unity-catalog "Direct link to Register model in Unity Catalog")

The next cell registers the fine-tuned model in Unity Catalog for governance and deployment:

### Model registration workflow[​](#model-registration-workflow "Direct link to Model registration workflow")

1.  **Load trained model**: Loads base model and applies LoRA adapters
2.  **Merge adapters**: Combines LoRA weights with base model for deployment
3.  **Prepare for logging**: Creates transformers model dictionary with model and tokenizer
4.  **Register in Unity Catalog**: Logs to MLflow and registers in Unity Catalog
5.  **Add metadata**: Includes task type, model family, and size information

### Benefits of Unity Catalog registration[​](#benefits-of-unity-catalog-registration "Direct link to Benefits of Unity Catalog registration")

*   **Governance**: Centralized model registry with access control and lineage tracking
*   **Versioning**: Automatic version management for model lifecycle
*   **Deployment**: Easy deployment to model serving endpoints
*   **Discoverability**: Models are searchable and documented in Unity Catalog

Python

    mlflow_run_id = mlflow.last_active_run().info.run_idprint("\nRegistering model with MLflow and Unity Catalog...")with mlflow.start_run(run_id = mlflow_run_id):    try:        # Load the trained model for registration        print("Loading LoRA model for registration...")        # For LoRA models, we need both base model and adapter        base_model = AutoModelForCausalLM.from_pretrained(            MODEL_NAME,            trust_remote_code=True        )        # Load tokenizer        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)        from peft import PeftModel        peft_model = PeftModel.from_pretrained(base_model, training_args.output_dir)        model_type = "LoRA"        size_params = "0.5b_lora"        # Merge LoRA into base and drop PEFT wrappers        merged_model = peft_model.merge_and_unload()        # Prepare transformers model dictionary        transformers_model = {            "model": merged_model,            "tokenizer": tokenizer        }        # Create Unity Catalog model name        full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"        print(f"Registering model as: {full_model_name}")        # Start MLflow run and log model        task = "llm/v1/chat"        model_info = mlflow.transformers.log_model(            transformers_model=transformers_model,            task=task,            registered_model_name=full_model_name,            metadata={                "task": task,                "pretrained_model_name": MODEL_NAME,                "databricks_model_family": "QwenForCausalLM",                "databricks_model_size_parameters": size_params,            },            repo_type="local",  # Fix: specify repo_type for local path        )        print(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")        print(f"✓ MLflow model URI: {model_info.model_uri}")        # Print deployment information        print(f"\n📦 Model Registration Complete!")        print(f"Unity Catalog Path: {full_model_name}")        print(f"Model Type: {model_type}")        print(f"Optimization: Liger Kernels + LoRA")    except Exception as e:        print(f"✗ Model registration failed: {e}")        print("Model is still saved locally and can be registered manually")        print(f"Local model path: {training_args.output_dir}")

## Next steps[​](#next-steps "Direct link to Next steps")

Your Qwen2-0.5B model has been successfully fine-tuned with LoRA and registered in Unity Catalog. Next, you can:

*   **Deploy the model**: [Serve models with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
*   **Learn more about distributed training**: [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   **Optimize serverless GPU usage**: [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   **Troubleshoot issues**: [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### LoRA fine-tuning of Qwen2-0.5B
