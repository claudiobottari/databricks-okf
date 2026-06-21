---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfa8ef48fad843d4be5f51a6199fe063e587c13a863a04dee5689efd2cf8e217
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-storage-for-evaluation-datasets
    - UCSFED
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Unity Catalog Storage for Evaluation Datasets
description: Evaluation datasets are stored as tables in Unity Catalog, providing built-in versioning, lineage tracking, cross-team sharing, and governance, requiring CREATE TABLE permissions on a schema.
tags:
  - unity-catalog
  - databricks
  - storage
  - governance
timestamp: "2026-06-19T17:42:11.488Z"
---

Here is the wiki page for "Unity Catalog Storage for Evaluation Datasets", written based solely on the provided source material.

---

## Unity Catalog Storage for Evaluation Datasets

**Unity Catalog Storage for Evaluation Datasets** refers to the mechanism by which [MLflow](/concepts/mlflow.md) evaluation datasets are stored and managed within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. This integration provides built-in versioning, lineage, sharing, and governance for evaluation data used in GenAI application testing. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Overview

An evaluation dataset is a selected set of example inputs used to systematically test and improve a GenAI application. These datasets can be labeled (with known expected outputs) or unlabeled (without ground-truth answers). Storing them in Unity Catalog enables teams to improve quality by testing fixes against known problematic examples, prevent regressions through a "golden set" of examples, compare app versions across different prompts or models, target specific features like safety or domain knowledge, and validate the app across different environments as part of [LLMOps](/concepts/large-language-models-llms-on-databricks.md). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Requirements

To create an evaluation dataset, you must have `CREATE TABLE` permissions on a Unity Catalog schema. The dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md); if you do not already have an experiment, you must create one first. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Data Sources

You can create an evaluation dataset from any of the following sources:

- **Existing traces**: If you have already captured traces from a GenAI application, you can use them to create an evaluation dataset based on real-world scenarios.
- **An existing dataset or directly entered examples**: Useful for quick prototyping or targeted testing of specific features.
- **Synthetic data**: Databricks can automatically generate a representative evaluation set from your documents, allowing quick evaluation with good coverage of test cases.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Creating a Dataset

#### Using the UI

To create a dataset from existing traces using the Databricks UI:

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click on the name of your experiment to open it.
3. In the left sidebar, click **Traces**.
4. Use the checkboxes to select the traces you want to add.
5. Click **Actions** and select **Add to evaluation dataset**.
6. If no evaluation datasets exist, click **Create new dataset**, select the Unity Catalog schema, enter a name, and click **Create Dataset**. Then click **Export** and **Done**.
7. If datasets already exist, click **Export** to the right of the dataset you want to add the traces to.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

#### Using the SDK

To create a dataset programmatically using the MLflow SDK:

```python
import mlflow
import mlflow.genai.datasets
from databricks.connect import [[databrickssession|DatabricksSession]]

# Connect to Serverless Spark
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()

# Create an evaluation dataset
uc_schema = "workspace.default"
evaluation_dataset_table_name = "email_generation_eval"
eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.{evaluation_dataset_table_name}",
)
```

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Adding Records

You can add records to a dataset from several sources:

- **From existing traces**: Use `mlflow.search_traces()` to find traces and then `eval_dataset.merge_records(traces)` to add them.
- **From domain expert labels**: Enrich traces with expected outputs or quality indicators.
- **Build from scratch or import existing**: Directly enter examples or import from other formats.
- **Seed using synthetic data**: Automatically generate representative examples.
- **For conversation simulation**: Create datasets designed for multi-turn evaluation.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Trace Selection Strategies

Before adding traces to a dataset, identify which traces represent important test cases. You can use both quantitative and qualitative analysis:

- **Quantitative**: Filter by tags (e.g., `tag.quality_score < 0.7`), search for specific inputs/outputs, or sort by latency or token usage using the MLflow UI or SDK.
- **Qualitative**: Review individual traces to identify patterns requiring human judgment, such as inputs that led to low-quality outputs, edge case handling, or missing context.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Updating Existing Datasets

You can update an evaluation dataset using either the UI or the SDK:

- **UI**: Open the dataset page from the experiment's **Datasets** tab, click **Add record**, edit the new row, and click **Save changes**.
- **SDK**: Use the `merge_records()` method to add new traces programmatically.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with [customer-managed keys (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record.

If you need any of these limitations relaxed for your use case, contact your Databricks representative. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- GenAI Application Testing
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Synthetic Data Generation

### Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
