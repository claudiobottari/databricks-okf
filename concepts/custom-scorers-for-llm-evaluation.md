---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29c994b5b1db03501f25e10b54edb09447e15f1e490515f6247645740f8c62b7
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorers-for-llm-evaluation
    - CSFLE
    - Custom Scorers for Evaluation
    - Custom Scorers Documentation
    - Use custom scorer functions
    - custom scorer functions
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: Custom scorers for LLM evaluation
description: User-defined evaluation functions that go beyond built-in scorers to assess LLM outputs on criteria specific to a given use case, such as markdown formatting quality.
tags:
  - llm-evaluation
  - scorers
  - custom-evaluation
timestamp: "2026-06-19T23:02:02.296Z"
---

# Custom [[scorers|Scorers]] for LLM Evaluation

**Custom [[scorers|Scorers]] for LLM evaluation** are user-defined judges that extend [MLflow](/concepts/mlflow.md)'s built-in evaluation capabilities to assess LLM outputs according to specific, application-tailored criteria. They enable teams to evaluate and optimize prompts against requirements that general-purpose [[scorers|Scorers]] cannot adequately measure. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Overview

Built-in [[scorers|Scorers]] and judges often do not fit every use case. Custom [[scorers|Scorers]] address this gap by allowing practitioners to define evaluation criteria specific to their domain, output format, or quality standards. This ensures that evaluations are accurate and relevant for the optimization tasks at hand. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Creating a Custom Scorer with `make_judge`

[MLflow](/concepts/mlflow.md) provides the `make_judge` function from `mlflow.genai.judges` to create [Custom Judges](/concepts/custom-judges.md) tailored to specific use cases. The function accepts the following parameters: ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

- **`name`** — A human-readable identifier for the judge (e.g., `"markdown_quality"`).
- **`instructions`** — Natural language instructions that describe what the judge should evaluate. These instructions can reference `{{ inputs }}`, `{{ outputs }}`, and `{{ expectations }}` from the evaluation data.
- **`model`** — The LLM model that acts as the judge, specified as a Databricks model reference (e.g., `"databricks:/databricks-claude-sonnet-4-5"`).

Example:
```python
from [[mlflow|MLflow]].genai.judges import make_judge

markdown_output_judge = make_judge(
    name="markdown_quality",
    instructions=(
        "Evaluate if the answer in {{ outputs }} follows a markdown formatting "
        "and accurately answers the question in {{ inputs }} and matches {{ expectations }}. "
        "Rate as high, medium or low quality"
    ),
    model="databricks:/databricks-claude-sonnet-4-5"
)
```
^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Mapping Judge Feedback to Numerical Scores

Optimizers require numerical scores to perform prompt optimization. Since [Custom Judges](/concepts/custom-judges.md) return categorical or qualitative feedback, a mapping function must convert the judge's output into a numerical value. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

The mapping function receives a `scores` dictionary where keys correspond to the judge name and values contain the judge's feedback. Example:
```python
def feedback_to_score(scores: dict) -> float:
    feedback_value = scores["markdown_quality"]
    feedback_mapping = {
        "high": 1.0,
        "medium": 0.5,
        "low": 0.0
    }
    if hasattr(feedback_value, 'value'):
        feedback_str = str(feedback_value.value).lower()
    else:
        feedback_str = str(feedback_value).lower()
    return feedback_mapping.get(feedback_str, 0.0)
```
^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Using Custom [[scorers|Scorers]] with Prompt Optimization

Custom [[scorers|Scorers]] are integrated into the prompt optimization workflow via the `scorers` parameter of `mlflow.genai.optimize_prompts`. The `aggregation` parameter specifies the function that converts judge feedback into numerical scores. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Training Data Format

The training dataset for optimization must include `inputs` and `expectations` keys. The `inputs` schema should match the argument names of the prediction function, and `expectations` should contain the desired output format or content. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

Example dataset entry:
```python
{
    "inputs": {"question": "What is the capital of France?"},
    "expectations": {"expected_response": "## Paris - Capital of France..."}
}
```
^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Optimization Execution

The optimization process uses a [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) (or similar optimizer) and runs the custom scorer against each prompt candidate to determine the best performing prompt template. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[markdown_output_judge],
    aggregation=feedback_to_score
)

optimized_prompt = result.optimized_prompts[0]
```
^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Workflow Summary

1. **Define the judge** using `make_judge` with instructions and a model reference.
2. **Implement the feedback-to-score mapping** function to convert qualitative judgments to numerical scores.
3. **Prepare training data** with `inputs` and `expectations` matching the prediction function signature and desired output format.
4. **Run the optimizer** with `mlflow.genai.optimize_prompts`, passing the custom scorer(s) and aggregation function.
5. **Load and test** the optimized prompt template to verify improved performance. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The framework for evaluating LLM outputs using built-in and [Custom Judges](/concepts/custom-judges.md).
- Prompt Optimization — The process of iteratively improving prompt templates using feedback from [[scorers|Scorers]].
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) — An optimizer that uses a reflection model to propose prompt improvements.
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The paradigm of using an LLM to evaluate outputs from another LLM.
- [Prompt Versioning](/concepts/prompt-versioning.md) — Managing different versions of prompt templates through registered prompts.

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
