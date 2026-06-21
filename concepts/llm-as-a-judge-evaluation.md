---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 814b01399f88f8598008322b35a85341696917b588286c8a1de50d82d9db4222
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-as-a-judge-evaluation
    - LLM Judge Evaluation
    - LLM Judge Evaluations
    - LLM judge evaluation
    - LLM judge evaluations
    - LLM Evaluation
    - LLM evaluation
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: LLM-as-a-Judge Evaluation
description: Using an LLM to automatically evaluate the quality of another LLM's outputs based on criteria like safety, correctness, and custom guidelines.
tags:
  - mlflow
  - evaluation
  - llm-judge
  - genai
timestamp: "2026-06-19T10:44:10.084Z"
---

---

title: LLM-as-a-Judge Evaluation
summary: A paradigm where LLMs are used to evaluate the quality of other AI system outputs, scoring dimensions like relevance, safety, groundedness, and correctness.
sources:
  - get-started-mlflow-3-for-genai-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:34:52.652Z"
updatedAt: "2026-06-18T14:34:52.652Z"
tags:
  - llm-evaluation
  - evaluation-paradigm
  - genai
aliases:
  - llm-as-a-judge-evaluation
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# LLM-as-a-Judge Evaluation

**LLM-as-a-Judge Evaluation** is a technique for assessing the quality of [GenAI](/concepts/mlflow-genai-evaluate-api.md) application outputs using [large language model](/concepts/large-language-models-llms-on-databricks.md)s (LLMs) as evaluators. Instead of relying on human raters or simple metrics, an LLM is instructed to score responses on dimensions such as correctness, safety, relevance, or groundedness. This approach is particularly useful for rapidly evaluating [RAG](/concepts/retrieval-augmented-generation-rag.md) systems, agentic workflows, and other GenAI applications where traditional metrics may be insufficient. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

In LLM-as-a-Judge evaluation, a **judge** is an LLM-based scorer that takes a model’s inputs and outputs and produces a quality score. In MLflow, evaluation uses _scorers_ that can judge common metrics like `Safety` and `Correctness` or fully custom metrics. This approach is central to both evaluation during development and monitoring in production. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Types of Judges (Scorers)

MLflow provides built-in LLM-as-a-judge scorers and supports custom judges through the `Guidelines` scorer or code-based scorers.

### Built-in Scorers

- **`Safety`** – A built-in LLM-as-a-judge scorer that evaluates whether content is free from harmful, offensive, or toxic material. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Custom Scorers (Guidelines)

- **`Guidelines`** – A custom LLM-as-a-judge scorer where the developer defines natural‑language criteria. For example, a guideline can state "Response must be in the same language as the input" to enforce language consistency. Multiple guideline-based judges can be combined in a single evaluation run. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

MLflow also supports [custom code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) for more complex evaluation logic. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Running an Evaluation

The main entry point is [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate). This function runs the target GenAI application on a given dataset, collects outputs, and then applies the specified scorers to judge them. Results are logged to the active MLflow experiment and are viewable in the Experiment UI under the **Evaluations** tab. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=[Safety(), Guidelines(guidelines="Response must be ...", name="...")]
)
```

The same scorers used during development can be reused for production monitoring, enabling continuous quality assessment of deployed GenAI apps. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Human Feedback as a Complement

While LLM-as-a-judge evaluation provides automated scoring, domain experts can confirm quality by reviewing traces and providing feedback. MLflow’s Review App allows sharing traces with experts who can rate responses using custom label schemas (e.g., "Very funny", "Slightly funny", "Not funny"). This human feedback can be used to define guidelines for future evaluation or to fine‑tune judges. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Best Practices

- **Use a representative evaluation dataset** that reflects real‑world inputs the application will encounter.
- **Combine multiple scorers** to cover different quality dimensions (e.g., safety, language consistency, creativity).
- **Iterate based on results** – review evaluation metrics and human feedback to improve prompts, models, or system design.
- **Reuse scorers in production** – the same LLM‑as‑a‑judge scorers used offline can monitor production traffic to detect regressions.

These practices are drawn from the MLflow 3 for GenAI getting‑started tutorial. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The framework that implements LLM‑as‑a‑judge scoring.
- GenAI Agent Evaluation – Broader context for evaluating agentic applications.
- [Custom Judges](/concepts/custom-judges.md) – Creating custom LLM‑based scorers via `make_judge` or code.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous quality monitoring.
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) – Collecting expert annotations to supplement automated judges.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Building and managing datasets for evaluation.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Instrumenting applications to capture traces for debugging and evaluation.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
