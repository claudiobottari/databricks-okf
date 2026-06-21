---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad0f33032c66a9eab85552a7eebb73c7201f056faa474054870daf55072f6b8d
  pageDirectory: concepts
  sources:
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-optimization-information-api
    - MOIA
  citations:
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
title: Model Optimization Information API
description: API endpoint that returns whether a model is optimizable for provisioned throughput and its throughput_chunk_size, used to determine suitable throughput ranges.
tags:
  - databricks
  - api
  - optimization
timestamp: "2026-06-19T19:59:19.699Z"
---

# Model Optimization Information API

The **Model Optimization Information API** is a REST endpoint on Databricks that returns information about whether a foundation model is eligible for [Provisioned Throughput](/concepts/provisioned-throughput.md) deployment and, if so, provides the throughput capacity details needed to configure a serving endpoint.

## Endpoint

**`GET /api/2.0/serving-endpoints/get-model-optimization-info/{registered_model_name}/{version}`** ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Response Schema

The API returns a JSON object with the following fields:

| Field | Type | Description |
|---|---|---|
| `optimizable` | boolean | Whether the model is eligible for provisioned throughput. |
| `model_type` | string | The model architecture (e.g., `llama`, `gte`). |
| `throughput_chunk_size` | integer | The base increment of tokens per second for the model. |

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Example Response

For an eligible model:

```json
{
  "optimizable": true,
  "model_type": "llama",
  "throughput_chunk_size": 980
}
```

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Usage

Use the API in the following flow:

1. Call `get-model-optimization-info` with the registered model name and version.
2. If `optimizable` is `false`, the model is not eligible for provisioned throughput.
3. If `optimizable` is `true`, use `throughput_chunk_size` to calculate the `min_provisioned_throughput` and `max_provisioned_throughput` values for the [Model Serving Endpoint](/concepts/model-serving-endpoint.md) creation request.

Calculations: ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

```python
chunk_size = optimizable_info['throughput_chunk_size']
min_provisioned_throughput = 2 * chunk_size
max_provisioned_throughput = 3 * chunk_size
```

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Dedicated inference capacity for foundation models with performance guarantees.
- [Model Units](/concepts/model-units.md) – The unit of throughput allocation for provisioned endpoints.
- Serving endpoint – The endpoint configuration that specifies provisioned throughput ranges.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The broader deployment framework that includes this optimization API.

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md

# Citations

1. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
