---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 964fd052f91c34679ebb76d6f56479f44e22771f7cbf978c47ef9a55f37f76e3
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset
    - MED
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: MLflow Evaluation Dataset
description: A curated set of example inputs (labeled or unlabeled) used to systematically test and improve GenAI applications, stored in Unity Catalog with versioning, lineage, sharing, and governance.
tags:
  - mlflow
  - evaluation
  - genai
  - databricks
timestamp: "2026-06-19T17:42:07.006Z"
---

Below is the updated wiki page for **MLflow Evaluation Dataset**, rewritten to use facts solely from the two provided source files (`building-mlflow-evaluation-datasets-databricks-on-aws.md` and `mlflow-evaluation-examples-for-genai-databricks-on-aws.md`). Content that previously relied on the unavailable `evaluation-dataset-reference-databricks-on-aws.md` has been removed or rephrased. Citations follow the required format.

---

---
title: MLflow Evaluation Dataset
summary: Versioned dataset abstraction for managing labeled traces used in evaluation workflows, providing lineage tracking for repeatable assessments.
sources:
  - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  - building-mlflow-evaluation-datasets-databricks-on-aws.md
  - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:54:22.857Z"
updatedAt: "2026-06-19T13:49:49.273Z"
tags:
  - mlflow
  - dataset
  - evaluation
  - lineage
aliases:
  - mlflow-evaluation-dataset
  - MED
confidence: 0.7
provenanceState: merged
inferredParagraphs: 2
---

# MLflow Evaluation Dataset

An **MLflow Evaluation Dataset** is a curated collection of example inputs — either labeled (with known expected outputs) or unlabeled — used for systematically testing and improving [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. These datasets help improve quality by testing fixes against known problematic examples, prevent regressions by maintaining a "golden set" that must always work correctly, compare application versions across different prompts or models, target specific features such as safety or domain knowledge, and validate applications across environments as part of LLMOps.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

MLflow evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance. Each dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md). To create an evaluation dataset, you must have `CREATE TABLE` permission on a Unity Catalog schema.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources

You can build an evaluation dataset from any of the following sources:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **Existing traces** – Real-world scenarios captured by [MLflow Tracing](/concepts/mlflow-tracing.md) from a GenAI application.
- **Manually entered examples** – Directly typed inputs, useful for quick prototyping or targeted testing of specific features.
- **Synthetic data** – Databricks can automatically generate a representative evaluation set from your documents, enabling broad test coverage without manual effort.
- **Existing datasets** – Use datasets already stored in other formats, such as Pandas DataFrames or lists of dictionaries.

## Creating a Dataset

### Using the UI

1. Click **Experiments** in the sidebar, then open your experiment.
2. In the left sidebar, click **Traces**.
3. Select the traces you want to add using the checkboxes.
4. Click **Actions** (the button shows the number of selected traces), then under **Use for evaluation**, select **Add to evaluation dataset**.
5. In the dialog, either create a new dataset by specifying a Unity Catalog schema and name, or add the traces to an existing dataset.
6. Click **Done**.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK

The Python SDK provides a programmatic path:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

```python
import mlflow
from databricks.connect import [[databrickssession|DatabricksSession]]

# Connect to Serverless Spark
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()

# Step 1: Create the evaluation dataset table
uc_schema = "workspace.default"
eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.email_generation_eval"
)

# Step 2: Add records (e.g., from traces)
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    order_by=["attributes.timestamp_ms DESC"],
    max_results=10
)
eval_dataset = eval_dataset.merge_records(traces)
```

You can also add records from domain expert labels, build from scratch, seed with synthetic data, or import an existing dataset.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Selecting Traces for a Dataset

Before adding traces, identify which ones represent important test cases:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **Quantitative selection** – Use the MLflow UI to filter by tags (e.g., `tag.quality_score < 0.7`), or search programmatically with `mlflow.search_traces()` using filters on status, latency, token usage, and other metrics.
- **Qualitative selection** – Review individual traces to identify patterns that require human judgment, such as low-quality outputs, edge cases, or missing context.

Traces can be enriched with expected outputs or quality indicators by collecting human feedback via the domain expert labeling workflow.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Update Existing Datasets

You can add records to an existing dataset both through the UI and the SDK.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **UI**: In the experiment's **Datasets** sidebar, click the dataset name, then **Add record**. Edit the new row and click **Save changes**.
- **SDK**: Use `eval_dataset.merge_records(new_records)` as shown in the creation example.

## Dataset Schema

Each evaluation dataset record contains at least the following fields, which are populated when traces are added or when records are manually created:^[building-mlflow-evaluation-datasets-databricks-on-aws.md, mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

- `inputs` — The input to the GenAI app (e.g., a question or prompt).
- `expectations` — Optional ground-truth data. In examples, the reserved keys `expected_facts`, `expected_response`, and `guidelines` are used, but the SDK does not enforce a strict schema.
- `tags` — Custom metadata.

The dataset can be previewed as a DataFrame using `eval_dataset.to_df()`.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with customer-managed keys (CMK). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record.

If you need relaxed limits, contact your Databricks representative.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Usage Patterns

MLflow evaluation datasets can be used directly with `mlflow.genai.evaluate()` as the `data` argument. This is the recommended pattern for production because it provides versioning, lineage tracking, and Unity Catalog integration.^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import Correctness, Safety
from my_app import agent

dataset = mlflow.genai.datasets.get_dataset("catalog.schema.eval_dataset_name")
results = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=agent,
    scorers=[Correctness(), Safety()]
)
```

Other supported data formats include lists of dictionaries (for quick prototyping), Pandas DataFrames, and Spark DataFrames (for large-scale evaluations or data already in Delta Lake). For production use, Databricks recommends converting these to an MLflow Evaluation Dataset.^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

The `predict_fn` argument can be:^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

- Your app function directly, if parameter names match the evaluation dataset's `inputs` keys.
- A wrapper function that translates between the evaluation dataset format and your app's interface.
- A deployed endpoint, using `mlflow.genai.to_predict_fn("endpoints:/endpoint-name")`.
- A logged MLflow model, wrapped to handle the model's single-parameter interface.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Captures the traces that feed evaluation datasets
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The evaluation framework that consumes these datasets
- [Unity Catalog](/concepts/unity-catalog.md) – Governs dataset storage, versioning, and sharing
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The experiment that an evaluation dataset is attached to
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) – Enriches traces with ground-truth labels for comparison
- [Active MLflow run management](/concepts/active-mlflow-run-management.md) – Best practice for controlling MLflow runs during training

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md
- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
2. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
