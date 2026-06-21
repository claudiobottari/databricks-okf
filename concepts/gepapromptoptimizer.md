---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: befcc292eea330259ebac564fad4cb01c3ec55aca4534881cadda421c18da90a
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gepapromptoptimizer
    - GEPA (GepaPromptOptimizer)
    - GEPA Prompt Optimizer
    - GEPA prompt optimizer
    - GEPA Optimizer
  citations:
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: GepaPromptOptimizer
description: An MLflow prompt optimizer that uses a reflection model to iteratively improve prompt templates based on evaluation scores from custom scorers.
tags:
  - mlflow
  - prompt-optimization
  - gepa
timestamp: "2026-06-19T23:01:20.132Z"
---

# GepaPromptOptimizer

**GepaPromptOptimizer** is an optimization class within the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) framework used for automatically improving prompt templates in LLM-based agent systems. It is part of the MLflow Prompt Engineering toolkit and leverages a separate, strong reflection model to iteratively refine prompts based on training data and evaluation [[scorers|Scorers]]. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## How It Works

GepaPromptOptimizer uses a reflection model — a more capable LLM — that reviews the outputs of the primary model and suggests improvements to the prompt templates themselves. This feedback loop runs across training data examples, allowing the optimizer to iteratively refine prompts to maximize scores from one or more [MLflow Scorers](/concepts/mlflow-scorers.md). The reflection model must be accessible from the Databricks environment (e.g., a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)). ^[optimize-multiple-prompts-together-databricks-on-aws.md, optimize-prompts-using-custom-scorers-databricks-on-aws.md]

A key feature is its ability to optimize **multiple prompts simultaneously** when those prompts are chained together in a system (e.g., one prompt generates a plan, and another uses the plan to produce the final output). It considers the entire chain holistically, adjusting each prompt to improve overall task performance. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Usage

GepaPromptOptimizer is passed as the `optimizer` parameter to `mlflow.genai.optimize_prompts()`. It requires a `reflection_model` parameter pointing to a strong model (e.g., `"databricks:/databricks-claude-sonnet-4-5"`). ^[optimize-multiple-prompts-together-databricks-on-aws.md, optimize-prompts-using-custom-scorers-databricks-on-aws.md]

The typical workflow:

1. **Register prompts** using `mlflow.genai.register_prompt()` to create prompt templates with Jinja-style variable placeholders.
2. **Define a predict function** that loads the registered prompts, formats them with inputs, calls the LLM (or multiple LLMs), and returns results.
3. **Prepare training data** as a list of dictionaries, each containing `inputs`, `outputs` (expected responses), and `expectations` (e.g., classification labels or expected response examples).
4. **Call `mlflow.genai.optimize_prompts()`** with the predict function, training data, a list of prompt URIs, the GepaPromptOptimizer instance (specifying a reflection model), and one or more [MLflow Scorers](/concepts/mlflow-scorers.md) (e.g., built-in Correctness scorer or a custom judge created via `make_judge`). An optional `aggregation` function can map feedback to numerical scores. ^[optimize-multiple-prompts-together-databricks-on-aws.md, optimize-prompts-using-custom-scorers-databricks-on-aws.md]

5. **Access optimized prompts** from the result object’s `optimized_prompts` list, indexed in the same order as the input `prompt_uris`. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Multi‑Prompt Optimization

For agent systems with chained prompts, pass **all** prompt URIs together in the `prompt_uris` parameter. GepaPromptOptimizer optimizes each prompt in context of the others. The optimized prompts are returned in the same order as the input URIs. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Example (Single Prompt with Custom Scorer)

The following example (adapted from the custom [[scorers|Scorers]] notebook) shows optimization of a single prompt using a reflection model and a custom markdown‑quality judge: ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai.optimize import GepaPromptOptimizer
from [[mlflow|MLflow]].genai.judges import make_judge

# Register initial prompt
prompt = [[mlflow|MLflow]].genai.register_prompt(
    name="catalog.schema.markdown",
    template="Answer this question: {{question}}",
)

# Create a custom judge
markdown_judge = make_judge(
    name="markdown_quality",
    instructions=(
        "Evaluate if the answer in {{ outputs }} follows markdown formatting "
        "and accurately answers the question in {{ inputs }} and matches {{ expectations }}. "
        "Rate as high, medium or low quality"
    ),
    model="databricks:/databricks-claude-sonnet-4-5",
)

def feedback_to_score(scores: dict) -> float:
    """Convert categorical feedback to numerical score."""
    ...

# Optimize
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=train_dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(
        reflection_model="databricks:/databricks-claude-sonnet-4-5"
    ),
    scorers=[markdown_judge],
    aggregation=feedback_to_score,
)

optimized_prompt = result.optimized_prompts[0]
```

## Requirements

- The `reflection_model` specified in GepaPromptOptimizer must be accessible from the Databricks environment (e.g., a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
- Training data must include `inputs`, `outputs`, and `expectations` fields.
- At least one scorer (built-in or custom) is required to evaluate prompt quality and drive optimization.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for LLM application development
- Prompt Optimization — General techniques for improving prompt templates
- [MLflow Scorers](/concepts/mlflow-scorers.md) — Evaluation metrics used during optimization
- make_judge()|make_judge — API for creating [Custom Judges](/concepts/custom-judges.md)/[[scorers|Scorers]]
- [MLflow Prompt Registry](/concepts/prompt-registry.md) — Central storage for prompt versions
- [LLM Chaining](/concepts/prompt-chaining.md) — Pattern of connecting multiple LLM calls in sequence
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating multi‑step agent workflows

## Sources

- optimize-multiple-prompts-together-databricks-on-aws.md
- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
2. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
