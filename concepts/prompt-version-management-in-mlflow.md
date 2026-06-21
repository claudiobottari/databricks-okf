---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 763a8631e33954040a81d9137263d971770a47deae11351ca0f6d086d1a1899d
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-version-management-in-mlflow
    - PVMIM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Prompt Version Management in MLflow
description: Systematic approach to creating, registering, versioning, and comparing different prompt templates for GenAI applications using MLflow's prompt registry.
tags:
  - mlflow
  - prompt-engineering
  - version-control
timestamp: "2026-06-18T12:11:27.389Z"
---

# Prompt Version Management in MLflow

**Prompt Version Management in MLflow** refers to the systematic process of creating, registering, tracking, evaluating, and deploying versions of prompts used in GenAI applications. It is part of the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) and enables teams to iterate on prompt designs with full reproducibility and traceability. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

Prompt version management allows you to store each iteration of a prompt template in Unity Catalog, associate them with commit messages, and retrieve them by version number or alias. This approach supports A/B testing, regression analysis, and production deployment of the best-performing prompts. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Key Concepts

- **Prompt Name**: A fully qualified Unity Catalog identifier (`catalog.schema.prompt_name`) that uniquely identifies the prompt.
- **Version**: An integer assigned by MLflow when a new prompt template is registered. Supports retrieval by version number or alias.
- **Template**: The prompt string with placeholders (e.g., `{{content}}`) that are filled at inference time.
- **Commit Message**: A human-readable note describing the changes introduced in the version.
- **Evaluation Dataset**: A table in Unity Catalog holding input–expectation pairs used to score prompt versions.

## Creating Prompt Versions

Use `mlflow.genai.register_prompt()` to register a new version of a prompt. If the prompt name does not exist, a new prompt is created. Each registration increments the version number. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
prompt_v1 = mlflow.genai.register_prompt(
    name=PROMPT_NAME,
    template="Summarize this text: {{content}}",
    commit_message="v1: Basic summarization prompt"
)
print(f"Created prompt version {prompt_v1.version}")
```

## Loading Prompt Versions

To retrieve a specific version at inference time, use `mlflow.genai.load_prompt()` with a URI of the form `prompts:/<prompt_name>/<version>`. The loaded object supports `.format(**kwargs)` to fill placeholders. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/my_prompt/2"
)
formatted = prompt.format(content="some text")
```

## Evaluating and Comparing Prompt Versions

The core workflow for managing prompt versions involves evaluating multiple versions against the same dataset and comparing their scores. This is done using `mlflow.genai.evaluate()` with consistent [[scorers]] and [Custom Judges](/concepts/custom-judges.md). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 1: Create an Evaluation Dataset

Build a dataset that contains `inputs` (the variables to pass to the prompt) and `expectations` (such as expected facts or required behaviors). Store it in Unity Catalog via `mlflow.genai.datasets.create_dataset()`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
eval_dataset = mlflow.genai.datasets.create_dataset(
    uc_table_name="my_catalog.my_schema.my_eval_dataset"
)
eval_dataset = eval_dataset.merge_records([
    {
        "inputs": {"content": "Text to summarize..."},
        "expectations": {"expected_facts": ["fact1", "fact2"]}
    }
])
```

### Step 2: Define Scorers

Scorers are functions that evaluate generated outputs. Use built-in scorers like `Correctness()` (which checks expected facts) or create custom judges with `make_judge`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness
from mlflow.genai import make_judge
from typing import Literal

sentence_count_judge = make_judge(
    name="sentence_count_compliance",
    instructions="Evaluate if this summary follows the 2-sentence rule.\nSummary: {{ outputs }}",
    feedback_value_type=Literal["correct", "incorrect"]
)
scorers = [Correctness(), sentence_count_judge]
```

### Step 3: Run Evaluation Per Version

For each prompt version, run `mlflow.genai.evaluate()` with the same dataset and scorers. Use `mlflow.start_run()` to log parameters and metrics for each version. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
results = {}
for version in [1, 2]:
    with mlflow.start_run(run_name=f"v{version}_eval"):
        mlflow.log_param("prompt_version", version)
        eval_results = mlflow.genai.evaluate(
            predict_fn=create_summary_function(PROMPT_NAME, version),
            data=eval_dataset,
            scorers=scorers,
        )
        results[f"v{version}"] = eval_results
```

### Step 4: Compare and Select the Best Version

Aggregate scores (e.g., via a weighted composite) to identify the best version. Evaluate both qualitative correctness and quantitative compliance with formatting constraints. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
for version, result in results.items():
    correctness = result.metrics.get('correctness/mean', 0)
    compliance = result.metrics.get('sentence_count_compliance/mean', 0)
    composite = 0.7 * correctness + 0.3 * compliance
    print(f"{version}: composite {composite:.2f}")
```

## Best Practices

- **Start simple**: Begin with a basic prompt and iteratively improve based on evaluation results. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Use consistent datasets**: Evaluate all versions against identical input–expectation pairs to ensure fair comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Track everything**: Log prompt versions, evaluation runs, and deployment decisions in MLflow. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Test edge cases**: Include challenging or adversarial examples in the evaluation dataset. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Monitor production**: Continue evaluating prompts after deployment to detect drift or degradation. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Document changes**: Write meaningful commit messages so that others can understand why each version was created. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Deploy with aliases**: Use aliases (e.g., `"prod"`) to point to the best version, enabling rollback without code changes.

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — Central store for prompt definitions and versions.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Framework for building and evaluating GenAI applications.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline scoring.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers created with `make_judge`.
- [[Scorers]] — Built-in and custom metrics for prompt quality.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer storing prompts and evaluation datasets.
- [Aliases](/concepts/model-aliases.md) — Named references to specific prompt versions for production use.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
