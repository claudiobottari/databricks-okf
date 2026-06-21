---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56474139fe3db18f5b1c6c552ec0976cff6efc6e44fc3370757e72a98854e9cd
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-foundation-model-families
    - LFMF
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
title: Legacy Foundation Model Families
description: Legacy model families (e.g., Meta Llama 2/3, DBRX, Mistral) on Databricks that provision inference capacity based on tokens per second ranges rather than model units.
tags:
  - machine-learning
  - models
  - legacy
timestamp: "2026-06-19T19:45:21.914Z"
---

# Legacy Foundation Model Families

**Legacy Foundation Model Families** refer to a set of older model architectures that, when deployed through [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoints on Databricks, provision inference capacity using **tokens per second (TPS) ranges** rather than the newer **[Model Units](/concepts/model-units.md)** system. These families are listed in the Databricks documentation alongside the note that "all foundation models supported for provisioned throughput provision inference capacity using model units, with the exception of the legacy models listed below." ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## List of Legacy Families

The following model families are considered legacy and use token‑per‑second provisioning:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- Meta Llama 3
- Meta Llama 2
- DBRX
- Mistral
- Mixtral
- MPT
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## How Provisioning Differs

For legacy families, users specify **tokens per second ranges** during [Endpoint Creation](/concepts/endpoint-creation-interfaces.md) instead of a discrete number of model units. This means the endpoint capacity is measured and priced in terms of the sustained throughput of tokens (input plus output) per second, rather than the abstract work units used for newer models. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

The legacy approach predates the model‑unit abstraction, which was introduced to provide a simpler and more consistent way to describe capacity across different model sizes and request patterns. For non‑legacy models, throughput is expressed as an estimated number of model units; legacy models continue to use the older tokens‑per‑second model. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Special Note on DeepSeek R1

DeepSeek R1 is listed among the legacy families, but with the additional annotation that it is **not available in [Unity Catalog](/concepts/unity-catalog.md)**. This means that if you are managing models through Unity Catalog, DeepSeek R1 cannot be served via provisioned throughput under that regime. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Model Units](/concepts/model-units.md) – The newer capacity metric used by non‑legacy models.
- [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) – How endpoints are created and scaled.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overall API for deploying foundation models.
- [Tokens per Second](/concepts/tokens-per-second-as-a-scaling-metric.md) – The capacity metric used by legacy families.
- [Unity Catalog](/concepts/unity-catalog.md) – Model governance catalog that excludes DeepSeek R1.

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
