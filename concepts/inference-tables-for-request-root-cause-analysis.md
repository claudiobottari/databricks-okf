---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5114da1a32286cecf18b8ec187de3d9fb6698c587cef8588e7ca98e6d1a0ab99
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-tables-for-request-root-cause-analysis
    - ITFRRCA
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Inference Tables for Request Root Cause Analysis
description: Using inference tables in Unity Catalog to log, query, and analyze model serving endpoint requests and responses for debugging failures.
tags:
  - model-serving
  - debugging
  - unity-catalog
  - monitoring
timestamp: "2026-06-18T15:11:31.622Z"
---

# Inference Tables for Request Root Cause Analysis

**Inference Tables for Request Root Cause Analysis** refers to the practice of using [Inference Tables](/concepts/inference-tables.md) — Unity Catalog tables that automatically log all requests and responses to a model serving endpoint — to diagnose and debug failed inference requests.

## Overview

When a request to a model serving endpoint fails, root cause analysis can be performed by querying the endpoint's inference table. If enabled, inference tables automatically capture every request and response sent to the endpoint, storing them in a Unity Catalog table for later analysis. This provides a complete historical record for investigating failures. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Prerequisites

To use inference tables for root cause analysis, the feature must first be enabled for the endpoint. See the documentation on Monitor served models using Unity AI Gateway-enabled inference tables for setup instructions. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Querying Inference Tables

To analyze failed requests:

1. **Locate the inference table**: In the workspace, go to the **Serving** tab and select the endpoint name. In the **Inference tables** section, find the table's fully-qualified name (e.g., `my-catalog.my-schema.my-table`). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

2. **Query the table**: Run the following in a Databricks notebook to view all data: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

```sql
SELECT * FROM my-catalog.my-schema.my-table
```

3. **Filter for failures**: Narrow results to only failed requests by filtering on `status_code`: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

```sql
SELECT * FROM my-catalog.my-schema.my-table
WHERE status_code != 200
```

## Key Columns for Analysis

Inference tables contain several columns useful for root cause analysis: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

| Column | Purpose |
|--------|---------|
| `request` | The input sent to the model |
| `response` | The output returned by the model (or error details) |
| `request_time` | Timestamp of the request |
| `status_code` | HTTP status code of the response |

By filtering and examining these columns, you can identify patterns in failed requests, understand which inputs cause errors, and narrow down the root cause. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Agent Tracing

If [agent tracing](/concepts/autogen-auto-tracing.md) has been enabled for AI agents, the **Response** column provides access to detailed execution traces that show the full history of the request, including tool calls, intermediate reasoning steps, and their results. See [Enable inference tables for AI agents](/concepts/inference-tables.md) for more information. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Inference Tables](/concepts/inference-tables.md) — The Unity Catalog feature that powers this analysis
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints whose traffic is logged
- Debugging Guide for Model Serving — Broader debugging approaches
- [Pre-deployment Validation](/concepts/pre-deployment-validation-for-model-serving.md) — Catching issues before they reach production
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where inference tables are stored

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
