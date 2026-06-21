---
title: Finetune Llama-3.2-3B with Unsloth | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-finetune-llama-unsloth
ingestedAt: "2026-06-18T08:08:52.125Z"
---

This notebook demonstrates how to finetune the Llama-3.2-3B large language model using the [Unsloth](https://github.com/unslothai/unsloth) library. Unsloth provides optimized implementations for parameter-efficient fine-tuning (PEFT) techniques like LoRA (Low-Rank Adaptation), enabling faster training with reduced memory usage.

The notebook covers:

*   Loading and configuring the base Llama-3.2-3B model
*   Creating a PEFT model with LoRA adapters
*   Processing training data from the FineTome-100k dataset
*   Training with supervised fine-tuning (SFT)
*   Logging experiments with MLflow
*   Registering the fine-tuned model in Unity Catalog

## Requirements: Serverless GPU compute[​](#requirements-serverless-gpu-compute "Direct link to Requirements: Serverless GPU compute")

This notebook requires GPU compute with an A10 accelerator.

1.  Select **A10** as the accelerator from Hardware option in the environment panel
2.  Select **AI v5** from the Base enviroment option in the environment panel
3.  Click **Apply**.

Note: Compute provisioning can take up to 8 minutes.

## Required libraries[​](#required-libraries "Direct link to Required libraries")

The Databricks AI v5 environment includes Unsloth and its dependencies (`unsloth`, `unsloth_zoo`, `bitsandbytes`, `trl`, `xformers`, and `mlflow`), so no additional installation is needed.

## Configure Unity Catalog and model settings[​](#configure-unity-catalog-and-model-settings "Direct link to Configure Unity Catalog and model settings")

Define Unity Catalog locations for storing model checkpoints and the final registered model. The configuration includes:

*   Unity Catalog namespace (catalog, schema, model name, volume)
*   Base model selection (Llama-3.2-3B-Instruct from Unsloth)
*   Output directory for saving checkpoints
*   Training dataset (FineTome-100k)

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "llama-3.2-3b")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")# Model selection - Choose based on your compute constraintsMODEL_NAME = "unsloth/Llama-3.2-3B-Instruct" # or choose "unsloth/Llama-3.2-1B-Instruct"OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"DATASET_NAME = "mlabonne/FineTome-100k"print(f"MODEL_NAME: {MODEL_NAME}")print(f"OUTPUT_DIR: {OUTPUT_DIR}")print(f"DAASET_NAME: {DATASET_NAME}")

## Load the base model and tokenizer[​](#load-the-base-model-and-tokenizer "Direct link to Load the base model and tokenizer")

Load the Llama-3.2-3B-Instruct model using Unsloth's `FastLanguageModel`. This configures the model with a maximum sequence length of 2048 tokens and automatic dtype detection for optimal performance on the available GPU.

Python

    from unsloth import FastLanguageModelmax_seq_length = 2048 # Choose any!dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+load_in_4bit = False # Use 4bit quantization to reduce memory usage. Can be False.model, tokenizer = FastLanguageModel.from_pretrained(    model_name = MODEL_NAME,    max_seq_length = max_seq_length,    dtype = dtype,    load_in_4bit = load_in_4bit,    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf)

## Apply LoRA adapters for efficient fine-tuning[​](#apply-lora-adapters-for-efficient-fine-tuning "Direct link to Apply LoRA adapters for efficient fine-tuning")

Convert the base model into a PEFT model by adding LoRA (Low-Rank Adaptation) adapters to the attention and feed-forward layers. This uses rank 16 adapters, which adds only a small fraction of trainable parameters while keeping the base model frozen, significantly reducing memory requirements and training time.

Python

    model = FastLanguageModel.get_peft_model(    model,    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",                    "gate_proj", "up_proj", "down_proj",],    lora_alpha = 16,    lora_dropout = 0, # Supports any, but = 0 is optimized    bias = "none",    # Supports any, but = "none" is optimized    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context    random_state = 3407,    use_rslora = False,  # We support rank stabilized LoRA    loftq_config = None, # And LoftQ)

## Load and format the training dataset[​](#load-and-format-the-training-dataset "Direct link to Load and format the training dataset")

Load the FineTome-100k dataset and prepare it for training. The data processing applies the Llama-3.1 chat template to format conversations, standardizes the ShareGPT format, and converts each conversation into tokenized text sequences suitable for supervised fine-tuning.

Python

    from unsloth.chat_templates import get_chat_templatetokenizer = get_chat_template(    tokenizer,    chat_template = "llama-3.1",)def formatting_prompts_func(examples):    convos = examples["conversations"]    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]    return { "text" : texts, }passfrom datasets import load_datasetdataset = load_dataset(DATASET_NAME, split = "train")

