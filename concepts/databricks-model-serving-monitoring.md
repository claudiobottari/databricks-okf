---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7dceed629b684ff4549b7115fc17c0c4e0f21490c93c544b9ad1604c083ce4d5
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-monitoring
    - DMSM
    - Model Serving Monitoring
    - Model Serving monitoring
    - System tables for serving monitoring
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: Databricks Model Serving Monitoring
description: Overview of monitoring tools available for model quality and endpoint health on Databricks Model Serving.
tags:
  - monitoring
  - machine-learning
  - databricks
timestamp: "2026-06-19T19:46:45.527Z"
---

# Databricks Model Serving Monitoring

**Databricks Model Serving Monitoring** encompasses a suite of tools and features for tracking the quality, performance, and health of models deployed on Databricks Model Serving endpoints. These tools provide capabilities ranging from real-time debugging to long-term compliance auditing.

## Overview

Model Serving provides advanced tooling for monitoring the quality and health of models and their deployments. The available monitoring tools serve different purposes, from debugging during deployment to analyzing production issues over extended periods. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Monitoring Tools

### Ephemeral Service Logs

Captures `stdout` and `stderr` streams from the model serving endpoint. This tool is useful for debugging during model deployment. Use `logging.warning(...)` or `logging.error(...)` for immediate display in the logs. Logs are accessible using the **Logs tab** in the Serving UI, streamed in real-time, and can be exported through the API. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

### OpenTelemetry for Custom Model Serving Endpoints

Persists standard system logs, custom application logs, metrics, and traces to [Unity Catalog](/concepts/unity-catalog.md) Delta tables using OpenTelemetry for long-term retention. This tool is useful for historical debugging, compliance requirements, and analyzing production issues using SQL queries. Configure telemetry settings in the Serving UI or API when creating the endpoint. Query logs using Unity Catalog SQL or Databricks notebooks. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

### Build Logs

Displays output from the process that automatically creates a production-ready Python environment for the model serving endpoint. This tool is useful for diagnosing model deployment and dependency issues. Build logs are available upon completion of the model serving build under **Build logs** in the **Logs** tab. Logs can be exported through the API and are retained for up to thirty (30) days. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

### Endpoint Health Metrics

Provides insights into infrastructure metrics like latency, request rate, error rate, CPU usage, and memory usage. These metrics are important for understanding the performance and health of the serving infrastructure. They are available by default in the Serving UI for the last 14 days. Data can also be streamed to observability tools in real-time. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

### AI Gateway-Enabled Inference Tables

Automatically logs online prediction requests and responses into Delta tables managed by Unity Catalog for endpoints that serve custom models, external models, or provisioned throughput workloads. Use this tool for monitoring and debugging model quality or responses, generating training data sets, or conducting compliance audits. Can be enabled for existing and new model serving endpoints when enabling [AI Gateway](/concepts/ai-gateway.md) features using the Serving UI or REST API. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Tool Comparison

| Tool | Description | Purpose | Access |
|------|-------------|---------|--------|
| Ephemeral service logs | Captures `stdout` and `stderr` streams | Debugging during model deployment | Logs tab in Serving UI; real-time streaming; API export |
| OpenTelemetry | Persists logs, metrics, and traces to Unity Catalog Delta tables | Historical debugging, compliance, SQL-based analysis | Configure in Serving UI or API; query via Unity Catalog SQL |
| Build logs | Output from production environment creation | Diagnosing deployment and dependency issues | Build logs in Logs tab; API export; 30-day retention |
| Endpoint health metrics | Infrastructure metrics (latency, request rate, error rate, CPU, memory) | Understanding serving infrastructure performance | Default in Serving UI (14 days); real-time streaming to observability tools |
| AI Gateway inference tables | Automatic logging of prediction requests/responses to Delta tables | Monitoring model quality, generating training data, compliance audits | Enable via Serving UI or REST API with AI Gateway |

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The core deployment infrastructure for models on Databricks
- [AI Gateway](/concepts/ai-gateway.md) — Feature set enabling inference tables and other monitoring capabilities
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing Delta tables used by OpenTelemetry and inference tables
- OpenTelemetry — Observability framework for collecting logs, metrics, and traces
- [Delta Tables](/concepts/delta-lake-table.md) — Storage format for persisted monitoring data
- Serving Endpoint Logs API — Programmatic access to service logs and build logs

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
