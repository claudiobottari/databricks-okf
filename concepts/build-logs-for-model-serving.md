---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d41a5a12bbf90f56add669bbaabcb912dbaf745ea93faaf05da044f7663dadb
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - build-logs-for-model-serving
    - BLFMS
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: Build Logs for Model Serving
description: Displays output from the process that creates a production-ready Python environment for model serving endpoints, retained for up to 30 days.
tags:
  - logging
  - deployment
  - dependency-management
timestamp: "2026-06-19T19:46:48.846Z"
---

# Build Logs for Model Serving

**Build Logs** capture output from the process that automatically creates a production-ready Python environment for a model serving endpoint on Databricks. These logs are essential for diagnosing model deployment issues and dependency problems during the build phase. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Overview

When a model is deployed to a serving endpoint, Databricks automatically builds a Python environment that includes all required dependencies. The build process generates logs that display the output of this environment creation. These logs are distinct from [Ephemeral Service Logs](/concepts/ephemeral-service-logs.md), which capture runtime `stdout` and `stderr` streams, and from OpenTelemetry Logs, which persist logs to Unity Catalog for long-term retention. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Accessing Build Logs

Build logs are available upon completion of the model serving build process. To access them:

1. Navigate to the **Serving UI** for your endpoint.
2. Open the **Logs** tab.
3. Select **Build logs** to view the output.

Logs can also be exported programmatically through the [Serving Endpoints API](https://docs.databricks.com/api/workspace/servingendpoints/buildlogs). ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Retention

Build logs are retained for up to thirty (30) days. After this period, they are automatically removed and are no longer accessible through the UI or API. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Use Cases

Build logs are primarily useful for:

- **Diagnosing model deployment issues**: When a model fails to deploy, build logs can reveal errors in the environment setup process.
- **Resolving dependency problems**: If a required Python package fails to install or has version conflicts, the build logs will show the relevant error messages.
- **Verifying environment configuration**: Confirming that the correct packages and versions are being installed during the build phase.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform for deploying and serving models on Databricks.
- [Ephemeral Service Logs](/concepts/ephemeral-service-logs.md) — Real-time runtime logs for debugging during model deployment.
- OpenTelemetry for Custom Model Serving Endpoints — Persistent logging to Unity Catalog for long-term analysis.
- [Endpoint Health Metrics](/concepts/endpoint-health-metrics.md) — Infrastructure metrics for monitoring serving performance.
- [AI Gateway Inference Tables](/concepts/ai-gateway-inference-tables.md) — Automatic logging of prediction requests and responses.

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
