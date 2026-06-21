---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1006b86688af9d15a051b78a17ee61560af46b883fe5a241cd4df87cd32e532c
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predict-function-contract-for-optimization
    - PFCFO
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: Predict Function Contract for Optimization
description: The requirement that predict_fn must use mlflow.entities.model_registry.PromptVersion.format() to load prompts from the registry, rather than hardcoding prompt strings, for optimization to work correctly.
tags:
  - mlflow
  - pattern
  - prompt-optimization
timestamp: "2026-06-19T19:40:18.267Z"
---

# Predict Function Contract for Optimization

The **Predict Function Contract for Optimization** defines the interface requirements that a `predict_fn` function must satisfy when used with the `mlflow.genai.optimize_prompts()` API in [MLflow](/concepts/mlflow.md). When MLflow performs prompt optimization, it calls the predict function with input data and expects the function to return predictions that can be evaluated against defined metrics. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Key Requirements

### Prompt Version Resolution

The predict function **must** load prompts from the [MLflow Prompt Registry](/concepts/prompt-registry.md) using `mlflow.entities.model_registry.PromptVersion.format()` rather than hardcoding prompt text. This ensures the optimization algorithm can substitute improved prompts during the optimization process. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

**Correct implementation:**
```python
def predict_fn(question: str):
    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}@latest")
    return llm_call(prompt.format(question=question))
```

**Incorrect implementation:**
```python
def predict_fn(question: str):
    return llm_call(f"Answer: {question}")
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Output Format Consistency

The predict function should return outputs that match the expectations of the scorers being used for evaluation. If the [Correctness Scorer](/concepts/correctness-scorer.md) expects factual answers, the function should return concise, direct responses. If the [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) is used, outputs should avoid harmful or inappropriate content. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Usage in Optimization

The predict function is passed directly to the `mlflow.genai.optimize_prompts()` API call: ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

```python
result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

During optimization, the [GEPA Optimization Algorithm](/concepts/gepa-optimization-algorithm.md) iteratively refines the prompt, and the predict function is called with each candidate prompt to generate outputs that scorers evaluate. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Framework Agnosticism

The contract is framework-agnostic, meaning the predict function can work with any Agent Framework or LLM calling pattern. The function's internal implementation can use frameworks like LangChain, PyFunc, or direct API calls, as long as it follows the prompt resolution and output consistency requirements. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Common Pitfalls

### Hardcoded Prompts

If the predict function hardcodes the prompt text rather than loading it from the registry, optimization will have no effect because the algorithm cannot substitute improved prompts. The optimization process completes, but the prompt remains unchanged. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Output Format Mismatch

If the output format does not match what the scorer expects, optimization may show no improvement. For example, if a [Correctness Scorer](/concepts/correctness-scorer.md) expects single-word answers but the function returns verbose paragraphs, the metric scores may not reflect the underlying prompt quality. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Troubleshooting

| Issue | Probable Cause | Solution |
|-------|----------------|----------|
| No improvement observed | Predict function hardcodes prompt | Use `mlflow.genai.load_prompt` with `prompts:/` URI |
| No improvement observed | Output format mismatch | Verify scorer expectations and adjust predict function output |
| Prompts not being used | Predict function ignores prompt registry | Replace hardcoded text with `prompt.format()` |
| Slow optimization | Large dataset with expensive predict function | Reduce dataset size or use faster model in optimizer |

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- [Prompt Optimization (Beta)](/concepts/mlflow-prompt-optimization-api.md) — The overall feature that uses the predict function contract
- [GEPA Optimization Algorithm](/concepts/gepa-optimization-algorithm.md) — The algorithm that drives iterative prompt refinement
- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The prompt storage system that the predict function must use
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) — User-defined evaluation metrics that the predict function outputs feed into
- [Multi-Prompt Optimization](/concepts/multi-prompt-optimization.md) — Joint optimization where the contract applies to multiple predict functions

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
