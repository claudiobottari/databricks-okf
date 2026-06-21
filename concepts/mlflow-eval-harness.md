---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcb865888ed32f2146068384e42e41478a250846a6e0094a2b4e0924e1192aeb
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-eval-harness
    - MEH
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: MLflow Eval Harness
description: Development-phase evaluation system that uses LLM judges and scorers to assess traces and measure the quality of GenAI applications
tags:
  - mlflow
  - evaluation
  - development
timestamp: "2026-06-19T10:22:28.453Z"
---

# MLflow Eval Harness

The **MLflow Eval Harness** is the evaluation framework within MLflow 3 that enables developers to assess the quality of AI agents, LLMs, RAG systems, and other GenAI applications during development. It provides a structured environment for running evaluations using built-in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) against [[MLflow Trace|MLflow Traces]].

## Overview

Evaluating AI agents and LLMs is more complex than traditional ML model evaluation because these applications involve multiple components, multi-turn conversations, and nuanced quality criteria. The Eval Harness is designed to help developers iteratively optimize the quality of their GenAI applications through systematic testing. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key Features

- **Trace-based evaluation**: The Eval Harness works with [MLflow Tracing](/concepts/mlflow-tracing.md), which captures execution traces during development. Traces can be evaluated using the harness to assess intermediate reasoning steps, tool invocations, and final outputs. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Reusable scorers**: Both built-in and custom LLM judges and scorers used during development can be reused in [Production Monitoring](/concepts/production-monitoring.md), ensuring consistent evaluation throughout the application lifecycle. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Integration with human feedback**: Domain experts can provide feedback using the integrated [Review App](/concepts/mlflow-review-app.md), producing evaluation data for further iteration. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Workflow

The Eval Harness supports an iterative development workflow:

1. **Development phase**: Traces are logged via [MLflow Tracing](/concepts/mlflow-tracing.md) during application development.
2. **Evaluation phase**: Traces are evaluated using the Eval Harness with appropriate judges and scorers.
3. **Human feedback**: Domain experts review outputs and provide feedback through the Review App.
4. **Iteration**: Insights from evaluation and feedback inform further optimization.
5. **Production monitoring**: The same judges and scorers can be deployed for continuous quality monitoring. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

![Overview diagram of MLflow 3 evaluation and monitoring](https://docs.databricks.com/aws/en/assets/images/flowchart-00c729ac75207b58d9c2243583a30d5a.png)

## Integration with MLflow 3

The Eval Harness is a core component of the evaluation and monitoring subsystem in MLflow 3. It is part of the Agent Evaluation SDK, available using the `mlflow[databricks]>=3.1` SDK. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Use Cases

- Testing LLM response quality against defined criteria
- Validating RAG system performance by evaluating retrieved context and generated answers
- Comparing different agent configurations (see [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md))
- Identifying regressions after prompt or model changes

## Related Concepts

- [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) — The evaluation criteria used by the Eval Harness
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The trace logging system that feeds data into the Eval Harness
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Reusing judges from the Eval Harness in production
- [Custom Judges](/concepts/custom-judges.md) — Creating evaluation criteria using `make_judge()`
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader GenAI capabilities in MLflow 3

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
