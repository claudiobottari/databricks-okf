---
title: Monitor model quality and endpoint health | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints
ingestedAt: "2026-06-18T08:12:18.123Z"
---

Model Serving provides advanced tooling for monitoring the quality and health of models and their deployments. The following table is an overview of each monitoring tool available.

Tool

Description

Purpose

Access

[Ephemeral service logs](https://docs.databricks.com/api/workspace/servingendpoints/logs)

Captures `stdout` and `stderr` streams from the model serving endpoint.

Useful for debugging during model deployment. Use `logging.warning(...)` or `logging.error(...)` for immediate display in the logs.

Accessible using the **Logs tab** in the Serving UI. Logs are streamed in real-time and can be exported through the API.

[OpenTelemetry for custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs)

Persists standard system logs, custom application logs, metrics, and traces to Unity Catalog Delta tables using OpenTelemetry for long-term retention.

Useful for historical debugging, compliance requirements, and analyzing production issues using SQL queries.

Configure telemetry settings in the Serving UI or API when creating the endpoint. Query logs using Unity Catalog SQL or Databricks notebooks.

[Build logs](https://docs.databricks.com/api/workspace/servingendpoints/buildlogs)

Displays output from the process which automatically creates a production-ready Python environment for the model serving endpoint.

Useful for diagnosing model deployment and dependency issues.

Available upon completion of the model serving build under **Build logs** in the **Logs** tab. Logs can be exported through the API. These logs are retained for up to thirty (30) days.

[Endpoint health metrics](https://docs.databricks.com/aws/en/machine-learning/model-serving/metrics-export-serving-endpoint)

Provides insights into infrastructure metrics like latency, request rate, error rate, CPU usage, and memory usage.

Important for understanding the performance and health of the serving infrastructure.

Available by default in the Serving UI for the last 14 days. Data can also be streamed to observability tools in real-time.

[AI Gateway-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables)

Automatically logs online prediction requests and responses into Delta tables managed by Unity Catalog for endpoints that serve custom models, external models, or provisioned throughput workloads.

Use this tool for monitoring and debugging model quality or responses, generating training data sets, or conducting compliance audits.

Can be enabled for existing and new model serving endpoints when enabling [AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) features using the Serving UI or REST API.
