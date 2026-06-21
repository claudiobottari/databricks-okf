---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cf50f406690a7b4c319f2bebeaa9516c223305218d5d8c66196da9967403260
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-lifecycle-management-registerstart-pattern
    - SLM(P
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Scorer Lifecycle Management (Register/Start Pattern)
description: Two-step API pattern (.register() then .start()) for associating scorers with an MLflow experiment and activating continuous quality monitoring.
tags:
  - mlflow
  - api
  - lifecycle
  - scorers
timestamp: "2026-06-19T19:46:40.506Z"
---

---
title: Scorer Lifecycle Management (Register/Start Pattern)
summary: The two-step `.register()` then `.start()` pattern used to deploy scorers for continuous quality monitoring on production traces.
sources:
  - monitor-genai-apps-in-production-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T19:00:00.000Z"
updatedAt: "2026-06-19T19:00:00.000Z"
tags:
  - production-monitoring
  - scorers
  - lifecycle
  - mlflow
aliases:
  - register-start-pattern
  - scorer-lifecycle
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Scorer Lifecycle Management (Register/Start Pattern)

**Scorer Lifecycle Management (Register/Start Pattern)** refers to the two-step process by which a scorer is deployed for [Production Monitoring](/concepts/production-monitoring.md) of GenAI applications. To set up continuous quality assessment, you first register a scorer with an [MLflow Experiment](/concepts/mlflow-experiment.md) and then start it with a sampling configuration. This `.register()` → `.start()` pattern applies to all scorer types — built-in LLM judges, guidelines judges, custom-prompt judges, custom code scorers, and multi-turn judges. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Prerequisites

Before registering a scorer, ensure the following:

- An MLflow experiment exists where traces are being logged.
- The production application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) for production.
- Scorers have been tested and are compatible with the application’s trace format.
- If the workspace does not allow the default serverless budget policy, a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) must be set on the experiment first; otherwise, registration fails with a 403 PERMISSION_DENIED Serverless Budget Policy Error. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## The Register Step

The `register()` method associates the scorer with the experiment. Each scorer must be given a unique name within that experiment via the `name` parameter. For example:

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="my_safety_judge")
```

Built-in judges, [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md), judges created with `make_judge`, and multi-turn judges all follow the same registration method. Custom scorer functions decorated with `@scorer` also call `.register(name=...)`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## The Start Step

The `start()` method activates continuous evaluation by providing a `ScorerSamplingConfig` that defines the sampling rate and optional trace filters. For example:

```python
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.7)
)
```

Once started, the monitoring service evaluates a configurable sample of incoming traces and attaches the results as feedback. A scorer remains running until explicitly stopped. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Sampling Configuration

`ScorerSamplingConfig` accepts two parameters:

- `sample_rate` (float, 0.0–1.0): The fraction of traces to evaluate. Use `1.0` for critical scorers (e.g., safety) and lower rates (e.g., 0.05–0.2) for expensive operations.
- `filter_string` (optional): An MLflow Trace Filter expression to restrict which traces are evaluated, using the same syntax as `mlflow.search_traces()`. Multiple conditions can be combined.

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="safety")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(
        sample_rate=1.0,
        filter_string="attributes.status = 'OK'"
    )
)
```

^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Limitations

- At any given time, at most 20 scorers can be associated with an experiment for continuous quality monitoring. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- Custom code scorers registered for production monitoring must be defined in a Databricks notebook using the `@scorer` decorator; class-based `Scorer` subclasses are not supported. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Managing the Lifecycle

After a scorer is started, you can manage it further by:

- Stopping a scorer (e.g., via the UI or API).
- Updating the sampling configuration without re-registering.
- Archiving [Backfill Historical Traces with Scorers|backfilling historical traces](/concepts/historical-trace-backfilling.md).

See the Manage production scorers guide for details. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md)
- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md)
- [Custom Scorer Functions](/concepts/custom-scorer-definition-in-mlflow.md)
- [Multi-turn Judges](/concepts/multi-turn-judges.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- Sampling Strategy
- [Trace Filtering](/concepts/mlflow-trace-search-and-filtering.md)

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
