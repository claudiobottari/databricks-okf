---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1354f5569cf307bc588b80a9eac0f0d7b8a62fee2cf89d452f21be6113af634
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-optimize_prompts
    - MGO
    - Optimize prompts tutorial
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: MLflow genai optimize_prompts
description: An MLflow function that orchestrates prompt optimization by combining a prediction function, training data, prompt URIs, an optimizer, custom scorers, and an aggregation function.
tags:
  - mlflow
  - prompt-optimization
  - genai
timestamp: "2026-06-19T23:01:42.697Z"
---

Here is the wiki page for "[MLflow](/concepts/mlflow.md) genai optimize_prompts".

---

## [MLflow](/concepts/mlflow.md) genai `optimize_prompts`

**`mlflow.genai.optimize_prompts`** is an API function in the [MLflow](/concepts/mlflow.md) GenAI module that performs automatic prompt optimization using a combination of user-provided [[scorers|Scorers]] and an optimization algorithm. It iteratively refines a prompt template based on feedback from [Custom Judges](/concepts/custom-judges.md) to improve the quality of a model's output for a given task. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Overview

The `optimize_prompts` function takes a prediction function, a dataset of inputs with expected outputs, one or more [Scorers (MLflow GenAI)](/concepts/scorers-mlflow-genai.md), and an optimizer (MLflow GenAI). It uses the optimizer to generate candidate prompts, evaluates them using the [[scorers|Scorers]] against the training data, and returns the best-performing prompt version. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `predict_fn` | callable | A function that accepts inputs from the training data and returns a model output. The function should have parameters matching the keys in the `"inputs"` dictionary of each training example. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |
| `train_data` | list[dict] | A list of examples, each containing `"inputs"` (matching the predict function arguments) and `"expectations"` (containing an `"expected_response"` key with the desired output). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |
| `prompt_uris` | list[str] | A list of URIs pointing to registered prompts. Each prompt is a [Prompt Version (MLflow)](/concepts/prompt-versioning.md) stored in [Unity Catalog](/concepts/unity-catalog.md). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |
| `optimizer` | `GepaPromptOptimizer` | An optimizer instance that defines the optimization strategy. It accepts a `reflection_model` parameter specifying the model used for generating prompt improvements (e.g., `"databricks:/databricks-claude-sonnet-4-5"`). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |
| `scorers` | list[judge] | A list of scorer objects created with `make_judge`. Each scorer provides a numerical or categorical feedback value for each output. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |
| `aggregation` | callable | A function that converts the output of the [[scorers|Scorers]] (a dict mapping scorer names to feedback values) into a single numerical score that the optimizer can use. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md] |

## Return Value

The function returns a result object containing an `optimized_prompts` list. Each element in the list has a `template` attribute containing the optimized prompt text. Typically, the first element is the best-performing prompt. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Example Usage

The following example demonstrates optimizing a prompt to produce Markdown-formatted answers:

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai.judges import make_judge
from [[mlflow|MLflow]].genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from databricks_openai import DatabricksOpenAI

# Create a custom judge
markdown_output_judge = make_judge(
    name="markdown_quality",
    instructions=(
        "Evaluate if the answer in {{ outputs }} follows a markdown formatting "
        "and accurately answers the question in {{ inputs }} and matches "
        "{{ expectations }}. Rate as high, medium or low quality"
    ),
    model="databricks:/databricks-claude-sonnet-4-5",
)

# Define mapping from judge feedback to numerical score
def feedback_to_score(scores: dict) -> float:
    feedback_value = scores["markdown_quality"]
    feedback_mapping = {"high": 1.0, "medium": 0.5, "low": 0.0}
    if hasattr(feedback_value, 'value'):
        feedback_str = str(feedback_value.value).lower()
    else:
        feedback_str = str(feedback_value).lower()
    return feedback_mapping.get(feedback_str, 0.0)

# Register an initial prompt
prompt = [[mlflow|MLflow]].genai.register_prompt(
    name="catalog.schema.markdown",
    template="Answer this question: {{question}}",
)

# Define the prediction function
def predict_fn(question: str) -> str:
    prompt = [[mlflow|MLflow]].genai.load_prompt("prompts:/catalog.schema.markdown/1")
    completion = openai_client.chat.completions.create(
        model="databricks-gpt-oss-20b",
        messages=[{"role": "user", "content": prompt.format(question=question)}],
    )
    return completion.choices[0].message.content

# Prepare training data
dataset = [
    {
        "inputs": {"question": "What is the capital of France?"},
        "expectations": {"expected_response": "## Paris - Capital of France\n..."},
    },
    # ... additional examples
]

# Run optimization
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(
        reflection_model="databricks:/databricks-claude-sonnet-4-5"
    ),
    scorers=[markdown_output_judge],
    aggregation=feedback_to_score,
)

optimized_prompt = result.optimized_prompts[0]
print(f"Optimized template: {optimized_prompt.template}")
```

^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Key Components

### [Custom Judges](/concepts/custom-judges.md) with `make_judge`

The `make_judge` function creates a custom scorer by defining evaluation instructions with template variables `{{ inputs }}`, `{{ outputs }}`, and `{{ expectations }}`. The judge evaluates each candidate prompt's output against these criteria. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Optimization Process

The `GepaPromptOptimizer` uses a reflection model to iteratively improve the prompt. The aggregation function maps the judge's categorical feedback (e.g., "high", "medium", "low") to a numeric score that drives the optimization search. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Training Data Format

Each training example must have an `"inputs"` dictionary whose keys match the parameters of the `predict_fn`, and an `"expectations"` dictionary with an `"expected_response"` key containing the ideal output. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Best Practices

- Register the initial prompt using `mlflow.genai.register_prompt()` before optimization to create a prompt version in [Unity Catalog](/concepts/unity-catalog.md). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
- Ensure the experiment type is set to "GenAI apps and agents" so that optimized prompts appear in the [MLflow Experiment](/concepts/mlflow-experiment.md) UI prompt tab. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
- Use a diverse training dataset with multiple examples to guide the optimizer toward a generalizable prompt. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related Concepts

- MLflow make_judge|MLflow GenAI judges — Creating and using custom evaluators with `make_judge`
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) — The optimization algorithm used to iteratively improve prompts
- [Prompt Version (MLflow)](/concepts/prompt-versioning.md) — Versioned prompt templates stored in [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow experiments](/concepts/mlflow-experiment.md) — Organization unit for tracking optimization runs and results
- Scoring functions (MLflow) — Defining prediction functions for evaluation

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
