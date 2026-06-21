---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00236aca9e581f03f20b883401cacbb1ca0579e56740cc41093402ea2d7985db
  pageDirectory: concepts
  sources:
    - custom-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-alignment-with-human-experts
    - JAWHE
  citations:
    - file: custom-judges-databricks-on-aws.md
title: Judge Alignment with Human Experts
description: A process where base LLM judges are refined by incorporating human expert feedback on application outputs to improve judge accuracy and alignment with human judgment.
tags:
  - mlflow
  - human-feedback
  - llm-evaluation
timestamp: "2026-06-19T09:39:34.767Z"
---

# Judge Alignment with Human Experts

**Judge Alignment with Human Experts** refers to the process of refining [Custom LLM Judges](/concepts/custom-llm-judges.md) by calibrating them against human expert feedback to improve their accuracy and reliability for evaluating GenAI applications.

## Overview

Custom LLM judges created with `make_judge()` provide natural language scoring guidelines for GenAI applications. While these judges serve as effective starting points, they can be further improved by aligning them with feedback from human experts. This alignment process helps ensure that automated evaluation criteria more closely match human judgment of quality. ^[custom-judges-databricks-on-aws.md]

## The Alignment Process

The base judge created with `make_judge()` is treated as a starting point. As you gather expert feedback on your application's outputs, you can align the LLM judges to that feedback. This iterative process improves judge accuracy over time, making the automated evaluation more consistent with human quality assessments. ^[custom-judges-databricks-on-aws.md]

## Benefits

- **Improved accuracy**: Aligned judges produce evaluations that better match human expert assessments
- **Iterative refinement**: Judges can be continuously improved as more expert feedback is collected
- **Consistent evaluation**: Reduces variance between automated scoring and human judgment

## When to Align Judges

Alignment with human experts is particularly valuable when:

- Building [Production Monitoring](/concepts/production-monitoring.md) systems for GenAI that need to reflect real user satisfaction
- Conducting [A/B comparisons of agent configurations](/concepts/ab-comparison-of-agent-configurations.md) where accurate quality measurement is critical
- Establishing evaluation baselines for iterative agent development

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers created with `make_judge()`
- make_judge()|Make Judge API — The `make_judge()` function for creating evaluators
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Platform for GenAI evaluation and monitoring
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Expert annotations used for alignment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality assessment in production

## Sources

- custom-judges-databricks-on-aws.md

# Citations

1. [custom-judges-databricks-on-aws.md](/references/custom-judges-databricks-on-aws-7a56fe4f.md)
