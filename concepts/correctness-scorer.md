---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 061ded7ce690d1f9ca1a8dd4adcb52938067d0a64a502362a06489a064e9b20e
  pageDirectory: concepts
  sources:
    - optimize-multiple-prompts-together-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-scorer
    - Answer Correctness Scorer
    - correctness-scorer-in-mlflow-genai
    - CSIMG
  citations:
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: Correctness Scorer
description: An MLflow GenAI evaluation scorer that measures the correctness of model outputs against expected responses, used as a feedback signal during prompt optimization.
tags:
  - evaluation
  - mlflow
  - scoring
timestamp: "2026-06-19T19:52:19.634Z"
---

# Correctness Scorer

The **Correctness Scorer** is a component of the [MLflow](/concepts/mlflow.md) GenAI module, used to evaluate the correctness of model outputs generated during prompt optimization workflows. It is imported from `mlflow.genai.scorers` and acts as an LLM‑as‑a‑judge scorer, relying on a separate large language model to assess whether the generated response is factually or logically correct based on provided expectations. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Usage in Multi-Prompt Optimization

In the [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md) (GenAI Prompt Adaptation) workflow, the Correctness Scorer is passed to the `scorers` parameter of `mlflow.genai.optimize_prompts()`. It takes a `model` argument specifying the judge LLM (for example, `"databricks:/databricks-claude-sonnet-4-5"`). During optimization, the scorer evaluates the output of each candidate prompt against the expected facts defined in the training dataset, providing a correctness score that guides the optimization process. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

The scorer is typically combined with other scorers or used alone to measure how accurately a model produces the desired response. In the provided example, it is used to optimise two chained prompts in a classification pipeline where the correctness of the label is assessed. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Related Concepts

- Prompt Optimization – The broader task of automatically improving prompts.
- [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md) – The optimizer that uses the Correctness Scorer.
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) – A pattern where an LLM evaluates outputs of another model.
- [[Scorers]] – The family of evaluation functions in MLflow GenAI.

## Sources

- optimize-multiple-prompts-together-databricks-on-aws.md

# Citations

1. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
