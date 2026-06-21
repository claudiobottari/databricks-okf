---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43df940c0174db963a0e388c3edd9453ce028e1ef508cae2693125fd7a6a3dce
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cnn-architecture-for-mnist-classification-in-pytorch
    - CAFMCIP
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: CNN Architecture for MNIST Classification in PyTorch
description: A simple CNN with two convolutional layers (kernel size 5), max pooling, dropout, and two fully connected layers, ending with log_softmax for 10-class digit classification.
tags:
  - pytorch
  - convolutional-neural-networks
  - mnist
  - image-classification
timestamp: "2026-06-19T19:09:09.176Z"
---

# CNN Architecture for MNIST Classification in PyTorch

The **CNN Architecture for MNIST Classification in PyTorch** is a demonstration notebook provided by Databricks that shows how to train a Convolutional Neural Network (CNN) on the [MNIST Dataset](/concepts/mnist-dataset.md) of handwritten digits (0–9) using PyTorch and serverless GPU compute. The notebook covers defining a simple CNN, training on a single GPU, saving checkpoints to Unity Catalog Volumes, and evaluating the trained model. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## CNN Architecture

The network, defined as a `Net` class that extends `torch.nn.Module`, consists of two convolutional layers followed by two fully connected layers, with dropout and max pooling for regularization. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

| Layer | Specification |
|-------|---------------|
| `conv1` | `nn.Conv2d(1, 10, kernel_size=5)` |
| `conv2` | `nn.Conv2d(10, 20, kernel_size=5)` |
| `conv2_drop` | `nn.Dropout2d()` |
| `fc1` | `nn.Linear(320, 50)` |
| `fc2` | `nn.Linear(50, 10)` |

In the forward pass, the input passes through `conv1`, ReLU activation, and 2×2 max pooling; then through `conv2`, dropout, ReLU, and again 2×2 max pooling. The resulting tensor is reshaped to a vector of size 320, fed to `fc1` with ReLU and dropout, then to `fc2`, and finally log_softmax is applied for classification. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Training Loop

The training function runs for five epochs using a batch size of 100, the SGD optimizer with momentum 0.5, and learning rate 0.001. For each batch, the model computes the negative log-likelihood loss (`F.nll_loss`), performs backward propagation, and updates weights. Training loss is logged to [MLflow](/concepts/mlflow.md) every 100 batches via `mlflow.log_metric`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

After each epoch, the model and optimizer state are saved to a Unity Catalog Volume using `torch.distributed.checkpoint.save()`. The checkpoint path is constructed as `/Volumes/{catalog}/{schema}/{volume}/{model_name}`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Checkpointing and Evaluation

A helper class `AppState`, implementing the `Stateful` protocol, wraps the model and optimizer so that `dcp.save` and `dcp.load` automatically handle distributed state dictionaries via `get_state_dict` and `set_state_dict`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

To evaluate, the notebook loads the checkpoint with `dcp.load`, sets the model to evaluation mode, and computes the average test loss on the MNIST test dataset using the same negative log-likelihood criterion. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure used to run the notebook on a 1xA10 GPU.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging training metrics and experiment metadata.
- Unity Catalog Volumes – Storage location for checkpoint files.
- [PyTorch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) – The API used for saving and loading model and optimizer states.
- Horovod PyTorch MNIST Example – The original source on which this implementation is based.

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
