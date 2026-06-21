---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8aaae4eac45f99e10db5c4488148bcb2e80af54e54b81c6c0c0ce9f9a743816b
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - run-evaluation-from-dataset
    - REFD
    - running-evaluations-from-datasets
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Run Evaluation From Dataset
description: The workflow to trigger mlflow.genai.evaluate() from a stored evaluation dataset, generating a Python code snippet from the UI.
tags:
  - mlflow
  - evaluation
  - workflow
timestamp: "2026-06-19T18:43:18.172Z"
---

# Run Evaluation From Dataset

**Run Evaluation From Dataset** refers to the workflow in [MLflow](/concepts/mlflow.md) where a pre‑defined evaluation dataset is used as the input for a GenAI app evaluation. This can be done either through the MLflow experiment UI or programmatically using the `mlflow.genai.evaluate()` function.

---

## Overview

Evaluation datasets in MLflow define the structured test data for evaluating a GenAI application. Each dataset contains `inputs`, optional ground‑truth `expectations`, and lineage fields such as source and tags. Running an evaluation from a dataset means passing this structured data to an evaluator (typically `mlflow.genai.evaluate()`) along with a model or application to produce scores and metrics. ^[evaluation-dataset-reference-databricks-on-aws.md]

---

## Run an Evaluation from the UI

The **Datasets** tab on the MLflow experiment page provides a visual way to start an evaluation using any stored dataset. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Steps

1. Open the MLflow experiment and click the **Datasets** tab.
2. In the left pane, select the evaluation dataset you want to use.
3. Click the **Run an evaluation** button at the top of the right pane.
4. A dialog appears containing a Python code snippet that loads the selected dataset and calls `mlflow.genai.evaluate()` with a default set of scorers.
5. Click the copy icon to copy the snippet to your clipboard, then paste and run it in a notebook or job.

![Run evaluation button](https://docs.databricks.com/aws/en/assets/images/run-evaluation-button-d5ed93c9e14b8858fa8abf74dd5319bd.png)

^[evaluation-dataset-reference-databricks-on-aws.md]

The generated code template automatically includes:
- A call to load the dataset by its ID.
- A call to `mlflow.genai.evaluate()` that references that dataset.
- A default set of scorers provided by MLflow GenAI.

---

## Run an Evaluation Programmatically

You can also run an evaluation from a dataset without using the UI. The SDK provides the `EvaluationDataset` class and methods to create and retrieve datasets, which can then be passed to `mlflow.genai.evaluate()`.

A typical programmatic workflow:

```python
import mlflow

# Retrieve an existing dataset
dataset = mlflow.genai.datasets.get_dataset("my_dataset_id")

# Run evaluation
mlflow.genai.evaluate(
    model=your_model,
    dataset=dataset,            # Use the EvaluationDataset object
    model_type="databricks-agents",  # or other supported type
    # ... additional scorers, params
)
```

For the full API reference, see [`mlflow.genai.datasets`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#module-mlflow.genai.datasets) and [`EvaluationDataset`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.datasets.EvaluationDataset). ^[evaluation-dataset-reference-databricks-on-aws.md]

---

## Related Concepts

- [EvaluationDataset](/concepts/evaluation-dataset.md) – The class representing a stored evaluation dataset.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs and evaluation datasets.
- [LLM-as-a-judge Scorers](/concepts/llm-judges-and-scorers.md) – Built‑in judges that use the `expectations` field of a dataset.
- Evaluate GenAI Apps During Development – General guide and examples for running evaluations.
- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) – Required field structure for inputs and expectations.

---

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
