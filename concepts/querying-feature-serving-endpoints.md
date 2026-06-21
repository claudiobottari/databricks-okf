---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a356b601b61d3c392a8e64d6538640a81ce84caafb6af8c0940a1b30fa836a5
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - querying-feature-serving-endpoints
    - QFSE
    - Feature Serving|feature serving endpoints
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Querying Feature Serving endpoints
description: Methods to query endpoints using REST API, MLflow Deployments SDK, or the Serving UI, passing dataframe_records with lookup keys and dynamic inputs.
tags:
  - serving
  - api
  - inference
timestamp: "2026-06-18T12:19:00.781Z"
---

# Querying Feature Serving endpoints

**Feature Serving endpoints** provide a high-availability, low-latency service for serving structured data — such as features for ML models, [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications, or other applications that require features based on data in [Unity Catalog](/concepts/unity-catalog.md). Once an endpoint is created and in a **Ready** state, you can query it using the REST API, the MLflow Deployments SDK, or the Serving UI. ^[feature-serving-endpoints-databricks-on-aws.md]

## Prerequisites for Querying

Before you can query a Feature Serving endpoint, you must have:

- A deployed endpoint backed by a [FeatureSpec](/concepts/featurespec.md) — a user-defined set of features and functions stored in Unity Catalog. ^[feature-serving-endpoints-databricks-on-aws.md]
- Authentication credentials: a Databricks API token (or, as a security best practice, OAuth tokens for service principals). ^[feature-serving-endpoints-databricks-on-aws.md]

## Querying with the MLflow Deployments SDK

The MLflow Deployments SDK provides a programmatic way to query endpoints. The following example sets up the client and sends a prediction request: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")

response = client.predict(
    endpoint="test-feature-endpoint",
    inputs={
        "dataframe_records": [
            {"user_id": 1, "ytd_spend": 598},
            {"user_id": 2, "ytd_spend": 280},
        ]
    },
)
```

The request body uses the `dataframe_records` format, where each record maps an input lookup key (e.g. `user_id`) to the values needed by the [FeatureLookup](/concepts/featurelookup.md) and [FeatureFunction](/concepts/featurefunction.md) definitions in the `FeatureSpec`. ^[feature-serving-endpoints-databricks-on-aws.md]

## Querying with the REST API

You can also query the endpoint directly via the REST API. The request format is identical to the MLflow Deployments SDK: ^[feature-serving-endpoints-databricks-on-aws.md]

```json
// Example request body
{
  "dataframe_records": [
    { "user_id": 1, "ytd_spend": 598 },
    { "user_id": 2, "ytd_spend": 280 }
  ]
}
```

To use the REST API, you must have an active Databricks API token and call the endpoint's URL (available from the Serving UI). ^[feature-serving-endpoints-databricks-on-aws.md]

## Querying with the Serving UI

The Serving UI provides an interactive query interface for testing endpoints: ^[feature-serving-endpoints-databricks-on-aws.md]

1. In the left sidebar of the Databricks workspace, click **Serving**.
2. Click the endpoint you want to query.
3. In the upper-right of the screen, click **Query endpoint**.
4. In the **Request** box, type the request body in JSON format using the `dataframe_records` structure.
5. Click **Send request**.

The **Query endpoint** dialog displays generated example code in `curl`, Python, and SQL. You can copy these examples by clicking the copy icon in the upper-right corner of the text box. ^[feature-serving-endpoints-databricks-on-aws.md]

## Response Format

The endpoint returns the feature values computed by the `FeatureSpec`. For each input record, the response includes the looked-up features (e.g. `average_yearly_spend`, `country`) and the computed function outputs (e.g. `spending_gap`). The exact shape of the response depends on the [FeatureSpec](/concepts/featurespec.md) definition and the features it combines. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) — The endpoints that serve features from Unity Catalog
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that hosts ML models and can also serve features
- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions that backs an endpoint
- [FeatureLookup](/concepts/featurelookup.md) — Defines which table columns to look up by a key
- [FeatureFunction](/concepts/featurefunction.md) — Defines a UDF (user-defined function) to compute a derived feature
- Databricks API token — Required for programmatic authentication
- OAuth tokens — Recommended alternative to personal access tokens for automated workflows
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where FeatureSpecs are stored

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
