---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38e5a3fdf5b446cf9f7c2c6b5dd4eb601fa06db901462e8bc18bcd0b12637bf2
  pageDirectory: concepts
  sources:
    - optimize-prompts-using-custom-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-openai-client-integration-with-mlflow
    - DOCIWM
  citations:
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
title: Databricks OpenAI client integration with MLflow
description: Using Databricks-hosted OpenAI-compatible models (via DatabricksOpenAI client) within MLflow prompt optimization workflows for prediction and evaluation.
tags:
  - databricks
  - openai
  - mlflow
  - integration
timestamp: "2026-06-19T23:01:41.793Z"
---

# Databricks OpenAI client integration with [MLflow](/concepts/mlflow.md)

The **Databricks OpenAI client** is a Python library (`databricks_openai`) that provides an OpenAI-compatible interface for models hosted on Databricks. When combined with [MLflow](/concepts/mlflow.md)’s generative AI (GenAI) capabilities, you can manage prompts, run evaluations, and optimize prompt templates using Databricks-hosted models — all within a single [MLflow Experiment](/concepts/mlflow-experiment.md). This integration enables rapid iteration on prompt quality by leveraging MLflow’s [Prompt Registry](/concepts/prompt-registry.md), evaluators, and optimizers. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Setting up the client

The `DatabricksOpenAI` class from the `databricks_openai` package is instantiated without arguments when run in a Databricks notebook; it automatically uses the workspace’s authentication context.

```python
from databricks_openai import DatabricksOpenAI

openai_client = DatabricksOpenAI()
```

^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

Once created, the client can be used to call any model deployed in the Databricks workspace. Common [Model Aliases](/concepts/model-aliases.md) include `"databricks-gpt-oss-20b"` for lightweight open‑source models or `"databricks:/databricks-claude-sonnet-4-5"` for Claude models via the serve endpoint. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Using the client with [MLflow](/concepts/mlflow.md)

MLflow’s GenAI tools allow you to register, version, and load prompts, then evaluate them with custom or built‑in [[scorers|Scorers]]. The typical integration pattern is:

1. **Register a prompt** using `mlflow.genai.register_prompt()`. The prompt template is defined with placeholders (e.g., `{{question}}`) that are filled at inference time. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
2. **Define a prediction function** (`predict_fn`) that uses the `DatabricksOpenAI` client. Inside the function, load the prompt with `mlflow.genai.load_prompt()` and send the formatted prompt to the model via the OpenAI‑compatible [Chat Completions API](/concepts/chat-completions-api.md). ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
3. **Optimize the prompt** by calling `mlflow.genai.optimize_prompts()`, passing the prediction function, training data, and one or more [[scorers|Scorers]] (including [Custom Scorers|custom scorers](/concepts/custom-scorers-mlflow-genai.md) created with `mlflow.genai.judges.make_judge`). The optimizer (e.g., [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)) uses the scorers’ feedback to refine the prompt template. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]
4. **Load the optimized prompt** version and use it in the same prediction function to see improved outputs. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

### Example workflow

The following snippet shows a complete end‑to‑end integration ([Catalog and Schema](/concepts/catalog-and-schema.md) variables must be set to the user’s workspace values):

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from databricks_openai import DatabricksOpenAI

openai_client = DatabricksOpenAI()

# 1. Register initial prompt
prompt = [[mlflow|MLflow]].genai.register_prompt(
    name=f"{catalog}.{schema}.markdown",
    template="Answer this question: {{question}}",
)

# 2. Define prediction function using the Databricks OpenAI client
def predict_fn(question: str) -> str:
    prompt = [[mlflow|MLflow]].genai.load_prompt(f"prompts:/{catalog}.{schema}.markdown/1")
    completion = openai_client.chat.completions.create(
        model="databricks-gpt-oss-20b",
        messages=[{"role": "user", "content": prompt.format(question=question)}],
    )
    return completion.choices[0].message.content

# 3. Provide training data with inputs and expected outputs
dataset = [
    {
        "inputs": {"question": "What is the capital of France?"},
        "expectations": {"expected_response": "## Paris ..."},
    },
    # ... more examples
]

# 4. Optimize the prompt
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

# 5. Use the optimized prompt
optimized_prompt = result.optimized_prompts[0]
print(f"Optimized template: {optimized_prompt.template}")
```

^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

In this example, the `DatabricksOpenAI` client is used both for the initial prediction and (optionally) for the reflection model inside the optimizer. The integration allows the same client to serve multiple models — one for the target task and another (e.g., Claude Sonnet 4‑5) as the judge or reflection model. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Viewing prompts in the [MLflow Experiment](/concepts/mlflow-experiment.md)

After optimization, prompts appear in the [MLflow](/concepts/mlflow.md) experiment’s **Prompt** tab when the experiment type is set to **GenAI apps and agents**. To see the registered prompt, click **select a schema** and enter the same [Catalog and Schema](/concepts/catalog-and-schema.md) used during registration. ^[optimize-prompts-using-custom-scorers-databricks-on-aws.md]

## Related concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – Overall framework for prompt management and evaluation.
- Prompt Optimization – Techniques for automatically improving prompt templates.
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – Creating judges with `make_judge` for use‑case‑specific evaluation.
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) – An optimizer that uses reflection models to refine prompts.
- Databricks OpenAI Client – The client library for calling Databricks‑hosted models via the OpenAI API.

## Sources

- optimize-prompts-using-custom-scorers-databricks-on-aws.md

# Citations

1. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
