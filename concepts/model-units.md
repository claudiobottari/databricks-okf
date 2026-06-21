---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdb2cf4b91b1dbb85a63ae30311d936a96bc35225d15561d15c89397d89a5fcc
  pageDirectory: concepts
  sources:
    - model-units-in-provisioned-throughput-databricks-on-aws.md
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-units
  citations:
    - file: model-units-in-provisioned-throughput-databricks-on-aws.md
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
title: Model Units
description: A unit of throughput that determines how much work a provisioned throughput endpoint can handle per minute, used to allocate inference capacity for foundation models.
tags:
  - machine-learning
  - inference
  - capacity-planning
timestamp: "2026-06-19T19:45:17.849Z"
---

# Model Units

**Model units** are a unit of throughput that determines how much work a provisioned throughput model serving endpoint can handle per minute. When you create a provisioned throughput endpoint, you specify how many model units to allocate for each model served. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## How Work is Measured

The amount of work required to process each request depends on both the input and generated output token counts. As the number of input and output tokens increases, the work required to process a request also increases. Generating output tokens is more resource-intensive than processing input tokens. The required work grows in a non-linear fashion as input or output token counts increase. ^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Capacity Implications

For a given number of model units, an endpoint can handle either:

- **Multiple small requests** at the same time.
- **Fewer long-context requests** at a time before exhausting capacity.

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Throughput Estimation

The estimated tokens per second throughput varies by model and model unit count. For example, with a medium-sized workload of 3,500 input tokens and 300 output tokens:

| Model | Model Units | Estimated Tokens per Second |
|-------|-------------|----------------------------|
| Llama 4 Maverick | 50 | 3,250 |

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Models Using Model Units

Most foundation models supported for provisioned throughput provision inference capacity using model units. The following legacy model families are exceptions — they provision throughput based on tokens per second ranges instead:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1
- Meta Llama 3
- Meta Llama 2
- DBRX
- Mistral
- Mixtral
- MPT

^[model-units-in-provisioned-throughput-databricks-on-aws.md]

## Provisioned Throughput and Model Units

When you create a [Provisioned Throughput Foundation Model API](/concepts/provisioned-throughput-foundation-model-apis.md) endpoint, you allocate dedicated inference capacity in chunks of model units. The number of model units you allocate determines the throughput you purchase for your production GenAI application. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Provisioned throughput is available in increments of tokens per second, with specific increments varying by model. The model optimization information API returns a `throughput_chunk_size` value that indicates the increment size for a given model. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Specifying Throughput via API

When deploying using the REST API, you specify `min_provisioned_throughput` and `max_provisioned_throughput` fields. To identify the suitable range, call the model optimization information API, which returns whether the model is optimizable and its `throughput_chunk_size`. You then set your throughput values as multiples of this chunk size. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Example response from the optimization API:
```json
{
  "optimizable": true,
  "model_type": "llama",
  "throughput_chunk_size": 980
}
```

### UI Configuration

In the serving UI, you configure the maximum tokens per second throughput for your endpoint via a dropdown. Provisioned throughput endpoints support automatic scaling, so you can also set a minimum throughput value to which the endpoint can scale down. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- [Foundation Model Serving on Databricks](/concepts/foundation-model-serving-endpoints-databricks.md)
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Tokens per Second](/concepts/tokens-per-second-as-a-scaling-metric.md)

## Sources

- model-units-in-provisioned-throughput-databricks-on-aws.md
- provisioned-throughput-foundation-model-apis-databricks-on-aws.md

# Citations

1. [model-units-in-provisioned-throughput-databricks-on-aws.md](/references/model-units-in-provisioned-throughput-databricks-on-aws-36ed2584.md)
2. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
