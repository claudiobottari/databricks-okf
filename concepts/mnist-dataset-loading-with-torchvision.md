---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e37659330e2310223dae021ffb80b0098b2655b6c6caf09e19802ab707c2ec4
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-dataset-loading-with-torchvision
    - MDLWT
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: MNIST Dataset Loading with torchvision
description: Loading and transforming the MNIST handwritten digit dataset using torchvision.datasets.MNIST with ToTensor and Normalize transformations.
tags:
  - pytorch
  - torchvision
  - mnist
  - datasets
timestamp: "2026-06-19T19:09:24.987Z"
---

# MNIST Dataset Loading with torchvision

The **MNIST dataset** (Mixed National Institute of Standards and Technology) is a well-known benchmark in machine learning, containing 70,000 grayscale images of handwritten digits from 0 to 9. Each image is 28×28 pixels. Due to its manageable size and balanced classes, MNIST is frequently used for learning image classification techniques. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

In PyTorch, the MNIST dataset can be loaded conveniently using the `torchvision.datasets.MNIST` class. This class handles downloading, caching, and applying transformations to the raw data, making it straightforward to integrate into a training pipeline. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Loading the Dataset

The standard way to load MNIST with torchvision is:

```python
from torchvision import datasets, transforms

train_dataset = datasets.MNIST(
    'data',
    train=True,
    download=True,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
)
```

This code does the following: ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

- **First argument (`'data'`):** Specifies the root directory where the dataset will be stored. If the directory does not exist, it is created automatically.
- **`train=True`** – Loads the training split (60,000 images). Use `train=False` to load the test split (10,000 images).
- **`download=True`** – Downloads the dataset from the official MNIST repository if it is not already present in the root directory.
- **`transform`** – A callable (or composition of callables) applied to each sample. The most common pipeline is described below.

## Transform Pipeline

The `transforms.Compose` object chains two transformations: ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

1. **`transforms.ToTensor()`** – Converts a PIL Image or NumPy array (H×W×C, values in [0,255]) to a PyTorch FloatTensor of shape (C×H×W) with values scaled to [0.0, 1.0].
2. **`transforms.Normalize((0.1307,), (0.3081,))`** – Normalizes the tensor channel-wise using the mean and standard deviation computed over the MNIST training set. For grayscale images, only a single channel mean and std are needed; the values `(0.1307,)` and `(0.3081,)` are the standard precomputed statistics for MNIST.

These two steps together ensure that the input data is in the expected range and distribution for many neural network architectures. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Using the Dataset with a DataLoader

Once the dataset object is created, it can be passed to a PyTorch `DataLoader` to iterate over mini‑batches during training or evaluation. For example:

```python
data_loader = torch.utils.data.DataLoader(train_dataset, batch_size=100, shuffle=True)
```

This creates a loader that yields batches of 100 images and their corresponding labels, shuffling the data each epoch. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Related Concepts

- torchvision – The library providing the `datasets` and `transforms` modules.
- PyTorch DataLoader – Utility for batching, shuffling, and parallel data loading.
- Transforms in torchvision – Preprocessing pipelines for image data.
- Convolutional Neural Network (CNN) – A common architecture trained on MNIST.
- [MNIST Dataset](/concepts/mnist-dataset.md) – The underlying data resource.

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
