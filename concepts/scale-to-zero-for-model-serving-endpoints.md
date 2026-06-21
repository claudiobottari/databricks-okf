---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20fb60275d86bec59f7f3aa9bbcf3ed474e029e2a4dd7672b6158965375f19f7
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scale-to-zero-for-model-serving-endpoints
    - SFMSE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Scale-to-Zero for Model Serving Endpoints
description: An optional configuration that allows endpoints to scale down to zero when idle, with the trade-off of cold-start latency and no guaranteed capacity when scaling back up.
tags:
  - model-serving
  - scaling
  - cost-optimization
timestamp: "2026-06-19T14:36:34.044Z"
---

# Scale to Zero for Model Serving Endpoints

**Scale to Zero** is an optional feature for [Model Serving](/concepts/model-serving.md) endpoints on Databricks that allows endpoints to automatically scale down to zero provisioned capacity after 30 minutes of sustained inactivity. This feature reduces costs for development, testing, or infrequently used endpoints by eliminating idle compute resources.

## How Scale to Zero Works

When enabled, an endpoint with no incoming traffic for 30 consecutive minutes shuts down all serving nodes. The endpoint remains registered and can serve requests again when new traffic arrives, but the first request after scaling to zero triggers a "cold start" while new compute resources are provisioned. You can enable or disable this option per served entity when creating or modifying an endpoint.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Cold Start Latency

Scaling from zero introduces additional latency on the first request, typically taking 10–20 seconds but potentially longer depending on model size and load time. For GPU endpoints, capacity is not guaranteed when scaled to zero, which may result in extra high latency for the first request after scaling back up.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Limitations and Warnings

Scale to zero is **not recommended for production endpoints**, as capacity is not guaranteed when scaled to zero. For latency-sensitive applications or endpoints requiring consistent uptime, this feature should be disabled. Databricks does not provide an SLA (Service Level Agreement) on scale-from-zero latency.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform that hosts custom models as production-grade APIs.
- [Serving Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) — General scaling behavior, including scale-up and scale-down timing.
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) — The maximum number of parallel requests the system can handle, used to estimate capacity.
- GPU Serving Endpoints — GPU compute types that may experience additional cold-start latency.
- [Express Deployments](/concepts/express-deployments-databricks.md) — An option for faster endpoint deployment speed.
- Route Optimization — Recommended for high QPS and low latency use cases.
- Custom Model Serving Tutorial — End-to-end guide for deploying models.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
