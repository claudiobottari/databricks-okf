---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88657dd6f67883f5905aa6ed53be97a025e5629b6f33fbffd9648b928ee38b3c
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - direct-model-query
    - DMQ
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Direct Model Query
description: The ability to bypass traffic splitting rules and query a specific served model directly on a multi-model endpoint using a dedicated invocation URL.
tags:
  - model-serving
  - api
  - databricks
timestamp: "2026-06-19T23:03:17.916Z"
---

# Direct Model Query

**Direct Model Query** is a feature of [Databricks Model Serving](/concepts/databricks-model-serving.md) that allows you to bypass the endpoint's traffic split configuration and send requests directly to a specific served model deployed behind a multi-model endpoint. This capability is particularly useful for testing, debugging, and A/B experimentation workflows. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) serves multiple models, the endpoint distributes incoming traffic according to the configured [Traffic Split](/concepts/traffic-splitting-between-models.md). The Direct Model Query feature provides an alternative way to access individual models by targeting them directly through a dedicated URL path, ignoring the traffic settings entirely. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## API Endpoint

To query an individual model behind a multi-model endpoint, use the following URL structure:

```
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

### Parameters

- `{endpoint-name}`: The name of the [Model Serving Endpoint](/concepts/model-serving-endpoint.md).
- `{served-model-name}`: The name of the specific served entity (model) you want to query.

### Behavior

- The request format is identical to querying the endpoint directly. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]
- The traffic split configuration is **ignored** — all requests sent to this URL are served exclusively by the specified model. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]
- This does not affect the normal traffic routing for other requests to the endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Example

For a multi-model endpoint named `multi-model` with served entities `current` and `challenger`, sending all requests to:

```
/serving-endpoints/multi-model/served-models/challenger/invocations
```

results in all those requests being handled by the `challenger` served model, regardless of the endpoint's traffic split configuration. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Cases

- **Testing new model versions** — Directly query a candidate model without routing production traffic to it. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Debugging** — Isolate a single model for troubleshooting without interference from traffic routing. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]
- **A/B testing** — Programmatically compare model outputs by sending test queries to individual served models. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Multi-Model Serving Endpoint](/concepts/multi-model-serving-endpoint.md) — Configuring a single endpoint to serve multiple models.
- [Traffic Split](/concepts/traffic-splitting-between-models.md) — Distribution of requests across served models.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The overall serving infrastructure on Databricks.
- Custom Models — One type of model that can be served on an endpoint.
- [External Models](/concepts/external-models.md) — Models hosted on external providers like OpenAI or Anthropic.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Reserved capacity for [Foundation Model APIs](/concepts/foundation-model-apis.md).

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
