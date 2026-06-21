---
title: Track runs with MLflow and the Jobs run page | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/track-runs
ingestedAt: "2026-06-18T08:08:17.073Z"
---

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

Each workload you submit with `air run` is both a Databricks job run and an MLflow run:

*   The job run (visible on the workspace **Jobs & Pipelines** page) tracks execution: status, compute, retries, and driver output.
*   The MLflow run tracks the experiment: parameters, metrics, system metrics, and artifacts.

One submission creates one job run and one MLflow run. A retry creates a new MLflow run.

## Experiments and runs[​](#experiments-and-runs "Direct link to Experiments and runs")

Two workload YAML fields control how the run appears in MLflow:

YAML

    experiment_name: my-training # Creates or appends to this MLflow experimentmlflow_run_name: baseline-lr3e5 # Names the MLflow run for this submissioncompute:  num_accelerators: 8  accelerator_type: GPU_8xH100command: torchrun --nproc_per_node=8 train.pymax_retries: 2

*   `experiment_name` (Required): Creates an MLflow experiment with this name if one doesn't exist, or appends a new run to the existing experiment. An experiment holds many runs.
*   `mlflow_run_name` (Optional): Sets the run name. If omitted, the run name defaults to the experiment name (`experiment_name`).
*   `max_retries` (Optional): Each retry attempt is a new MLflow run in the same experiment, so you can compare attempts. The original submission and its retries share one job run.

![MLflow run page showing metrics](https://docs.databricks.com/aws/en/assets/images/mlflow-run-page-fd8ebc6be4d360327532ae97b03fe1fb.png)

## Navigate between Jobs, MLflow, and previous workloads[​](#navigate-between-jobs-mlflow-and-previous-workloads "Direct link to Navigate between Jobs, MLflow, and previous workloads")

You can get to a run from three places:

*   **Jobs**: The Jobs run page lists your runs, and each run links to its MLflow run and experiment.
*   **MLflow**: The Experiments page lists your MLflow experiments.
*   **Previous workloads**: `air get run <job-run-id>` prints clickable links to the run's job, experiment, and MLflow run. `air list runs` lists your previous runs and lets you filter to find a specific run.

Bash

    air get run <job-run-id> # Links to the job, experiment, and MLflow runair list runs # List previous runs; filter to find a specific run

## System metrics[​](#system-metrics "Direct link to System metrics")

GPU, CPU, and memory system metrics are captured automatically for every run. No configuration is required. View them on the MLflow run's **System metrics** tab.

![System metrics tab of an MLflow run (GPU/CPU/memory)](https://docs.databricks.com/aws/en/assets/images/mlflow-system-metrics-1a0898f1033502b9c1fb89df94b34473.png)

## Log custom metrics[​](#log-custom-metrics "Direct link to Log custom metrics")

The platform creates the MLflow run and exposes its ID to your training process through the `MLFLOW_RUN_ID` environment variable. Use the [MLflow tracking API](https://docs.databricks.com/aws/en/mlflow/tracking) to log your own parameters, metrics, and artifacts to that run.

On distributed (multi-node) workloads, every node shares the same MLflow run. Log from the rank-0 process only, so each metric is recorded once:

Python

    import osimport mlflow# Log from rank 0 only; all nodes share the same MLFLOW_RUN_ID.if os.environ.get("RANK", "0") == "0":    with mlflow.start_run(run_id=os.environ["MLFLOW_RUN_ID"]):        mlflow.log_param("learning_rate", 3e-4)        for step, loss in enumerate(training_losses):            mlflow.log_metric("train_loss", loss, step=step)

## Logs and artifacts[​](#logs-and-artifacts "Direct link to Logs and artifacts")

Stream or download a run's logs with `air logs`:

Bash

    air logs <job-run-id> # Stream logs from node 0air logs <job-run-id> --node 2 # Logs from a specific nodeair logs <job-run-id> --download-to ./logs/ # Download instead of streaming

Logs are also available as artifacts on the MLflow run. To persist model checkpoints, write them to a Unity Catalog volume. For checkpointing patterns and managing volumes, see [Experiment tracking and observability](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability).

## See also[​](#see-also "Direct link to See also")

*   [AI Runtime CLI quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
*   [Experiment tracking and observability](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
