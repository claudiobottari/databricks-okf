---
title: Fine-tune OpenAI's GPT-OSS 120B model using distributed training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-gpt-oss-120b-ddp-fsdp
ingestedAt: "2026-06-18T08:08:58.154Z"
---

This notebook demonstrates supervised fine-tuning (SFT) of the large 120B parameter GPT-OSS model on 8 H100 GPUs using Databricks Serverless GPU Compute. The training leverages:

*   **FSDP (Fully Sharded Data Parallel)**: Shards model parameters, gradients, and optimizer states across GPUs to enable training of large models that don't fit on a single GPU.
*   **DDP (Distributed Data Parallel)**: Distributes training across multiple GPUs for faster training.
*   **LoRA (Low-Rank Adaptation)**: Reduces the number of trainable parameters by adding small adapter layers, making fine-tuning more efficient.
*   **TRL (Transformers Reinforcement Learning)**: Provides the SFTTrainer for supervised fine-tuning.

By setting `remote=False` and specifying 16 GPUs, this can be extended to multi-node training across 16 GPUs.

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook runs on Databricks Serverless GPU compute with H100 accelerators. To connect:

1.  From the compute selector in the top right, select **Serverless GPU**.
2.  In the **Environment** panel on the right, select **H100** as the accelerator (8 H100 chips on a single node).
3.  Set the **Environment version** to **4**.
4.  Click **Apply**.

This notebook does not use a base environment; it installs its required libraries in the next cell.

## Install required packages[​](#install-required-packages "Direct link to Install required packages")

Install the necessary libraries for distributed training and model fine-tuning:

*   `trl`: Transformers Reinforcement Learning library for SFT training
*   `peft`: Parameter-Efficient Fine-Tuning for LoRA adapters
*   `transformers`: Hugging Face transformers library
*   `datasets`: For loading training datasets
*   `accelerate`: For distributed training orchestration
*   `hf_transfer`: For faster model downloads from Hugging Face

Python

    %pip install "trl==1.1.0"%pip install "peft==0.19.1"%pip install "transformers==5.5.4"%pip install "fsspec==2024.9.0"%pip install "huggingface_hub==1.11.0"%pip install "datasets==3.2.0"%pip install "accelerate==1.13.0"%restart_python

## Define the distributed training function with FSDP[​](#define-the-distributed-training-function-with-fsdp "Direct link to Define the distributed training function with FSDP")

This cell defines the training function that will run on 8 H100 GPUs using the `@distributed` decorator. The function includes:

*   **Model loading**: Loads the 120B parameter GPT-OSS model in bfloat16 precision
*   **LoRA configuration**: Applies Low-Rank Adaptation with rank 16 to reduce trainable parameters
*   **FSDP setup**: Configures Fully Sharded Data Parallel with automatic layer wrapping and activation checkpointing
*   **Training configuration**: Sets batch size, learning rate, gradient accumulation, and other hyperparameters
*   **Dataset**: Uses the HuggingFaceH4/Multilingual-Thinking dataset for fine-tuning

The function automatically detects transformer block classes for FSDP wrapping and handles distributed training coordination across all GPUs.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "gpt-oss-120b-peft")dbutils.widgets.text("uc_volume", "checkpoints")dbutils.widgets.text("model", "openai/gpt-oss-120b")dbutils.widgets.text("dataset_path", "HuggingFaceH4/Multilingual-Thinking")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")UC_VOLUME = dbutils.widgets.get("uc_volume")HF_MODEL_NAME = dbutils.widgets.get("model")DATASET_PATH = dbutils.widgets.get("dataset_path")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"HF_MODEL_NAME: {HF_MODEL_NAME}")print(f"DATASET_PATH: {DATASET_PATH}")OUTPUT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"print(f"OUTPUT_DIR: {OUTPUT_DIR}")

