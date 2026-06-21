---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11fd8cffec3cbe69f868b29ee0c7e412a83d8a2daa19b2d8a823d791d98e716d
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-endpoint
    - PTE
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
title: Provisioned Throughput Endpoint
description: A Databricks serving endpoint type that reserves dedicated inference capacity for foundation models, configured using model units or tokens per second.
tags:
  - machine-learning
  - inference
  - databricks
timestamp: "2026-06-19T19:45:28.297Z"
---

# Provisioned Throughput Endpoint

**Provisioned Throughput Endpoint** is a type of model serving endpoint on Databricks that allows you to reserve a fixed amount of inference capacity for a foundation model, measured in [Model Units](/concepts/model-units.md). When you create such an endpoint, you specify the number of model units to provision for each model served, and Databricks guarantees that capacity is available for handling incoming requests. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## How Model Units Determine Throughput

Model units are a unit of throughput that determine how much work your endpoint can handle per minute. The amount of work required to process each request depends on both the size of the input tokens and the generated output tokens. Generating output tokens is more resource-intensive than processing input tokens, and the work required grows in a non‑linear fashion as token counts increase. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

For a given number of model units, your endpoint can handle either:

- **Multiple small requests** at a time.
- **Fewer long‑context requests** at a time before it runs out of capacity.

### Example Throughput Estimate

For a medium‑sized workload with 3,500 input tokens and 300 output tokens, a Llama 4 Maverick model with 50 model units is estimated to deliver approximately 3,250 tokens per second. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Models That Use Model Units

All foundation models supported for provisioned throughput use model units to provision inference capacity, with the exception of the following legacy model families, which instead provision capacity based on tokens‑per‑second ranges configured during endpoint creation:

- Meta Llama 3.3, 3.2 (3B and 1B), 3.1, 3, and 2
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1
- DBRX
- Mistral
- Mixtral
- MPT

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Model Units](/concepts/model-units.md)
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- [Foundation Model Serving Endpoint](/concepts/foundation-model-serving-endpoints.md)
- Token-Based Workload Estimation

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
