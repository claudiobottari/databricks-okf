---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0178aadb908d2cd6465ceec181ab86aa37feef97d69e7543605b88d4f5b83a6
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-serve-on-databricks-limitations
    - RSODL
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Ray Serve on Databricks Limitations
description: Challenges of using Ray Serve for real-time inference on Databricks clusters due to network security constraints, with recommendation to use Databricks Model Serving instead.
tags:
  - ray
  - databricks
  - model-serving
  - limitations
timestamp: "2026-06-19T19:11:19.690Z"
---

# Ray Serve on Databricks Limitations

**Ray Serve on Databricks Limitations** refers to the challenges and restrictions encountered when using Ray Serve, a Ray-based model serving framework, on Databricks clusters for production real-time inference. The primary limitation is related to network security and connectivity constraints that hinder interaction with external applications. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Network and Connectivity Constraints

Databricks clusters are designed with network security boundaries that can prevent external applications from communicating with Ray Serve endpoints running inside the cluster. This makes Ray Serve unsuitable for real-time inference workloads that require publicly accessible or externally routable REST API endpoints. The limitation stems from the cluster’s network architecture rather than from Ray Serve itself. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Recommended Alternative

Because of these limitations, Databricks recommends using [Model Serving](/concepts/model-serving.md) to deploy machine learning models in production to a REST API endpoint. Model Serving is a fully managed service that provides secure, low‑latency access from external applications without the network configuration challenges of running Ray Serve on a cluster. For details, see the [Custom models overview](/concepts/custom-models-on-model-serving.md) documentation. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- Ray Serve – The model serving framework affected by these limitations.
- [Model Serving](/concepts/model-serving.md) – The recommended alternative for production inference on Databricks.
- Databricks Clusters – The compute environment where Ray Serve runs.
- Real-time inference – The workload type for which Ray Serve is limited.

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
