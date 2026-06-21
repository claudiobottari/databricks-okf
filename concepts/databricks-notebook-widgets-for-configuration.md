---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69154385833a6ad210c20fbb20201cb472c1778644018fff009796694366ae11
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-notebook-widgets-for-configuration
    - DNWFC
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: Databricks Notebook Widgets for Configuration
description: Using dbutils.widgets.text to create parameterized notebook inputs for Unity Catalog paths and model names, enabling reusable training workflows.
tags:
  - databricks
  - notebooks
  - configuration
timestamp: "2026-06-19T19:09:17.370Z"
---

# Databricks Notebook Widgets for Configuration

**Databricks Notebook Widgets for Configuration** refers to the practice of using `dbutils.widgets` to create interactive, parameterized inputs within a Databricks notebook. These widgets allow users to specify configuration values — such as catalog names, schema names, or model paths — without modifying the notebook code. The values can be set via the notebook UI or programmatically, and are then retrieved within the notebook using `dbutils.widgets.get()`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Overview

Widgets are created with `dbutils.widgets.text()` which accepts a widget name and a default value. Once created, a text input field appears at the top of the notebook, allowing users to change the value interactively. This pattern is useful for making notebooks reusable across different environments or datasets without hardcoding paths or parameters. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Creating Widgets with `dbutils.widgets.text()`

The following example from an image classification tutorial creates four widgets to store configuration for a [Unity Catalog](/concepts/unity-catalog.md) Volume checkpoint path:

```python
dbutils.widgets.text("uc_catalog", "main")
dbutils.widgets.text("uc_schema", "default")
dbutils.widgets.text("uc_volume", "checkpoints")
dbutils.widgets.text("uc_model_name", "cnn_mnist")
```

Each widget is given a name (the first argument) and a default value (the second argument). The default value serves as a placeholder that is used if the user does not modify the widget. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Updating Widget Values

Users can update widget values in two ways:

- **Via the notebook UI:** The widgets appear as text input fields at the top of the notebook. The user can type a new value directly into each field.
- **By editing the default values in the code:** The default values in the `dbutils.widgets.text()` calls can be changed directly in the cell.

After updating, the notebook retrieves the current values using `dbutils.widgets.get()`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Using Widget Values to Construct Paths

The retrieved widget values are used to construct runtime paths. In the example, the checkpoint directory is built as:

```python
UC_CATALOG = dbutils.widgets.get("uc_catalog")
UC_SCHEMA = dbutils.widgets.get("uc_schema")
UC_VOLUME = dbutils.widgets.get("uc_volume")
UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")
CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"
```

This path is then used throughout the notebook for saving and loading model checkpoints via [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP). ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Benefits

- **Reusability:** The same notebook can be run with different Unity Catalog locations by simply changing the widget values.
- **Separation of code and configuration:** Hardcoded strings are avoided, making the notebook cleaner and more maintainable.
- **User-friendly:** Non-coders can adjust parameters without editing the underlying Python cells.

## Related Concepts

- dbutils – The utility module that provides `widgets`, `fs`, and other notebook helpers.
- [Unity Catalog](/concepts/unity-catalog.md) – The fine-grained governance solution for data and AI assets on Databricks.
- Unity Catalog Volumes – Storage locations for non-tabular data such as model checkpoints.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Often used alongside widgets to log experiment parameters.
- Notebook Parameterization – Broader patterns for making notebooks configurable.

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
