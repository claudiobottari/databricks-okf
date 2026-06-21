---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe1c3e8d2388f818942cf039571050e5a6a3f2d55a993111cedddaa5eaf48a04
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
    - mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - llm-judges-and-scorers
    - Scorers and LLM Judges
    - LJAS
    - Judges and Scorers
    - LLM Judge (Scorer)
    - LLM judges (scorers)
    - judges and scorers
    - Judge Scorer
    - LLM-as-Judge Scorers
    - LLM-as-a-Judge Scorers
    - LLM-as-a-judge Scorers
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
    - file: mlflow-3-for-genai-databricks-on-aws.md
title: LLM Judges and Scorers
description: Built-in or custom evaluation components used to assess LLM and agent outputs, reusable across both development testing and production monitoring.
tags:
  - mlflow
  - evaluation
  - llm
timestamp: "2026-06-19T18:41:27.190Z"
---

---
title: LLM Judges and Scorers
summary: Built-in or custom components used to evaluate traces during development and production monitoring, ensuring consistent evaluation across the application lifecycle
sources:
  - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  - mlflow-3-for-genai-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:12:08.826Z"
updatedAt: "2026-06-19T10:22:27.332Z"
tags:
  - mlflow
  - evaluation
  - llm-judges
aliases:
  - llm-judges-and-scorers
  - Scorers and LLM Judges
  - LJAS
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

# LLM Judges and Scorers

**LLM judges** and **scorers** are automated evaluation tools that use large language models to assess the quality of GenAI application outputs. In [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md), they replace manual testing with consistent, repeatable measurements that can be applied during development and in production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md, mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Evaluating AI agents and LLMs is more complex than traditional ML model evaluation because inputs and outputs are often free-form text and many different outputs can be considered correct. Quality depends on factors such as correctness, precision, length, completeness, and appropriateness. LLM judges and scorers provide structured quality metrics by using an LLM to score responses against defined criteria. ^[mlflow-3-for-genai-databricks-on-aws.md]

MLflow provides both **built-in** and **custom** judges and scorers, allowing teams to define various aspects of quality and tailor metrics to their specific use case. These evaluation tools are used throughout the development lifecycle — from offline testing to production monitoring. ^[mlflow-3-for-genai-databricks-on-aws.md]

## How Judges and Scorers Work

A judge is an LLM-based evaluator that takes an agent’s input and output (and optionally a trace) and returns a structured assessment — for example, a categorical label (e.g., `true`/`false`) or a numeric score. Scorers are a broader category that can include judges as well as other metric functions (e.g., latency, token count). Together, they form the evaluation component of [MLflow Tracing](/concepts/mlflow-tracing.md): traces logged during development or production are evaluated using these tools to produce quality metrics. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Built-in vs Custom Judges

MLflow includes a set of built-in judges for common quality dimensions (e.g., relevance, correctness, safety). When the built-in metrics do not capture domain-specific criteria, teams can create [Custom Judges](/concepts/custom-judges.md). Custom judges allow you to define your own evaluation criteria and choose the output type (boolean, numeric, or categorical). They are essential for [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) and for aligning with human feedback. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Usage in Development and Production

The same judges and scorers can be used in both phases:

- **Development**: Use `mlflow.genai.evaluate()` to run offline evaluations on a test dataset. This helps iteratively optimize agent quality before deployment. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Production**: Deploy judges as part of [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md). Every production interaction is traced and evaluated, providing continuous quality tracking. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

Domain experts can provide feedback using the integrated [Review App](/concepts/mlflow-review-app.md), producing evaluation data that can be used to align judges with expert judgement. ^[mlflow-3-for-genai-databricks-on-aws.md, evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Integration with the MLflow Lifecycle

LLM judges and scorers are part of a broader iterative workflow:

1. **Tracing** provides the data foundation (inputs, intermediate steps, outputs).
2. **Evaluation** applies judges and scorers to traces to produce quality metrics.
3. **Human feedback** collected via the Review App is used to improve judges and refine metrics.
4. **Versioning** tracks prompts, apps, and traces, enabling comparison across iterations.

This loop helps teams efficiently improve app quality during development and continue tracking quality in production. ^[mlflow-3-for-genai-databricks-on-aws.md, evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The observability layer that feeds data to judges and scorers
- [Custom Judges](/concepts/custom-judges.md) — Creating domain-specific evaluators
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using judges to compare agent variants
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Applying judges in production
- [Review App for Human Feedback](/concepts/review-app-for-human-feedback.md) — Collecting expert feedback to align judges
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — The broader evaluation framework for AI agents

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md
- mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
2. [mlflow-3-for-genai-databricks-on-aws.md](/references/mlflow-3-for-genai-databricks-on-aws-ac0de02b.md)
