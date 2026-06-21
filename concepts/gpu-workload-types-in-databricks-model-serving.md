---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fa967e15c516e8111f1f43d8a52ae8a3a00e7158a3c018665bdb857d9a9f739
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-types-in-databricks-model-serving
    - GWTIDMS
    - GPU Workload Types on Databricks
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: GPU Workload Types in Databricks Model Serving
description: GPU compute options for model serving endpoints supporting PyTorch 1.13-2.0.1, TensorFlow 2.5-2.13, and MLflow 2.4+; concurrency determines replica count (concurrency / 4).
tags:
  - model-serving
  - gpu
  - compute
timestamp: "2026-06-19T18:01:06.597Z"
---

# GPU Workload Types in Databricks Model Serving

**GPU Workload Types** in [Databricks Model Serving](/concepts/databricks-model-serving.md) are compute configurations that use GPU accelerators instead of CPUs to serve custom models. They are intended for models that benefit from GPU parallelism, such as deep learning models built with PyTorch, TensorFlow, or MLflow. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Compatibility

GPU deployment is compatible with:

- PyTorch 1.13.0 – 2.0.1
- TensorFlow 2.5.0 – 2.13.0
- MLflow 2.4.0 and above

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Available GPU Workload Types

The specific GPU types (instance families) available depend on your cloud provider. The [create-custom-model-serving-endpoints-databricks-on-aws.md](/concepts/custom-model-serving-endpoint-databricks.md) documentation provides a table that lists the supported types per provider. When creating an endpoint, you select the GPU type from the **Compute Type** dropdown in the Serving UI, or specify it via the REST API or MLflow Deployments SDK. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Concurrency and Replicas

For GPU endpoints, the concurrency value (for example, `min_provisioned_concurrency`) directly determines the number of replicas allocated to serve the model.

- **Number of replicas** = concurrency value ÷ 4.
- Example: Setting `min_provisioned_concurrency` to 12 provisions 3 replicas.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Configuring GPU Workloads

You can configure GPU workloads when creating a custom model serving endpoint using any of the following methods:

- **Serving UI** – Select the desired GPU type from the **Compute Type** dropdown.
- **REST API** – Specify the GPU workload type in the endpoint creation payload.
- **MLflow Deployments SDK** – Include GPU type parameters when calling the deployment client.
- **Workspace Client** – The Databricks Python SDK also supports endpoint creation with GPU settings.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

After creating the endpoint, you can modify the compute configuration (including GPU type) by editing the endpoint. Note that the endpoint name and certain immutable properties cannot be changed. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Overview of serving custom and foundation models on Databricks.
- Custom Models – Models that are not provided by Databricks Foundation Model APIs.
- [Serving Endpoint Permissions](/concepts/serving-endpoint-acls.md) – Access control and identity requirements for endpoints.
- Concurrency and Scale-Out – How compute scale-out sizes map to request capacity.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – Full guide for endpoint creation.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
