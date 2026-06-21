---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4fda42b18d96f8cbf03436392b6e7d68ed55f89a26a7d76b774b3778025f742
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorers-for-prompt-evaluation
    - CSFPE
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: Custom Scorers for Prompt Evaluation
description: MLflow's support for custom evaluation scorers (e.g., Correctness, Safety) and aggregation functions to guide prompt optimization based on specific quality metrics.
tags:
  - evaluation
  - scorers
  - mlflow
timestamp: "2026-06-19T19:40:08.367Z"
---

# Custom Scorers for Prompt Evaluation

**Custom Scorers for Prompt Evaluation** allow you to define your own metrics when using MLflow's prompt optimization capabilities, enabling evaluation criteria tailored to specific use cases beyond built-in scorers like `Correctness` or `Safety`. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Overview

When optimizing prompts with the `mlflow.genai.optimize_prompts()` API, you can supply custom scorers to guide the optimization process. This flexibility allows you to measure and improve aspects of prompt performance that are unique to your application, such as domain-specific accuracy, style adherence, or business-specific constraints. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Built-in Scorers

MLflow provides built-in scorers for common evaluation dimensions, which serve as examples of how custom scorers can be structured:

- **`Correctness`**: Evaluates the factual accuracy of model outputs. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **`Safety`**: Assesses whether outputs are safe and appropriate. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

These built-in scorers accept a model parameter, such as `model="databricks:/databricks-claude-sonnet-4-5"`, to specify the judge model used for evaluation. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Creating Custom Scorers

Custom scorers implement evaluation logic that measures specific qualities of prompt responses. They can be designed to:

- Evaluate domain-specific knowledge accuracy
- Enforce output format or structure requirements
- Measure adherence to style guidelines
- Assess compliance with business rules
- Combine multiple criteria into a single score

The optimization API accepts custom scorers in the same `scorers` parameter where built-in scorers are provided. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Usage in Prompt Optimization

Custom scorers are passed to the `optimize_prompts()` function alongside the predictor function, training data, and prompt URIs. The optimization algorithm — such as the [GEPA (GepaPromptOptimizer)](/concepts/gepapromptoptimizer.md) algorithm — uses these scorers to iteratively refine prompts based on evaluation results. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

```python
result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[my_custom_scorer, another_custom_scorer],
)
```

## Best Practices

When creating custom scorers for prompt evaluation:

- **Accurate measurement**: Ensure scorers accurately measure what you care about, as the quality of optimization depends on the quality of your evaluation metrics. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Align with output format**: Verify that the form of outputs matches scorer expectations to avoid misleading results. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Combine with built-in scorers**: Use custom scorers alongside built-in options like `Correctness` and `Safety` for comprehensive evaluation. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Troubleshooting

If no improvement is observed during optimization, first check that your custom scorers accurately measure what you care about. Inaccurate or misaligned scorers can prevent the algorithm from finding meaningful improvements. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- MLflow Prompt Optimization (beta) — The overall optimization workflow
- [GEPA (GepaPromptOptimizer)](/concepts/gepapromptoptimizer.md) — The optimization algorithm used for prompt refinement
- [Prompt Version Control](/concepts/prompt-versioning.md) — Managing optimized prompt versions in MLflow Prompt Registry
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Broader evaluation framework for generative AI applications
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Observability for GenAI application execution

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
