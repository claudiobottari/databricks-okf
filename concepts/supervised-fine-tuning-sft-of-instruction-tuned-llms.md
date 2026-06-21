---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8aa7f54e90d58fabd8cb61eda2052b63eb3379c162f16b94b4a4b97501b24636
  pageDirectory: concepts
  sources:
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-of-instruction-tuned-llms
    - SF(OIL
  citations:
    - file: multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) of Instruction-Tuned LLMs
description: A training technique where a causal language model is fine-tuned on instruction-response pairs (e.g., Alpaca dataset) by tokenizing prompt-response sequences with EOS tokens and training with standard causal LM loss, often using FSDP for 8B+ parameter models.
tags:
  - fine-tuning
  - llm
  - nlp
timestamp: "2026-06-19T19:48:23.808Z"
---

# Supervised Fine-Tuning (SFT) of Instruction-Tuned LLMs

**Supervised Fine-Tuning (SFT)** is a training stage in which a pre-trained large language model (LLM) is further trained on a dataset of instruction–response pairs to improve its ability to follow user instructions. This page describes a concrete implementation of SFT for an 8‑billion-parameter model (Llama‑3.1‑8B) using PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) across 16 H100 GPUs spread over two nodes, orchestrated with Databricks AI Runtime and the `air` CLI. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Overview

The example workload performs supervised fine-tuning of the gated [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) model on the [tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) instruction dataset. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md] FSDP shards model parameters, gradients, and optimizer states across all 16 GPU ranks so that the 8B‑parameter model and its optimizer state fit comfortably in GPU memory. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

The workload accomplishes the following:
- Uploads the local project as a `snapshot`.
- Launches one process per GPU with `torchrun`, using rendezvous environment variables set automatically by AI Runtime on each node.
- Reads the gated model from Hugging Face using a Databricks secret.
- Logs metrics to [MLflow](/concepts/mlflow.md) and writes the consolidated checkpoint to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Prerequisites

Before running the SFT workload, the following must be in place:

- The `air` CLI installed and authenticated. (See [Install the AI Runtime CLI](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation).)
- A Unity Catalog volume with write access for the output checkpoint.
- Access to the gated model on Hugging Face and a Hugging Face access token stored as a Databricks secret.

### Getting access to the model

Llama‑3.1‑8B is a gated model. To download it:
1. Open the model page at [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B), accept the license, and wait until access is granted.
2. Create a [Hugging Face access token](https://huggingface.co/docs/hub/en/security-tokens) with **read** permission.

### Storing the token

The workload reads the token from a [Databricks Secret](/concepts/databricks-secret-scopes.md) instead of hard‑coding it. Create a secret scope and add the token:

```bash
databricks secrets create-scope my_scope
databricks secrets put-secret my_scope hf_token
```

The workload YAML references it as `my_scope/hf_token` under the `secrets` block. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Project Layout

The example project consists of two files in a directory named `multinode_llm_sft/`:

- `train.yaml` – the AI Runtime workload configuration (inline dependencies, `torchrun` launcher, compute resources, hyperparameters).
- `train.py` – the FSDP fine‑tuning script. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Workload Configuration (`train.yaml`)

The YAML file requests 16 GPUs as two `GPU_8xH100` nodes, mounts the Hugging Face token as a secret, and passes hyperparameters to the script through the `parameters` block. Dependencies are declared inline under `environment` (with the AI Runtime client image version). ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

Key sections of the configuration:

| Section | Description |
|---------|-------------|
| `experiment_name` | Name of the [MLflow Experiment](/concepts/mlflow-experiment.md) for logging metrics. |
| `compute` | `num_accelerators: 16`, `accelerator_type: GPU_8xH100` (8 H100 GPUs per node). |
| `command` | Invokes `torchrun` with the rendezvous environment variables (`NUM_NODES`, `NODE_RANK`, `LOCAL_WORLD_SIZE`, `MASTER_ADDR`, `MASTER_PORT`) set by AI Runtime on each node. |
| `env_variables` | `NCCL_SOCKET_IFNAME: eth0` to pin NCCL control‑plane traffic to the correct interface. `HF_HOME: /tmp/hf` for Hugging Face cache. |
| `secrets` | Maps `HF_TOKEN` to a Databricks secret (e.g., `my_scope/hf_token`). |
| `parameters` | Model name, dataset name, `max_seq_len`, batch size, gradient accumulation steps, learning rate, `max_steps`, and output directory (a Unity Catalog volume). |

The inline command runs `torchrun` directly; no separate launcher script is required because AI Runtime supplies the rendezvous environment variables. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Training Script (`train.py`)

The training script initialises the [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) process group, wraps each transformer block in FSDP, trains on a tokenised instruction dataset, and saves a consolidated checkpoint from rank 0. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### FSDP wrapping

Each `LlamaDecoderLayer` is wrapped independently so that no single GPU holds the full model. The script uses `FULL_SHARD` sharding strategy and bfloat16 mixed precision:

```python
auto_wrap_policy = functools.partial(
    transformer_auto_wrap_policy, transformer_layer_cls={LlamaDecoderLayer})
model = FSDP(
    model,
    auto_wrap_policy=auto_wrap_policy,
    sharding_strategy=ShardingStrategy.FULL_SHARD,
    mixed_precision=MixedPrecision(
        param_dtype=torch.bfloat16,
        reduce_dtype=torch.bfloat16,
        buffer_dtype=torch.bfloat16,
    ),
    device_id=local_rank,
    use_orig_params=True,
)
```

Gradient checkpointing is enabled (`model.gradient_checkpointing_enable()`) to reduce memory usage during the forward pass. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Dataset preparation

The script loads the instruction dataset using the `datasets` library, formats each example as a prompt/response string with an EOS token, and tokenises it to a fixed length (`max_seq_len`). The tokenised columns (`input_ids`, `attention_mask`, `labels`) are stored as Torch tensors for efficient collation. A `DistributedSampler` ensures each rank processes a different subset of the data. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Training loop

The loop runs for `max_steps` steps, accumulating gradients over `gradient_accumulation_steps` micro‑batches before each optimizer step. Gradients are clipped to a norm of 1.0. Loss values are printed on rank 0 and, if an MLflow Run ID is present, logged to MLflow. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Checkpoint saving

After training, rank 0 gathers the full state dictionary (offloaded to CPU) and writes a consolidated checkpoint to the Unity Catalog volume using `save_pretrained`:

```python
save_policy = FullStateDictConfig(offload_to_cpu=True, rank0_only=True)
with FSDP.state_dict_type(model, StateDictType.FULL_STATE_DICT, save_policy):
    cpu_state = model.state_dict()
if rank == 0:
    model.module.save_pretrained(output_dir, state_dict=cpu_state)
    tokenizer.save_pretrained(output_dir)
```

A barrier synchronisation ensures all ranks complete before destroying the process group. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Submitting and Monitoring the Run

The run is submitted with the `air` CLI:

```bash
air run -f train.yaml --dry-run   # validate configuration
air run -f train.yaml --watch     # submit and watch logs
```

Distributed runs span multiple nodes. Logs can be inspected per node:

```
air get run <run-id>
air logs <run-id> --node 0
air logs <run-id> --node 1
```

Metrics and parameters appear in the MLflow experiment named in `train.yaml`. The fine‑tuned checkpoint is written to the Unity Catalog volume path specified in `parameters.output_dir`. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

---

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Unity Catalog Volumes
- Databricks Secrets
- torchrun
- H100 GPU Support on Databricks
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

---

## Sources

- multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md

# Citations

1. [multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md](/references/multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws-d26ca320.md)
