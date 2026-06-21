---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a68875e642bbb1f04bedf23350affecb67fe3ae21ab78db247bc74587ca6310
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - golden-set
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Golden Set
description: A curated collection of test examples that must always pass correctly, used to prevent regressions when iterating on prompts, models, or application logic.
tags:
  - evaluation
  - testing
  - quality-assurance
timestamp: "2026-06-19T14:10:23.784Z"
---

# Golden Set

A **golden set** is a curated subset of evaluation examples that must always work correctly for a GenAI application. Golden sets serve as a quality gate: any change to the system prompt, model, agent logic, or tools must pass the golden set before being promoted to production. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Purpose

The primary purpose of a golden set is to **prevent regressions**. As an application evolves, the golden set provides a repeatable benchmark that catches unintended degradations. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md] Beyond regression prevention, golden sets also help:

- Improve quality by testing fixes against production-proven problem cases.
- Compare app versions (different prompts, models, or logic) against a stable reference.
- Validate the application across different environments as part of [LLMOps](/concepts/large-language-models-llms-on-databricks.md).

## Relationship to Evaluation Datasets

In [MLflow](/concepts/mlflow.md), evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md) and can be versioned, shared, and governed like any other data asset. A golden set is usually implemented as a dedicated evaluation dataset (or a tagged subset of a broader dataset) that is treated as a non-negotiable quality gate. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

The dataset can be created from:

- **Production traces** — Real interactions that the application must handle correctly.
- **Domain expert labels** — Human-annotated examples representing critical edge cases.
- **Synthetic data** — Programmatically generated inputs that cover high-risk scenarios.

Once defined, the golden set is included in every evaluation pipeline (e.g., via `mlflow.genai.evaluate()`). If the application's outputs fail the golden set's quality criteria, the change is blocked until fixed.

## Data Sources

Golden sets are commonly built from historical application interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md). You can search for traces by success, failure, production environment tags, or other properties using `search_traces()`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

**Quantitative trace selection** involves filtering traces by measurable characteristics such as quality scores, latency, or token usage. **Qualitative trace selection** involves reviewing individual traces to identify patterns requiring human judgment, such as edge cases, missing context, or faulty reasoning. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Best Practices

- **Keep the golden set small and focused.** A few dozen to a few hundred carefully chosen examples are more maintainable than thousands.
- **Review and update periodically.** As the application's domain or acceptance criteria evolve, retire obsolete examples and add new ones. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Make every golden-set failure actionable.** Each example should map to a clear quality expectation so the team knows what broke.
- **Integrate with CI/CD.** Run the golden set automatically before every deployment. Failures should halt the pipeline.

## Updating Golden Sets

You can update golden sets using either the Databricks UI or the [MLflow SDK](/concepts/mlflow.md). From the UI, open the dataset page, click **Add record**, edit the new row to enter inputs and expectations, then click **Save changes**. Using the SDK, you can programmatically search for traces and merge them into the dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The broader category of MLflow-managed test inputs.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Side-by-side evaluation where a golden set can serve as the reference.
- [Multi-turn Evaluation](/concepts/multi-turn-conversation-evaluation.md) — Evaluating conversational agents where golden sets may include multi-turn interactions.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used to automatically evaluate golden-set outputs.
- Align Judges with Human Feedback — Process of tuning judges to match expert quality assessments.
- Regression Testing — The general software engineering practice that golden sets implement.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
