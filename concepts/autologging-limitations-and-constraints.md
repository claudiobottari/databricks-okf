---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ec9119da228cf11ce024082d85218a76bc3c96723936e43690aeb3f4799ba45
  pageDirectory: concepts
  sources:
    - tracing-gemini-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-limitations-and-constraints
    - Constraints and Autologging Limitations
    - ALAC
  citations:
    - file: tracing-gemini-databricks-on-aws.md
title: Autologging Limitations and Constraints
description: "MLflow Gemini autolog has known constraints: not auto-enabled on serverless compute clusters, only supports synchronous text interactions (no async), and may not record full inputs for multi-modal inputs."
tags:
  - mlflow
  - tracing
  - gemini
  - limitations
timestamp: "2026-06-19T23:11:46.770Z"
---

Here is the wiki page for "Autologging Limitations and Constraints", written based solely on the provided source material.

---

## Autologging Limitations and Constraints

**Autologging Limitations and Constraints** refers to the specific behaviors and conditions where [Automatic Tracing](/concepts/automatic-tracing.md) and logging of machine learning workflows are restricted or not fully supported. These limitations vary by integration and compute environment.

### Serverless Compute Environments

On serverless compute clusters, autologging is **not automatically enabled**. Users must explicitly call the autolog function for each integration to enable [Automatic Tracing](/concepts/automatic-tracing.md). For example, to enable tracing for Google Gemini on serverless compute, you must call `mlflow.gemini.autolog()`. ^[tracing-gemini-databricks-on-aws.md]

### Integration-Specific Constraints

#### Google Gemini Integration

The [MLflow](/concepts/mlflow.md) Gemini integration has several specific limitations:

- **Synchronous calls only**: Tracing is only supported for synchronous calls for text interactions. **Async APIs are not traced**. ^[tracing-gemini-databricks-on-aws.md]
- **Multi-modal inputs**: Full inputs may not be recorded for multi-modal inputs. ^[tracing-gemini-databricks-on-aws.md]

#### Other Integrations

While not detailed in the source material, limitations may exist for other integrations such as OpenAI and Bedrock. Users should consult the specific documentation for each integration to understand any constraints that apply. ^[tracing-gemini-databricks-on-aws.md] <!-- inferred: The source mentions other integrations exist but doesn't detail their limitations -->

### Disabling Autologging

Autologging can be disabled globally by calling the disable method on the autolog function. For example, to disable Gemini tracing globally, call `mlflow.gemini.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-gemini-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that autologging relies on
- [Gemini Autologging](/concepts/mlflow-gemini-autolog.md) — [Automatic Tracing](/concepts/automatic-tracing.md) for the Google Gemini SDK
- Trace Data Capture — What information is automatically captured during tracing
- Serverless Compute — The compute environment where autologging requires explicit calls

### Sources

- tracing-gemini-databricks-on-aws.md

# Citations

1. [tracing-gemini-databricks-on-aws.md](/references/tracing-gemini-databricks-on-aws-52fc6461.md)
