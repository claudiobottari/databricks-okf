---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4dfeb9a9117cf8ad339400618e27f633450448ea1d5c90d2ad70fe56ce73802
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-production-monitoring
    - MGPM
    - GenAI Application Monitoring
    - GenAI application monitoring
    - MLflow GenAI monitoring
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: MLflow GenAI Production Monitoring
description: Automated continuous quality assessment of GenAI app traces using scheduled scorers in production, with configurable sampling and multi-turn conversation evaluation.
tags:
  - mlflow
  - monitoring
  - genai
  - production
timestamp: "2026-06-19T19:46:43.580Z"
---

# MLflow GenAI Production Monitoring

**MLflow GenAI Production Monitoring** is a service in [MLflow 3](/concepts/mlflow-3.md) that automatically evaluates the quality of deployed generative AI applications by running [[scorers]] on production [Traces](/concepts/traces.md). It allows teams to schedule automated quality assessments, detect quality regressions, identify problematic queries, and surface improvement opportunities without manual intervention. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Overview

Production monitoring automatically runs MLflow 3 scorers on traces from GenAI applications to continuously assess quality. Scorers are scheduled against an [MLflow Experiment](/concepts/mlflow-experiment.md), and the monitoring service evaluates a configurable sample of incoming traces. Results are attached as feedback to each evaluated trace. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

The same scorers used for development evaluation with `mlflow.genai.evaluate()` can be used in production, ensuring consistency between pre‑deployment and post‑deployment quality assessments. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Capabilities

Production monitoring includes the following features: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- **Automated quality assessment** using built-in or custom scorers, including [Multi-turn Judges](/concepts/multi-turn-judges.md) for evaluating entire conversations.
- **Configurable sampling rates** to control the tradeoff between coverage and computational cost.
- **Continuous evaluation** running in the background after scorers are started.
- **Compatiblity with MLflow 2 traces** – MLflow 3 production monitoring works with traces logged from MLflow 2.

## Prerequisites

Before setting up production monitoring, ensure you have: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- **MLflow experiment**: An MLflow experiment where traces are being logged. If no experiment is specified, the active experiment is used.
- **Instrumented production application**: Your GenAI app must log traces using [MLflow Tracing](/concepts/mlflow-tracing.md). See the Production Tracing guide.
- **Defined scorers**: Tested scorers that work with your application's trace format. If you used your production app as the `predict_fn` in `mlflow.genai.evaluate()` during development, your scorers are likely already compatible.
- **Serverless budget policy**: If your workspace does not allow the default serverless budget policy, set a policy on the MLflow experiment before registering scorers. See [Configure a serverless budget policy for an MLflow experiment](/concepts/serverless-budget-policy-for-mlflow-experiments.md).
- **SQL warehouse ID (for Unity Catalog traces)**: If your traces are stored in [Unity Catalog](/concepts/unity-catalog.md), you must configure a SQL warehouse ID for monitoring to work.

## How It Works

### Registration and Start Pattern

Production monitoring follows a two‑step pattern: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

1. **Register** a scorer with an experiment using `.register(name="scorer_name")`.
2. **Start** monitoring with a sampling configuration using `.start(sampling_config=ScorerSamplingConfig(...))`.

At any given time, at most **20 scorers** can be associated with an experiment for continuous quality monitoring. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Scorer Types

Production monitoring supports several types of scorers: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- **Built‑in LLM judges** – Out‑of‑the‑box judges such as `Safety`, provided by MLflow.
- **Guidelines LLM judges** – Evaluate inputs and outputs using pass/fail natural language criteria.
- **LLM judges with custom prompts** – Allow multi‑level quality assessment with customizable choice categories, created using `make_judge()`.
- **Custom scorer functions** – User‑defined functions using the `@scorer` decorator for maximum flexibility.
- **Multi‑turn judges** – Evaluate entire conversations rather than individual traces. The monitoring job groups traces into conversations based on the `mlflow.trace.session` tag.

### Sampling Strategy

Use the `sample_rate` parameter to control evaluation coverage: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- **Critical scorers** (e.g., safety checks): `sample_rate=1.0` (100% coverage).
- **Expensive scorers** (e.g., complex LLM judges): `sample_rate=0.05` to `0.2`.
- **Iterative improvement**: `sample_rate=0.3` to `0.5`.

