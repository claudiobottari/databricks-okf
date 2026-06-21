---
title: Fine-tune Llama 3.2 1B using AI Runtime | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-sft-trl-deepspeed-llama-1b
ingestedAt: "2026-06-18T08:09:07.769Z"
---

This notebook demonstrates how to fully fine-tune a large language model using supervised fine-tuning (SFT) on Databricks AI Runtime. The notebook uses the Transformers Reinforcement Learning (TRL) library with DeepSpeed ZeRO Stage 3 optimization to efficiently train Llama 3.2 1B on a single node with 8 H100 GPUs.

**Key concepts:**

*   **TRL (Transformers Reinforcement Learning)**: A library that provides tools for training language models with reinforcement learning and supervised fine-tuning.
*   **DeepSpeed ZeRO Stage 3**: A memory optimization technique that partitions model parameters, gradients, and optimizer states across GPUs to enable training of large models.
*   **AI Runtime**: Databricks-managed GPU compute that automatically provisions and scales GPU resources for training workloads.

For more information, see [AI Runtime](https://docs.databricks.com/aws/en/compute/gpu).

## Requirements[​](#requirements "Direct link to Requirements")

This notebook requires the following:

*   **AI Runtime**: The notebook uses Databricks AI Runtime with 8 H100 GPUs for distributed training. No cluster configuration is needed.
*   **Unity Catalog**: A Unity Catalog catalog and schema to store model checkpoints and register the trained model.
*   **HuggingFace token**: A HuggingFace access token stored in Databricks secrets to download the base model and dataset.
*   **Python packages**: AI Runtime preinstalls most required libraries. The setup section below installs `deepspeed`.

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires serverless GPU compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**.
2.  On the right side, click the environment button.
3.  Select **8xH100** as the **Accelerator**.
4.  Choose **AI v5** environment from the right panel that contains all the required libraries to run this notebook example.
5.  Click **Apply**.

The training function automatically provisions 8 H100 GPUs for distributed training.

## Install required packages[​](#install-required-packages "Direct link to Install required packages")

AI Runtime already has most of the required libraries preinstalled. For this example, you need to install only `deepspeed`.

Python

    %pip install deepspeed==0.19.1%restart_python

## Configure Unity Catalog and environment variables[​](#configure-unity-catalog-and-environment-variables "Direct link to Configure Unity Catalog and environment variables")

Set up Unity Catalog locations for storing model checkpoints and registering the trained model. The notebook uses query parameters to configure:

*   **Catalog and schema**: Unity Catalog namespace for organizing models and checkpoints
*   **Model name**: Name for the registered model in Unity Catalog
*   **Volume**: Unity Catalog volume for storing model checkpoints during training

The configuration also retrieves the HuggingFace token from Databricks secrets and sets up the MLflow experiment for tracking training metrics.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "llama3_2-1b")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")# Get HuggingFace token and usernamehf_token = dbutils.secrets.get(scope="sgc-nightly-notebook", key="hf_token")username = spark.sql("SELECT session_user()").collect()[0][0]REGISTERED_MODEL_NAME = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"MLFLOW_EXPERIMENT_NAME = f"/Users/{username}/{UC_MODEL_NAME}"# Create the Unity Catalog volume if it doesn't existspark.sql(f"CREATE VOLUME IF NOT EXISTS {UC_CATALOG}.{UC_SCHEMA}.{UC_VOLUME}")print(f"👤 Username: {username}")print("🔑 HuggingFace token configured")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"CHECKPOINT_DIR: {CHECKPOINT_DIR}")print(f"MLFLOW_EXPERIMENT_NAME: {MLFLOW_EXPERIMENT_NAME}")

Python

    import osimport jsonimport tempfileimport torchimport mlflowfrom huggingface_hub import constantsfrom datasets import load_datasetfrom transformers import AutoTokenizer, AutoModelForCausalLMfrom trl import SFTTrainer

## Create DeepSpeed ZeRO Stage 3 configuration[​](#create-deepspeed-zero-stage-3-configuration "Direct link to Create DeepSpeed ZeRO Stage 3 configuration")

