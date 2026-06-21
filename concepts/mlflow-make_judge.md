---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c93fe0d883ba0d821c7bdba6409dfb5d610486a37aa3ff074ab19cebd2ec66c
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-make_judge
    - MLflow GenAI Judges
    - MLflow GenAI judges
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: MLflow make_judge
description: A function in MLflow's GenAI module that allows users to create custom judges/scorers for evaluating LLM outputs based on custom instructions and criteria.
tags:
  - mlflow
  - llm-evaluation
  - judges
timestamp: "2026-06-19T23:01:21.842Z"
---

# [MLflow](/concepts/mlflow.md) `make_judge`

**`make_judge`** is a utility in the `mlflow.genai.judges` module that allows you to create [Custom Judges](/concepts/custom-judges.md) (also called [[scorers|Scorers]]) tailored to specific evaluation criteria. It is used when built-in [[scorers|Scorers]] and judges do not fit a particular use case, enabling more accurate evaluation of model outputs for prompt optimization. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Overview

[MLflow](/concepts/mlflow.md)'s `make_judge` is designed to let you define your own scoring logic using a natural language instruction. The judge takes a model (typically an LLM endpoint) and evaluates generated outputs against criteria you specify. The resulting judge can be passed directly as a scorer in optimization workflows, such as [MLflow Prompt Optimization](/concepts/mlflow-prompt-optimization-api.md) and [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Usage

The `make_judge` function accepts three primary parameters: `name`, `instructions`, and `model`.

```python
from [[mlflow|MLflow]].genai.judges import make_judge

my_judge = make_judge(
    name="markdown_quality",
    instructions=(
        "Evaluate if the answer in {{ outputs }} follows a markdown formatting "
        "and accurately answers the question in {{ inputs }} and matches {{ expectations }}. "
        "Rate as high, medium or low quality"
    ),
    model="databricks:/databricks-claude-sonnet-4-5"
)
```

- **`name`**: A string identifier for the judge (e.g., `"markdown_quality"`). The name is later used as a key in the feedback dictionary returned during evaluation. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
- **`instructions`**: A template string that describes the evaluation criteria. It may include placeholders such as `{{ inputs }}` (the input to the model), `{{ outputs }}` (the generated response), and `{{ expectations }}` (the expected answer). The judge uses these placeholders to incorporate evaluation context at runtime. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
- **`model`**: The LLM endpoint used to perform the evaluation. The value should be the Databricks serving endpoint URI (e.g., `"databricks:/databricks-claude-sonnet-4-5"`). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Mapping Feedback to Numerical Scores

The feedback returned by a `make_judge` judge is typically a categorical string (e.g., `"high"`, `"medium"`, `"low"`). Optimizers such as [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) require numerical scores for optimization. Therefore, a mapping function must be provided to convert the judge's feedback into a floating-point number. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
def feedback_to_score(scores: dict) -> float:
    feedback_value = scores["markdown_quality"]
    feedback_mapping = {"high": 1.0, "medium": 0.5, "low": 0.0}
    if hasattr(feedback_value, 'value'):
        feedback_str = str(feedback_value.value).lower()
    else:
        feedback_str = str(feedback_value).lower()
    return feedback_mapping.get(feedback_str, 0.0)
```

- The `scores` dictionary contains keys matching the `name` of each judge. In the example, `"markdown_quality"` maps to the judge's feedback.
- The function handles both plain strings and `Feedback` objects (by accessing the `.value` attribute).
- A dictionary defines the mapping from categorical labels to numeric values; unrecognized values default to `0.0`. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Integration with Prompt Optimization

The custom judge is used as a scorer when calling `mlflow.genai.optimize_prompts()`. The optimizer iteratively refines the prompt template based on the judge's feedback, aiming to maximize the aggregated score. The `aggregation` parameter receives the `feedback_to_score` function to turn judge evaluations into a single numeric value for each sample. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[my_judge],
    aggregation=feedback_to_score
)
```

- The `scorers` argument accepts a list of judge objects created with `make_judge`.
- The `aggregation` function is called on the dictionary returned by the [[scorers|Scorers]] for each evaluation sample.
- The optimizer (e.g., [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)) uses the aggregated scores as the objective to minimize or maximize. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Optimization](/concepts/mlflow-prompt-optimization-api.md) – The overall workflow of refining prompt templates using [Evaluation Feedback](/concepts/evaluation-feedback.md).
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) – An optimizer that uses a reflection model to iteratively improve prompts.
- Scorers in MLflow – Overview of built-in and custom functions for evaluating generative AI outputs.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The environment in which optimization runs are tracked.

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
