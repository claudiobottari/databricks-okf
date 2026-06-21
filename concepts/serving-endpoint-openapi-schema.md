---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c66941d4ef1cdca3e14ecb90c4237f6baf7fb95b48c915d53670e2361d499249
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-openapi-schema
    - SEOS
    - Serving endpoint schema
    - OpenAPI schema
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Serving Endpoint OpenAPI Schema
description: A formal OpenAPI specification (JSON) that describes a serving endpoint's query interface, request/response format, and data types for reproducibility and client code generation.
tags:
  - model-serving
  - api-schema
  - openapi
  - databricks
timestamp: "2026-06-19T19:26:16.088Z"
---

# Serving Endpoint OpenAPI Schema

A **Serving Endpoint OpenAPI Schema** is a formal description of a Databricks model serving endpoint, structured according to the OpenAPI specification (version 3.1.0) and returned in JSON format. It provides a machine-readable description of the endpoint’s query interface, including the request and response body formats, data types for each field, and the endpoint URL. The schema is especially useful for reproducibility scenarios or when you need endpoint details but are not the original endpoint creator or owner. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Prerequisites

To obtain the schema, the served model must have a [model signature](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#get-a-model-serving-endpoint-schema) logged, and the endpoint must be in a `READY` state. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Retrieving the Schema

You can programmatically retrieve the schema using the Databricks REST API. The following `curl` example demonstrates the request:

```bash
ACCESS_TOKEN="<endpoint-token>"
ENDPOINT_NAME="<endpoint name>"
curl "https://example.databricks.com/api/2.0/serving-endpoints/$ENDPOINT_NAME/openapi" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

^[manage-model-serving-endpoints-databricks-on-aws.md]

## Schema Response Details

The API response is an OpenAPI specification JSON object containing the following key fields:

- **`openapi`**: The version of the OpenAPI specification (always `"3.1.0"`).
- **`info.title`**: The name of the serving endpoint.
- **`servers`**: An array with a single object whose `url` field is the base URL of the endpoint.
- **`paths`**: An object whose keys are path URLs (e.g., `/served-models/{model-name}/invocations`). Each path may support multiple input formats, listed in a `oneOf` field within the `requestBody`. The `paths` object also includes the response schema for the `200` status code.

Because the response is a standard JSON object, you can parse it in any programming language, generate client code using third‑party tools, or visualize the specification with tools like Swagger Editor. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Example

The source provides an example schema for an endpoint named `example-endpoint`. The `paths` section shows two input formats: `dataframe_split` (with columns and data arrays) and `dataframe_records` (an array of objects), both including optional `params`. The response contains a `predictions` array of double numbers. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- OpenAPI Specification
- Serving Endpoint REST API
- [Model Signature](/concepts/model-signatures-in-unity-catalog.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- [Feature Serving Endpoint Schema](/concepts/feature-serving-endpoint.md)

## Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