DeepSpeed ZeRO (Zero Redundancy Optimizer) Stage 3 partitions model parameters, gradients, and optimizer states across all GPUs to reduce memory consumption per GPU. This enables training of large models that wouldn't fit in a single GPU's memory.

Key configuration settings:

*   **bf16 enabled**: Uses bfloat16 precision for faster training and reduced memory usage
*   **Stage 3 optimization**: Partitions all model states across GPUs
*   **No CPU offloading**: Keeps all data on GPUs for maximum performance on H100 hardware
*   **Overlap communication**: Overlaps gradient communication with computation for efficiency

Python

    def create_deepspeed_config(stage: int):    """Create a DeepSpeed ZeRO configuration for single-node 8xH100 training."""    deepspeed_config = {        "fp16": {            "enabled": False        },        "bf16": {            "enabled": True        },        "zero_optimization": {            "stage": stage,            "offload_optimizer": {                "device": "none"            },            "offload_param": {                "device": "none"            },            "overlap_comm": True,            "contiguous_gradients": True,            "sub_group_size": 1e9,            "reduce_bucket_size": "auto",            "stage3_prefetch_bucket_size": "auto",            "stage3_param_persistence_threshold": 0,            "stage3_max_live_parameters": 1e9,            "stage3_max_reuse_distance": 1e9,            "stage3_gather_16bit_weights_on_model_save": True        },        "gradient_accumulation_steps": 1,        "gradient_clipping": "auto",        "steps_per_print": 2000,        "train_batch_size": "auto",        "train_micro_batch_size_per_gpu": "auto",        "wall_clock_breakdown": False    }    return deepspeed_config# Create DeepSpeed configurationzero_stage = 3deepspeed_config = create_deepspeed_config(zero_stage)print(f"⚙️  DeepSpeed ZeRO Stage {zero_stage} configuration created")

## Define training parameters[​](#define-training-parameters "Direct link to Define training parameters")

Configure the supervised fine-tuning parameters:

*   **Model**: Llama 3.2 1B Instruct, a compact model suitable for H100 GPUs
*   **Dataset**: Capybara dataset from the TRL library for conversational AI training
*   **Batch size**: 2 per device with 4 gradient accumulation steps for effective batch size of 64
*   **Learning rate**: 2e-4 with cosine scheduler and warmup
*   **Training steps**: 60 steps for demonstration (increase for full training)

The configuration uses bfloat16 precision and gradient checkpointing to optimize memory usage.

Python

    def create_training_config():    """Create training configuration for TRL SFT."""    # Model and dataset configuration (not part of TrainingArguments)    model_config = {        "model_name": "meta-llama/Llama-3.2-1B-Instruct",  # Small Llama model suitable for 8xH100        "dataset_name": "trl-lib/Capybara"    }    # Training arguments that will be passed directly to TrainingArguments    training_args_config = {        "output_dir": CHECKPOINT_DIR,        "per_device_train_batch_size": 2,        "per_device_eval_batch_size": 2,        "gradient_accumulation_steps": 1,        "learning_rate": 2e-4,        "max_steps": 60,   # TO DO remove when fine-tuning on full dataset. Demo purposes only.        "logging_steps": 10,        "save_steps": 30,        "eval_steps": 30,        "eval_strategy": "steps",        "warmup_steps": 10,        "lr_scheduler_type": "cosine",        "gradient_checkpointing": False,        "fp16": False,        "bf16": True,        "optim": "adamw_torch",        "remove_unused_columns": False,        "run_name": f"llama3.2-1b-fft-zero3",        "report_to": "mlflow",        "save_total_limit": 2,        "load_best_model_at_end": True,        "metric_for_best_model": "eval_loss",        "greater_is_better": False,    }    return model_config, training_args_config# Create training configurationmodel_config, training_args_config = create_training_config()print("📊 Training Configuration:")print(f"  🤖 Model: {model_config['model_name']}")print(f"  📚 Dataset: {model_config['dataset_name']}")print(f"  🎯 Batch size: {training_args_config['per_device_train_batch_size']}")print(f"  📈 Learning rate: {training_args_config['learning_rate']}")

## Define the distributed training function[​](#define-the-distributed-training-function "Direct link to Define the distributed training function")

