---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f09fd7fdf8d77eff23a18a6dd62724ee73706f647ed4651e7ec187f07c21034
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resource-availability-for-model-serving
    - GRAFMS
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: GPU Resource Availability for Model Serving
description: Constraints and failure modes related to GPU supply limitations when building and deploying GPU-backed model serving endpoints on Databricks.
tags:
  - model-serving
  - gpu
  - infrastructure
timestamp: "2026-06-19T18:17:09.670Z"
---

# GPU Resource Availability for Model Serving

GPU Resource Availability for Model Serving refers to the limited supply of GPU compute resources that can cause container build failures when deploying machine learning models on Databricks Model Serving endpoints. Due to global restrictions in GPU supply and availability, a GPU build may fail with the error: `Build could not start due to an internal error - please contact your Databricks representative.` ^[debugging-guide-for-model-serving-databricks-on-aws.md]

To resolve this issue, users must contact their Databricks account team, which can provision additional GPU resources depending on region availability. This limitation is separate from [Provisioned Concurrency](/concepts/provisioned-concurrency.md) or parallel requests limits, which are related to endpoint throughput rather than the underlying hardware allocation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- Container Build Failure
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- H100 GPU Support on Databricks

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
