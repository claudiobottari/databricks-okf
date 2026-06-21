---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00b8b43d903c4cf815bb3a751d19d27ba64cc147511f1a4ce6b29810157f857c
  pageDirectory: concepts
  sources:
    - optimize-multiple-prompts-together-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-chaining
    - LLM Chaining
  citations:
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: Prompt Chaining
description: An architectural pattern where the output of one prompt (e.g., a plan) is fed as input into a subsequent prompt (e.g., an answer) to decompose complex tasks into sequential steps.
tags:
  - architecture
  - prompt-engineering
  - agent-systems
timestamp: "2026-06-19T19:52:07.118Z"
---

# Prompt Chaining

**Prompt chaining** is a technique in which the output of one prompt is used as input to a subsequent prompt, creating a sequence of language model calls that build on each other. This pattern is common in complex agent systems where a single task is decomposed into multiple steps, each handled by a separate prompt. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Overview

In a typical chain, a first prompt (the “planner”) produces a structured output, such as a plan or reasoning trace. That output is then fed into a second prompt (the “answerer”) that uses it to generate the final response. By splitting the work, different models or different prompt templates can be used for each stage. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

For example, a strong model (e.g., `databricks-gpt-5`) can be used for the planning step that requires reasoning, while a smaller, cost-efficient model (e.g., `databricks-gpt-5-nano`) handles the classification step that follows the plan. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Optimization of Chained Prompts

When multiple prompts are chained, their templates can be **optimized together** using techniques such as GEPA (Genetic Prompt Optimization). The `GepaPromptOptimizer` in MLflow’s GenAI API takes a list of prompt URIs and a `predict_fn` that implements the chain, then jointly optimizes every prompt in the chain to improve a given scoring metric (e.g., `Correctness`). ^[optimize-multiple-prompts-together-databricks-on-aws.md]

```python
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[plan_prompt.uri, answer_prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gemini-2-5-pro"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
optimized_plan = result.optimized_prompts[0]
optimized_answer = result.optimized_prompts[1]
```

After optimization, the new prompt versions can be loaded and used in the same chaining workflow. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Use Cases

- **Multi‑step classification** – A planning prompt generates a reasoning plan; a second prompt classifies the input following that plan. ^[optimize-multiple-prompts-together-databricks-on-aws.md]
- **Retrieval‑augmented generation (RAG)** – One prompt retrieves or summarizes context, another generates the final answer.
- **Agent workflows** – A controller prompt decomposes a user goal into sub‑tasks that are delegated to specialized prompts, whose outputs are then aggregated.

## Related Concepts

- Prompt engineering
- Agent systems
- GEPA (Genetic Prompt Optimization)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- Prompt templates

## Sources

- optimize-multiple-prompts-together-databricks-on-aws.md

# Citations

1. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
