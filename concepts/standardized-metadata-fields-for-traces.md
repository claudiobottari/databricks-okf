---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa1494766a14f249303889e660af03bf7f0aab61b69a390054f674536ae6bbe0
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - standardized-metadata-fields-for-traces
    - SMFFT
    - Standard metadata fields for traces
    - Standard Metadata Fields
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Standardized Metadata Fields for Traces
description: Predefined metadata field names (like mlflow.trace.user, mlflow.trace.session, mlflow.source.type) that MLflow recognizes for automatic UI filtering, grouping, and environment detection.
tags:
  - mlflow
  - tracing
  - metadata
  - observability
timestamp: "2026-06-19T17:27:13.041Z"
---

# Standardized Metadata Fields for Traces

**Standardized Metadata Fields for Traces** are predefined key–value pairs that MLflow provides to capture common contextual information about GenAI application executions. Using these fields enables consistent tracking, filtering, and analysis of user behavior, session continuity, environment characteristics, and application versions across traces.

## Overview

Adding context to traces allows you to track execution details, analyze user behavior, debug issues across environments, and monitor application performance. MLflow offers standardized metadata fields for common context types plus the flexibility to attach custom metadata specific to your application. ^[add-context-to-traces-databricks-on-aws.md]

These metadata fields are set during application execution by calling `mlflow.update_current_trace()` with a `metadata` dictionary. After a trace is logged, metadata values are **immutable** (cannot be updated), unlike tags which remain mutable. ^[add-context-to-traces-databricks-on-aws.md]

Using the standardized fields automatically enables filtering and grouping in the MLflow UI, making it easier to slice traces by user, session, or environment. ^[add-context-to-traces-databricks-on-aws.md]

## Requirements

To use standardized metadata fields for traces, you must:

- Install the `mlflow-tracing` package (optimized for production with minimal dependencies). ^[add-context-to-traces-databricks-on-aws.md]
- Use MLflow 3 (MLflow 2.x is not supported due to performance limitations and missing features). ^[add-context-to-traces-databricks-on-aws.md]

## Standard Fields for Users and Sessions

MLflow provides two standard metadata fields for user and session tracking:

| Field | Purpose |
|-------|---------|
| `mlflow.trace.user` | Associates traces with specific users. |
| `mlflow.trace.session` | Groups traces that belong to multi-turn conversations. |

^[add-context-to-traces-databricks-on-aws.md]

Tracking users and sessions enables powerful analytics:

- **User behavior analysis** – understand how different users interact with your application.
- **Conversation flow tracking** – analyze multi-turn conversations and context retention.
- **Personalization insights** – identify patterns to improve user-specific experiences.
- **Quality per user** – track performance metrics across different user segments.
- **Session continuity** – maintain context across multiple interactions.

Because these are immutable metadata fields, they are ideal for identifiers that should not change after a trace is logged. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Fields for Environments and Versions

Tracking the execution environment and application version helps debug performance and quality issues relative to code changes. MLflow automatically populates certain standard metadata fields based on the execution environment, such as `mlflow.source.type` and `mlflow.source.name`. These can be overridden via `mlflow.update_current_trace()` if the automatic detection does not meet your requirements. ^[add-context-to-traces-databricks-on-aws.md]

The standardized deployment metadata supports:

- **Environment-specific analysis** across `development`, `staging`, and `production`.
- **Performance/quality tracking** and regression detection across app versions.
- **Faster root cause analysis** when issues occur.

Best practice is to populate these metadata fields from environment variables rather than hard-coding values, simplifying deployment. ^[add-context-to-traces-databricks-on-aws.md]

## Custom Metadata

In addition to the standardized fields, you can attach any application‑specific context using custom `metadata` keys. Examples include:

- Application version
- Deployment ID
- Deployment region
- Feature flags

Custom metadata provides flexibility to capture additional context that is specific to your application’s domain. ^[add-context-to-traces-databricks-on-aws.md]

## Accessing Metadata in Trace Logs

Metadata can be retrieved from trace logs using the `metadata` field in the pandas DataFrame returned by `mlflow.search_traces()`, or by accessing the `Trace.info.trace_metadata` attribute on [Trace objects](/concepts/tracedata-and-span-objects.md). Tags are similarly accessible via the `tags` field or `Trace.info.tags`. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Consistent ID formats** – Use standardized formats for user and session IDs across your application.
2. **Session boundaries** – Define clear rules for when sessions start and end.
3. **Environment variables** – Populate metadata from environment variables rather than hard-coding values.
4. **Combine context types** – Track user, session, and environment context together for complete traceability.
5. **Regular analysis** – Set up dashboards to monitor user behavior, session patterns, and version performance.
6. **Override defaults thoughtfully** – Only override automatically populated metadata when necessary.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The foundational instrumentation framework for traces.
- [Trace Metadata](/concepts/trace-metadata.md) – General discussion of metadata in traced executions.
- User Behavior Analysis – Analytics enabled by user and session metadata.
- [Environment Tracking](/concepts/mlflow-environment-and-version-tracking.md) – Using environment metadata for debugging and regression detection.
- Custom Metadata and Tags – Adding arbitrary context beyond standard fields.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
