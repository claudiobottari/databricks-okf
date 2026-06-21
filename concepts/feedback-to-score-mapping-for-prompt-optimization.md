---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4a33b414e0cf2333ca2344d8a6ed861bd1aae178d52f9c71745f4f9788bab7c
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-to-score-mapping-for-prompt-optimization
    - FMFPO
    - Feedback-to-score mapping
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: Feedback-to-score mapping for prompt optimization
description: A technique where categorical or qualitative feedback from LLM judges is mapped to numerical scores (e.g., high→1.0, medium→0.5, low→0.0) for use by prompt optimizers.
tags:
  - prompt-optimization
  - scoring
  - evaluation
timestamp: "2026-06-19T23:01:24.071Z"
---

# Feedback-to-Score Mapping for Prompt Optimization

**Feedback-to-score mapping** is a critical component in prompt optimization workflows that transforms qualitative or categorical feedback from [AI judges](/concepts/llm-judges.md) into numerical scores that optimization algorithms can process. This mapping function serves as a bridge between the natural language evaluations produced by judges and the mathematical optimization objectives used by prompt optimizers.

## Overview

When optimizing prompts using [custom scorers](/concepts/custom-scorers-mlflow-genai.md) and judges, the evaluation output is often in a categorical or qualitative format—such as "high," "medium," or "low" quality ratings. However, prompt optimization algorithms require numerical inputs to guide their search for improved prompts. The feedback-to-score mapping function converts these categorical evaluations into floating-point numbers that the optimizer can use as optimization targets. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Implementation

A feedback-to-score mapping function receives the scores dictionary produced by the judge and returns a numerical value. The function handles the conversion logic, including extracting the relevant judge output and mapping categorical values to numeric scores.

```python
def feedback_to_score(scores: dict) -> float:
    """Convert feedback values to numerical scores."""
    feedback_value = scores["markdown_quality"]
    # Map categorical feedback to numerical values
    feedback_mapping = {
        "high": 1.0,
        "medium": 0.5,
        "low": 0.0
    }
    # Handle [[feedback-objects|Feedback objects]] by accessing .value attribute
    if hasattr(feedback_value, 'value'):
        feedback_str = str(feedback_value.value).lower()
    else:
        feedback_str = str(feedback_value).lower()
    return feedback_mapping.get(feedback_str, 0.0)
```

^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Key Components

### Judge Output Handling

The mapping function must handle different types of judge output objects. When the judge returns a [Feedback Object](/concepts/feedback-object.md) (common in [MLflow](/concepts/mlflow.md)'s evaluation framework), the function accesses the `.value` attribute to extract the categorical rating. For plain string outputs, it directly converts the value to lowercase for consistent mapping. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Categorical-to-Numerical Mapping

The core logic uses a dictionary that defines the mapping from categorical labels to numerical scores. This mapping assigns higher numerical values to desirable outcomes and lower values to undesirable ones, creating a clear optimization gradient. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Default Fallback

The function includes a default fallback value (typically 0.0) for unrecognized feedback values. This ensures robustness when the judge returns unexpected output, preventing optimization failures. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Usage in Optimization Workflow

The feedback-to-score function is passed as the `aggregation` parameter when calling `mlflow.genai.optimize_prompts()`. The optimizer uses this function to convert judge evaluations into optimization scores, incorporating both the [Evaluation Feedback](/concepts/evaluation-feedback.md) and the numerical objective into the prompt improvement process. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[markdown_output_judge],
    aggregation=feedback_to_score
)
```

^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Design Considerations

When designing a feedback-to-score mapping, consider the number of scoring categories and their relative weights. A three-tier system (high/medium/low) maps naturally to scores of 1.0, 0.5, and 0.0, but more granular systems are possible. The mapping should create sufficient differentiation between categories to guide the optimizer effectively while maintaining robustness against judge variability. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related Concepts

- Prompt optimization — The overall process of improving prompts through iterative evaluation
- [Custom scorers](/concepts/custom-scorers-mlflow-genai.md) — User-defined judges for specific evaluation criteria
- [AI judges](/concepts/llm-judges.md) — Models that evaluate output quality based on defined criteria
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) — An optimizer that incorporates [Evaluation Feedback](/concepts/evaluation-feedback.md) into prompt refinement
- [MLflow prompt optimization](/concepts/mlflow-prompt-optimization-api.md) — The [MLflow](/concepts/mlflow.md) framework for prompt improvement workflows
- Categorical evaluation metrics — Evaluation approaches that use discrete categories rather than continuous scores

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
