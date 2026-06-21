---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfea598c996911c6d6f8053fc6ca3077a2fc5c0b399821062ad1ec54b706ca49
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-linear-token-work-scaling
    - NTWS
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
title: Non-linear Token Work Scaling
description: The principle that computational work required for inference grows non-linearly as input or output token counts increase, rather than scaling linearly.
tags:
  - machine-learning
  - inference
  - scaling
timestamp: "2026-06-19T19:45:14.664Z"
---

# Non-linear Token Work Scaling

**Non-linear Token Work Scaling** is a property of provisioned throughput endpoints in Databricks Foundation Model APIs where the computational work required to process a request grows non-linearly as input or output token counts increase. This means that the relationship between token volume and computational resources is not proportional, affecting how many concurrent requests an endpoint can handle.^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Overview

When serving models through provisioned throughput endpoints, the work required to process each request depends on both the input and generated output token counts. As these token counts increase, the computational demand grows in a non-linear fashion. This non-linearity means that a given allocation of [Model Units](/concepts/model-units.md) can support either multiple small requests or fewer long-context requests simultaneously.^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Key Characteristics

### Resource Intensity of Output Tokens

Generating output tokens is more resource-intensive than processing input tokens. This asymmetry means that endpoints with high output generation requirements consume proportionally more capacity per request compared to input-heavy workloads.^[model-units-in-provisioned-throughput-databricks-on-aws.md]

### Capacity Trade-offs

Due to non-linear scaling, a fixed number of model units can handle:

- **Multiple small requests** at a time (low input and output tokens).
- **Fewer long-context requests** at a time before capacity is exhausted.

For example, with a medium-sized workload of 3,500 input tokens and 300 output tokens, 50 model units of Llama 4 Maverick can sustain an estimated 3,250 tokens per second.^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Practical Implications

When provisioning [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md), users must account for the non-linear scaling behavior. Workloads with long input contexts or large output generations require significantly more model units per request than short-context workloads. This makes accurate capacity planning essential for cost-effective deployment.^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Model Units](/concepts/model-units.md) — The unit of throughput that determines endpoint capacity.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Endpoints that provision inference capacity using model units.
- [Foundation model serving](/concepts/foundation-model-serving-modes.md) — The broader framework for deploying and serving models.
- [Token-based pricing](/concepts/pay-per-token-pricing.md) — Pricing models that account for token volume and processing costs.

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
