---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ce88232c14815c69d97e8683342815e3ff7592eb895df7eea12aeb1d767e2af
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-processing-asymmetry
    - TPA
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
title: Token Processing Asymmetry
description: The concept that generating output tokens is significantly more resource-intensive than processing input tokens during model inference.
tags:
  - machine-learning
  - inference
  - performance
timestamp: "2026-06-19T19:45:23.620Z"
---

# Token Processing Asymmetry

**Token Processing Asymmetry** is the property of large language model inference where **generating output tokens** is significantly more resource-intensive than **processing input tokens**, and where the computational cost scales non-linearly with token counts. This asymmetry directly affects how many requests a [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoint can handle for a given number of [Model Units](/concepts/model-units.md).

## Overview

When a provisioned throughput endpoint processes a request, the total work required depends on both the number of input tokens and the number of generated output tokens. The workload is not symmetric: generating output tokens consumes more resources than processing input tokens. Furthermore, the required work grows in a non-linear fashion as either the input or output token count increases. This means that, for a fixed allocation of model units, an endpoint can handle either multiple small requests concurrently or fewer long-context requests before exhausting its capacity. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Details

The asymmetry originates from the autoregressive nature of text generation. During input processing (prefill), the model processes all input tokens in parallel. During output generation (decode), tokens are produced one at a time, and each step requires a full forward pass, making output generation compute-bound. Combined with attention mechanisms that scale quadratically with sequence length, the cost rises non-linearly as the total context window grows. The source documentation emphasizes this asymmetry directly:

> “Generating output tokens is more resource-intensive than processing input tokens. The work required for each request grows in a non-linear fashion as the input or output token counts increase.”

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Implications for Capacity Planning

Because of token processing asymmetry, estimating endpoint capacity requires modelling both the typical input length and the expected output length. A model unit allocation that comfortably serves many short prompts may struggle with a few long-context prompts. The documentation provides a reference example: for a medium-sized workload with 3,500 input tokens and 300 output tokens on Llama 4 Maverick, 50 model units yield an estimated 3,250 tokens per second. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

### Legacy Models

Some legacy model families (Meta Llama 3, 3.1, 3.2, 3.3, GTE, BGE, DeepSeek R1, DBRX, Mistral, Mixtral, MPT) provision inference capacity based on tokens per second ranges rather than model units. While the specific units differ, the underlying token processing asymmetry still governs their behaviour. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Model Units](/concepts/model-units.md) – The unit of throughput for provisioned endpoints.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Endpoints that allocate dedicated capacity via model units.
- [Tokens per Second](/concepts/tokens-per-second-as-a-scaling-metric.md) – Direct throughput measure used by legacy models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API tier to which this asymmetry applies.
- Autoregressive Decoding – The generation mechanism that causes the asymmetry.

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
