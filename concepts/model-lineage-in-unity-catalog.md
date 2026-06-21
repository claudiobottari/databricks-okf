---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1324de4634c14151a9d9f2017770edd3de5901ecf395ea8a840d53ca8a594102
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-lineage-in-unity-catalog
    - MLIUC
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Lineage in Unity Catalog
description: Tracking the upstream datasets used to train or evaluate a model by logging input tables with mlflow.log_input, visible in Catalog Explorer's lineage graph.
tags:
  - machine-learning
  - data-lineage
  - unity-catalog
timestamp: "2026-06-19T19:24:40.602Z"
---

##Model Lineage in Unity Catalog

**Model Lineage in Unity Catalog** refers to the ability to track the upstream datasets that were used to train and evaluate a registered model. This lineage information is captured automatically when you use MLflow APIs (such as `mlflow.log_input`) or Databricks Feature Store APIs, and is stored as part of the model version metadata in Unity Catalog. It provides visibility into which tables and features contributed to a model’s creation, supporting auditability, reproducibility, and governance. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### How to Track Lineage

Lineage is captured by logging input dataset information during an [MLflow Run](/concepts/mlflow-run.md) that produces a model. The recommended method is to use `mlflow.log_input`, which saves the table reference (e.g., a Unity Catalog table) and a dataset tag (e.g., `"training"`) with the run. When the resulting model is later registered to Unity Catalog, the lineage from that input table to the model version is automatically persisted. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

Support for table-to-model lineage in Unity Catalog is available in MLflow 2.11.0 and above. For models logged using Databricks Feature Store APIs, lineage is also automatically captured; see [Feature Store Lineage](/concepts/databricks-feature-store-lineage.md) for details. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

The following code example demonstrates capturing lineage for a model trained on a Unity Catalog table:

```python
import mlflow
from sklearn.ensemble import RandomForestRegressor

# Write a table to Unity Catalog
iris_df = pd.DataFrame(...)
ps.from_pandas(iris_df).to_table("prod.ml_team.iris", mode="overwrite")

# Load the table, train a model, and log the input
dataset = mlflow.data.load_delta(table_name="prod.ml_team.iris", version="0")
X = dataset.df.toPandas().drop("species", axis=1)
y = dataset.df.toPandas()["species"]

with mlflow.start_run():
    clf = RandomForestRegressor(n_estimators=100)
    clf.fit(X, y)
    mlflow.log_input(dataset, "training")
    mlflow.sklearn.log_model(
        sk_model=clf,
        name="model",
        input_example=X.iloc0,
        registered_model_name="prod.ml_team.iris_classifier",
    )
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Viewing Lineage in Catalog Explorer

Once a model version is registered, its lineage is visible in the Unity Catalog UI. To view it:

1. Open **Catalog** from the sidebar and navigate to the registered model.
2. Click the model version to open its detail page.
3. Select the **Lineage** tab. The sidebar lists components that were logged with the model (e.g., the training dataset).
4. Click **See lineage graph** to open an interactive graph showing the relationships between the model version and its upstream datasets. From the graph you can explore table and column-level lineage.

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Notes and Best Practices

- Lineage is captured per model version, not per registered model. Each version can have different input datasets.
- The lineage information is automatically saved when the model is registered to Unity Catalog; no additional configuration is required beyond logging the inputs during training.
- To share lineage across workspaces, ensure the model is registered in Unity Catalog and the target workspace is attached to the same [Metastore](/concepts/metastore.md).
- For models promoted across environments (e.g., staging to production) using `copy_model_version`, the lineage from the source version is preserved in the copied version.

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores model metadata and lineage.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The framework used to log input datasets during runs.
- mlflow.log_input – API to log a dataset reference and tag for lineage tracking.
- [Feature Store Lineage](/concepts/databricks-feature-store-lineage.md) – Automatic lineage capture for models using Databricks Feature Store.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for viewing lineage graphs.
- [Model Promotion Across Environments](/concepts/model-version-promotion-across-environments.md) – Copying model versions while retaining lineage.

### Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
