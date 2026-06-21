---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4531eb959947c6eb16d3468acefe96cb1bbb0126b402f42641a0e46c72556100
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-object-return-format
    - FORF
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Feedback Object Return Format
description: Guidelines judges return an `mlflow.entities.Feedback` object containing a pass/fail value ('yes'/'no'), detailed rationale, assessment name, and optional error details.
tags:
  - mlflow
  - llm-evaluation
  - api
timestamp: "2026-06-19T14:29:59.838Z"
---

# Feedback Object Return Format

The **Feedback Object Return Format** defines the structure of the `mlflow.entities.Feedback` object returned by [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) (and other LLM judges) when evaluating GenAI outputs. This structured response enables downstream analysis, comparison, and monitoring of evaluation results.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Structure

The `mlflow.entities.Feedback` object contains four fields:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

| Field | Type | Description |
|-------|------|-------------|
| `value` | string | `"yes"` (meets guidelines) or `"no"` (fails guidelines) |
| `rationale` | string | Detailed explanation of why the content passed or failed |
| `name` | string | The assessment name (either provided or auto-generated) |
| `error` | string or null | Error details if evaluation failed; `null` otherwise |

## Usage in Evaluation

When used with `mlflow.genai.evaluate()`, each scorer (including Guidelines judges and custom judges created via make_judge()|Make Judge API) produces one or more Feedback objects per row. These objects are collected in the evaluation results and can be inspected programmatically.

For [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md), the `value` field directly reflects compliance with the specified natural language guidelines. The `rationale` provides interpretable reasoning, which supports debugging and iterative refinement of guidelines.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) — The scorer type that returns this Feedback format.
- [Custom Judge](/concepts/custom-judges.md) — User-defined judges that also return `mlflow.entities.Feedback`.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that aggregates Feedback objects.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing Feedback scores across agent variants.
- Align judges with human feedback — Improving judge output consistency with human annotations.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
