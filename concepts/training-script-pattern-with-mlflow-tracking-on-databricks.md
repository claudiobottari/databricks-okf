---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6fde5e08d68fc5b8e97d7f0767e7e4a5b40b70c681fd0c0d114dad0bc03e2fa8
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - training-script-pattern-with-mlflow-tracking-on-databricks
    - TSPWMTOD
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Training Script Pattern with MLflow Tracking on Databricks
description: Pattern for training a PyTorch model on Databricks that includes MLflow experiment logging, Unity Catalog checkpointing, and single-GPU training with SGD optimizer.
tags:
  - databricks
  - mlflow
  - training
  - pytorch
timestamp: "2026-06-19T19:09:22.563Z"
---

# Training Script Pattern with MLflow Tracking on Databricks

The **Training Script Pattern with MLflow Tracking on Databricks** describes a repeatable structure for authoring machine learning training scripts that leverage Databricks’ managed [MLflow](/concepts/mlflow.md) for experiment tracking, serverless GPU compute for efficient training, and Unity Catalog Volumes for persistent checkpoint storage. This pattern is demonstrated in the image classification tutorial using a Convolutional Neural Network (CNN) on the MNIST dataset. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Overview

In this pattern, a training script performs the following steps in sequence: connect to serverless GPU compute, configure checkpoint storage via Unity Catalog Volumes, define the model architecture, set up the training loop with MLflow metric logging, run training, save checkpoints after each epoch, and optionally load and evaluate the trained model. The pattern ensures experiment reproducibility and observability through MLflow’s automatic run tracking and metric logging. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Key Components

### Serverless GPU Compute

Training scripts require a GPU for efficient model training. The pattern uses **Serverless GPU compute** from the notebook’s **Connect** dropdown. The user selects **Serverless GPU**, then in the **Environment** side panel sets the **Accelerator** (e.g., **1xA10** for the MNIST demo) and the **Environment** (e.g., **AI v5**). After clicking **Apply** and **Confirm**, the notebook session connects to the specified GPU. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

To avoid unnecessary GPU usage, the notebook connection can be terminated manually via the **Connected** menu (select **Terminate** and confirm). The connection also auto‑terminates after 60 minutes of inactivity. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### MLflow Tracking

MLflow is used to log training metrics (e.g., loss) and to track experimental runs. Within the training script, a run is started with `mlflow.start_run()`, and metrics are logged using `mlflow.log_metric()` at regular intervals during training. This allows users to visualize training progress in the Databricks MLflow UI. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

The pattern also supports setting a serverless budget policy on the MLflow experiment via the experiment’s **Details** panel or by calling `mlflow.set_experiment_tag()` with the key `mlflow.workload_creation_policy_id`. This is required when the workspace’s default budget policy is disabled and MLflow must use a dedicated policy for serverless workloads it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Unity Catalog Volumes

Model checkpoints are saved to a Unity Catalog Volume, which provides persistent, governance‑controlled storage. The training script defines the checkpoint path as `/Volumes/{catalog}/{schema}/{volume}/{model_name}`. This path is constructed from widget parameters (e.g., `uc_catalog`, `uc_schema`, `uc_volume`, `uc_model_name`) that are set at the top of the notebook. The `torch.distributed.checkpoint.dcp.save()` API is used to persist the model and optimizer state after each epoch. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### Training Loop

The training loop iterates over the data loader, performs forward and backward propagation, and updates the model parameters. The helper function `train_one_epoch` logs the training loss to MLflow every `log_interval` batches. After each epoch, the state dict (model and optimizer) is saved to the Unity Catalog Volume. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Pattern Implementation

The following steps outline the typical implementation of this pattern, based on the CNN notebook:

1. **Connect to serverless GPU compute** as described above.
2. **Configure checkpoint path** using notebook widgets for Unity Catalog catalog, schema, volume, and model name.
3. **Define the model architecture** (e.g., a `Net` class inheriting from `nn.Module`).
4. **Create a helper class** (e.g., `AppState`) that implements the `Stateful` protocol for checkpointing the model and optimizer with `torch.distributed.checkpoint`.
5. **Set training hyperparameters** (batch size, number of epochs, learning rate, momentum, log interval).
6. **Define the training function**:
   - Start an [MLflow Run](/concepts/mlflow-run.md).
   - Prepare the device (CUDA if available).
   - Load the training dataset and create a data loader.
   - Instantiate the model and optimizer.
   - For each epoch, call `train_one_epoch` (logging loss to MLflow) and save the checkpoint.
7. **Run the training function** with a chosen learning rate.
8. **Load and evaluate** the model from the checkpoint on a test dataset, computing the average test loss.

## Code Example

The following code snippets illustrate the core pattern elements, taken from the MNIST CNN tutorial.

### Checkpoint Path and AppState

```python
CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"

class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)
        return {"model": model_state_dict, "optim": optimizer_state_dict}

    def load_state_dict(self, state_dict):
        set_state_dict(self.model, self.optimizer,
                       model_state_dict=state_dict["model"],
                       optim_state_dict=state_dict["optim"])
```

^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### Training Function with MLflow Logging

```python
import mlflow

def train_one_epoch(model, device, data_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(data_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            mlflow.log_metric('loss', loss.item(),
                              step=epoch * len(data_loader) + batch_idx)

def train(learning_rate):
    with mlflow.start_run() as run:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # … dataset, model, optimizer setup …
        for epoch in range(1, num_epochs + 1):
            train_one_epoch(model, device, data_loader, optimizer, epoch)
            state_dict = {"app": AppState(model, optimizer)}
            dcp.save(state_dict, checkpoint_id=CHECKPOINT_DIR)
```

^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Distributed Training Extension

For models that require multiple GPUs or nodes, the pattern can be extended with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or the [[@distributed Decorator for GPU Orchestration|@distributed decorator from the `serverless_gpu` library]]. When using FSDP, the `AppState` helper class still handles checkpointing via `get_state_dict` and `set_state_dict`, which automatically manage FSDP’s fully qualified names. The `setup()` and `cleanup()` functions initialize and destroy the process group with NCCL backend. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md] ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

The `@distributed` decorator allows running a function across multiple GPUs on a single node, and the `serverless_gpu.runtime` module provides local and global rank information for coordination. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Unity Catalog Volumes
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- PyTorch
- Convolutional Neural Network (CNN)
- [Checkpointing with torch.distributed.checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md)

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