The `@distributed` decorator from the `serverless_gpu` library enables execution of GPU workloads on Databricks AI Runtime. The decorator provisions 8 H100 GPUs and handles distributed training setup automatically.

Key parameters:

*   **gpus=8**: Requests 8 GPUs for distributed training
*   **gpu\_type='H100'**: Specifies H100 GPU hardware

The training function:

1.  Loads the base model and tokenizer from HuggingFace
2.  Sets up chat formatting for conversational AI
3.  Loads the training dataset
4.  Initializes the TRL SFTTrainer with DeepSpeed optimization
5.  Trains the model and saves checkpoints
6.  Returns training results and MLflow run ID

For more information, see the [AI Runtime API documentation](https://api-docs.databricks.com/python/serverless_gpu/index.html).

Python

    from serverless_gpu import distributedmlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)@distributed(    gpus=8,    gpu_type='H100',)def run_distributed_trl_sft():    """    Distributed TRL SFT training function using AI Runtime.    This function will be executed on the H100 GPU with DeepSpeed optimization.    """    # Set up environment variables for remote jobs    import os    import tempfile    import json    from huggingface_hub import constants    from datasets import load_dataset    from transformers import AutoTokenizer    from trl import SFTTrainer, SFTConfig    # HuggingFace configuration    os.environ["HUGGING_FACE_HUB_TOKEN"] = hf_token    os.environ['HF_TOKEN'] = hf_token    constants.HF_HUB_ENABLE_HF_TRANSFER = True    # Set up temporary directories    temp_dir = tempfile.mkdtemp()    print("🚀 Starting TRL SFT training on H100 GPU...")    try:        # Load tokenizer        print(f"📥 Loading tokenizer from model: {model_config['model_name']}")        tokenizer = AutoTokenizer.from_pretrained(model_config['model_name'])        # Add pad token if not present        if tokenizer.pad_token is None:            tokenizer.pad_token = tokenizer.eos_token        # Load dataset        print(f"📚 Loading dataset: {model_config['dataset_name']}")        dataset = load_dataset(model_config['dataset_name'])        # Create temporary DeepSpeed config file        deepspeed_config_path = os.path.join(temp_dir, "deepspeed_config.json")        with open(deepspeed_config_path, "w") as f:            json.dump(deepspeed_config, f, indent=2)        # Training arguments - dynamically pass all config parameters        training_args = SFTConfig(            **training_args_config,            deepspeed=deepspeed_config_path,  # Override deepspeed with the config file path        )        # Initialize SFT Trainer        print("🏋️ Initializing SFT Trainer with DeepSpeed...")        trainer = SFTTrainer(            model=model_config["model_name"],            args=training_args,            train_dataset=dataset["train"],            eval_dataset=dataset["test"] if "test" in dataset else None,            processing_class=tokenizer,        )        # Start training        print("🎯 Starting training...")        trainer.train()        # Save the model        print("💾 Saving trained model...")        trainer.save_model()        # Get training results        train_results = trainer.state.log_history        final_loss = train_results[-1].get('train_loss', 'N/A') if train_results else 'N/A'        print("✅ Training completed successfully!")        print(f"📊 Final training loss: {final_loss}")        mlflow_run_id = None        if mlflow.last_active_run() is not None:            mlflow_run_id = mlflow.last_active_run().info.run_id        return {            "status": "success",            "final_loss": final_loss,            "output_dir": training_args_config['output_dir'],            "model_name": model_config['model_name'],            "mlflow_run_id": mlflow_run_id,        }    except Exception as e:        print(f"❌ Training failed: {e}")        import traceback        traceback.print_exc()        return {            "status": "failed",            "error": str(e)        }

## Run the distributed training job[​](#run-the-distributed-training-job "Direct link to Run the distributed training job")

Run the training function by calling `.distributed()` on the decorated function. This provisions the AI Runtime resources, runs the training across 8 H100 GPUs with DeepSpeed optimization, and returns the results.

The training process:

*   Provisions 8 H100 GPUs automatically
*   Downloads the model and dataset from HuggingFace
*   Trains the model with full fine-tuning
*   Saves checkpoints to the Unity Catalog volume
*   Logs metrics to MLflow
*   Returns training status, final loss, and MLflow run ID