Python

    from serverless_gpu import distributed@distributed(gpus=8, gpu_type='H100')def train_gpt_oss_fsdp_120b():    """    Fine-tune a 120B-class model with TRL SFTTrainer + FSDP2 on H100s.    Uses LoRA + activation ckpt + full_shard auto_wrap.    """    # --- imports inside for pickle safety ---    import os, torch, torch.distributed as dist    from transformers import AutoModelForCausalLM, AutoTokenizer, Mxfp4Config    from trl import SFTTrainer, SFTConfig    from datasets import load_dataset    from peft import LoraConfig, get_peft_model    # ---------- DDP / CUDA binding ----------    local_rank = int(os.environ.get("LOCAL_RANK", "0"))    torch.cuda.set_device(local_rank)    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")    os.environ.setdefault("NCCL_DEBUG", "WARN")    os.environ.setdefault("CUDA_LAUNCH_BLOCKING", "0")    os.environ.setdefault("TORCH_NCCL_ASYNC_ERROR_HANDLING", "1")  # replaces NCCL_ASYNC_ERROR_HANDLING    # ---------- Config ----------    MAX_LENGTH = 2048    PER_DEVICE_BATCH = 1                 # start conservative for 120B    GRAD_ACCUM = 4                       # tune for throughput    LR = 1.5e-4    EPOCHS = 1    is_main  = int(os.environ.get("RANK", "0")) == 0    world_size = int(os.environ.get("WORLD_SIZE", "1"))    if is_main:        print("=" * 60)        print("FSDP (full_shard) launch for 120B")        print(f"WORLD_SIZE={world_size} | LOCAL_RANK={local_rank}")        print("=" * 60)    # ---------- Tokenizer ----------    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)    if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:        tokenizer.pad_token = tokenizer.eos_token    tokenizer.model_max_length = MAX_LENGTH    tokenizer.truncation_side = "right"    # ---------- Model ----------    # IMPORTANT: no device_map, no .to(device) — let Trainer/Accelerate+FSDP handle placement    # low_cpu_mem_usage helps with massive checkpoints (still needs decent host RAM)    quantization_config = Mxfp4Config(dequantize=True)    model = AutoModelForCausalLM.from_pretrained(        HF_MODEL_NAME,        dtype=torch.bfloat16,        attn_implementation="eager",        quantization_config=quantization_config,        use_cache=False,                  # needed for grad ckpt        low_cpu_mem_usage=True,    )    # ---------- LoRA ----------    # the following config works    # include MoE layers as well.    peft_config = LoraConfig(        r=32,        lora_alpha=32,        target_modules="all-linear",        rank_pattern={            "mlp.experts.gate_up_proj": 8,            "mlp.experts.down_proj": 8        },        target_parameters=["mlp.experts.gate_up_proj", "mlp.experts.down_proj"],        lora_dropout=0.0,        bias="none",        task_type="CAUSAL_LM",    )    model = get_peft_model(model, peft_config)    # Cast all parameters to bfloat16 so FSDP sees a uniform dtype    # (LoRA adapters are initialized in float32 by default)    model = model.to(torch.bfloat16)    if is_main:        model.print_trainable_parameters()    # ---------- Data ----------    dataset = load_dataset("HuggingFaceH4/Multilingual-Thinking", split="train")    if is_main:        print(f"Dataset size: {len(dataset)}")    # ---------- FSDP settings ----------    def infer_transformer_blocks_for_fsdp(model):        COMMON = {            "LlamaDecoderLayer", "MistralDecoderLayer", "MixtralDecoderLayer",            "Qwen2DecoderLayer", "Gemma2DecoderLayer", "Phi3DecoderLayer",            "GPTNeoXLayer", "MPTBlock", "BloomBlock", "FalconDecoderLayer",            "DecoderLayer", "GPTJBlock", "OPTDecoderLayer"        }        hits = set()        for _, m in model.named_modules():            name = m.__class__.__name__            if name in COMMON:                hits.add(name)        # Fallback: grab anything that *looks* like a decoder block        if not hits:            for _, m in model.named_modules():                name = m.__class__.__name__                if any(s in name for s in ["Block", "DecoderLayer", "Layer"]) and "Embedding" not in name:                    hits.add(name)        return sorted(hits)    fsdp_wrap_classes = infer_transformer_blocks_for_fsdp(model)    if not fsdp_wrap_classes:        raise RuntimeError("Could not infer transformer block classes for FSDP wrapping; "                       "print(model) and add the block class explicitly.")    training_args = SFTConfig(        output_dir=OUTPUT_DIR,        num_train_epochs=EPOCHS,        per_device_train_batch_size=PER_DEVICE_BATCH,        gradient_accumulation_steps=GRAD_ACCUM,        learning_rate=LR,        warmup_ratio=0.03,        lr_scheduler_type="cosine",        bf16=True,        logging_steps=5,        logging_strategy="steps",        save_strategy="no",        report_to="none",        ddp_find_unused_parameters=False,        dataloader_pin_memory=True,        max_length=MAX_LENGTH,        gradient_checkpointing=False,        # ---- FSDP2 knobs ----        fsdp="full_shard auto_wrap",        fsdp_config={            "version": 2,            "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,            "reshard_after_forward": True,            "activation_checkpointing": True,    # <- use activation ckpt (not gradient)            "xla": False,            "limit_all_gathers": True,        },    )    # ---------- Trainer ----------    trainer = SFTTrainer(        model=model,        args=training_args,        train_dataset=dataset,        processing_class=tokenizer,    )    # verify distributed init & FSDP    rank = int(os.getenv("RANK", "0"))    print(f"[rank {rank}] dist.is_initialized() -> {dist.is_initialized()}")    acc = getattr(trainer, "accelerator", None)    print(f"[rank {rank}] accelerator.distributed_type = {getattr(getattr(acc,'state',None),'distributed_type','n/a')}")    print(f"[rank {rank}] accelerator.num_processes = {getattr(acc, 'num_processes', 'n/a')}")    # ---------- Train ----------    result = trainer.train()    if is_main:        print("\nTraining complete (FSDP).")        print(result.metrics)

## Run the distributed training job[​](#run-the-distributed-training-job "Direct link to Run the distributed training job")

Execute the training function on 8 H100 GPUs. The `@distributed` decorator handles the orchestration of launching the training across all GPUs with proper distributed setup.

Python

    train_gpt_oss_fsdp_120b.distributed()

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [Best practices for Serverless GPU Compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on Serverless GPU Compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [PEFT documentation](https://huggingface.co/docs/peft/index)
*   [TRL documentation](https://huggingface.co/docs/trl/index)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Fine-tune OpenAI's GPT-OSS 120B model using distributed training
