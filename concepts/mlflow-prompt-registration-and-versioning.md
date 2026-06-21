---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7b41a17bc75dff7932b203e96d11346e64dad51ac98d24852034477f241703c
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-prompt-registration-and-versioning
    - versioning and MLflow prompt registration
    - MPRAV
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: MLflow prompt registration and versioning
description: The process of registering prompt templates in MLflow's prompt registry, creating versioned prompts that can be loaded and used in prediction functions.
tags:
  - mlflow
  - prompt-management
  - versioning
timestamp: "2026-06-19T23:01:54.247Z"
---

---
title: "[MLflow](/concepts/mlflow.md) Prompt Registration and Versioning"
summary: "The process of storing, versioning, and managing prompt templates within [MLflow](/concepts/mlflow.md) for use in generative AI applications and agent workflows."
sources:
  - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - [MLflow](/concepts/mlflow.md)
  - prompt-engineering
  - versioning
  - genai
  - llmops
aliases:
  - mlflow-prompt-registration
  - mlflow-prompt-versioning
  - prompt-registration-and-versioning
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# [MLflow](/concepts/mlflow.md) Prompt Registration and Versioning

**MLflow Prompt Registration and Versioning** is a feature within [MLflow](/concepts/mlflow.md)’s Generative AI (GenAI) toolkit that enables the storage, management, and iterative optimization of prompt templates used with large language models (LLMs). Prompt registration and versioning provide a structured way to capture a prompt’s configuration, track its history, and later retrieve it for use in predictions or evaluations.

## Overview

[MLflow](/concepts/mlflow.md) allows users to register a prompt as a versioned entity under a named prompt location (e.g., `prompts:/{catalog}.{schema}.{prompt_name}`). This is done using the `mlflow.genai.register_prompt()` function, which stores the prompt template and returns a prompt object with a `.uri` property that can be used for subsequent loading or optimization. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
prompt = [[mlflow|MLflow]].genai.register_prompt(
    name=prompt_location,
    template="Answer this question: {{question}}",
)
```

After registration, the prompt can be loaded via `mlflow.genai.load_prompt()` using its versioned URI, e.g., `prompts:/{catalog}.{schema}.{prompt_name}/1` for the initial version, or `prompts:/{prompt_location}/10` after optimization. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Versioning and Iteration

Prompt versions are immutable snapshots of a template. Each call to `register_prompt()` creates a new version, and subsequent operations such as `mlflow.genai.optimize_prompts()` produce an `optimized_prompts` list containing new versions of the prompt (e.g., version 10 after optimization). The optimizer uses the [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) with a reflection model to refine the template based on training data and evaluation scores. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
result = [[mlflow|MLflow]].genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[markdown_output_judge],
    aggregation=feedback_to_score,
)
```

## Loading and Using Registered Prompts

A registered prompt can be loaded and used as a template with the `prompt.format()` method, which fills in variables from the template. This is useful when integrating the prompt into a larger prediction pipeline, such as calling a language model API with the formatted prompt. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

```python
completion = openai_client.chat.completions.create(
    model="databricks-gpt-oss-20b",
    messages=[{"role": "user", "content": prompt.format(question=question)}],
)
```

## Integration with [MLflow](/concepts/mlflow.md) Experiments

Registered prompts are associated with an [MLflow Experiment](/concepts/mlflow-experiment.md). When the experiment type is set to **GenAI apps and agents**, the prompt appears in the experiment's **Prompt** tab within the Databricks UI. Users can select a schema ([Catalog and Schema](/concepts/catalog-and-schema.md)) to see their registered prompts. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Retrieval

To load a specific version of a prompt, use its versioned URI. For example, `f"prompts:/{prompt_location}/10"` loads version 10. The `prompt.template` attribute contains the raw template string for inspection. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related Concepts

- Prompt optimization — The process of refining a prompt template using the [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md).
- [Custom scorers](/concepts/custom-scorers-mlflow-genai.md) — [[scorers|Scorers]] created with `mlflow.genai.judges.make_judge()` that provide feedback for optimization.
- [Feedback-to-score mapping](/concepts/feedback-to-score-mapping-for-prompt-optimization.md) — Functions that convert judge feedback (e.g., "high", "medium", "low") into numerical scores for the optimizer.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — A policy that controls the budget for serverless workloads, such as [[scorers|Scorers]] and evaluators, when working with [MLflow](/concepts/mlflow.md) experiments.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational container for runs, prompts, and evaluations.
- GenAI apps and agents — An experiment type that enables prompt management and versioning.

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
