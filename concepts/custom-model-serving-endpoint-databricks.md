---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cff0463ff7a3f58c9e82f2aac9b39effda9fa4816ca16d399fcf6911736775d
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-model-serving-endpoint-databricks
    - CMSE(
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Custom Model Serving Endpoint (Databricks)
description: A serving endpoint that hosts custom ML models for real-time inference on Databricks, created via UI, REST API, MLflow Deployments SDK, or Workspace Client.
tags:
  - model-serving
  - databricks
  - mlops
timestamp: "2026-06-19T18:00:59.018Z"
---

## Custom Model Serving Endpoint (Databricks)

A **Custom Model Serving Endpoint** on Databricks is a real-time inference endpoint that serves user-registered custom models—as opposed to pre-built foundation models or feature-serving tables. These endpoints are created, managed, and queried through Databricks [Model Serving](/concepts/model-serving.md), which supports serving models registered in [Unity Catalog](/concepts/unity-catalog.md) or the Workspace Model Registry. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Requirements

Before creating a custom model serving endpoint, the workspace must be in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions). If custom Python libraries or libraries from a private mirror are needed, see [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) beforehand. For the MLflow Deployments SDK option, the `mlflow.deployments` client must be installed and initialized with `mlflow.deployments.get_deploy_client("databricks")`. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Identity and Access

The identity that creates the endpoint—typically a service principal—is recorded as the endpoint's **creator**. This creator identity is used to access Unity Catalog resources on behalf of the endpoint and cannot be changed after creation. The creator must be a current workspace member and hold the `workspace-access` entitlement. If the creator loses workspace membership or required grants, the endpoint must be deleted and recreated under a valid identity. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

At endpoint creation or update time, the recorded creator must hold the appropriate grants (e.g., `EXECUTE`) on each served entity (model or function). Missing grants cause a `PERMISSION_DENIED` error at create/update time; missing grants at query time produce runtime errors. If the served entity uses transitive function dependencies in Unity Catalog, the creator also needs `EXECUTE` on those upstream functions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Creating an Endpoint

Endpoints can be created through four interfaces: the **Serving UI**, the **REST API**, the **MLflow Deployments SDK**, and the **Workspace Client** (Python SDK). All methods share common configuration fields: endpoint name (cannot use the `databricks-` prefix), served entity selection (model and version), traffic percentage, compute type (CPU or GPU), compute scale-out size (Small/Medium/Large), and scale-to-zero option. Advanced configuration includes renaming the served entity, attaching an instance profile for AWS resources, and setting environment variables for resource connections or feature lookup logging. Multiple served entities can be added to a single endpoint with a traffic split between them. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Optional features available during creation:

- **Route optimization** – Recommended for high-QPS endpoints. See [Route optimization on serving endpoints](/concepts/route-optimization-for-serving-endpoints.md).
- **AI Gateway** – Unity AI Gateway governance features. See [Unity AI Gateway](/concepts/unity-ai-gateway.md).
- **Inference tables** – Automatically capture incoming requests and outgoing responses. See [Inference Tables](/concepts/inference-tables.md).

After creation, the endpoint shows **Serving endpoint state** as *Not Ready* until deployment completes. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

#### GPU Workload Types

For GPU endpoints, the available GPU instance types depend on the cloud provider (AWS, Azure, GCP). Compatible framework versions are PyTorch 1.13.0–2.0.1, TensorFlow 2.5.0–2.13.0, and MLflow 2.4.0+. When creating a GPU endpoint, the concurrency value determines the number of replicas: each replica handles up to 4 concurrent requests, so `min_provisioned_concurrency` divided by 4 gives the number of replicas. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Modifying a Custom Model Endpoint

After an endpoint is enabled, you can update its compute configuration (e.g., workload size, scale-out, served entity versions) by using the **Edit endpoint** button in the UI or the corresponding API/SDK calls. Configuration updates re-validate the recorded creator’s workspace membership and grants. To avoid update failures, use a long-lived service principal as the creator rather than a personal user account. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

While a new configuration is being applied, the old configuration continues to serve traffic. Only one update can be in progress at a time; a pending update can be cancelled from the Serving UI. If an update fails, the existing active configuration remains in effect. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Scoring a Model Endpoint

To query a deployed custom model endpoint, send prediction requests to the endpoint URL. See [Query serving endpoints for custom models](/concepts/model-serving-endpoint-custom-models.md) and Use foundation models for detailed API usage. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Additional Resources

- Manage model serving endpoints – Overview of endpoint lifecycle operations.
- [External models in Model Serving](/concepts/external-model-multi-serving.md) – Serving models hosted outside Databricks.
- Databricks real-time serving Python SDK – Python SDK for endpoint management and scoring.
- [Tutorial: Deploy and query a custom model](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro) – Step-by-step guide with notebook examples.

### Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
