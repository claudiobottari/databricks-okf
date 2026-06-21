---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 478b5184423cf602ef529d251969e7b0683c5f43e1551d4bffd259acbc4410d4
  pageDirectory: concepts
  sources:
    - tensorboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorboard-log-directory-best-practices
    - TLDBP
  citations:
    - file: tensorboard-databricks-on-aws.md
title: TensorBoard Log Directory Best Practices
description: Recommendations for writing TensorBoard logs to cloud storage instead of ephemeral cluster storage, and organizing logs by experiment and run subdirectories.
tags:
  - databricks
  - logging
  - best-practices
timestamp: "2026-06-19T23:06:41.473Z"
---

# TensorBoard Log Directory Best Practices

**TensorBoard Log Directory Best Practices** refers to the recommended patterns for organizing and storing log directories used by [TensorBoard](/concepts/tensorboard-on-databricks.md) for visualizing machine learning training runs.

## Core Principles

### Use Unique Directories per Experiment

For each experiment, start TensorBoard in a unique directory. This ensures that the TensorBoard UI shows separate, organized data for each experiment, preventing confusion between different training sessions. ^[tensorboard-databricks-on-aws.md]

### Use Subdirectories for Each Run

For each run of your machine learning code within an experiment, configure the TensorBoard callback or file writer to write to a **subdirectory** of the experiment directory. This structure separates data by individual runs in the TensorBoard UI, making it easy to compare different training iterations. ^[tensorboard-databricks-on-aws.md]

Example directory structure:
```
experiment_1/
├── run_1/
├── run_2/
└── run_3/
```

### Storage Location Best Practices

#### Prefer Cloud Storage

Databricks recommends writing logs to **cloud storage** (such as AWS S3) rather than to the ephemeral cluster file system. The cluster file system is temporary and can be lost when the cluster terminates. Cloud storage provides reliable, persistent storage for experiment logs. ^[tensorboard-databricks-on-aws.md]

#### Avoid DBFS and UC Volumes

When logging TensorBoard-related data to DBFS or [Unity Catalog](/concepts/unity-catalog.md) Volumes, you may encounter the following error:
```
No dashboards are active for the current data set
```

To resolve this, call `writer.flush()` and `writer.close()` after using the writer to log data. This ensures all logged data is properly written and available for TensorBoard to render. ^[tensorboard-databricks-on-aws.md]

## Starting TensorBoard

### Using the `%tensorboard` Magic Command

The standard way to start TensorBoard is:

1. Load the `%tensorboard` magic:
   ```python
   %load_ext tensorboard
   ```

2. Define your log directory:
   ```python
   experiment_log_dir = <log-directory>
   ```

3. Start TensorBoard:
   ```python
   %tensorboard --logdir $experiment_log_dir
   ```

The TensorBoard server starts and displays the UI inline in the notebook, with a link to open it in a new tab. ^[tensorboard-databricks-on-aws.md]

## Process Management

### Manual Termination

TensorBoard processes started within Databricks notebooks are **not automatically terminated** when the notebook is detached or the REPL is restarted. To manually kill a TensorBoard process: ^[tensorboard-databricks-on-aws.md]

```bash
%sh kill -15 pid
```

Improperly killed TensorBoard processes might corrupt `notebook.list()`.

### Listing Running Processes

To list currently running TensorBoard servers with their log directories and process IDs: ^[tensorboard-databricks-on-aws.md]

```python
from tensorboard import notebook
notebook.list()
```

## Known Issues

- **Port Conflicts**: If too many TensorBoard processes run on the cluster, all ports in the default range may be unavailable. Specify a port with `--port` (between 6006 and 6106). ^[tensorboard-databricks-on-aws.md]

- **Inline UI**: External links within the iframe-based UI require opening in a new tab. ^[tensorboard-databricks-on-aws.md]

- **Download Links**: Only work when TensorBoard is opened in a tab. ^[tensorboard-databricks-on-aws.md]

## Related Concepts

- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- AWS S3
- DBFS
- [Unity Catalog](/concepts/unity-catalog.md)
- Cluster File System

## Sources

- tensorboard-databricks-on-aws.md

# Citations

1. [tensorboard-databricks-on-aws.md](/references/tensorboard-databricks-on-aws-052f8833.md)
