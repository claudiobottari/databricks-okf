---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39dccfbd517a15bf9ef7f28fed440b540fe6152e576184c56f9bf45478794b09
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-tagging-system
    - MRTS
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run Tagging System
description: Key-value metadata tags that can be added, edited, and deleted on MLflow runs to enable searching and organizing experiment executions.
tags:
  - mlflow
  - experiment-tracking
  - metadata
timestamp: "2026-06-19T23:25:34.198Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Tagging System

The **MLflow Run Tagging System** provides a mechanism for adding metadata to [MLflow](/concepts/mlflow.md) runs through key-value pair tags. Tags are used to store run metadata and enable run discovery through search and filtering.

## Overview

Tags are key-value pairs that can be created and later used to search for runs. Both keys and values can contain spaces. If a key includes spaces, it must be enclosed in backticks when used in search queries. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Adding Tags to a Run

Tags can be added to a run through the [MLflow Run](/concepts/mlflow-run.md) page in the Databricks UI:

1. In the **Details** table on the run page, click **Add tags** next to **Tags**.
2. In the Add/Edit tags dialog that opens, enter a name for the key in the **Key** field, and click **Add tag**.
3. In the **Value** field, enter the value for the tag.
4. Click the plus sign to save the key-value pair.
5. To add additional tags, repeat steps 2 through 4.
6. When finished, click **Save tags**.

^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Editing and Deleting Tags

To edit or delete existing tags on a run:

1. In the **Details** table on the run page, click the pencil icon next to the existing tags.
2. The Add/Edit tags dialog opens:
   - To delete a tag, click the X on that tag.
   - To edit a tag, select the key from the drop-down menu, edit the value in the **Value** field, and click the plus sign to save the change.
3. When finished, click **Save tags**.

^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Searching Runs by Tag

Runs can be searched based on their tags using query syntax in the search field on the experiment details page. Tags can be searched in the format: `tags.<key>="<value>"`. String values must be enclosed in quotes. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

Examples of tag-based search queries:

- `tags.estimator_name="RandomForestRegressor"`
- `tags.color="blue" AND tags.size=5`

For keys containing spaces, use backtick notation:

```
tags.`my custom tag` = "my value"
```

^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Filtering Runs by State and Creation Time

Beyond tag-based filtering, runs can also be filtered based on their state (Active or Deleted), when the run was created, and what datasets were used. These selections are made using the **Time created**, **State**, or **Datasets** drop-down menus respectively on the experiment details page. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Related Concepts

- [MLflow Runs](/concepts/mlflow-run.md) — The core concept of a single execution of model code that tags are attached to
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that contains runs and where tag-based search is performed
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The broader [MLflow](/concepts/mlflow.md) component for logging and querying run information
- [MLflow Run Details](/concepts/mlflow-run.md) — The interface where tags are viewed, added, edited, and deleted

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
