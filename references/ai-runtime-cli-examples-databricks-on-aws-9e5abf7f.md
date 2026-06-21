---
title: AI Runtime CLI examples | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/
ingestedAt: "2026-06-18T08:08:06.881Z"
---

The following examples are complete, end-to-end workloads you submit from the `air` CLI with `air run -f train.yaml`. Each shows a real distributed-training pattern on H100 GPUs, including the workload YAML, launcher script, and training code. Start with the [quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart) if you haven't submitted a run before.

*   *   [Multi-node LLM fine-tuning with FSDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/multinode-llm-sft)
    *   Supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun` and PyTorch Fully Sharded Data Parallel (FSDP). Logs to MLflow and checkpoints to a Unity Catalog volume.
*   *   [Distributed training with Ray Train](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/ray-train-distributed)
    *   Distributed data-parallel fine-tuning with Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU.
