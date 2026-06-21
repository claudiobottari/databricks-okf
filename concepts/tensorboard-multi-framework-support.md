---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4ba6f7ce59abb45448e6609ae5696a470221615d8d50b986022f21da8554de1
  pageDirectory: concepts
  sources:
    - tensorboard-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorboard-multi-framework-support
    - TMS
  citations:
    - file: tensorboard-databricks-on-aws.md
title: TensorBoard Multi-Framework Support
description: TensorBoard supports visualization for TensorFlow, PyTorch, Hugging Face Transformers, and other ML programs through callbacks, functions, and file writers.
tags:
  - tensorflow
  - pytorch
  - visualization
  - machine-learning
timestamp: "2026-06-19T23:07:01.525Z"
---

# TensorBoard Multi-Framework Support

**TensorBoard Multi-Framework Support** refers to TensorBoard's ability to visualize and debug machine learning programs built with various frameworks beyond TensorFlow, including PyTorch, Hugging Face Transformers, and other machine learning libraries. ^[tensorboard-databricks-on-aws.md]

## Overview

TensorBoard is a suite of visualization tools originally developed for TensorFlow, but it now supports multiple machine learning frameworks. On Databricks, TensorBoard can be used to visualize logs from TensorFlow, PyTorch, Hugging Face Transformers, and other machine learning programs. ^[tensorboard-databricks-on-aws.md]

## Supported Frameworks

TensorBoard natively supports logging and visualization from the following frameworks:

- **TensorFlow** — Using TensorBoard callbacks and `tf.summary` file writers (for TensorFlow 2.x) or `tf.compat.v1.summary` (for TensorFlow 1.x). ^[tensorboard-databricks-on-aws.md]
- **PyTorch** — Using the `torch.utils.tensorboard.SummaryWriter` to log metrics, model graphs, and embeddings. ^[tensorboard-databricks-on-aws.md]
- **Hugging Face Transformers** — Via the `Trainer` integration that automatically logs to TensorBoard. ^[tensorboard-databricks-on-aws.md]

## Generating Logs for Other Libraries

For machine learning libraries that do not have native TensorBoard integration, you can generate logs by directly writing to TensorFlow file writers. This approach works for any library by using `tf.summary` (TensorFlow 2.x) or `tf.compat.v1.summary` (TensorFlow 1.x) APIs to create summary data that TensorBoard can read. ^[tensorboard-databricks-on-aws.md]

## Starting [TensorBoard on Databricks](/concepts/tensorboard-on-databricks.md)

Starting TensorBoard in a Databricks notebook follows the same process as on a local Jupyter notebook. You can start it using the `%tensorboard` magic command or by using the TensorBoard notebook module directly. ^[tensorboard-databricks-on-aws.md]

### Using the %tensorboard Magic Command

```python
%load_ext tensorboard
experiment_log_dir = <log-directory>
%tensorboard --logdir $experiment_log_dir
```

The TensorBoard server starts and displays the user interface inline in the notebook, and provides a link to open TensorBoard in a new tab. ^[tensorboard-databricks-on-aws.md]

### Using the Notebook Module

```python
from tensorboard import notebook
notebook.start("--logdir {}".format(experiment_log_dir))
```

^[tensorboard-databricks-on-aws.md]

## Log Directory Best Practices

To ensure reliable storage of experiment logs, Databricks recommends writing logs to cloud storage rather than the ephemeral cluster file system. For each experiment, start TensorBoard in a unique directory. For each run of machine learning code within an experiment, set the TensorBoard callback or file writer to write to a subdirectory of the experiment directory. This approach separates data into runs in the TensorBoard UI. ^[tensorboard-databricks-on-aws.md]

## Known Issues

- The inline TensorBoard UI is inside an iframe, which prevents external links from working unless opened in a new tab. ^[tensorboard-databricks-on-aws.md]
- The `--window_title` option of TensorBoard is overridden on Databricks. ^[tensorboard-databricks-on-aws.md]
- If too many TensorBoard processes run on the cluster, ports in the default range may become unavailable. You can specify a port between 6006 and 6106 using `--port`. ^[tensorboard-databricks-on-aws.md]
- For download links to work, TensorBoard must be opened in a separate tab. ^[tensorboard-databricks-on-aws.md]
- When using TensorBoard 1.15.0, the Projector tab appears blank. A workaround is to replace `#projector` in the URL with `data/plugin/projector/projector_binary.html`. ^[tensorboard-databricks-on-aws.md]
- TensorBoard 2.4.0 has a [known issue](https://github.com/tensorflow/tensorboard/issues/4421) that may affect rendering if upgraded. ^[tensorboard-databricks-on-aws.md]
- When logging to DBFS or Unity Catalog Volumes, you may receive the error "No dashboards are active for the current data set". To resolve this, call `writer.flush()` and `writer.close()` after logging data to ensure all data is properly written. ^[tensorboard-databricks-on-aws.md]

## Related Concepts

- TensorFlow
- PyTorch
- Hugging Face Transformers
- Model Training Visualization
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- Distributed Training Logging

## Sources

- tensorboard-databricks-on-aws.md

# Citations

1. [tensorboard-databricks-on-aws.md](/references/tensorboard-databricks-on-aws-052f8833.md)
