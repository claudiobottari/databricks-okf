---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e495b04997564736701bb6e3ebe592a75568ba71650c123c08d38cf26ea67fb
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorers-and-llm-judges
    - LLM Judges and Scorers
    - SALJ
    - Scorers and Judges
    - Scorers and judges
    - Predefined LLM judges
    - Scorers / Judges
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Scorers and LLM Judges
description: Evaluation components (built-in, guidelines-based, custom-prompt, code-based) used to assess GenAI trace quality, supporting both single-turn and multi-turn judging.
tags:
  - mlflow
  - evaluation
  - judges
  - genai
timestamp: "2026-06-19T19:46:24.803Z"
---

# Scorers and LLM Judges

**Scorers and LLM Judges** are the core evaluation components in MLflow 3 used to assess the quality of GenAI application outputs. They power both offline evaluation during development and continuous quality monitoring in production. Scorers can be built-in LLM judges, custom judges with user-defined criteria, or custom code functions.

## Overview

Scorers evaluate traces from GenAI applications by analyzing inputs, outputs, or both, and returning assessment scores. In production monitoring, scorers are registered against an MLflow experiment and scheduled to run automatically on incoming traces. The monitoring service evaluates a configurable sample of traces and attaches the results as feedback to each evaluated trace. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Scorers allow consistent evaluation across development and production — the same scorers used during offline evaluation with `mlflow.genai.evaluate()` can be used in production monitoring by registering them with an experiment. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Types of LLM Judges

### Built-in LLM Judges

MLflow provides several built-in LLM judges that can be used out-of-the-box without additional configuration. These judges use a Databricks-hosted LLM by default to perform GenAI quality assessments. The judge model can be changed to a custom Databricks model serving endpoint by specifying a model argument in the format `databricks:/<databricks-serving-endpoint-name>`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Guidelines LLM Judges

[Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) evaluate inputs and outputs using pass/fail natural language criteria. They allow you to specify simple rules, such as "The response must be in English," and the judge determines whether the output passes each guideline. Guidelines judges can also be configured to use a custom Databricks model serving endpoint for the underlying LLM. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Custom Prompt LLM Judges

For more flexibility than guidelines judges, [LLM Judges with custom prompts](/concepts/llm-judge-customization.md) allow multi-level quality assessment with customizable choice categories. Using `mlflow.genai.make_judge()`, you can define custom instructions, specify feedback value types using `Literal` types, and optionally set a custom judge model. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Custom Scorer Functions

[Code-based Scorers](/concepts/code-based-scorers.md) provide maximum flexibility for evaluation. A custom scorer is defined using the `@scorer` decorator from `mlflow.genai.scorers`. For production monitoring, custom scorers must meet several requirements:

- **Only `@scorer` decorator-based scorers are supported.** Class-based `Scorer` subclasses cannot be registered for production monitoring.
- **Scorers must be defined and registered from a Databricks notebook.** The monitoring service serializes the scorer function code for remote execution, and this serialization requires the notebook environment.
- **Scorers must be self-contained.** All imports must be inline within the function body. The function cannot reference variables, objects, or modules defined outside of it.
- **Type hints that require imports should not be used** in the scorer function signature. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Some packages are available by default without inline import, including `databricks-agents`, `mlflow-skinny`, `openai`, and all packages included in Serverless environment version 2. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Multi-Turn Judges

[Multi-turn Judges](/concepts/multi-turn-judge.md) evaluate entire conversations rather than individual traces. These judges assess quality patterns across multiple interactions, such as user frustration and conversation completeness. The monitoring job automatically groups traces into conversations based on the `mlflow.trace.session` tag. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Multi-turn judges run after a conversation is considered complete — by default, a conversation is complete when no new traces with that session ID are ingested for 5 minutes. This buffer can be configured using the `MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS` environment variable on the monitoring job. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Available multi-turn judges include `ConversationCompleteness` and `UserFrustration`, among others. Multi-turn judges are registered and started the same way as single-turn judges. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Production Monitoring Lifecycle

Setting up a scorer for production monitoring follows a two-step pattern: `.register()` then `.start()`. This pattern applies to all scorer types. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Scorers can be created and managed using either the MLflow Experiment UI or the Python API. From the UI, navigate to the **Judges** tab, click **New LLM judge**, and configure evaluation criteria, sampling rates, and filter strings. Custom code judges cannot be created using the UI but can be defined in a notebook and registered programmatically. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

At any given time, at most 20 scorers can be associated with an experiment for continuous quality monitoring. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Sampling and Filtering

Production monitoring supports configurable sampling rates through the `ScorerSamplingConfig` class, allowing control over the tradeoff between coverage and computational cost. Best practices include:

- For critical scorers such as safety and security checks, use `sample_rate=1.0` for 100% coverage.
- For expensive scorers such as complex LLM judges, use lower sample rates (0.05–0.2).
- For iterative improvement during development, use moderate rates (0.3–0.5). ^[monitor-genai-apps-in-production-databricks-on-aws.md]

The `filter_string` parameter in `ScorerSamplingConfig` controls which traces a scorer evaluates, using the same filter syntax as `mlflow.search_traces()`. Multiple conditions can be combined to target specific trace attributes, status codes, or time ranges. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Viewing Results

After scheduling scorers, allow 15–20 minutes for initial processing. Results can be viewed in the MLflow experiment's **Traces** tab, where assessments are attached to each evaluated trace. Monitoring dashboards track quality trends over time. For multi-turn judges, assessments are attached to the first trace in each session. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — Automated quality assessment of GenAI app traces
- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) — Pass/fail evaluation using natural language criteria
- [Custom Prompt LLM Judges](/concepts/custom-llm-judges.md) — Multi-level assessment with customizable categories
- [Code-based Scorers](/concepts/code-based-scorers.md) — Maximum flexibility for custom evaluation logic
- [Multi-turn Judges](/concepts/multi-turn-judge.md) — Conversation-level evaluation across multiple interactions
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and evaluations
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Required configuration for running scorers in restricted workspaces

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
