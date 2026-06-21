---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb0909185221caaa55e4a2a128ea750e0c31aca5b469d1377e8e6dc935694918
  pageDirectory: concepts
  sources:
    - optimize-multiple-prompts-together-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-prompt-optimization
    - Prompt Optimization
    - Prompt optimization
    - prompt optimization
  citations:
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: Multi-Prompt Optimization
description: The technique of jointly optimizing multiple chained prompts in an agent system using GEPA (GepaPromptOptimizer) to improve overall pipeline performance.
tags:
  - prompt-engineering
  - optimization
  - agent-systems
  - mlflow
timestamp: "2026-06-19T19:51:58.096Z"
---

# Multi-Prompt Optimization

**Multi-Prompt Optimization** is a technique in which several linked prompts are provided together to an optimization system, such as GEPA (GEPA Prompt Optimizer), so that the system can consider and improve each prompt in the context of the entire chain. This approach is particularly useful in complex agent systems where multiple prompts are chained together to accomplish a task. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Overview

In many real-world applications, a single prompt is not sufficient: an agent may first need to plan, then execute a classification, or perform other sequential steps. These steps are often implemented as separate prompts that pass information from one to the next. Multi-Prompt Optimization allows a developer to register all such prompts and optimize them jointly, rather than tuning each prompt in isolation. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Workflow in MLflow

The optimization is performed using the `mlflow.genai.optimize_prompts()` function, which accepts:

- `predict_fn` – a Python function that uses the prompts and calls an LLM.
- `train_data` – a dataset of input/output examples, each containing `inputs`, `outputs`, and `expectations`.
- `prompt_uris` – a list of prompt URIs (e.g., versions of registered prompts).
- `optimizer` – an instance of `GepaPromptOptimizer` (with a `reflection_model`).
- `scorers` – a list of evaluation scorers, such as `Correctness`.

The optimizer then generates improved versions of each prompt. The results are accessible via `result.optimized_prompts`, which contains one optimized prompt per input URI. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Example: Plan-and-Answer Pipeline

A common pattern demonstrated in the source material is a two‑step pipeline:

1. **Plan prompt** – “Make a plan to classify {{query}}.”
2. **Answer prompt** – “classify {{query}} following the plan: {{plan}}.”

These prompts are registered with `mlflow.genai.register_prompt()` and used inside `predict_fn`. The plan prompt is sent to a stronger model (e.g., `databricks-gpt-5`), while the answer prompt is sent to a cost‑efficient model (e.g., `databricks-gpt-5-nano`). ^[optimize-multiple-prompts-together-databricks-on-aws.md]

After optimization, the developer loads the new prompt versions (e.g., version 4) and tests the pipeline again to see how the improved prompts affect the model’s output. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Benefits

- **Contextual tuning**: The optimizer can adjust each prompt based on how they interact in the chain, leading to better overall accuracy.
- **Reduced manual effort**: Instead of hand‑tuning every step, the developer provides examples and lets the optimizer search for improvements.
- **Supports heterogeneous models**: Different prompts can be assigned to different models (e.g., a strong planner and a lightweight classifier), and the optimizer can account for their different capabilities.

## Requirements

- MLflow version that supports `mlflow.genai.optimize_prompts` and `GepaPromptOptimizer`.
- A Databricks workspace with access to the necessary foundation models for reflection and scoring.
- Prompts must be registered via `mlflow.genai.register_prompt()` so they have a persistent URI.

## Related Concepts

- [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md) – The optimization engine used for multi‑prompt tuning.
- [MLflow](/concepts/mlflow.md) – The platform that provides prompt management and optimization APIs.
- Prompt Engineering – The broader practice of designing effective prompts.
- Agent Systems – Complex systems that often chain multiple prompts.
- [LLM Chaining](/concepts/prompt-chaining.md) – The sequential use of prompts where the output of one step becomes the input of another.
- [Prompt Registration](/concepts/prompt-registry.md) – The process of saving a prompt template with a name and version.

## Sources

- optimize-multiple-prompts-together-databricks-on-aws.md

# Citations

1. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
