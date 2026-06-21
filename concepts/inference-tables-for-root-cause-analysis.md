---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3b51defd7273f6cb8df4839c87992840e51bdd0b28bd3a40b43c9f8ab32e26f
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-tables-for-root-cause-analysis
    - ITFRCA
    - Root Cause Analysis
    - Root cause analysis
    - inference-tables-for-request-root-cause-analysis
    - ITFRRCA
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Inference Tables for Root Cause Analysis
description: Using Unity Catalog inference tables to automatically log all requests and responses to model serving endpoints for query-based debugging of failed requests.
tags:
  - model-serving
  - debugging
  - monitoring
  - unity-catalog
timestamp: "2026-06-19T18:17:26.833Z"
---

# Inference Tables for Root Cause Analysis

**Inference Tables for Root Cause Analysis** is a debugging technique that uses [Unity Catalog](/concepts/unity-catalog.md) tables automatically populated with the requests and responses sent to a [Model Serving](/concepts/model-serving.md) endpoint. When enabled, these tables allow engineers to query historical inference data, including status codes, request inputs, and response outputs, to diagnose why specific requests failed. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Overview

Inference tables are a feature of the [AI Gateway](/concepts/ai-gateway.md) that automatically log every request and response made to a model serving endpoint into a user-configurable Unity Catalog table. For root cause analysis, the key columns are `request`, `response`, `request_time`, and `status_code`. By filtering on non-200 status codes or inspecting the response payload, developers can pinpoint errors such as input incompatibility, model crashes, or configuration issues. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Using Inference Tables for Root Cause Analysis

### 1. Locate the Inference Table

In the Databricks workspace, navigate to the **Serving** tab and select the endpoint you want to debug. Under the **Inference tables** section, note the fully-qualified table name (e.g., `my-catalog.my-schema.my-table`). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### 2. Query Failed Requests

Use SQL in a notebook to retrieve records with non-200 status codes:

```sql
SELECT * 
FROM my-catalog.my-schema.my-table
WHERE status_code != 200
```

This returns only the requests that encountered errors, along with their full request and response payloads. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### 3. Analyze the Response Column

For each failed request, inspect the `response` column to find error messages. Common patterns include:

- `MlflowException` errors (mapped to 4xx responses) – typically fixed by adjusting the input format or model dependencies.
- Timeout or internal errors (5xx responses) – may indicate resource exhaustion or model code bugs.

If [agent tracing for AI agents](/concepts/crewai-task-and-agent-tracing.md) is enabled, the **Response** column also contains detailed execution traces. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### 4. Narrow by Time and Input

Combine filtering on `request_time` and `status_code` to isolate spikes of errors or correlate with deployment changes. You can also join with external monitoring data to correlate with upstream system health. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Benefits

- **No additional instrumentation** – tables are populated automatically once the inference table feature is enabled.
- **Full historical record** – enables after-the-fact analysis of intermittent failures.
- **Integration with Unity Catalog** – tables can be queried, shared, and governed like any other Unity Catalog object.

## Requirements

- Inference tables must be enabled on the serving endpoint. See Enable Inference Tables for Model Serving (documented in the AI Gateway section of the Databricks documentation).
- The user querying the table must have `SELECT` permission on the table in Unity Catalog.

## Related Concepts

- Model Serving Debugging – broader debugging strategies for model serving endpoints.
- [AI Gateway Inference Tables](/concepts/ai-gateway-inference-tables.md) – configuration and management of inference tables.
- [Root Cause Analysis](/concepts/inference-tables-for-root-cause-analysis.md) – general methodology for diagnosing failures.
- [Model Serving Monitoring](/concepts/databricks-model-serving-monitoring.md) – tools for endpoint health and quality monitoring.
- [Unity Catalog](/concepts/unity-catalog.md) – the data governance layer that stores inference tables.

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
