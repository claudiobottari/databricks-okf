---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 601beff24298b53f1eed2e024c2329d0222d14568ae5a657c27373825fe19ceb
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpointing-and-resume-training
    - Resume Training and Model Checkpointing
    - MCART
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: Model Checkpointing and Resume Training
description: A technique to save model state during training (e.g., after each epoch) and later resume training from a saved checkpoint, enabling long-running or interrupted training workflows.
tags:
  - deep-learning
  - training-workflow
  - model-management
  - checkpointing
timestamp: "2026-06-18T12:23:52.430Z"
---

---
title: Model Checkpointing and Resume Training
summary: Saving intermediate model states during training to enable recovery, experimentation, and continued training from a specific epoch.
sources:
  - forecasting-time-series-with-gluonts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T13:00:00.000Z"
updatedAt: "2026-06-18T13:00:00.000Z"
tags:
  - mlops
  - training
  - checkpointing
  - gluonts
  - pytorch-lightning
aliases:
  - model-checkpointing-and-resume-training
  - MCRT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Model Checkpointing and Resume Training

**Model checkpointing** is the practice of saving the state of a machine learning model at regular intervals during training, enabling recovery from interruptions, comparison of intermediate results, and resumption of training from a saved epoch. **Resume training** loads a previously saved checkpoint and continues the optimization process, allowing longer training runs to be split across sessions or extended without starting from scratch. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

Checkpointing is essential for long-running training jobs on distributed or GPU‑based infrastructure. In the context of [GluonTS](/concepts/gluonts.md) with a [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) trainer, checkpoints store the model weights, optimizer state, and training metadata. By default, Lightning saves the best model according to a monitored metric, but users can configure it to keep multiple snapshots — for example, one per epoch. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

When training a [DeepAR](/concepts/deepar.md) model for probabilistic time‑series forecasting, checkpoints are stored on a Unity Catalog Volume to persist model state across sessions. The checkpoint path is constructed from catalog, schema, and volume names provided as widgets, ensuring that artifacts are governed by Unity Catalog access policies. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Components

### Checkpoint Storage

Checkpoints are written to a directory within a Unity Catalog volume. The path follows the convention `/Volumes/{catalog}/{schema}/{volume}/{model_name}`. The volume must exist and the user must have `WRITE VOLUME` or equivalent privileges. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
CHECKPOINT_PATH = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"
os.makedirs(CHECKPOINT_PATH, exist_ok=True)
```

### ModelCheckpoint Callback

PyTorch Lightning’s `ModelCheckpoint` callback controls how and when checkpoints are saved. In GluonTS, the callback is passed via the `trainer_kwargs` argument of the estimator. The following configuration saves a checkpoint after every epoch and retains all of them: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from lightning.pytorch.callbacks import ModelCheckpoint

checkpoint_cb = ModelCheckpoint(
    dirpath=CHECKPOINT_PATH,
    filename="deepar-{epoch:02d}-{step}",       # e.g. deepar-epoch=09-step=500
    save_top_k=-1,                              # keep all checkpoints
    every_n_epochs=1,                           # save every epoch
    save_on_train_epoch_end=True,
)
```

The `filename` template can include placeholders like `{epoch}` and `{step}` to generate unique names. `save_top_k=-1` prevents automatic deletion of older checkpoints. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Implementation

### Setting Up the Estimator with Checkpointing

When creating a `DeepAREstimator` (or any GluonTS estimator backed by PyTorch Lightning), the checkpoint callback is included in the `trainer_kwargs`:

```python
trainer_hyperparameters = {
    "accelerator": "auto",
    "max_epochs": NUM_EPOCHS,
    "callbacks": [checkpoint_cb],
}

deepar_estimator = DeepAREstimator(
    freq="1h",
    prediction_length=168,
    context_length=672,
    trainer_kwargs=trainer_hyperparameters,
)

deepar_predictor = deepar_estimator.train(train_ds)
```

After training completes, the checkpoint directory contains one file per epoch (e.g., `deepar-epoch=09-step=500.ckpt`). ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Resume Training from a Checkpoint

To continue training from a specific checkpoint, pass the `ckpt_path` argument to the `.train()` method. The estimator’s hyperparameters (like `freq`, `prediction_length`, and `context_length`) must match the original training configuration. The `max_epochs` should be set to the total desired epochs — for example, `NUM_EPOCHS + 10` to add ten more epochs beyond the original plan. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
# Train for another 10 epochs starting from checkpoint
trainer_hyperparameters = {
    "accelerator": "auto",
    "max_epochs": NUM_EPOCHS + 10,   # total epochs = original + additional
    "callbacks": [checkpoint_cb],
}

deepar_estimator = DeepAREstimator(
    freq="1h",
    prediction_length=168,
    context_length=672,
    trainer_kwargs=trainer_hyperparameters,
)

updated_predictor = deepar_estimator.train(
    training_data=train_ds,
    ckpt_path=f"{CHECKPOINT_PATH}/deepar-epoch=09-step=500.ckpt",
)
```

The trainer loads the model and optimizer state from the checkpoint file and continues training from that point onward. New checkpoints are saved according to the same `ModelCheckpoint` callback settings. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Best Practices

- **Store checkpoints in a governed location.** Use a Unity Catalog volume to ensure that model artifacts are subject to the same access controls and auditing as other data assets. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Use descriptive filenames.** Include epoch and step information so you can easily identify which checkpoint to resume from. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Keep multiple checkpoints** (`save_top_k=-1`) to allow rollback to any earlier state, not just the best one. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Record the checkpoint path as an experiment parameter** or in the model registry to tie a deployed model to its exact training snapshot. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Match hyperparameters precisely** when resuming. The checkpoint contains metadata that is validated against the estimator’s current configuration; mismatches may cause errors or silent re‑initialization. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The deep‑learning time‑series library used alongside PyTorch Lightning
- [DeepAR](/concepts/deepar.md) — A probabilistic RNN model for forecasting
- Unity Catalog Volume — Governed storage location for model checkpoints
- PyTorch Lightning ModelCheckpoint — The callback that orchestrates checkpoint saving
- [Model Registry](/concepts/mlflow-model-registry.md) — For versioning and promoting finalized checkpoints to production
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging checkpoint metadata alongside experiments
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment where the training runs

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
