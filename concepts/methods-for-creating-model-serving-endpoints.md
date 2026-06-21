---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4730e06eb312882d1aa31531fbfb46971955ce66a331978aa1f85b3dd9ad6c95
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - methods-for-creating-model-serving-endpoints
    - MFCMSE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Methods for Creating Model Serving Endpoints
description: "Databricks Model Serving supports four creation methods: Serving UI, REST API, MLflow Deployments SDK, and Workspace Client."
tags:
  - model-serving
  - api
  - workflow
timestamp: "2026-06-18T11:22:47.505Z"
---

# Methods for Creating Model Serving Endpoints

**Model Serving** on Databricks provides three primary methods for creating endpoints that serve [custom models](/concepts/custom-mlflow-pythonmodel.md): the **Serving UI**, the **REST API**, and the **MLflow Deployments SDK**. Each method offers flexibility depending on the user’s workflow — from interactive UI configuration to programmatic automation.

## Overview

Model Serving allows you to deploy custom MLflow models as scalable REST API endpoints. The creation process requires a registered model (in Unity Catalog or the Workspace Model Registry), an endpoint name, a compute configuration, and a traffic allocation for each served entity.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

For endpoints serving generative AI models, see Create foundation model serving endpoints.

## Requirements

- The workspace must be in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions).^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- If using custom libraries, see [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) before creating the endpoint.^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- For the MLflow Deployments SDK, install the MLflow Deployment client:
  ```python
  import mlflow.deployments
  client = mlflow.deployments.get_deploy_client("databricks")
  ```^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access

### Creator Identity

When an endpoint is created, Databricks records the calling identity (usually a service principal) as the **creator**. This identity is used to access Unity Catalog resources during inference and cannot be changed after creation. If the recorded creator lacks required grants or is removed from the workspace, the endpoint must be deleted and recreated under a valid service principal. Configuration updates re-evaluate the recorded creator’s workspace membership; updates fail with `PERMISSION_DENIED` if the creator is no longer a member.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Served Entity Grants

The recorded creator must hold appropriate grants on each served entity, such as `EXECUTE` on models. If a Unity Catalog model declares transitive function dependencies, the creator also needs `EXECUTE` on those upstream functions. Required grants are validated at endpoint creation or update; missing grants cause a `PERMISSION_DENIED` error. Missing grants at query time lead to runtime errors.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

For managing access control on endpoints, see Manage permissions on a model serving endpoint.

## Method 1: Serving UI

The Serving UI provides a step-by-step wizard for endpoint creation.

1. Navigate to **Serving** in the sidebar, then click **Create serving endpoint**.
2. Enter a **Name** (cannot use the `databricks-` prefix).
3. In **Served entities**:
   - Select **My models – Unity Catalog** or **My models – Model Registry**.
   - Choose the model and model version.
   - Set the traffic percentage for the served entity.
   - Select the compute type (CPU or GPU).
   - Under **Compute Scale-out**, choose **Small** (0–4 concurrent requests), **Medium** (8–16), or **Large** (16–64).
   - Enable or disable **Scale to zero** (not recommended for production; causes cold-start latency).
4. In **Advanced configuration**, you can:
   - Rename the served entity.
   - Add an instance profile for AWS resource access.
   - Add environment variables for resource connectivity or feature lookup logging.
5. (Optional) Add additional served entities with a traffic split.
6. In **Route optimization**, enable for high-QPS endpoints.
7. In **AI Gateway**, choose governance features such as [Inference Tables](/concepts/inference-tables.md).
8. Click **Create**. The endpoint state displays as **Not Ready** until deployment completes.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Method 2: REST API

The REST API allows programmatic endpoint creation and management. The request payload specifies the endpoint name, served entities, and configuration parameters such as compute type and concurrency.

Example request structure:

- `name`: endpoint name.
- `served_entities`: list of model entities, each with `entity_name`, `entity_version`, `workload_size`, `scale_to_zero_enabled`, and `traffic_percentage`.
- GPU workload types can be specified in the configuration.

For detailed API reference, see the [Model Serving REST API documentation](https://docs.databricks.com/aws/en/api/workspace/serving-endpoints).^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Method 3: MLflow Deployments SDK

The **MLflow Deployments SDK** provides a Python client for creating and managing endpoints. After obtaining a client:

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
                "traffic_percentage": 100,
            }
        ]
    },
)
```

The SDK also supports updating and deleting endpoints. See [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) for more details.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## GPU Workload Types

GPU deployment is compatible with PyTorch 1.13.0–2.0.1, TensorFlow 2.5.0–2.13.0, and MLflow 2.4.0+. GPU types vary by cloud provider. When using the UI, select the desired GPU type from the **Compute Type** dropdown. For GPU endpoints, the concurrency value determines the number of replicas allocated — replicas = concurrency ÷ 4. For example, setting `min_provisioned_concurrency` to 12 provisions 3 replicas.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Modifying an Endpoint

After creation, you can update the compute configuration, served entities, traffic percentages, and advanced settings from the **Serving UI** by selecting **Edit endpoint**. Configuration updates re-validate the creator’s workspace membership and grants. In-progress updates block further updates until complete; you can cancel an update from the UI. The old configuration remains active until the new one is ready.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- Custom models
- [Route optimization on serving endpoints](/concepts/route-optimization-for-serving-endpoints.md)
- [Inference Tables](/concepts/inference-tables.md)
- Manage permissions on a model serving endpoint
- [GPU workload types](/concepts/gpu-workload-types-for-model-serving.md)

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
