---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99bc13478a71250518b49a69902350bdff5688ac8efe1b86fdf98de98fe82a76
  pageDirectory: concepts
  sources:
    - manage-production-scorers-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - production-monitoring-for-genai-applications
    - PMFGA
    - Production Monitoring (MLflow)|Monitor safety in production
    - Production Monitoring for GenAI|continuous monitoring in production
    - Production Monitoring for GenAI|production monitoring
    - Production monitoring for GenAI|production monitoring
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Production Monitoring for GenAI Applications
description: The broader framework for setting up, managing, and backfilling production monitoring of GenAI applications using scorers in Databricks MLflow.
tags:
  - mlflow
  - genai
  - monitoring
  - production
timestamp: "2026-06-19T19:28:35.601Z"
---

```markdown
---
title: Production Monitoring for GenAI Applications
summary: Automated quality and safety assessment for GenAI applications in production via scheduled MLflow scorers.
sources:
  - monitor-genai-apps-in-production-databricks-on-aws.md
  - archive-traces-to-a-delta-table-databricks-on-aws.md
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:03:09.342Z"
updatedAt: "2026-06-19T09:03:09.342Z"
tags:
  - genai
  - monitoring
  - mlflow
aliases:
  - production-monitoring-for-genai-applications
  - PMFGA
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# Production Monitoring for GenAI Applications

**Production monitoring** for GenAI applications automatically runs MLflow 3 scorers on traces from your deployed applications to continuously assess quality, safety, and custom metrics. By scheduling scorers against an [[MLflow experiment]], the monitoring service evaluates a configurable sample of incoming traces and attaches the results as feedback to each evaluated trace. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Key Features

- **Automated quality assessment** using built-in or custom scorers, including [[multi-turn judges]] that evaluate entire conversations. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Configurable sampling rates** to balance coverage and computational cost. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Consistent evaluation** across development and production by reusing the same scorers. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Continuous background monitoring** with results viewable in the MLflow experiment UI. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Compatibility with MLflow 2 traces** — production monitoring works with traces logged from either MLflow 2 or MLflow 3. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Trace archiving** to a Unity Catalog Delta table for long-term storage and advanced analytics. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Prerequisites

Before setting up production monitoring, you need:

- **An MLflow experiment** where traces are being logged. If no experiment is specified, the active experiment is used. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **An instrumented production application** that logs traces using [[MLflow Tracing]] (see the [Production Tracing guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing)). ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Defined scorers** that are tested to work with your application’s trace format. If you used your production app as the `predict_fn` in `mlflow.genai.evaluate()` during development, your scorers are likely already compatible. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **A serverless budget policy** — if your workspace does not allow the default serverless budget policy, set a policy on the MLflow experiment before registering scorers to avoid the 403 PERMISSION_DENIED Serverless Budget Policy Error. ^[monitor-genai-apps-in-production-databricks-on-aws.md] ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **A SQL warehouse ID (for Unity Catalog traces)** — if your traces are stored in Unity Catalog, you must configure a SQL warehouse ID for monitoring to work. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Getting Started

Production monitoring follows a two-step pattern for all scorer types: **register** the scorer with the experiment, then **start** it with a sampling configuration. At most 20 scorers can be associated with one experiment at any time. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Using Built-in LLM Judges

MLflow provides built-in judges such as `Safety`, `Guidelines`, and multi-turn judges like `ConversationCompleteness` and `UserFrustration`. You can optionally override the model used for scoring by specifying a Databricks model serving endpoint in the format `databricks:/<endpoint-name>`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="my_safety_judge")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))
```

### Using Guidelines Judges

Guidelines judges evaluate inputs and outputs against pass/fail natural language criteria. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Guidelines

english_judge = Guidelines(
    name="english",
    guidelines=["The response must be in English"]
).register(name="is_english")

english_judge = english_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))
```

### Using Custom LLM Judges (make_judge)

For multi-level quality assessment with customizable choice categories, use [`make_judge`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/). The judge’s instructions can reference `{{ inputs }}` and `{{ outputs }}` placeholders. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from typing import Literal
from mlflow.genai import make_judge

formality_judge = make_judge(
    name="formality",
    instructions="...",
    feedback_value_type=Literal["formal", "semi_formal", "not_formal"],
    model="databricks:/databricks-gpt-oss-20b",
)
registered_judge = formality_judge.register(name="my_formality_judge")
registered_judge = registered_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.1))
```

### Using Custom Scorer Functions

For maximum flexibility, use the `@scorer` decorator to define custom criteria. Scorers must be **self-contained** — all imports must be inline, and the function cannot reference external variables. Class-based `Scorer` subclasses are not supported. Scorers must also be defined and registered from a Databricks notebook to enable serialization. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer, ScorerSamplingConfig

@scorer
def mentions_databricks(outputs):
    """Check if the response mentions Databricks"""
    return "databricks" in str(outputs.get("response", "")).lower()

databricks_scorer = mentions_databricks.register(name="databricks_mentions")
databricks_scorer = databricks_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))
```

### Using Multi-Turn Judges

Multi-turn judges evaluate entire conversations rather than individual traces. They are registered and started the same way as single-turn judges. The monitoring job groups traces into conversations based on the `mlflow.trace.session` tag. A conversation is considered complete when no new traces with that session ID are ingested for **5 minutes** (configurable via the `MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS` environment variable). ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

completeness_scorer = ConversationCompleteness().register(name="conversation_completeness")
completeness_scorer = completeness_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=1.0))
```

### Combining Judges

Single-turn and multi-turn judges can be combined in the same experiment by registering and starting each individually. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Viewing Results

After scheduling scorers, allow 15–20 minutes for initial processing. Then:

1. Navigate to your MLflow experiment.
2. Open the **Traces** tab to see assessments attached to traces.
3. Use the monitoring dashboards to track quality trends.

For multi-turn judges, assessments are attached to the first trace in each session. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Best Practices

### Sampling Strategy

- **Critical scorers** (safety, security): use `sample_rate=1.0` for 100% coverage. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Expensive scorers** (complex LLM judges): use lower rates (0.05–0.2). ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Iterative development**: use moderate rates (0.3–0.5). ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Filter Traces

Use the `filter_string` parameter in `ScorerSamplingConfig` to control which traces are evaluated. The filter syntax is the same as `mlflow.search_traces()`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(
        sample_rate=1.0,
        filter_string="attributes.status = 'OK'"
    ),
)
```

### Custom Scorer Design

- Keep scorers **self-contained** with inline imports. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- Handle missing data gracefully (e.g., use `.get()` with defaults). ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- Return consistent types. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- Avoid type hints in function signatures that require imports (e.g., `List` from `typing`). ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Trace Archiving

Use `enable_databricks_trace_archival` to save traces and their assessments to a Unity Catalog Delta table for long-term storage, custom dashboards, and building evaluation datasets. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

Archiving can be disabled with `disable_databricks_trace_archival`. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Troubleshooting

### Scorers Not Running

- **Check experiment**: Ensure traces are logged to the experiment, not to individual runs. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Sampling rate**: With low rates, results may take longer to appear. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Verify filter string**: Ensure `filter_string` matches actual traces. ^

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
2. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
