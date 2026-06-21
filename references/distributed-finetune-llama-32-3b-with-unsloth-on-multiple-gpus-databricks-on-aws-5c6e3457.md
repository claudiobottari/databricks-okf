---
title: Distributed finetune Llama-3.2-3B with Unsloth on Multiple GPUs | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-finetune-llama-unsloth-distributed
ingestedAt: "2026-06-18T08:08:54.245Z"
---

This notebook demonstrates how to finetune the Llama-3.2-3B LLM using the Unsloth and serverless\_gpu library on 8 H100 GPUs

## Connect to compute[​](#connect-to-compute "Direct link to Connect to compute")

1.  Select **8xH100** as your accelerator in the environment panel
2.  Choose **AI v5** from Base environment option
3.  Click "Apply".

Note that this can take up to 8 minutes.

The AI v5 environment includes Unsloth and its supporting stack (`unsloth`, `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, `einops`), so no additional installation is needed.

Python

    import osos.environ["UNSLOTH_COMPILE_DISABLE"] = "1"

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "llama-3_2-3b")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")# Model selection - Choose based on your compute constraintsMODEL_NAME = "unsloth/Llama-3.2-3B-Instruct" # or choose "unsloth/Llama-3.2-1B-Instruct"OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}" # Save checkpoint to UC VolumeDATASET_NAME = "mlabonne/FineTome-100k"print(f"MODEL_NAME: {MODEL_NAME}")print(f"OUTPUT_DIR: {OUTPUT_DIR}")print(f"DATASET_NAME: {DATASET_NAME}")

Python

    from serverless_gpu import distributedfrom serverless_gpu import runtime as rt@distributed(gpus=8, gpu_type='h100')def run_train():    from datasets import load_dataset    import logging    import mlflow    import os    import torch    # Set up device for distributed training    local_rank = int(os.environ.get("LOCAL_RANK", 0))    torch.cuda.set_device(local_rank)    # IMPORTANT: import unsloth BEFORE trl    from unsloth import FastLanguageModel, is_bfloat16_supported    from unsloth.chat_templates import get_chat_template, standardize_sharegpt, train_on_responses_only    from trl import SFTTrainer    from transformers import TrainingArguments, DataCollatorForSeq2Seq    from transformers.integrations import MLflowCallback    max_seq_length = 2048 # Choose any!    dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+    load_in_4bit = False # Use 4bit quantization to reduce memory usage. Can be False.    # Load model and tokenizer    model, tokenizer = FastLanguageModel.from_pretrained(        model_name=MODEL_NAME,        max_seq_length=max_seq_length,        dtype=dtype,        load_in_4bit=load_in_4bit,        device_map={'': local_rank},        # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf    )    model = FastLanguageModel.get_peft_model(        model,        r=16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",                        "gate_proj", "up_proj", "down_proj",],        lora_alpha=16,        lora_dropout=0, # Supports any, but = 0 is optimized        bias="none",    # Supports any, but = "none" is optimized        use_gradient_checkpointing=True,        random_state=3407,        use_rslora=False,  # We support rank stabilized LoRA        loftq_config=None, # And LoftQ    )    # DDP needs non-reentrant gradient checkpointing to avoid "mark a variable ready only once"    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})    # Process data    tokenizer = get_chat_template(        tokenizer,        chat_template="llama-3.1",    )    def formatting_prompts_func(examples):        convos = examples["conversations"]        texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]        return { "text" : texts, }    dataset = load_dataset(DATASET_NAME, split="train")    dataset = standardize_sharegpt(dataset)    dataset = dataset.map(formatting_prompts_func, batched=True,)    trainer = SFTTrainer(        model = model,        tokenizer = tokenizer,        train_dataset = dataset,        dataset_text_field = "text",        max_seq_length = max_seq_length,        data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer),        dataset_num_proc = 6,        packing = False, # Can make training 5x faster for short sequences.        args = TrainingArguments(            per_device_train_batch_size = 2,            gradient_accumulation_steps = 4,            warmup_steps = 5,            # num_train_epochs = 1, # Set this for 1 full training run.            max_steps = 25,            learning_rate = 2e-4,            fp16 = not is_bfloat16_supported(),            bf16 = is_bfloat16_supported(),            logging_steps = 1,            optim = "adamw_8bit",            weight_decay = 0.01,            lr_scheduler_type = "linear",            seed = 3407,            output_dir = OUTPUT_DIR,            report_to = "mlflow", # Use MLflow to track model metrics,            run_name = f"{MODEL_NAME}-finetune-unsloth",        ),    )    trainer = train_on_responses_only(        trainer,        instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",        response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",        num_proc=1    )    trainer.train()    # Save model    if rt.get_global_rank() == 0:        logging.info("\nSaving trained model...")        trainer.save_model(OUTPUT_DIR)        logging.info("✓ LoRA adapters saved - use with base model for inference")        tokenizer.save_pretrained(OUTPUT_DIR)        logging.info("✓ Tokenizer saved with model")        logging.info(f"\n🎉 All artifacts saved to: {OUTPUT_DIR}")    mlflow_run_id = None    if mlflow.last_active_run() is not None:        mlflow_run_id = mlflow.last_active_run().info.run_id    return mlflow_run_id

Python

    run_id = run_train.distributed()[0]

## MLflow and Unity Catalog registration[​](#mlflow-and-unity-catalog-registration "Direct link to MLflow and Unity Catalog registration")

### Model registration strategy[​](#model-registration-strategy "Direct link to Model registration strategy")

*   **MLflow Tracking**: Log model artifacts and metadata
*   **Unity Catalog**: Register model for governance and deployment
*   **Model Versioning**: Automatic versioning for model lifecycle management
*   **Metadata**: Complete model information for reproducibility

Python

    print("\nRegistering model with MLflow and Unity Catalog...")from transformers import AutoTokenizer, AutoModelForCausalLMfrom peft import PeftModelimport mlflow# Load the trained model for registrationprint("Loading LoRA model for registration...")# For LoRA models, we need both base model and adapterbase_model = AutoModelForCausalLM.from_pretrained(    MODEL_NAME,    trust_remote_code=True)# Load tokenizertokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)adapter_dir = OUTPUT_DIRpeft_model = PeftModel.from_pretrained(base_model, adapter_dir)# Merge LoRA into base and drop PEFT wrappersmerged_model = peft_model.merge_and_unload()components = {    "model": merged_model,    "tokenizer": tokenizer,}# Create Unity Catalog model namefull_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"print(f"Registering model as: {full_model_name}")# Start MLflow run and log modeltask = "llm/v1/chat"with mlflow.start_run(run_id=run_id):    model_info = mlflow.transformers.log_model(        transformers_model=components,        name="model",        task=task,        registered_model_name=full_model_name,        metadata={            "task": task,            "pretrained_model_name": MODEL_NAME,            "databricks_model_family": "Llama3.2",        },    )print(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")print(f"✓ MLflow model URI: {model_info.model_uri}")print(f"✓ Model version: {model_info.registered_model_version}")# Print deployment informationprint(f"\n📦 Model Registration Complete!")print(f"Unity Catalog Path: {full_model_name}")print(f"Optimization: Liger Kernels + LoRA")

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed finetune Llama-3.2-3B with Unsloth on Multiple GPUs
