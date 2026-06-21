---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e92700116cc98c0c1a279caece8939f8c668021ea175673106efe6f999cc447
  pageDirectory: concepts
  sources:
    - tensorboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorboard-known-issues-and-workarounds-on-databricks
    - Workarounds on Databricks and TensorBoard Known Issues
    - TKIAWOD
  citations:
    - file: tensorboard-databricks-on-aws.md
title: TensorBoard Known Issues and Workarounds on Databricks
description: Specific issues encountered when using TensorBoard on Databricks including iframe limitations, port availability, blank projector tabs, and DBFS logging errors.
tags:
  - databricks
  - troubleshooting
  - known-issues
timestamp: "2026-06-19T23:06:13.502Z"
---

## TensorBoard Known Issues and Workarounds on Databricks

TensorBoard is a suite of visualization tools for debugging and understanding machine learning programs, and it is commonly used within Databricks notebooks. While TensorBoard runs similarly on Databricks as on a local Jupyter notebook, several known issues and platform‑specific behaviors can affect the user experience. This page lists those issues and describes the available workarounds. ^[tensorboard-databricks-on-aws.md]

### Inline TensorBoard UI and External Links

The inline TensorBoard UI is rendered inside an iframe inside the notebook. Browser security features prevent external links within the TensorBoard UI from working unless the link is opened in a new tab. ^[tensorboard-databricks-on-aws.md]

### `--window_title` Option Overridden

The `--window_title` option of TensorBoard is overridden on Databricks; any custom window title set via this flag is not displayed. ^[tensorboard-databricks-on-aws.md]

### Port Range Exhaustion

By default, TensorBoard scans a port range to select a port to listen on. If too many TensorBoard processes are running on the same cluster, all ports in the default range may become unavailable.  
**Workaround:** Specify a port number explicitly with the `--port` argument. The specified port must be between 6006 and 6106. ^[tensorboard-databricks-on-aws.md]

### Download Links Require Tab‑Mode TensorBoard

For download links to work, you must open TensorBoard in a separate browser tab rather than viewing it inline in the notebook. ^[tensorboard-databricks-on-aws.md]

### TensorBoard 1.15.0 Projector Tab Blank

When using TensorBoard version 1.15.0, the Projector tab appears blank.  
**Workaround:** To visit the projector page directly, replace `#projector` in the URL with `data/plugin/projector/projector_binary.html`. ^[tensorboard-databricks-on-aws.md]

### TensorBoard 2.4.0 Rendering Issue

TensorBoard 2.4.0 has a [known issue](https://github.com/tensorflow/tensorboard/issues/4421) that may affect TensorBoard rendering if upgraded. Databricks does not provide a platform‑specific workaround; users should consult the upstream issue tracker for updates. ^[tensorboard-databricks-on-aws.md]

### Logging to DBFS or UC Volumes Causes “No Dashboards Active”

If you log TensorBoard‑related data to DBFS or UC Volumes, you may encounter an error: `No dashboards are active for the current data set`.  
**Workaround:** After using the TensorBoard writer to log data, call `writer.flush()` and `writer.close()`. This ensures that all logged data is properly written and available for TensorBoard to render. ^[tensorboard-databricks-on-aws.md]

### TensorBoard Processes Not Killed on Notebook Detach

TensorBoard processes started inside a Databricks notebook are **not** terminated when the notebook is detached or the REPL is restarted (for example, when clearing the notebook state). Improperly killed TensorBoard processes can corrupt the output of `notebook.list()`. ^[tensorboard-databricks-on-aws.md]

To manually kill a TensorBoard process, send a termination signal using `%sh kill -15 pid`. To list currently running TensorBoard servers with their log directories and process IDs, run `notebook.list()` from the TensorBoard notebook module. ^[tensorboard-databricks-on-aws.md]

### Related Concepts

- [TensorBoard](/concepts/tensorboard-on-databricks.md) – Official TensorFlow documentation
- DBFS – Databricks File System
- UC Volumes – [Unity Catalog](/concepts/unity-catalog.md) Volumes
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Alternative experiment tracking on Databricks

### Sources

- tensorboard-databricks-on-aws.md

# Citations

1. [tensorboard-databricks-on-aws.md](/references/tensorboard-databricks-on-aws-052f8833.md)
