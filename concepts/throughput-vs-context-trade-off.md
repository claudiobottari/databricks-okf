---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 234d51ccb745925e124c23a93d4fe865df5fb530cd66ae16281534fcee84719c
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - throughput-vs-context-trade-off
    - TVCT
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
title: Throughput vs Context Trade-off
description: The capacity trade-off where a fixed number of model units can handle either many small requests simultaneously or fewer long-context requests before exhausting capacity.
tags:
  - machine-learning
  - inference
  - capacity-planning
timestamp: "2026-06-19T19:45:19.016Z"
---

# Throughput vs Context Trade-off

**Throughput vs Context Trade-off** describes the inverse relationship between the number of input and output tokens per request and the number of requests a [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) can handle per minute for a given number of [Model Units](/concepts/model-units.md). As the context size (input plus output tokens) increases, the amount of work required to process each request grows, reducing the maximum concurrency the endpoint can support. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## How Model Units Measure Work

When you create a provisioned throughput endpoint, you specify a number of **model units** that determine the endpoint's capacity. The work required to process a request depends on both the input and generated output tokens. Generating output tokens is more resource-intensive than processing input tokens, and the work grows in a non‑linear fashion as either token count increases. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

For a fixed allocation of model units, the endpoint can therefore handle either:

- **Multiple small requests** at a time (short input and output tokens), or
- **Fewer long‑context requests** at a time before reaching capacity.

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Example Throughput Estimates

The following table shows an example throughput estimate for a medium‑sized workload with 3,500 input tokens and 300 output tokens:

| Model                | Model Units | Estimated Tokens per Second |
|----------------------|-------------|-----------------------------|
| Llama 4 Maverick      | 50          | 3,250                       |

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

If the same 50 model units were used for requests with significantly longer contexts (e.g., 32K input tokens), the estimated tokens per second would be lower because fewer requests could be processed concurrently.

## Scope of the Trade-off

The trade‑off applies to all foundation models supported for provisioned throughput except legacy model families that provision throughput based on tokens‑per‑second ranges instead of model units. Legacy models such as Meta Llama 3, Llama 3.1, Llama 3.2 (1B/3B), Llama 3.3, DBRX, Mistral, Mixtral, MPT, DeepSeek R1, GTE v1.5, and BGE v1.5 are excluded from this mechanism. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Dedicated inference capacity for foundation models.
- [Model Units](/concepts/model-units.md) – The throughput unit that defines how much work an endpoint can handle.
- [Foundation model serving](/concepts/foundation-model-serving-modes.md) – Deployment and management of LLMs for inference.
- Context window – The maximum number of tokens a model can process in a single request.

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
