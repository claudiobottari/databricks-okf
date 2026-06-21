---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94deb91aad13dc94bb12051ce180f1f6c35acfc624ce3e38c0adc5b91164c426
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-custom-models
    - MSE(M
    - Custom Model Serving Endpoints|custom model serving endpoints
    - Query serving endpoints for custom models
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint (Custom Models)
description: A Databricks endpoint that serves custom machine learning models via UI, REST API, MLflow Deployments SDK, or Workspace Client
tags:
  - model-serving
  - databricks
  - endpoints
timestamp: "2026-06-18T14:53:45.096Z"
---

# Model Serving Endpoint (Custom Models)

**Model Serving Endpoint (Custom Models)** refers to a Databricks-hosted API endpoint that serves a user-uploaded or registered machine learning model — as opposed to Databricks’ pre-built foundation models. Custom model endpoints can be created via the Serving UI, REST API, or the MLflow Deployments SDK. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Model Serving offers three pathways to create custom model endpoints: the **Serving UI**, the **REST API**, and the **MLflow Deployments SDK**. For generative AI models, see [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The workspace must be in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- If the model uses custom Python libraries or libraries from a private mirror, consult [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) before creating the endpoint. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- To use the MLflow Deployments SDK, install the client:
  ```python
  import mlflow.deployments
  client = mlflow.deployments.get_deploy_client("databricks")
  ``` ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access

### Creator Identity

When an endpoint is created, Databricks records the caller’s identity as the endpoint’s **creator** (typically a service principal). This identity is used to access [Unity Catalog](/concepts/unity-catalog.md) resources on the endpoint’s behalf and **cannot be changed** after creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

If the recorded creator lacks the required Unity Catalog grants or has been removed from the workspace, you must delete and recreate the endpoint under a service principal that has the correct grants and is a current workspace member. Configuration and served-entity updates re-evaluate the creator’s workspace membership and grants; updates fail with `PERMISSION_DENIED` if the creator is no longer a workspace member, even if the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Served Entity Grants

The recorded creator must hold the following grants on each served entity:

- Grants needed at endpoint creation or update (validated upfront; fail with `PERMISSION_DENIED` if missing).
- Grants required only at query time are **not** validated upfront — missing grants cause runtime errors when the endpoint serves traffic.

> If the Unity Catalog model declares transitive function dependencies, the recorded creator also needs `EXECUTE` on those upstream functions.

⁠[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Manage Endpoint Access

Access control for model serving endpoints is configured separately; see Manage permissions on a model serving endpoint. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Create an Endpoint

Endpoints can be created via the **Serving UI**, **REST API**, or **MLflow Deployments SDK**.

### Serving UI

1. Click **Serving** in the sidebar.
2. Click **Create serving endpoint**.
3. In the **Name** field, provide a name (cannot use the `databricks-` prefix).
4. Under **Served entities**, select the model registry (Workspace Model Registry or Unity Catalog), choose the model and version, set traffic percentage, compute type (CPU or GPU), and scale-out size.
   - Scale-out sizes: **Small** (0–4 concurrent requests), **Medium** (8–16), **Large** (16–64).
   - Option to **scale to zero** — not recommended for production due to cold start latency.
   - Advanced configuration: rename served entity, add instance profile, or set environment variables (including for feature lookup DataFrame logging).
5. Add additional served entities via **Add served entity** to serve multiple models with traffic splitting.
6. Configure **Route optimization** (recommended for high QPS/throughput).
7. Under **AI Gateway**, select governance features (see [Unity AI Gateway](/concepts/unity-ai-gateway.md)).
8. Click **Create**. The endpoint state initially shows **Not Ready**. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

You can also enable [Inference Tables](/concepts/inference-tables.md) to capture request/response logs, and log the feature lookup DataFrame to the inference table. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### REST API & MLflow Deployments SDK

The source material references that these methods exist but does not provide detailed examples; refer to the official documentation for code snippets. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## GPU Workload Types

GPU deployment is compatible with PyTorch 1.13.0–2.0.1, TensorFlow 2.5.0–2.13.0, and MLflow 2.4.0+. To configure GPU endpoints, select the desired GPU type in the Serving UI’s **Compute Type** dropdown. The available GPU types depend on the cloud provider. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

For GPU endpoints, the concurrency value determines the number of replicas: `replicas = concurrency / 4`. For example, `min_provisioned_concurrency = 12` provisions 3 replicas. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Modify a Custom Model Endpoint

After an endpoint is enabled, you can update its compute configuration via the **Edit endpoint** button. Most settings can be changed except the endpoint name and certain immutable properties. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

During an update, the old configuration continues serving traffic until the new one is ready. In-progress updates can be cancelled from the Serving UI. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

> Configuration and served-entity updates re-evaluate the creator’s workspace membership and grants. To avoid failures:
> - Use a long-lived service principal owned by your team as the endpoint creator.
> - Do not use a personal user account that might be deactivated or removed later.
> - The recorded creator must remain a workspace member for the endpoint’s lifetime.

⁠[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Scoring a Model Endpoint

To score a model, send requests to the endpoint. See [Query serving endpoints for custom models](/concepts/model-serving-endpoint-custom-models.md) and Use foundation models. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Additional Resources

- Manage model serving endpoints
- [External models in Model Serving](/concepts/external-model-multi-serving.md)
- Databricks real-time serving Python SDK (see [Databricks SDK docs](https://databricks-sdk-py.readthedocs.io/en/latest/dbdataclasses/serving.html))
- Notebook examples: Train and register a scikit-learn model notebook; Train and register a HuggingFace model notebook. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md)
- Instance Profile
- Route optimization
- Manage permissions on a model serving endpoint
- [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md)

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
