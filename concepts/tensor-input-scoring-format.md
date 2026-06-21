---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5557a99afd14cbe43ca7834197daa95b69e4c8ad4f271fef0ffe728f4b48df74
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensor-input-scoring-format
    - TISF
  citations:
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
title: Tensor Input Scoring Format
description: A JSON format for scoring requests to Databricks Model Serving endpoints that accept tensor inputs, supporting both 'instances' (row format with same 0-th dimension) and 'inputs' (columnar format for heterogeneous tensors)
tags:
  - databricks
  - tensorflow
  - pytorch
  - scoring
timestamp: "2026-06-19T20:04:44.604Z"
---

# Tensor Input Scoring Format

**Tensor Input Scoring Format** refers to the JSON structure used to send scoring requests to a [Model Serving](/concepts/model-serving.md) endpoint when the deployed model expects tensor inputs, such as a TensorFlow or PyTorch model. Databricks Model Serving supports two format options for tensor-based requests: `instances` and `inputs`. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Overview

When querying a custom model serving endpoint that accepts tensor inputs, the request must be formatted according to the guidelines described in TensorFlow Serving's API documentation. The response from the endpoint contains the model's output, serialized with JSON and wrapped in a `predictions` key. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Supported Formats

### Instances Format

The `instances` format accepts tensors in row format. Use this format when all input tensors have the same 0-th dimension. Conceptually, each tensor in the instances list could be joined with other tensors of the same name in the rest of the list to construct the full input tensor for the model. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

**Simple example:**

```json
{ "instances": [1, 2, 3] }
```

**Multiple named tensors example:**

```json
{
  "instances": [
    {
      "t1": "a",
      "t2": [1, 2, 3, 4, 5],
      "t3": [
        [1, 2],
        [3, 4],
        [5, 6]
      ]
    },
    {
      "t1": "b",
      "t2": [6, 7, 8, 9, 10],
      "t3": [
        [7, 8],
        [9, 10],
        [11, 12]
      ]
    }
  ]
}
```

### Inputs Format

The `inputs` format sends queries with tensors in columnar format. This format is useful when different tensors have different numbers of instances, making it impossible to represent the input in the `instances` format. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

**Example:**

```json
{
  "inputs": {
    "t1": ["a", "b"],
    "t2": [
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10]
    ],
    "t3": [
      [
        [1, 2],
        [3, 4],
        [5, 6]
      ],
      [
        [7, 8],
        [9, 10],
        [11, 12]
      ]
    ]
  }
}
```

In this example, there are a different number of tensor instances of `t2` (3) than `t1` and `t3`, so it is not possible to represent this input in the `instances` format. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Response Format

The response from the endpoint contains the model's output, serialized with JSON and wrapped in a `predictions` key:

```json
{
  "predictions": [0, 1, 1, 1, 0]
}
```

## Sending Requests

To send a tensor input scoring request via the REST API, use a `curl` command with the endpoint URL and a Databricks API token:

```bash
curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \
    -H 'Content-Type: application/json' \
    -d '{"inputs": 5.1, 3.5, 1.4, 0.2}'
```

The `ENDPOINT_INVOCATION_URL` follows the format `https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations`, where `<databricks-instance>` is the name of your Databricks instance. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Requirements

- A [Model Serving Endpoint](/concepts/model-serving-endpoint.md) must be created and deployed.
- For the [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md), MLflow 2.9 or above is required.
- A Databricks API token is required to send scoring requests through the REST API or MLflow Deployment SDK. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Related Concepts

- [Pandas DataFrame Scoring Format](/concepts/pandas-dataframe-scoring-format.md) — Alternative scoring format for models that accept DataFrame inputs.
- Custom Models — Traditional ML models or customized Python models packaged in MLflow format.
- [Model Serving](/concepts/model-serving.md) — The Databricks service for deploying and querying models.
- Foundation Model Scoring — Query format for generative AI and LLM workloads.

## Sources

- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [query-serving-endpoints-for-custom-models-databricks-on-aws.md](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
