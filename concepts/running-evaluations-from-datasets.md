---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 377f8c9014ed9036e01f7bad7e529e5531feec06bd80524d47e10a246aca2daf
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - running-evaluations-from-datasets
    - REFD
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
    - file: a-b-comparison-of-agent-configurations-databricks-on-aws.md
title: Running Evaluations from Datasets
description: The workflow and UI integration for triggering mlflow.genai.evaluate() directly from a saved evaluation dataset, including auto-generated Python code snippets.
tags:
  - mlflow
  - evaluation
  - workflow
  - genai
timestamp: "2026-06-18T12:13:44.722Z"
---

# Running Evaluations from Datasets

Running evaluations from datasets is a core workflow in MLflow GenAI evaluation, enabling developers to assess their GenAI applications systematically using structured test data. This page covers the key concepts, methods, and best practices for running evaluations using the evaluation dataset abstraction.

## Overview

Evaluation datasets in MLflow provide a structured way to define test data for evaluating GenAI applications. When running an evaluation, you typically use `mlflow.genai.evaluate()` with an evaluation dataset that contains `inputs` (the conversation history or prompts passed to your agent) and optional `expectations` (ground-truth responses that judges can reference). ^[evaluation-dataset-reference-databricks-on-aws.md]

## Core Concepts

### Evaluation Dataset Schema

Evaluation datasets must use a specific schema with the following core fields:

- **inputs**: The primary input data (e.g., conversation history) passed to the GenAI app being evaluated
- **expectations**: Optional ground-truth responses with reserved keys used by built-in LLM judges
- **source**: Tracks dataset record lineage — each record can have only one source type

The `expectations` field has several reserved keys that are used by built-in LLM judges: `guidelines`, `expected_facts`, and `expected_response`. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Source Tracking

The `source` field tracks where a dataset record came from. Each record can have **only one** source type: ^[evaluation-dataset-reference-databricks-on-aws.md]

- **Human source**: Record created manually by a person (specifies `user_name`)
- **Document source**: Record synthesized from a document (specifies `doc_uri` and optional `content`)
- **Trace source**: Record created from a production trace (specifies `trace_id`)

## Running an Evaluation

### Using the MLflow Python SDK

The primary method for running evaluations is `mlflow.genai.evaluate()`, which accepts an evaluation dataset and a set of scorers (judges) to evaluate the outputs: ^[evaluation-dataset-reference-databricks-on-aws.md]

```python
import mlflow

# Load an existing evaluation dataset
dataset = mlflow.genai.datasets.get_dataset("my_evaluation_dataset")

# Run evaluation with judges
result = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=my_agent_function,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

### Using the Evaluation Dataset UI

From the **Datasets** tab in the MLflow experiment page, you can run evaluations directly: ^[evaluation-dataset-reference-databricks-on-aws.md]

1. Open the experiment and click the **Datasets** tab
2. Click **Run an evaluation** to open a dialog with a Python code template
3. The template loads the dataset and runs `mlflow.genai.evaluate()` with a default set of scorers
4. Click the copy icon to copy the code snippet to your clipboard

![Run evaluation button showing the UI for initiating an evaluation from a dataset](https://docs.databricks.com/aws/en/assets/images/run-evaluation-button-d5ed93c9e14b8858fa8abf74dd5319bd.png)

## Working with Evaluation Datasets

### Creating and Managing Datasets

You can create, manage, and use evaluation datasets programmatically using the MLflow evaluation datasets SDK: ^[evaluation-dataset-reference-databricks-on-aws.md]

```python
# Create a new evaluation dataset
mlflow.genai.datasets.create_dataset(
    name="my_dataset",
    catalog="my_catalog",
    schema="my_schema"
)

# Delete a dataset
mlflow.genai.datasets.delete_dataset("my_dataset_id")
```

### Adding Records and Editing

Records can be added to evaluation datasets through the UI or programmatically. Each record contains: ^[evaluation-dataset-reference-databricks-on-aws.md]

- **inputs**: The input data for evaluation (JSON format)
- **expectations**: Optional ground-truth responses (JSON format)
- **source**: Lineage information tracking where the record came from
- **tags**: Optional tags for organizing and filtering records

### Editing Records

From the UI, you can: ^[evaluation-dataset-reference-databricks-on-aws.md]

- Edit **Inputs** and **Expectations** fields directly in the table (these accept JSON and validate your input)
- Add new records
- Delete existing records
- Save all pending edits

## Best Practices for Running Evaluations

### Use a Representative Evaluation Dataset

The evaluation dataset should reflect the range of real-world inputs your GenAI application will encounter in production. A well-constructed dataset helps ensure that evaluation results are meaningful and actionable. ^[evaluation-dataset-reference-databricks-on-aws.md, a-b-comparison-of-agent-configurations-databricks-on-aws.md]

### Consistent Judges Across Configurations

When performing A/B comparisons of different agent configurations, use the same set of judges for both configurations. This ensures that differences in scores reflect changes in agent behavior rather than inconsistencies in the evaluation criteria. ^[a-b-comparison-of-agent-configurations-databricks-on-aws.md]

### Control One Variable at a Time

When comparing configurations, change only the agent behavior being tested (e.g., system prompt, model, or tool set) while keeping all other factors constant. This ensures clear attribution of any performance differences. ^[a-b-comparison-of-agent-configurations-databricks-on-aws.md]

### Document Configurations

Record the exact parameters, prompts, and code versions used for each configuration to ensure reproducibility and enable meaningful comparison of results. ^[a-b-comparison-of-agent-configurations-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) — The structured schema for evaluation datasets
- GenAI Agent Evaluation — The evaluation workflow for GenAI applications
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate agent quality
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing different agent configurations using evaluation datasets
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring

## Sources

- evaluation-dataset-reference-databricks-on-aws.md
- a-b-comparison-of-agent-configurations-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
2. a-b-comparison-of-agent-configurations-databricks-on-aws.md
