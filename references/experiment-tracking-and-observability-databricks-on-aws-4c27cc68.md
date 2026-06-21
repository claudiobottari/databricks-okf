---
title: Experiment tracking and observability | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability
ingestedAt: "2026-06-18T08:09:18.578Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page describes how to use MLflow, view logs, manage model checkpoints, and monitor GPU resources on AI Runtime.

## MLflow integration[​](#mlflow-integration "Direct link to MLflow integration")

AI Runtime integrates natively with MLflow for experiment tracking, model logging, and metric visualization.

Setup recommendations:

*   Upgrade MLflow to version 3.7 or newer and follow the [deep learning workflow patterns](https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow).
    
*   Enable autologging for PyTorch Lightning:
    
    Python
    
        import mlflowmlflow.pytorch.autolog()
    
*   Customize your MLflow run name by encapsulating your model training code within the `mlflow.start_run()` API scope. This gives you control over the run name and enables you to restart from a previous run.You can customize the run name using the `run_name` parameter in `mlflow.start_run(run_name="your-custom-name")` or in third-party libraries that support MLflow (for example, Hugging Face Transformers). Otherwise, the default run name is `jobTaskRun-xxxxx`.
    
    Python
    
        from transformers import TrainingArgumentsargs = TrainingArguments(    report_to="mlflow",    run_name="llama7b-sft-lr3e5",  # <-- MLflow run name    logging_steps=50,)
    
*   The Serverless GPU API automatically launches an MLflow experiment with default name `/Users/{WORKSPACE_USER}/{get_notebook_name()}`. Users can overwrite it with the environment variable `MLFLOW_EXPERIMENT_NAME`.Always use absolute paths for the `MLFLOW_EXPERIMENT_NAME` environment variable:
    
    Python
    
        import osos.environ["MLFLOW_EXPERIMENT_NAME"] = "/Users/<username>/my-experiment"
    
*   Resume previous training by setting the `MLFLOW_RUN_ID` from the earlier run:
    
    Python
    
        mlflow.start_run(run_id="<previous-run-id>")
    
*   Set the `step` parameter in `MLFlowLogger` to reasonable batch numbers. MLflow has a limit of 10 million metric steps — logging every single batch on large training runs can hit this limit. See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).
    

## Viewing logs[​](#viewing-logs "Direct link to Viewing logs")

*   **Notebook output** — Standard output and errors from your training code appear in the notebook cell output.
*   **MLflow logs** — The MLflow experiment UI displays training metrics, parameters, and artifacts.

## Model checkpointing[​](#model-checkpointing "Direct link to Model checkpointing")

