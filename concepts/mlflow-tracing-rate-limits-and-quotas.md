---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c283c793a47d5233f507ad3ba798e5c5657e36ea5d1d56cc9e47f486a115b3f2
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-rate-limits-and-quotas
    - Quotas and MLflow Tracing Rate Limits
    - MTRLAQ
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Tracing Rate Limits and Quotas
description: Databricks workspaces impose rate limits and quotas on MLflow Tracing to ensure service stability and fair usage.
tags:
  - mlflow
  - tracing
  - databricks
  - quotas
timestamp: "2026-06-19T23:11:24.297Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Rate Limits and Quotas

**MLflow Tracing** in Databricks is subject to several quotas and rate limits designed to ensure service stability and fair usage across workspaces. These limits affect the number of [Traces](/concepts/traces.md) that can be stored, retrieved, and searched. ^[tracing-faq-databricks-on-aws.md]

## General Resource Limits

When using [MLflow Tracing](/concepts/mlflow-tracing.md) within a Databricks workspace, general [workspace-level resource limits](https://docs.databricks.com/aws/en/resources/limits) apply. For the most current set of rate limits and quotas, consult the official Databricks documentation on resource limits. ^[tracing-faq-databricks-on-aws.md]

## Trace List Limit

By default, the trace list in the [MLflow](/concepts/mlflow.md) UI returns only the **most recent 1,000 traces**. If an older trace falls outside this window, it will not appear in search results, even if you search by trace ID. ^[tracing-faq-databricks-on-aws.md]

To retrieve an older trace, you can narrow the time range filter so that the trace becomes one of the 1,000 most recent entries for that specific period. Alternatively, if you know the experiment ID and trace ID, you can navigate directly to the trace using the URL pattern: `<workspace-url>/ml/experiments/<experiment-id>/[Traces](/concepts/traces.md)/<trace-id>`. ^[tracing-faq-databricks-on-aws.md]

## Total Trace Limit for Non-Unity Catalog Experiments

Experiments that are **not** stored in [Unity Catalog](/concepts/unity-catalog.md) are capped at **100,000 [Traces](/concepts/traces.md) total**. Once this limit is reached, no new [Traces](/concepts/traces.md) can be added to the experiment through the default [MLflow Tracking](/concepts/mlflow-tracking.md) service. ^[tracing-faq-databricks-on-aws.md]

To remove both the trace list limit (1,000 most recent) and the total trace cap (100,000), you can [migrate [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc). [Traces](/concepts/traces.md) stored in [Unity Catalog](/concepts/unity-catalog.md) are not subject to these storage limits and support full search across all [Traces](/concepts/traces.md) within a time range. ^[tracing-faq-databricks-on-aws.md]

## Related Concepts

- Resource limits (Databricks)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Trace list](/concepts/traces.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Trace search

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
