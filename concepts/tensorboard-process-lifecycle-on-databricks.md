---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82aac088fc347131a1ebecb6ea1a27d543057c4ef21973b35baef5d69efde401
  pageDirectory: concepts
  sources:
    - tensorboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorboard-process-lifecycle-on-databricks
    - TPLOD
  citations:
    - file: tensorboard-databricks-on-aws.md
title: TensorBoard Process Lifecycle on Databricks
description: Managing TensorBoard server processes on Databricks clusters including starting, listing, and killing processes, and handling port range limitations.
tags:
  - databricks
  - process-management
  - troubleshooting
timestamp: "2026-06-19T23:06:15.370Z"
---

# TensorBoard Process Lifecycle on Databricks

**TensorBoard Process Lifecycle on Databricks** describes how TensorBoard server processes are started, managed, and terminated within Databricks notebooks. Unlike typical notebook resources, TensorBoard processes persist beyond notebook session boundaries and require explicit management.

## Starting TensorBoard

TensorBoard can be started within a Databricks notebook using the `%tensorboard` magic command or by directly using TensorBoard's notebook module. ^[tensorboard-databricks-on-aws.md]

### Using the Magic Command

1. Load the `%tensorboard` extension and define a log directory:
   ```python
   %load_ext tensorboard
   experiment_log_dir = <log-directory>
   ```
2. Invoke the magic command:
   ```python
   %tensorboard --logdir $experiment_log_dir
   ```
   The TensorBoard server starts and displays the user interface inline in the notebook, along with a link to open TensorBoard in a new tab. ^[tensorboard-databricks-on-aws.md]

### Using the Notebook Module

```python
from tensorboard import notebook
notebook.start("--logdir {}".format(experiment_log_dir))
```

## Process Persistence

TensorBoard processes started within a Databricks notebook are **not terminated** when the notebook is detached or the REPL is restarted (for example, when clearing the state of the notebook). This persistence means that TensorBoard continues running on the cluster even after the initiating notebook session ends, consuming cluster resources. ^[tensorboard-databricks-on-aws.md]

## Process Management

### Listing Active Processes

To list the TensorBoard servers currently running on your cluster, including their corresponding log directories and process IDs, run `notebook.list()` from the TensorBoard notebook module. ^[tensorboard-databricks-on-aws.md]

### Manually Terminating Processes

To manually kill a TensorBoard process, send it a termination signal using `%sh kill -15 pid`, where `pid` is the process ID identified through `notebook.list()`. ^[tensorboard-databricks-on-aws.md]

**⚠️ Important:** Improperly killed TensorBoard processes might corrupt `notebook.list()`, making it unable to accurately report active processes. Using `kill -15` (SIGTERM) rather than `kill -9` (SIGKILL) is recommended to allow graceful shutdown. ^[tensorboard-databricks-on-aws.md]

## Port Management

By default, TensorBoard scans a port range for selecting a port to listen on. If too many TensorBoard processes are running on the cluster, all ports in the default range might become unavailable. To work around this limitation, specify a port number with the `--port` argument. The specified port should be between **6006 and 6106**. ^[tensorboard-databricks-on-aws.md]

## Best Practices

- **Use unique log directories**: For each experiment, start TensorBoard in a unique directory. For each run within the experiment, write to a subdirectory so the TensorBoard UI separates data into runs. ^[tensorboard-databricks-on-aws.md]
- **Write logs to cloud storage**: Databricks recommends writing logs to cloud storage rather than the ephemeral cluster file system to ensure reliable storage. ^[tensorboard-databricks-on-aws.md]
- **Clean up processes**: Terminate TensorBoard processes when they are no longer needed to free up cluster resources and port availability. ^[tensorboard-databricks-on-aws.md]

## Known Issues Related to Process Lifecycle

- The `--window_title` option of TensorBoard is overridden on Databricks. ^[tensorboard-databricks-on-aws.md]
- If TensorBoard-related data is logged to DBFS or Unity Catalog Volumes, you may encounter the error `No dashboards are active for the current data set`. To resolve this, call `writer.flush()` and `writer.close()` after using the `writer` to log data, ensuring all logged data is properly written and available for TensorBoard to render. ^[tensorboard-databricks-on-aws.md]

## Related Concepts

- TensorBoard - Inline UI Limitations
- Notebook Magic Commands - %tensorboard
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- [Deep Learning Training Logging](/concepts/mlflow-deep-learning-tracking.md)
- Cluster Resource Management

## Sources

- tensorboard-databricks-on-aws.md

# Citations

1. [tensorboard-databricks-on-aws.md](/references/tensorboard-databricks-on-aws-052f8833.md)