For distributed training, save and load model checkpoints asynchronously to [Unity Catalog volumes](https://docs.databricks.com/aws/en/volumes/volume-files), which provide the same governance as other Unity Catalog objects. Use `UCVolumeWriter` and `UCVolumeReader` from the `serverless_gpu.data` package with the [Torch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html) (DCP) API. These storage backends stage all I/O through a fast local directory (`/tmp`, which is NVMe-backed on serverless GPU nodes) and upload to or download from the Unity Catalog volume, which is faster than writing checkpoint shards directly to the FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after its data shards finish uploading.

note

`UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu) or above (Serverless GPU Python API 0.5.16+).

Checkpoint often enough to limit lost work after an interruption, but not so often that I/O overhead slows training. Aim for one checkpoint every 30 minutes to an hour, and tune the interval based on your step time and checkpoint size.

To upload checkpoints in the background while training continues, pass a `UCVolumeWriter` as the `storage_writer` to `dcp.async_save`. Asynchronous saves require a CPU backend on the process group, so initialize it with `torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)`:

Python

    import torch.distributed.checkpoint as dcpfrom serverless_gpu.data import UCVolumeWritercheckpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"writer = UCVolumeWriter(checkpoint_path)future = dcp.async_save(state_dict, storage_writer=writer)# ...continue training...future.result()  # blocks until the upload lands on the UC volume

Load a checkpoint with `UCVolumeReader`:

Python

    from serverless_gpu.data import UCVolumeReaderreader = UCVolumeReader(checkpoint_path)dcp.load(state_dict, storage_reader=reader)

### Data pipeline checkpointing[​](#data-pipeline-checkpointing "Direct link to Data pipeline checkpointing")

A model checkpoint captures model and optimizer state, but not the position of your data pipeline within the dataset, so a resumed run cannot fast-forward to the exact sample where it stopped. Account for this in how you resume: restart from an epoch boundary, or track processed samples or shards in your own training state so you can skip them on resume.

## Monitor GPU resources[​](#monitor-gpu-resources "Direct link to Monitor GPU resources")

Use the **GPU resources** pane to monitor GPU health and utilization while your code runs on AI Runtime. The pane supports both single-node and multi-node workloads.

To open the pane, connect your notebook to AI Runtime, then click ![Chip icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTciIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNyAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTguMDA1ODYgM0g5LjQ5NDE0VjEuNUgxMC45OTQxVjNIMTIuOTUwMkwxMy4wMzIyIDMuMDAzOTFDMTMuNDM1NCAzLjA0NTA2IDEzLjc0OTkgMy4zODU4NSAxMy43NSAzLjc5OThWNS43NTU4NkgxNS4yMzM0VjcuMjU1ODZIMTMuNzVWOC43NDQxNEgxNS4yMzM0VjEwLjI0NDFIMTMuNzVWMTIuMjAwMkwxMy43NDYxIDEyLjI4MjJDMTMuNzA3NyAxMi42NTg0IDEzLjQwODQgMTIuOTU3NyAxMy4wMzIyIDEyLjk5NjFMMTIuOTUwMiAxM0gxMC45OTQxVjE0LjVIOS40OTQxNFYxM0g4LjAwNTg2VjE0LjVINi41MDU4NlYxM0g0LjU0OThMNC40Njc3NyAxMi45OTYxQzQuMDkxNjIgMTIuOTU3NyAzLjc5MjM0IDEyLjY1ODQgMy43NTM5MSAxMi4yODIyTDMuNzUgMTIuMjAwMlYxMC4yNDQxSDIuMjY3NThWOC43NDQxNEgzLjc1VjcuMjU1ODZIMi4yNjc1OFY1Ljc1NTg2SDMuNzVWMy43OTk4QzMuNzUwMTQgMy4zNTgxNiA0LjEwODE1IDMuMDAwMTEgNC41NDk4IDNINi41MDU4NlYxLjVIOC4wMDU4NlYzWk01LjI1IDExLjVIMTIuMjVWNC41SDUuMjVWMTEuNVpNMTAuNzQ4IDEwSDYuNzQ4MDVWNkgxMC43NDhWMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **GPU resources** in the right side pane.

![GPU resources pane showing utilization, memory, and temperature metrics for each GPU.](https://docs.databricks.com/aws/en/assets/images/gpu-resources-panel-16e1691e01f494715a6aeb3b22f3d387.png)

The pane displays the following metrics for each GPU:

*   GPU utilization percentage
*   GPU memory usage
*   Temperature

The pane polls metrics every 10 seconds and retains up to 2 hours of history. Click ![Refresh icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xIDhDMSA0LjEzNDAxIDQuMTM0MDEgMSA4IDFDOS44ODI3NSAxIDExLjU5MzIgMS43NDQyOSAxMi44NTA3IDIuOTUzMDlMMTMuNSAzLjU0NzIxVjJMMTUgMkwxNSA2TDExIDZWNC41SDEyLjMxOTJMMTEuODIzOCA0LjA0NjczTDExLjgxNjggNC4wMzk5NEMxMC44MjcgMy4wODU3IDkuNDgyNjggMi41IDggMi41QzQuOTYyNDMgMi41IDIuNSA0Ljk2MjQzIDIuNSA4QzIuNSAxMS4wMzc2IDQuOTYyNDIgMTMuNSA3Ljk5OTk4IDEzLjVDOS41MjQyMSAxMy41IDEwLjkwMjQgMTIuODgxIDExLjg5OTQgMTEuODc4N0wxMi45NjI4IDEyLjkzNjZDMTEuNjk1OSAxNC4yMTAyIDkuOTM5NDYgMTUgNy45OTk5OCAxNUM0LjEzMzk5IDE1IDEgMTEuODY2IDEgOFoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) **Refresh** to fetch the latest values immediately. After 5 minutes of inactivity, the pane pauses; reopen it to resume monitoring.

## Multi-user collaboration[​](#multi-user-collaboration "Direct link to Multi-user collaboration")

*   To ensure all users can access shared code (for example, helper modules or environment YAML files), store them in `/Workspace/Shared` instead of user-specific folders like `/Workspace/Users/<your_email>/`.
*   For code that is in active development, use Git folders in user-specific folders `/Workspace/Users/<your_email>/` and push to remote Git repos. This allows multiple users to have a user-specific clone and branch, while still using a remote Git repo for version control. See [best practices](https://docs.databricks.com/aws/en/repos/ci-cd) for using Git on Databricks.
*   Collaborators can [share and comment](https://docs.databricks.com/aws/en/notebooks/notebooks-collaborate) on notebooks.

## Global limits in Databricks[​](#global-limits-in-databricks "Direct link to global-limits-in-databricks")

See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).
