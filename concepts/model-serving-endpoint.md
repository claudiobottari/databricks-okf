---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53cae5cb7e728175ca3ce2acf2aefbd99d4f96e248d9fb362ba46aec4dcd9521
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint
    - MSE
    - Debug Model Serving Endpoints
    - Debug a Model Serving Endpoint
    - LLM serving endpoint
    - Model Serving Endpoint Events
    - Model Serving Endpoint Health
    - Model Serving Endpoints
    - Model Serving endpoints
    - Model serving endpoints
    - Model-serving endpoints
    - model serving endpoints
    - model-serving endpoints
    - Create model serving endpoints
    - LLM endpoint
    - LLM endpoints
    - LLM serving endpoints
    - Model Endpoints
    - Model Serving Endpoint Management
    - Model Serving Endpoint Requirements
    - Model Serving Endpoints|Model Serving endpoint
    - model serving endpoint requirements
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 14
      end: 15
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 18
      end: 19
    - file: tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 5
      end: 9
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 34
      end: 35
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 39
      end: 53
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 55
      end: 73
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 81
      end: 107
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 109
      end: 130
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 73
      end: 75
    - file: 133-135
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
      start: 23
      end: 28
    - file: 30-32
title: Model Serving Endpoint
description: A REST API endpoint on Databricks that serves custom ML models for real-time inference, accessed via a URL pattern like https://<instance>/serving-endpoints/<endpoint-name>/invocations
tags:
  - databricks
  - model-serving
  - mlops
  - inference
timestamp: "2026-06-19T20:04:38.823Z"
---

# Model Serving Endpoint

A **Model Serving Endpoint** is a managed endpoint on [Databricks Model Serving](/concepts/databricks-model-serving.md) that hosts a registered custom model for real-time inference. Endpoints can serve models registered in [Unity Catalog](/concepts/unity-catalog.md) or the workspace [MLflow Model Registry](/concepts/mlflow-model-registry.md), support CPU and GPU compute, and can host multiple served entities with configurable traffic splits. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Model Serving endpoints provide a production-grade infrastructure for deploying custom models. They can be created and managed through the Serving UI, the Databricks REST API, the MLflow Deployments SDK, or the Databricks Workspace Client. For serving generative AI or foundation models, see Create foundation model serving endpoints. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

After creation, an endpoint exposes a scoring URL that accepts JSON requests and returns predictions. Endpoints can optionally be configured with [Inference Tables](/concepts/inference-tables.md), [instance profiles](/concepts/instance-profile-databricks-on-aws.md) for accessing AWS resources, and environment variables for resource connections or logging feature lookup DataFrames. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The workspace must be in a supported region for Model Serving. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- If using custom libraries or private mirror servers, see [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- To create endpoints via the MLflow Deployments SDK, MLflow 2.9 or above is required. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:14-15]
- For REST API or SDK scoring, a Databricks API token is required. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:18-19]

### Prerequisites for creating an endpoint

```python
import mlflow.deployments
client = mlflow.deployments.get_deploy_client("databricks")
```

## Identity and Access

### Creator Identity

When an endpoint is created, Databricks records the calling identity (typically a service principal) as the **creator**. This identity is used to access [Unity Catalog](/concepts/unity-catalog.md) resources on behalf of the endpoint and cannot be changed after creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

If the recorded creator loses workspace membership or required grants, the endpoint must be deleted and recreated under a valid service principal. Updates to the endpoint configuration re-validate the creator’s workspace membership and per-served-entity grants; failure causes the update to be rejected with `PERMISSION_DENIED`. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Served Entity Grants

The recorded creator must hold the following grants on each served entity and (if applicable) transitive function dependencies. Grants validated at creation or update time cause the request to fail if missing. Grants required only at query time cause runtime errors when traffic arrives. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Managing Endpoint Access

See Manage permissions on a model serving endpoint for access control options. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Create an Endpoint

### Using the Serving UI

1.  Click **Serving** in the sidebar, then **Create serving endpoint**. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
2.  Provide a **Name** (cannot use the reserved `databricks-` prefix). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
3.  In **Served entities**:
    - Select the entity type (Unity Catalog or Model Registry).
    - Choose the model and version.
    - Set traffic percentage.
    - Select compute type (CPU or GPU; see [GPU workload types](/concepts/gpu-workload-types-for-model-serving.md)).
    - Choose **Compute Scale-out**: Small (0–4 requests), Medium (8–16), Large (16–64). This should approximate QPS × model execution time.
    - Specify whether the endpoint should scale to zero when not in use (not recommended for production; cold starts incur latency).
    - Advanced configuration: rename the served entity, add an instance profile, or set environment variables.
