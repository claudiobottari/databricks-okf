---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68ed43587f88d81064dc7d695f183525ce783f769678dbe4f73783eeeb9d235a
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - joint-multi-prompt-optimization
    - JMO
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: Joint Multi-Prompt Optimization
description: The ability to simultaneously refine multiple prompts together for best overall performance, enabled by passing multiple prompt_uris to the optimize_prompts API.
tags:
  - optimization
  - multi-prompt
  - mlflow
timestamp: "2026-06-19T19:40:20.386Z"
---

# Joint Multi-Prompt Optimization

**Joint Multi-Prompt Optimization** is an advanced capability of the `mlflow.genai.optimize_prompts()` API that enables the simultaneous refinement of multiple prompts to achieve the best overall performance for a system. Rather than optimizing each prompt in isolation, this approach considers how prompts interact and collectively contribute to the final output quality. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Overview

Joint multi-prompt optimization extends the standard prompt optimization workflow by accepting multiple prompt URIs and optimizing them together. This is particularly useful for complex agent systems where multiple prompts work in concert—for example, a system prompt, a task-specific instruction prompt, and a formatting prompt that all contribute to the final response. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

The API leverages the [GEPA](https://arxiv.org/abs/2507.19457) optimization algorithm through the [`GepaPromptOptimizer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize.[GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)), which was researched and validated by the Databricks AI Research Team. The GEPA algorithm iteratively refines prompts using LLM-driven reflection and automated feedback, enabling systematic and data-driven improvements across multiple prompts simultaneously. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Key Benefits

Joint multi-prompt optimization provides several advantages over optimizing prompts individually:

- **Holistic Optimization**: Considers the combined effect of all prompts, ensuring they work together effectively rather than optimizing each prompt independently without regard for interactions. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Consistency**: Maintains coherence across prompts, as changes to one prompt can be evaluated in the context of how they affect the behavior of other prompts. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Efficiency**: Optimizes all prompts in a single optimization run, reducing the overhead of multiple sequential optimization cycles. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Framework Agnostic**: Works with any agent framework, providing broad compatibility for multi-prompt systems. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Usage

To optimize multiple prompts jointly, pass a list of prompt URIs to the `prompt_uris` parameter: ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

```python
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from mlflow.genai.scorers import Correctness

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt1.uri, prompt2.uri, prompt3.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

The `predict_fn` must use `mlflow.entities.model_registry.PromptVersion.format` for each prompt to ensure the prompts are loaded from the registry and properly formatted with input variables. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Correct Predict Function

```python
# ✅ Correct - loads from registry
def predict_fn(question: str):
    prompt1 = mlflow.genai.load_prompt("prompts:/system-prompt@latest")
    prompt2 = mlflow.genai.load_prompt("prompts:/task-prompt@latest")
    prompt3 = mlflow.genai.load_prompt("prompts:/format-prompt@latest")
    combined = f"{prompt1.format()}\n{prompt2.format(question=question)}\n{prompt3.format()}"
    return llm_call(combined)
```

## Version Control

Optimized prompts are automatically registered in the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md), creating new versions for each prompt that was optimized. This provides full version control and traceability for all prompt changes made during joint optimization. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Requirements

The `optimize_prompts` API requires **MLflow >= 3.5.0**. The feature is currently in Beta. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Optimization](/concepts/mlflow-prompt-optimization-api.md) — The general prompt optimization framework
- [GEPA Optimization Algorithm](/concepts/gepa-optimization-algorithm.md) — The underlying algorithm used for optimization
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) — The MLflow optimizer class implementing GEPA
- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — Version control system for optimized prompts
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation framework for agent systems
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Tracing capability for GenAI applications

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
