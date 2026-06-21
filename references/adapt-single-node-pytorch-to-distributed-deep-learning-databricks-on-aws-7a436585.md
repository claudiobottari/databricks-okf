---
title: Adapt single node PyTorch to distributed deep learning | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-pytorch
ingestedAt: "2026-06-18T08:03:03.951Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Documentation archive](https://docs.databricks.com/aws/en/archive/)
*   [Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod)
*   [HorovodRunner: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner)
*   Adapt single node PyTorch to distributed deep learning

Last updated on **Sep 26, 2024**

Learn how to perform distributed training of machine learning models using PyTorch.

This notebook follows the recommended [development workflow](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner#development-workflow). It first shows how to train the model on a single node, and then how to adapt the code using HorovodRunner for distributed training.

#### HorovodRunner PyTorch MNIST example notebook

[Open notebook in new tab](https://docs.databricks.com/aws/en/notebooks/source/deep-learning/mnist-pytorch.html)
