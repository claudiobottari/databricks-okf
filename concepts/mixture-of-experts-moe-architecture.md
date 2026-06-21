---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb609bdaa840de83fddeb8e4f28bf18d58126f285a59093b2d1f0ca29566bb40
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mixture-of-experts-moe-architecture
    - M(A
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Mixture-of-Experts (MoE) Architecture
description: A neural network architecture where only a subset of parameters (e.g., 10B active out of 122B total) are activated per inference, enabling compute-efficient reasoning and coding, exemplified by models like Qwen3.5.
tags:
  - llm-architecture
  - efficiency
  - ai-models
timestamp: "2026-06-18T11:39:13.974Z"
---

# Mixture-of-Experts (MoE) Architecture

**Mixture-of-Experts (MoE) Architecture** is a neural network design pattern that improves computational efficiency by activating only a subset of the model's total parameters for each input. Instead of routing every input through all parameters, an MoE model uses a routing mechanism to selectively activate only relevant "expert" sub-networks, while keeping the remaining parameters idle. This allows the model to maintain a large total parameter count while keeping the per-inference computational cost proportional to the number of active parameters. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## How MoE Works

An MoE layer consists of multiple feed-forward sub-networks called "experts" and a gating (routing) mechanism that determines which expert(s) to activate for a given input. For each token or input, the router computes a probability distribution over experts and activates only the top-k experts (typically one or two). The outputs of the selected experts are combined, weighted by the router's probabilities. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The key parameters that define an MoE model are:

- **Total parameters**: The sum of all parameters across every expert and the router.
- **Active parameters**: The number of parameters actually used during a single forward pass, equal to the parameters of the activated experts plus the router.

For example, a model with 122 billion total parameters might activate only 10 billion parameters per inference, meaning 112 billion parameters remain idle for that particular input. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Benefits

The primary benefit of MoE is the decoupling of model capacity from computational cost. A model with many experts can store a large amount of knowledge in its total parameter count, while the per-token cost remains proportional to the number of active parameters. This enables deploying very large models that would otherwise be prohibitively expensive for real-time inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Example: Qwen3.5 122B A10B

Alibaba Cloud's Qwen3.5 122B A10B is an example of a production MoE model. It has 122 billion total parameters but only 10 billion active parameters per inference. The model uses a 256K token context window and up to 8,000 output tokens. As a reasoning-only model, Qwen3.5 122B A10B always reasons before responding, and reasoning cannot be disabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Example: Qwen3-Next 80B A3B

The Qwen3-Next-80B-A3B-Instruct model uses an even more aggressive MoE ratio, with 80 billion total parameters and just 3 billion active parameters. This model is designed for instruction-following tasks and excels at handling ultra-long contexts, multi-step workflows, and retrieval-augmented generation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Example: Llama 4 Maverick

Meta's Llama 4 Maverick is the first model in the Llama family to use a mixture-of-experts architecture for compute efficiency. It supports multiple languages and is optimized for precise image and text understanding. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## MoE vs. Dense Models

In a traditional dense transformer architecture, all parameters are activated for every input. A dense model with N parameters always uses N parameters per forward pass. In an MoE architecture, the model can have many more total parameters than a dense model while maintaining the same or lower inference cost, because only a fraction of the parameters are active at any time. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Practical Considerations

### Expert Specialization

In practice, different experts learn to specialize in different types of inputs or tasks. For example, one expert might specialize in mathematical reasoning, another in code generation, and another in factual recall. The router learns to direct inputs to the most appropriate experts. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Routing Trade-offs

The router must make optimal choices to avoid common failure modes such as:

- **Load imbalance**: All inputs routing to the same expert, leaving other experts unused.
- **Expert collapse**: A subset of experts learning nothing useful while others do all the work.
- **Router oscillation**: The router frequently changing its decisions, leading to unstable training.

Advanced training techniques such as auxiliary loss functions and capacity factors are used to address these issues. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Limitations

MoE models can be more complex to train and serve than dense models of equivalent capacity. They require careful routing design and load-balancing during training. Additionally, MoE models may have higher memory requirements because the parameters of all experts must be kept in memory even though only a subset are active per inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks' API for serving MoE and other foundation models
- Transformer Architecture — The neural network architecture that underlies most MoE models
- [Model Serving](/concepts/model-serving.md) — Deploying and serving large models in production
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — A serving mode for production workloads that supports MoE models
- LLM Optimization — Techniques for improving large language model efficiency
- Qwen3.5 122B A10B — A specific MoE model available on Databricks

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
