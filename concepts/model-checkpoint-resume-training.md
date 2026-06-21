---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a627d42a4928a83627f7a0bb8cd4db3fdf9934ef3afd0688e17a570e690e5aa1
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpoint-resume-training
    - MCRT
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
    - file: forecasting-time-series-with-glounts-databricks-on-aws.md
      start: 262
      end: 285
    - file: forecasting-time-series-with-glounts-databricks-on-aws.md
      start: 301
      end: 321
    - file: forecasting-time-series-with-glounts-databricks-on-aws.md
title: Model Checkpoint Resume Training
description: A technique for saving model state during training (via PyTorch Lightning's ModelCheckpoint) and later resuming training from a saved checkpoint.
tags:
  - machine-learning
  - training
  - checkpointing
timestamp: "2026-06-19T18:53:27.687Z"
---

# Model Checkpoint Resume Training

**Model Checkpoint Resume Training** is a technique that allows a machine learning model to continue training from a previously saved state, rather than starting from scratch. This approach is essential for long-running training jobs, iterative model development, and recovering from interruptions.

## Overview

During training, model checkpoints capture the model's parameters, optimizer state, and training progress at specific intervals. Resume training loads these saved states and continues the training process for additional epochs or iterations, preserving all learned patterns and optimizer momentum. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Benefits

- **Interruption Recovery**: If a training job fails or is stopped, training can resume from the latest checkpoint instead of restarting from epoch zero.
- **Iterative Development**: Models can be trained incrementally, allowing practitioners to review intermediate results and decide to continue training.
- **Extended Training**: Checkpoints enable extending training beyond the originally planned number of epochs without losing progress.

## Implementation Example

The following example demonstrates checkpoint resume training using [GluonTS](/concepts/gluonts.md) with a [DeepAREstimator](/concepts/deepar-estimator.md) on [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu-compute.md): ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Saving Checkpoints

Configure a `ModelCheckpoint` callback to save checkpoints after each epoch: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from lightning.pytorch.callbacks import ModelCheckpoint
import os

CHECKPOINT_PATH = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"
os.makedirs(CHECKPOINT_PATH, exist_ok=True)

checkpoint_cb = ModelCheckpoint(
    dirpath=CHECKPOINT_PATH,
    filename="deepar-{epoch:02d}-{step}",
    save_top_k=-1,           # keep all checkpoints
    every_n_epochs=1,        # save after every epoch
    save_on_train_epoch_end=True,
)
```

### Initial Training

Train the model for the initial number of epochs, which produces checkpoints at each epoch boundary: ^[forecasting-time-series-with-glounts-databricks-on-aws.md:262-285]

```python
NUM_EPOCHS = 10

trainer_hyperparameters = {
    "accelerator": "auto",
    "max_epochs": NUM_EPOCHS,
    "callbacks": [checkpoint_cb],
}

deepar_estimator = DeepAREstimator(
    freq=freq,
    prediction_length=prediction_length,
    context_length=4 * prediction_length,
    trainer_kwargs=trainer_hyperparameters,
)

deepar_predictor = deepar_estimator.train(train_ds)
```

### Resuming Training

To resume training for additional epochs, create a new estimator with an increased `max_epochs` value and pass the checkpoint path to the `train()` method: ^[forecasting-time-series-with-glounts-databricks-on-aws.md:301-321]

```python
# Configure for additional 10 epochs
trainer_hyperparameters = {
    "accelerator": "auto",
    "max_epochs": NUM_EPOCHS + 10,  # Extend total epochs
    "callbacks": [checkpoint_cb],
}

deepar_estimator = DeepAREstimator(
    **model_hyperparameters,
    trainer_kwargs=trainer_hyperparameters,
)

updated_predictor = deepar_estimator.train(
    training_data=train_ds,
    ckpt_path=f"{CHECKPOINT_PATH}/deepar-epoch=09-step=500.ckpt",
)
```

The `ckpt_path` parameter specifies which checkpoint file to load. The trainer continues training from that state for the remaining epochs. ^[forecasting-time-series-with-glounts-databricks-on-aws.md]

## Best Practices

- **Store checkpoints in durable storage**: Use Unity Catalog Volumes or cloud object storage (e.g., AWS S3) to persist checkpoints across sessions.
- **Use consistent model architecture**: The model architecture defined in the estimator must match the checkpoint; otherwise, loading will fail.
- **Save checkpoints regularly**: Frequent checkpointing (e.g., every epoch) minimizes potential progress loss from interruptions.
- **Keep multiple checkpoints**: Retaining several checkpoints (`save_top_k=-1`) provides fallback options if a specific checkpoint is corrupted.

## Related Concepts

- Model Checkpointing — The general practice of saving model state during training.
- [DeepAREstimator](/concepts/deepar-estimator.md) — A probabilistic forecasting model that supports checkpoint resume training.
- [GluonTS](/concepts/gluonts.md) — A time series forecasting library that integrates checkpointing with PyTorch Lightning.
- Unity Catalog Volumes — Storage volumes for persisting artifacts like model checkpoints.
- Training Interruption Recovery — Broader strategies for handling training failures.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Checkpointing considerations in multi-GPU or multi-node setups.

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
2. forecasting-time-series-with-glounts-databricks-on-aws.md:262-285
3. forecasting-time-series-with-glounts-databricks-on-aws.md:301-321
4. forecasting-time-series-with-glounts-databricks-on-aws.md
