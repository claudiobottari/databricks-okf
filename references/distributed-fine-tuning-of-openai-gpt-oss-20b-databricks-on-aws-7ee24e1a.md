---
title: Distributed fine-tuning of OpenAI gpt-oss-20b | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-distributed-gpt-oss-20b
ingestedAt: "2026-06-18T08:08:48.038Z"
---

This notebook demonstrates how to fine-tune OpenAI's [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) model using distributed training on serverless GPU compute. You'll learn how to:

*   Apply **LoRA (Low-Rank Adaptation)** to efficiently fine-tune a 20B parameter model
*   Use **MXFP4 quantization** to reduce memory requirements during training
*   Leverage **distributed data parallelism** across 8 H100 GPUs
*   Register the fine-tuned model in Unity Catalog for deployment

**Key concepts:**

*   [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b): OpenAI's 20 billion parameter open-source language model
*   [LoRA](https://arxiv.org/abs/2106.09685): Parameter-efficient fine-tuning that trains small adapter layers while freezing the base model
*   [MXFP4 quantization](https://huggingface.co/docs/transformers/main/en/quantization/mxfp4): Microscaling 4-bit floating point format that reduces memory usage
*   [TRL](https://huggingface.co/docs/trl): Transformer Reinforcement Learning library for supervised fine-tuning
*   [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/): Databricks managed compute that automatically scales GPU resources

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires serverless GPU compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**
2.  On the right side, click the environment button
3.  Select **8xH100** as the **Accelerator**
4.  Choose **AI v5** environment from the right panel that contains all the required libraries to run this notebook example
5.  Click **Apply**

The training function will automatically provision 8 H100 GPUs for distributed training.

## Configure Unity Catalog and model parameters[​](#configure-unity-catalog-and-model-parameters "Direct link to Configure Unity Catalog and model parameters")

Set up the configuration parameters for Unity Catalog registration and model training. You can customize these parameters using the widgets above:

*   **uc\_catalog**, **uc\_schema**, **uc\_model\_name**: Unity Catalog location for model registration
*   **uc\_volume**: Volume name for storing model checkpoints
*   **model**: Hugging Face model identifier (default: openai/gpt-oss-20b)
*   **dataset\_path**: Dataset to use for fine-tuning (default: HuggingFaceH4/Multilingual-Thinking)

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "gpt-oss-20b-peft")dbutils.widgets.text("uc_volume", "checkpoints")dbutils.widgets.text("model", "openai/gpt-oss-20b")dbutils.widgets.text("dataset_path", "HuggingFaceH4/Multilingual-Thinking")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")HF_MODEL_NAME = dbutils.widgets.get("model")DATASET_PATH = dbutils.widgets.get("dataset_path")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"HF_MODEL_NAME: {HF_MODEL_NAME}")print(f"DATASET_PATH: {DATASET_PATH}")OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"print(f"OUTPUT_DIR: {OUTPUT_DIR}")

### Choose your dataset[​](#choose-your-dataset "Direct link to Choose your dataset")

By default, this notebook uses 'HuggingFaceH4/Multilingual-Thinking', which has been specifically curated with translated chain-of-thoughts in multiple languages. You can edit the "Dataset Path" parameter above to use another dataset.

## Define GPU memory logging utility[​](#define-gpu-memory-logging-utility "Direct link to Define GPU memory logging utility")

This utility function helps monitor GPU memory usage during distributed training. It logs allocated and reserved memory for each GPU rank, which is useful for debugging memory issues.

Python

    import osimport torchimport torch.distributed as distdef log_gpu_memory(tag=""):    if not torch.cuda.is_available():        return    # rank info (if distributed is initialized)    if dist.is_available() and dist.is_initialized():        rank = dist.get_rank()        world_size = dist.get_world_size()    else:        rank = 0        world_size = 1    device = torch.cuda.current_device()  # current GPU for this process    torch.cuda.synchronize(device)    allocated = torch.cuda.memory_allocated(device) / 1024**2    reserved  = torch.cuda.memory_reserved(device) / 1024**2    print(        f"[{tag}] rank={rank}/{world_size-1}, "        f"device={device}, "        f"allocated={allocated:.1f} MB, reserved={reserved:.1f} MB"    )

## Define the distributed training function[​](#define-the-distributed-training-function "Direct link to Define the distributed training function")

The following cell defines the training function using the `@distributed` decorator from the serverless\_gpu library. This decorator:

*   Provisions 8 H100 GPUs on-demand for distributed training
*   Handles data parallelism across multiple GPUs automatically

The function includes:

*   Dataset loading and tokenization
*   Model initialization with MXFP4 quantization
*   LoRA adapter configuration
*   Training with gradient checkpointing and mixed precision
*   Model saving to Unity Catalog volumes

Python

    from serverless_gpu import distributed@distributed(gpus=8, gpu_type="h100")def run_train():    import logging    import os    import torch    rank = int(os.environ.get("RANK", "0"))    local_rank = int(os.environ.get("LOCAL_RANK", "0"))    torch.cuda.set_device(local_rank)    world_size = int(os.environ.get("WORLD_SIZE", str(torch.cuda.device_count())))    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")    is_main = rank == 0    if is_main:        logging.info("DDP environment")        logging.info(f"\tWORLD_SIZE={world_size}  RANK={rank}  LOCAL_RANK={local_rank}")        logging.info(f"\tCUDA device count (this node): {torch.cuda.device_count()}")    from datasets import load_dataset    dataset = load_dataset(DATASET_PATH, split="train")    from transformers import AutoTokenizer    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)    from transformers import AutoModelForCausalLM, Mxfp4Config    quantization_config = Mxfp4Config(dequantize=True)    model_kwargs = dict(        attn_implementation="eager", # Use eager attention implementation for better performance        dtype=torch.bfloat16,        quantization_config=quantization_config,        use_cache=False, # Since using gradient checkpointing    )    model = AutoModelForCausalLM.from_pretrained(HF_MODEL_NAME, **model_kwargs)    from peft import LoraConfig, get_peft_model    peft_config = LoraConfig(        r=8,        lora_alpha=16,        target_modules="all-linear",        lora_dropout=0.05,        bias="none",        task_type="CAUSAL_LM",    )    peft_model = get_peft_model(model, peft_config)    if is_main:        peft_model.print_trainable_parameters()    from trl import SFTConfig    training_args = SFTConfig(        learning_rate=2e-4,        num_train_epochs=1,        logging_steps=1,        per_device_train_batch_size=1,        gradient_accumulation_steps=2,        gradient_checkpointing=True,        gradient_checkpointing_kwargs={"use_reentrant": False},        max_length=2048,        warmup_ratio=0.03,        lr_scheduler_type="cosine_with_min_lr",        lr_scheduler_kwargs={"min_lr_rate": 0.1},        output_dir=OUTPUT_DIR,        report_to="mlflow",  # No reporting to avoid Gradio issues        push_to_hub=False,  # Disable push to hub to avoid authentication issues        logging_dir=None,  # Disable tensorboard logging        disable_tqdm=False,  # Keep progress bars for monitoring        ddp_find_unused_parameters=False,    )    from trl import SFTTrainer    trainer = SFTTrainer(        model=peft_model,        args=training_args,        train_dataset=dataset,        processing_class=tokenizer,    )    #torch.cuda.empty_cache()    #log_gpu_memory("before model training")    result = trainer.train()    #log_gpu_memory("after model loading")    if is_main:        logging.info("Training complete!")        logging.info(f"Final training loss: {result.training_loss:.4f}")        logging.info(f"Train runtime (s): {result.metrics.get('train_runtime', 'N/A')}")        logging.info(f"Samples/sec: {result.metrics.get('train_samples_per_second', 'N/A')}")        logging.info("\nSaving trained model...")        trainer.save_model(OUTPUT_DIR)        logging.info("✓ LoRA adapters saved - use with base model for inference")        tokenizer.save_pretrained(OUTPUT_DIR)        logging.info("✓ Tokenizer saved with model")        logging.info(f"\n🎉 All artifacts saved to: {OUTPUT_DIR}")    import mlflow    mlflow_run_id = None    if mlflow.last_active_run() is not None:        mlflow_run_id = mlflow.last_active_run().info.run_id    return mlflow_run_id

## Execute the distributed training[​](#execute-the-distributed-training "Direct link to Execute the distributed training")

This cell runs the training function on 8 H100 GPUs. The training typically takes 30-60 minutes depending on dataset size and compute availability. The function returns the MLflow run ID for model registration.

Python

    run_id = run_train.distributed()[0]

## Register model in Unity Catalog[​](#register-model-in-unity-catalog "Direct link to Register model in Unity Catalog")

Now you can register the fine-tuned model with MLflow and Unity Catalog for deployment.

**Important:** Given the size of the model (20B parameters), reconnect the notebook to **H100** accelerator before running the registration cells.

The registration process will:

1.  Load the base model and merge it with the fine-tuned LoRA adapters
2.  Create a text generation pipeline
3.  Log the model to MLflow with Unity Catalog registration

Python

    dbutils.widgets.dropdown("register_model", "False", ["True", "False"])register_model = dbutils.widgets.get("register_model")if register_model == "False":  dbutils.notebook.exit("Skipping model registration...")

## Check registration parameter[​](#check-registration-parameter "Direct link to Check registration parameter")

This cell checks the `register_model` parameter. If set to `False`, the notebook will skip model registration. You can change this parameter using the widget at the top of the notebook.

Python

    print("\nRegistering model with MLflow and Unity Catalog...")from transformers import AutoTokenizer, AutoModelForCausalLM, pipelinefrom peft import PeftModelimport mlflowimport torchtorch.cuda.empty_cache()# Load the trained model for registrationprint("Loading LoRA model for registration...")# For LoRA models, we need both base model and adapterbase_model = AutoModelForCausalLM.from_pretrained(    HF_MODEL_NAME,    trust_remote_code=True)# Load tokenizertokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)adapter_dir = OUTPUT_DIRpeft_model = PeftModel.from_pretrained(base_model, adapter_dir)# Merge LoRA into base and drop PEFT wrappersmerged_model = peft_model.merge_and_unload()components = {    "model": merged_model,    "tokenizer": tokenizer,}# Create Unity Catalog model namefull_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"print(f"Registering model as: {full_model_name}")text_gen_pipe = pipeline(    task="text-generation",    model=peft_model,    tokenizer=tokenizer,)input_example = ["Hello, world!"]with mlflow.start_run():    model_info = mlflow.transformers.log_model(        transformers_model=text_gen_pipe,   # 🚨 pass the pipeline, not just the model        artifact_path="model",        input_example=input_example,        # optional: save_pretrained=False for reference-only PEFT logging        # save_pretrained=False,    )# Start MLflow run and log modelprint(f"✓ Model successfully registered in Unity Catalog: {full_model_name}")print(f"✓ MLflow model URI: {model_info.model_uri}")print(f"✓ Model version: {model_info.registered_model_version}")# Print deployment informationprint(f"\n📦 Model Registration Complete!")print(f"Unity Catalog Path: {full_model_name}")print(f"Optimization: Liger Kernels + LoRA")

## Test multilingual reasoning capabilities[​](#test-multilingual-reasoning-capabilities "Direct link to Test multilingual reasoning capabilities")

The fine-tuned model has been trained on the Multilingual-Thinking dataset, which includes chain-of-thought reasoning in multiple languages.

The following cell demonstrates this capability by:

*   Setting the reasoning language to German
*   Providing a prompt in Spanish ("What is the capital of Australia?")
*   Observing that the model's internal reasoning is performed in German

Python

    REASONING_LANGUAGE = "German"SYSTEM_PROMPT = f"reasoning language: {REASONING_LANGUAGE}"USER_PROMPT = "¿Cuál es el capital de Australia?"  # Spanish for "What is the capital of Australia?"messages = [    {"role": "system", "content": SYSTEM_PROMPT},    {"role": "user", "content": USER_PROMPT},]input_ids = tokenizer.apply_chat_template(    messages,    add_generation_prompt=True,    return_tensors="pt",).to(merged_model.device)gen_kwargs = {"max_new_tokens": 512, "do_sample": True, "temperature": 0.6, "top_p": None, "top_k": None}output_ids = merged_model.generate(input_ids, **gen_kwargs)response = tokenizer.batch_decode(output_ids)[0]print(response)

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've fine-tuned and tested your model, you can:

*   **Deploy the model**: [Serve models with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
*   **Learn more about distributed training**: [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   **Optimize serverless GPU usage**: [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   **Troubleshoot issues**: [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   **Learn about OpenAI's gpt-oss**: [OpenAI fine-tuning cookbook](https://cookbook.openai.com/articles/gpt-oss/fine-tune-transfomers)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed fine-tuning of OpenAI gpt-oss-20b
