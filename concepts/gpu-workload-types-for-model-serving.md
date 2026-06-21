---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc2ca3379e3c5db015598402a55b3a846320c3ff0484483b72776da343f53845
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-types-for-model-serving
    - GWTFMS
    - GPU workload types in Model Serving
    - GPU workload types
    - GPU workload types|GPU workload type
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: GPU Workload Types for Model Serving
description: GPU compute configurations available for Databricks Model Serving endpoints, with concurrency determining replica count (replicas = concurrency / 4).
tags:
  - model-serving
  - GPU
  - compute-configuration
timestamp: "2026-06-19T14:36:24.199Z"
---

# GPU Workload Types for Model Serving

**GPU Workload Types** determine the compute resource configuration used when deploying a custom model to a [Model Serving](/concepts/model-serving.md) endpoint on Databricks. These types specify whether inference runs on CPU or GPU hardware, and which GPU instance type is allocated. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

When creating a custom model serving endpoint, you can select either CPU or GPU compute. GPU workloads are appropriate for models built with deep learning frameworks and can reduce inference latency for suitable workloads. The available GPU types depend on your cloud provider and are presented in a dropdown in the Serving UI. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Compatibility

GPU deployment is compatible with the following package versions: ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

| Package | Supported Versions |
|---------|-------------------|
| PyTorch | 1.13.0 – 2.0.1 |
| TensorFlow | 2.5.0 – 2.13.0 |
| MLflow | 2.4.0 and above |

## Available GPU Types

The specific GPU workload types available vary by cloud provider. During endpoint creation, the Serving UI summarizes the options in a table when you open the **Compute Type** dropdown. To configure a GPU endpoint:

1. Follow the standard endpoint creation steps.
2. In the **Served entities** section, open the **Compute Type** dropdown.
3. Select the desired GPU type instead of CPU.
4. Configure **Compute Scale-out** (Small, Medium, or Large) as needed. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

The same GPU type can be selected through the REST API, the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), or the [Workspace Client](/concepts/workspaceclient-dbutils.md). ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Concurrency and Replicas

For GPU endpoints, the concurrency value determines the number of replicas allocated to serve the model. The number of replicas equals the concurrency value divided by 4. For example, setting `min_provisioned_concurrency` to 12 provisions 3 replicas. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## GPU vs CPU Considerations

GPU endpoints are recommended for deep learning models that benefit from parallel processing capabilities. CPU endpoints may be more cost-effective for simpler models or those with lower throughput requirements. The choice between GPU and CPU should be based on model architecture, latency requirements, and cost constraints. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform that hosts custom and foundation models
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Full workflow for endpoint creation
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — High-performance GPU option for deep learning workloads
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Serverless GPU compute with eight H100 GPUs
- Model Serving Limits — Constraints and capacity planning for serving endpoints
- [Serve multiple models to serving endpoint](/concepts/multi-model-serving-endpoint.md) — Serving multiple entities on a single endpoint

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
