---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c15ff64a5b56de6f03bb6fa00e2e3a7d4de491b5b71263fe75095441b16fc6a5
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - environment-and-version-tracking-in-traces
    - Version Tracking in Traces and Environment
    - EAVTIT
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Environment and Version Tracking in Traces
description: Capturing execution environment (development, staging, production) and application version metadata via environment variables and standardized MLflow fields like mlflow.source.type.
tags:
  - mlflow
  - tracing
  - devops
  - deployment
timestamp: "2026-06-19T17:27:48.601Z"
---

# Environment and Version Tracking in Traces

**Environment and Version Tracking in Traces** refers to the practice of attaching metadata about the execution environment (e.g., `development`, `staging`, `production`) and application version to [Traces](/concepts/traces.md) in [MLflow](/concepts/mlflow.md) GenAI. This metadata enables debugging of performance and quality issues relative to code, environment-specific analysis, regression detection across application versions, and faster root cause analysis when issues occur. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow provides standardized metadata fields for deployment context. The key field is `mlflow.source.type`, which indicates the environment. To set these fields, your application should generally extract the metadata from environment variables rather than hard-coding values. For example: ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow
import os

mlflow.update_current_trace(
    metadata={
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    }
)
```

## Automatically Populated Metadata

MLflow automatically sets certain standard metadata fields based on your execution environment. You can override any of these automatically populated fields using `mlflow.update_current_trace()`. This is useful when the automatic detection does not meet your requirements — for instance, you can override the execution environment value by calling `mlflow.update_current_trace(metadata={"mlflow.source.name": "custom_name"})`. ^[add-context-to-traces-databricks-on-aws.md]

## Custom Metadata

Beyond the standard fields, you can use custom `metadata` keys to capture application-specific context such as:

- Application version
- Deployment ID
- Deployment region
- Feature flags

These custom keys are added to the trace via the `metadata` parameter of `mlflow.update_current_trace()`. Once a trace is logged, `metadata` becomes immutable, so values must be set before the trace is finalized. Tags, by contrast, remain mutable after logging. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Use environment variables** – Populate metadata from environment variables rather than hard-coding values, which simplifies deployment across different environments. ^[add-context-to-traces-databricks-on-aws.md]
2. **Combine context types** – Track environment, version, user, and session context together for complete traceability. ^[add-context-to-traces-databricks-on-aws.md]
3. **Override defaults thoughtfully** – Only override automatically populated metadata when the default values do not fit your deployment model. ^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) – The fundamental unit of observability in MLflow GenAI.
- [MLflow](/concepts/mlflow.md) – The machine learning lifecycle platform that provides tracing capabilities.
- [Adding Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – Broader concept covering user, session, and environment metadata.
- [User and Session Tracking in Traces](/concepts/user-and-session-tracking-in-llm-traces.md) – Tracking user identity and conversation groupings.
- [Trace Metadata](/concepts/trace-metadata.md) – The immutable key-value store attached to a trace.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