### Filtering Traces

Use the `filter_string` parameter to control which traces a scorer evaluates, using the same filter syntax as `mlflow.search_traces()`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(
        sample_rate=1.0,
        filter_string="attributes.status = 'OK'"
    ),
)
```

## Creating Scorers

### Using the UI

You can create and schedule LLM judges using the MLflow Experiment UI: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

1. Navigate to the **Judges** tab in the MLflow Experiment UI.
2. Click **New LLM judge**.
3. Specify what the scorer will evaluate by selecting **Traces** or **Sessions**.
4. Enter a name for the judge.
5. Select the evaluation criteria and judge type.
6. Set the **Run on all future traces** toggle and configure sample rate and filter string.
7. Test the judge on a set of existing traces before creating it.
8. Click **Create judge**.

Custom code judges cannot be created through the UI. Use a notebook to define and register them instead. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Using Python

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

# Register and start a built-in safety judge
safety_judge = Safety().register(name="my_safety_judge")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))
```

## Viewing Results

After scheduling scorers, allow 15–20 minutes for initial processing. Then: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

1. Navigate to your MLflow experiment.
2. Open the **Traces** tab to see assessments attached to traces.
3. Use monitoring dashboards to track quality trends.

For multi‑turn judges, assessments are attached to the first trace in each session. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Custom Scorer Requirements

Custom scorers for production monitoring have specific requirements due to serialization for remote execution: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- **Only `@scorer` decorator‑based scorers are supported.** Class‑based `Scorer` subclasses cannot be registered.
- **Scorers must be defined and registered from a Databricks notebook.** The monitoring service serializes the scorer function code for remote execution, and this serialization requires the notebook environment.
- **Scorers must be self-contained.** All imports must be done inline within the function body. The function cannot reference variables, objects, or modules defined outside of it.
- **No type hints requiring imports.** Type hints in the function signature that require import statements cause serialization failures.

Some packages are available by default without inline import, including `databricks-agents`, `mlflow-skinny`, `openai`, and all packages included in Serverless environment version 2. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Best Practices

### Sampling Strategy

- For critical scorers such as safety and security checks, use `sample_rate=1.0`.
- For expensive scorers such as complex LLM judges, use lower sample rates (0.05–0.2).
- For iterative improvement during development, use moderate rates (0.3–0.5).

### Custom Scorer Design

Keep custom scorers self-contained with all imports inside the function body. Handle missing data gracefully and return consistent types. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Troubleshooting

### Scorers Not Running

If scorers aren't executing, check the following: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

1. **Check experiment**: Ensure traces are logged to the experiment, not to individual runs.
2. **Sampling rate**: With low sample rates, it might take time to see results.
3. **Verify filter string**: Ensure your `filter_string` matches actual traces.

### Serialization Issues

Custom scorers for production monitoring are serialized for remote execution. To avoid serialization failures: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

- Define and register scorers from a Databricks notebook.
- Include all imports inline within the function body.
- Use only `@scorer` decorator‑based scorers, not class‑based subclasses.
- Avoid type hints that require imports in the function signature.

## Related Concepts

- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Overview of the metrics that power monitoring.
- [MLflow Evaluation Harness](/concepts/mlflow-genai-evaluation-harness.md) – The development‑side counterpart for systematic quality testing.
- [Traces](/concepts/traces.md) – Complete execution logs of a GenAI application.
- [Feedback](/concepts/feedback-object.md) – Quality measurements attached to traces.
- [Multi‑Turn Judges](/concepts/multi-turn-judges.md) – Judges that evaluate entire conversations.
- [Configure a Serverless Budget Policy for an MLflow Experiment](/concepts/serverless-budget-policy-for-mlflow-experiments.md) – Required policy configuration for monitoring setup.
- Manage Production Scorers – Lifecycle management of production scorers.
- [Backfill Historical Traces with Scorers](/concepts/backfillscorers.md) – Retroactively applying scorers.
- [Archive Traces to a Delta Table](/concepts/trace-archiving-to-delta-tables.md) – Saving traces and assessments.

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