Python

    from unsloth.chat_templates import standardize_sharegptdataset = standardize_sharegpt(dataset)dataset = dataset.map(formatting_prompts_func, batched = True,)

## Configure the supervised fine-tuning trainer[​](#configure-the-supervised-fine-tuning-trainer "Direct link to Configure the supervised fine-tuning trainer")

Set up the `SFTTrainer` with training hyperparameters including batch size, learning rate, and optimizer settings. The trainer is configured to run for 25 steps with MLflow tracking enabled. Response-only training ensures the model learns only from assistant responses, not user prompts, improving training efficiency.

Python

    from trl import SFTTrainerfrom transformers import TrainingArguments, DataCollatorForSeq2Seqfrom unsloth import is_bfloat16_supportedfrom transformers.integrations import MLflowCallbackfrom unsloth.chat_templates import train_on_responses_onlyimport mlflowtrainer = SFTTrainer(    model = model,    tokenizer = tokenizer,    train_dataset = dataset,    dataset_text_field = "text",    max_seq_length = max_seq_length,    data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer),    dataset_num_proc = 6,    packing = False, # Can make training 5x faster for short sequences.    args = TrainingArguments(        per_device_train_batch_size = 2,        gradient_accumulation_steps = 4,        warmup_steps = 5,        # num_train_epochs = 1, # Set this for 1 full training run.        max_steps = 25,        learning_rate = 2e-4,        fp16 = not is_bfloat16_supported(),        bf16 = is_bfloat16_supported(),        logging_steps = 1,        optim = "adamw_8bit",        weight_decay = 0.01,        lr_scheduler_type = "linear",        seed = 3407,        output_dir = OUTPUT_DIR,        report_to = "mlflow", # Use MLflow to track model metrics    ),)trainer = train_on_responses_only(    trainer,    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",    num_proc=1)

## Execute the training loop[​](#execute-the-training-loop "Direct link to Execute the training loop")

Run the fine-tuning process within an MLflow run to automatically track training metrics (loss, learning rate, etc.) and system metrics (GPU utilization, memory usage). The training runs for 25 steps as configured in the trainer, with checkpoints saved to the Unity Catalog volume.

Python

    import mlflowwith mlflow.start_run(    run_name='finetune-llama-3.2-3b-unsloth',    log_system_metrics=True):    trainer.train()

## Merge LoRA adapters and register in Unity Catalog[​](#merge-lora-adapters-and-register-in-unity-catalog "Direct link to Merge LoRA adapters and register in Unity Catalog")

Combine the trained LoRA adapter weights with the base model to create a single, deployable model. The merged model is then logged to MLflow and registered in Unity Catalog with the chat task type, making it ready for deployment to model serving endpoints.

Python

    mlflow_run_id = mlflow.last_active_run().info.run_idmerged_model = model.merge_and_unload()# Create Unity Catalog model namefull_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"try:    with mlflow.start_run(run_id = mlflow_run_id):        model_info = mlflow.transformers.log_model(            transformers_model={'model': merged_model, 'tokenizer': tokenizer},            name='model',            registered_model_name=full_model_name, # TODO: Replace with your own model name!            await_registration_for=3600,            task='llm/v1/chat',        )    print(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")    print(f"✓ MLflow model URI: {model_info.model_uri}")    print(f"✓ Model version: {model_info.version}")except Exception as e:    print(f"✗ Model registration failed: {e}")    print("Model is still saved locally and can be registered manually")    print(f"Local model path: {OUTPUT_DIR}")

## Next steps[​](#next-steps "Direct link to Next steps")

The fine-tuned model is now registered in Unity Catalog and ready to serve. Learn more about deploying and using the model:

*   [Deploy models for batch or real-time inference](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
*   [Create and manage model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
*   [Unsloth documentation](https://docs.unsloth.ai/)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Finetune Llama-3.2-3B with Unsloth