4.  Optionally add more served entities (see [Serve multiple models to serving endpoint](/concepts/multi-model-serving-endpoint.md)). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
5.  Configure Route optimization for high-QPS endpoints. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
6.  Configure [AI Gateway](/concepts/ai-gateway.md) governance features. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
7.  Click **Create**. The endpoint shows **Not Ready** initially. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

For step-by-step tutorial, see Tutorial: Deploy and query a custom model. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

### Using the REST API

Use the Databricks Serving API to create endpoints programmatically. See [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) for API details. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

```python
client.create_endpoint(
    name="my-endpoint",
    config={
        "served_entities": [
            {
                "entity_name": "my_model",
                "entity_version": "1",
                "workload_size": "Small",
                "scale_to_zero_enabled": False,
            }
        ],
    },
)
```

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Using the Workspace Client

The Databricks real-time serving Python SDK (`databricks-sdk-py`) provides a Pythonic interface for endpoint management. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## GPU Workload Types

GPU deployment is compatible with PyTorch 1.13.0–2.0.1, TensorFlow 2.5.0–2.13.0, and MLflow 2.4.0+. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Available GPU workload types vary by cloud provider. For GPU endpoints, concurrency determines the number of replicas: replicas = concurrency ÷ 4 (e.g., `min_provisioned_concurrency` of 12 provisions 3 replicas). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Modify a Custom Model Endpoint

After creation, you can update the compute configuration, served entities, and scaling settings via the **Edit endpoint** button in the UI (or through API/SDK). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Important considerations:
- The endpoint name and certain immutable properties cannot be changed. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- An update in progress cannot be interrupted by another update, but can be cancelled from the UI. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- The old configuration continues serving traffic until the new one is ready. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- The recorded creator must remain a workspace member and retain required grants for the endpoint’s lifetime. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Scoring a Model Endpoint

To query a custom model serving endpoint, send a JSON request to the endpoint’s invocations URL. The easiest method is the **Query endpoint** tab in the Serving UI. For programmatic access, use the REST API, the MLflow Deployments SDK, or Power BI. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:5-9]

### Supported Input Formats

Model Serving supports scoring requests in Pandas DataFrame format or Tensor input format. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:34-35]

**Pandas DataFrame**: Send a JSON-serialized Pandas DataFrame using one of the following keys:

- `dataframe_split` (recommended): Contains `index`, `columns`, and `data` arrays. This format preserves column ordering. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:39-53]
- `dataframe_records`: Array of row objects. Column ordering is not guaranteed; the `split` format is preferred. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:55-73]

**Tensor input**: For models expecting tensors (e.g., TensorFlow, PyTorch), use one of:

- `instances`: Row-based format where each element corresponds to one row. Works when all input tensors have the same 0-th dimension. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:81-107]
- `inputs`: Columnar format for multiple named tensors that may have different dimensions. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:109-130]

Responses are returned in a JSON object with a `predictions` key. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:73-75, 133-135]

### Example: Pandas DataFrame using REST API

```bash
curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \
  -H 'Content-Type: application/json' \
  -d '{"dataframe_split": {
        "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
        "data": [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]]
      }}'
```

^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:23-28]

### Example: Tensor input using MLflow Deployments SDK

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(
    endpoint="my-endpoint",
    inputs={"instances": 5.1, 3.5, 1.4, 0.2}
)
print(response)
```

^[query-serving-endpoints-for-custom-models-databricks-on-aws.md:5-9, 30-32]

For foundation model scoring, see Score foundation models. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Additional Resources

- Manage model serving endpoints
- [External models in Model Serving](/concepts/external-model-multi-serving.md)
- Deploy Python code with Model Serving
- Monitor served models using Unity AI Gateway-enabled inference tables
- Debugging guide for Model Serving
- Notebook examples for training and registering models.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Model registry for serving.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Alternative model storage.
- [Inference Tables](/concepts/inference-tables.md) – Capture request/response logs.
- [AI Gateway](/concepts/ai-gateway.md) – Governance features.
- Route optimization – Performance tuning.
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) – Programmatic access to endpoints.
- TensorFlow Serving API – Reference for tensor input formatting.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md
- tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
2. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:14-15](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
3. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:18-19](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
4. [tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md](/references/tutorial-deploy-and-query-a-custom-model-databricks-on-aws-16c7ace5.md)
5. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:5-9](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
6. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:34-35](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
7. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:39-53](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
8. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:55-73](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
9. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:81-107](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
10. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:109-130](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
11. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:73-75](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
12. 133-135
13. [query-serving-endpoints-for-custom-models-databricks-on-aws.md:23-28](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
14. 30-32