Python

    # Execute the distributed trainingresults = run_distributed_trl_sft.distributed()print("🏁 Training execution completed!")print(f"📊 Results: {results}")if results and results[0].get('status') == 'success':    print("✅ Training completed successfully!")    print(f"💾 Model saved to: {results[0].get('output_dir', 'N/A')}")    print(f"📈 Final loss: {results[0].get('final_loss', 'N/A')}")    print(f"🎉 MLflow run ID: {results[0].get('mlflow_run_id', 'N/A')}")else:    print("❌ Training failed!")    if results and 'error' in results:        print(f"🔍 Error: {results['error']}")

## Save the fine-tuned model and test inference[​](#save-the-fine-tuned-model-and-test-inference "Direct link to Save the fine-tuned model and test inference")

This optional step loads the fine-tuned model and tests it with a sample prompt to verify the results.

The process:

1.  Loads the saved model
2.  Tests the model with a sample conversational prompt

Python

    def save_and_load_trained_model():    """Load the fully fine-tuned model from the Unity Catalog volume."""    import torch    from transformers import AutoModelForCausalLM, AutoTokenizer    print(f"📥 Loading fine-tuned model from: {training_args_config['output_dir']}")    # Load the fully fine-tuned model directly from the checkpoint directory    model = AutoModelForCausalLM.from_pretrained(        training_args_config['output_dir'],        torch_dtype=torch.bfloat16,        trust_remote_code=True,        device_map={"":0}    )    tokenizer = AutoTokenizer.from_pretrained(training_args_config['output_dir'], trust_remote_code=True)    print("✅ Model loaded successfully!")    return model, tokenizerdef test_trained_model(model, tokenizer):    """Test the trained model with simple inference."""    try:        import torch        # Test prompt        # Create a conversation following the schema        conversation = [            {                "content": "What is machine learning?",                "role": "user"            }        ]        # Convert conversation to chat format        prompt = ""        for message in conversation:            if message["role"] == "user":                prompt += f"### User: {message['content']}\n### Response:"            else:                prompt += f" {message['content']}\n\n"        # Tokenize        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")        # Generate        with torch.no_grad():            outputs = model.generate(                **inputs,                max_new_tokens=500,                temperature=0.7,                do_sample=True,                pad_token_id=tokenizer.eos_token_id            )        # Decode        response = tokenizer.decode(outputs[0], skip_special_tokens=True)        print("🤖 Model Response:")        print(response)        return response    except Exception as e:        print(f"❌ Model testing failed: {e}")# Save and load the trained modelmodel, tokenizer = save_and_load_trained_model()# Test the trained modeltest_trained_model(model, tokenizer)

## Register the model in Unity Catalog[​](#register-the-model-in-unity-catalog "Direct link to Register the model in Unity Catalog")

Log the fine-tuned model to MLflow and register it in Unity Catalog for deployment and serving. The model is logged with:

*   **Model and tokenizer**: Both components needed for inference
*   **Task type**: Configured as `llm/v1/chat` for conversational AI
*   **Input example**: Sample chat message format for testing
*   **Unity Catalog registration**: Automatically registers the model in the configured catalog and schema

Once registered, the model can be deployed to model serving endpoints or used for batch inference.

Python

    run_id = results[0].get('mlflow_run_id')mlflow.set_registry_uri("databricks-uc")# log the model to mlflow using the latest run id and register to Unity Catalogwith mlflow.start_run(run_id=run_id) as run:    components = {        "model": model,        "tokenizer": tokenizer    }    logged_model = mlflow.transformers.log_model(        transformers_model=components,        name="model",        task="llm/v1/chat",        input_example={            "messages": [                {"role": "user", "content": "What is machine learning?"}            ]        },        registered_model_name=REGISTERED_MODEL_NAME        )    print(f"🔍 Model logged to: {logged_model}")

## Next steps[​](#next-steps "Direct link to Next steps")

*   [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/)
*   [Best practices for AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [Train models with MLflow](https://docs.databricks.com/aws/en/mlflow/models)
*   [Deploy models with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Fine-tune Llama 3.2 1B using AI Runtime
