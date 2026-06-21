---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04b9b98889a4fc3f8fd99fd2e480b7cf236653a580a0ea16a92fb85315439e8f
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-prompt-optimization-api
    - MPOA
    - MLflow Prompt Optimization
    - MLflow Prompt Optimization (beta)
    - MLflow prompt optimization
    - Prompt Optimization (Beta)
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: MLflow Prompt Optimization API
description: The `mlflow.genai.optimize_prompts()` API for automatically improving prompts using evaluation metrics and training data, part of MLflow's GenAI capabilities.
tags:
  - mlflow
  - prompt-optimization
  - api
timestamp: "2026-06-19T19:39:20.574Z"
---

# MLflow Prompt Optimization API

The **MLflow Prompt Optimization API** is a feature of [MLflow](/concepts/mlflow.md) (in Beta) that provides a programmatic interface for automatically improving prompts using evaluation metrics and training data. It is accessible via the `mlflow.genai.optimize_prompts()` function and supports the **GEPA** (Generalized Evolutionary Prompt Optimization) algorithm through the `GepaPromptOptimizer`. The API aims to reduce manual prompt engineering effort and ensure consistent prompt quality across agent frameworks. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Key Benefits

The API offers several advantages for prompt development:

- **Automatic Improvement** – Optimizes prompts based on evaluation metrics without manual tuning.
- **Data-Driven Optimization** – Uses training data and custom scorers to guide refinement.
- **Framework Agnostic** – Works with any agent framework, providing broad compatibility.
- **Joint Optimization** – Enables simultaneous refinement of multiple prompts for best overall performance.
- **Flexible Evaluation** – Supports custom scorers and aggregation functions.
- **Version Control** – Automatically registers optimized prompts in the [MLflow Prompt Registry](/concepts/prompt-registry.md).
- **Extensible** – Allows plugging in custom optimization algorithms by extending the base class.

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Version Requirements

The `optimize_prompts` API requires **MLflow >= 3.5.0**. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## GEPA Optimization Algorithm

The API relies on the [GEPA algorithm](/concepts/gepa-optimization-algorithm.md) (Generalized Evolutionary Prompt Optimization), researched and validated by the Databricks AI Research Team. GEPA iteratively refines prompts using LLM-driven reflection and automated feedback, leading to systematic, data-driven improvements. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Example: Simple to Optimized Prompt

The following example illustrates the transformation:

**Before Optimization:**
```
Answer this question: {{question}}
```

**After Optimization:**
```
Answer this question: {{question}}.Focus on providing precise,factual information without additional commentary or explanations.1. **Identify the Subject**: Clearly determine the specific subjectof the question (e.g., geography, history)and provide a concise answer.2. **Clarity and Precision**: Your response should be a single,clear statement that directly addresses the question.Do not add extra details, context, or alternatives.3. **Expected Format**: The expected output should be the exact answerwith minimal words where appropriate.For instance, when asked about capitals, the answer shouldsimply state the name of the capital city,e.g., "Tokyo" for Japan, "Rome" for Italy, and "Paris" for France.4. **Handling Variations**: If the question contains multipleparts or variations, focus on the primary query and answer it directly. Avoid over-complication.5. **Niche Knowledge**: Ensure that the responses are based oncommonly accepted geographic and historical facts,as this type of information is crucial for accuracy in your answers.Adhere strictly to these guidelines to maintain consistencyand quality in your responses.
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Common Use Cases

### Improving Accuracy

The API can optimize prompts to produce more accurate outputs. The following code uses the [Correctness Scorer](/concepts/correctness-scorer.md):

```python
from mlflow.genai.scorers import Correctness

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Optimizing for Safeness

To ensure outputs are safe, use the [Safety scorer](/concepts/safety-scorer-in-mlflow.md):

```python
from mlflow.genai.scorers import Safety

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[Safety(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Advanced Usage

For more advanced scenarios, refer to the following guides:

- [Optimize prompts using custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/custom-scorers)
- [Optimize multiple prompts together](https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/multi-prompt-optimization)

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Optimization takes too long** | Reduce dataset size or reduce the optimizer budget: `optimizer = [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)(reflection_model="databricks:/databricks-gpt-5-mini", max_metric_calls=100)` |
| **No improvement observed** | Ensure scorers accurately measure what matters, increase training data size and diversity, modify optimizer configurations, and verify output form matches expectations. |
| **Prompts not being used** | Ensure `predict_fn` calls `mlflow.entities.model_registry.PromptVersion.format` (e.g., `prompt.format(question=question)`) rather than using a hardcoded prompt. |

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md)
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)
- [Correctness Scorer](/concepts/correctness-scorer.md)
- [Safety scorer](/concepts/safety-scorer-in-mlflow.md)
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Automated Prompt Optimization

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
