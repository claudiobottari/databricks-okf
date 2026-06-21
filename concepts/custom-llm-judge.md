---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c8af4cbd977537ac6d34e1e46dd0472143224f241bc4b776cf2d01effca29ad
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-judge
    - CLJ
    - Build a custom LLM judge
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Custom LLM Judge
description: User-defined evaluators created when built-in LLM judges do not fit a specific use case, offering more control over evaluation criteria and behavior.
tags:
  - llm-evaluation
  - customization
  - mlflow
timestamp: "2026-06-19T09:11:45.847Z"
---

# Custom LLM Judge

**Custom LLM Judge** refers to a user-defined evaluator that uses a large language model (LLM) to score or assess the quality of outputs from a GenAI agent or other generative AI application. Custom judges are created when the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) provided by [MLflow](/concepts/mlflow.md) do not cover the specific quality dimensions or evaluation criteria required for a particular use case. ^[built-in-llm-judges-databricks-on-aws.md]

## Overview

Custom LLM judges allow developers to define their own evaluation criteria beyond the predefined dimensions such as relevance, safety, groundedness, and correctness. They are particularly useful for domain-specific assessments, custom behavioral checks, or evaluating complex agent workflows that involve tool calls and multi-turn conversations. ^[built-in-llm-judges-databricks-on-aws.md]

## When to Use Custom Judges

Use custom LLM judges when:

- The built-in judges do not cover the quality dimensions you need to evaluate.
- You need to assess domain-specific criteria (e.g., medical accuracy, legal compliance, or industry-specific terminology).
- You want to evaluate agent behavior such as tool call correctness, issue resolution, or adherence to custom guidelines.
- You need to analyze execution traces to validate intermediate reasoning steps and tool invocations.

For simpler evaluation needs, start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) or Python [Code-based Scorers](/concepts/code-based-scorers.md). ^[built-in-llm-judges-databricks-on-aws.md]

## Creating a Custom Judge

Custom judges are typically created using the `make_judge()` function from the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) API. The function accepts parameters that define the judge's name, evaluation instructions, feedback value type, and the underlying LLM model to use.

### Basic Structure

```python
from mlflow.genai import make_judge

custom_judge = make_judge(
    name="my_custom_judge",
    instructions="Evaluate the response based on [your criteria here].",
    feedback_value_type=str,  # or bool, int, float
    model="databricks:/databricks-gpt-5-mini",
)
```

### Key Parameters

- **`name`**: A unique identifier for the judge.
- **`instructions`**: Natural language instructions that describe what the judge should evaluate and how to score the output.
- **`feedback_value_type`**: The data type of the judge's output (e.g., `str`, `bool`, `int`, `float`).
- **`model`**: The LLM that powers the judge. This can be a Databricks-hosted model or an external endpoint.

## Types of Custom Judges

### Input/Output Judges

These judges evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). Common criteria include issue resolution status, adherence to expected behaviors, and response quality.

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. To create a trace-based judge, include `{{ trace }}` in the judge's instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

## Using Custom Judges in Evaluation

Custom judges are passed to the `scorers` parameter of `mlflow.genai.evaluate()`:

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_agent,
    scorers=[custom_judge, another_custom_judge],
)
```

## Aligning Judges with Human Feedback

To improve the accuracy of custom judges on your specific domain, you can [align judges with human feedback](/concepts/aligning-judges-with-human-experts.md). This process involves collecting expert annotations on agent outputs and fine-tuning the judge's instructions or underlying model to better reflect human quality assessments. ^[built-in-llm-judges-databricks-on-aws.md]

## Best Practices

- **Start simple**: Begin with built-in judges and add custom judges only when needed.
- **Write clear instructions**: The quality of a custom judge depends heavily on the clarity and specificity of its instructions.
- **Test iteratively**: Validate judge outputs against human judgments to ensure alignment.
- **Use consistent judges**: When comparing agent configurations, apply the same custom judges across all variants to ensure fair comparison.
- **Document judge definitions**: Record the exact instructions, model, and parameters used for each custom judge to ensure reproducibility.

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined evaluators for common quality dimensions
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis
- Human Feedback Alignment — Improving judge accuracy with expert annotations
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using custom judges to compare agent variants
- [Code-based Scorers](/concepts/code-based-scorers.md) — Python-based evaluators as an alternative to LLM judges

## Sources

- built-in-llm-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
