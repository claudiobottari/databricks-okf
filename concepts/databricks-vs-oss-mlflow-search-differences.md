---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b0eda43069535257351a2387daad38f59102c4296ffa7f9f3e4c06bef14a0c4
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-vs-oss-mlflow-search-differences
    - DVOMSD
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: Databricks vs OSS MLflow Search Differences
description: Databricks-managed MLflow shares most search query syntax with open-source MLflow but has field-level differences in supported filters and capabilities.
tags:
  - mlflow
  - databricks
  - compatibility
timestamp: "2026-06-19T20:20:05.692Z"
---

# Databricks vs OSS MLflow Search Differences

**Databricks vs OSS MLflow Search Differences** refers to the field-level and syntax-level distinctions between the search query language used by Databricks-managed MLflow and open source (OSS) MLflow when using `mlflow.search_traces()`. While the two implementations share most search query syntax, there are specific differences that users must account for when writing filter strings or migrating queries between environments. ^[search-traces-programmatically-databricks-on-aws.md]

## Overview

The `mlflow.search_traces()` API is available in both Databricks-managed MLflow and OSS MLflow, and both use a SQL-like `filter_string` parameter to query traces. Databricks-managed MLflow closely tracks the OSS MLflow search syntax, but introduces a few field-level differences. These differences affect which fields and comparators are supported in filter expressions. ^[search-traces-programmatically-databricks-on-aws.md]

## Key Differences

### Supported Fields and Comparators

The primary difference between Databricks and OSS MLflow lies in the set of supported filter fields and comparators. Databricks-managed MLflow supports a specific set of fields (prefixed with `trace.`, `tag.`, or `metadata.`) and comparators that may differ from the OSS version. Users should consult the Databricks documentation for the exact list of supported fields and operators in their environment. ^[search-traces-programmatically-databricks-on-aws.md]

### Third-Party OpenTelemetry Span Attributes

Databricks-managed MLflow provides a distinct mechanism for searching traces ingested from third-party OpenTelemetry tools (such as Langfuse). To search these traces, users must use the `span.attributes.*` prefix instead of the standard `trace.` prefix. This is a Databricks-specific extension not present in OSS MLflow. ^[search-traces-programmatically-databricks-on-aws.md]

## Shared Syntax Rules

Despite the differences, both Databricks and OSS MLflow share the following syntax rules for `filter_string`:

- String values must be wrapped in single quotes (e.g., `trace.status = 'OK'`).
- Numeric values must not be quoted (e.g., `trace.execution_time_ms > 1000`).
- Conditions can be combined with `AND`.
- The `OR` operator is **not** supported in either implementation.
- Time values must be expressed as Unix timestamps in milliseconds (e.g., `1749006880539`), not as dates.
- Tag or attribute names containing dots must be wrapped in backticks (e.g., `` tag.`mlflow.traceName` ``).

^[search-traces-programmatically-databricks-on-aws.md]

## Best Practices for Cross-Environment Queries

When writing filter strings that need to work across both Databricks and OSS MLflow:

1. **Use only shared syntax**: Stick to the common syntax rules listed above.
2. **Avoid Databricks-specific fields**: If portability is required, avoid fields that are only documented for Databricks-managed MLflow.
3. **Test in both environments**: Validate filter strings against both Databricks and OSS MLflow to catch unsupported fields or operators.
4. **Use keyword arguments**: Always use keyword (named) arguments with `mlflow.search_traces()` to avoid issues with evolving function signatures. ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- mlflow.search_traces() — The API function for programmatic trace search
- [Trace Search Query Syntax](/concepts/trace-search-query-syntax.md) — The SQL-like filter language used by MLflow
- [OpenTelemetry Span Attributes](/concepts/opentelemetry-mlflow-span-attribute-mapping.md) — Third-party trace ingestion and search
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and traces
- [Inference Tables](/concepts/inference-tables.md) — Storage backend for trace data on Databricks

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
