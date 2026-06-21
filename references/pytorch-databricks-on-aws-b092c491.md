---
title: PyTorch | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch
ingestedAt: "2026-06-18T08:13:33.359Z"
---

[PyTorch project](https://github.com/pytorch) is a Python package that provides GPU accelerated tensor computation and high level functionalities for building deep learning networks. For licensing details, see the PyTorch [license doc on GitHub](https://github.com/pytorch/pytorch/blob/a90c259edad1ea4fa1b8773e3cb37240df680d62/LICENSE).

To monitor and debug your PyTorch models, consider using [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard).

PyTorch is included in Databricks Runtime for Machine Learning. If you are using Databricks Runtime, see [Install PyTorch](#install-pytorch) for instructions on installing PyTorch.

note

This is not a comprehensive guide to PyTorch. For more information, see the [PyTorch website](https://pytorch.org/).

## Single node and distributed training[​](#single-node-and-distributed-training "Direct link to Single node and distributed training")

To test and migrate single-machine workflows, use a [Single Node cluster](https://docs.databricks.com/aws/en/compute/configure#single-node).

For distributed training options for deep learning, see [Distributed training](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/).

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

#### MLflow PyTorch end-to-end model training notebook

#### PyTorch notebook

#### MLflow PyTorch model training notebook with TensorFlow

## Install PyTorch[​](#install-pytorch "Direct link to Install PyTorch")

### Databricks Runtime for ML[​](#databricks-runtime-for-ml "Direct link to databricks-runtime-for-ml")

[Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/) includes PyTorch so you can create the cluster and start using PyTorch. For the version of PyTorch installed in the Databricks Runtime ML version you are using, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/).

### Databricks Runtime[​](#databricks-runtime "Direct link to Databricks Runtime")

Databricks recommends that you use the PyTorch included in Databricks Runtime for Machine Learning. However, if you must use [the standard Databricks Runtime](https://docs.databricks.com/aws/en/release-notes/runtime/), PyTorch can be installed as a [Databricks PyPI library](https://docs.databricks.com/aws/en/libraries/). The following example shows how to install PyTorch 1.5.0:

*   On GPU clusters, install `pytorch` and `torchvision` by specifying the following:
    
    *   `torch==1.5.0`
    *   `torchvision==0.6.0`
*   On CPU clusters, install `pytorch` and `torchvision` by using the following Python wheel files:
    
        https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp37-cp37m-linux_x86_64.whlhttps://download.pytorch.org/whl/cpu/torchvision-0.6.0%2Bcpu-cp37-cp37m-linux_x86_64.whl
    

## Errors and troubleshooting for distributed PyTorch[​](#errors-and-troubleshooting-for-distributed-pytorch "Direct link to errors-and-troubleshooting-for-distributed-pytorch")

The following sections describe common error messages and troubleshooting guidance for the classes: [PyTorch DataParallel](https://pytorch.org/docs/stable/generated/torch.nn.DataParallel.html) or [PyTorch DistributedDataParallel](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel). Most of these errors can likely be resolved with [TorchDistributor](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.torch.distributor.TorchDistributor.html), which is available on Databricks Runtime ML 13.0 and above. However, if `TorchDistributor` is not a viable solution, recommended solutions are also provided within each section.

The following is an example of how to use TorchDistributor:

Python

    from pyspark.ml.torch.distributor import TorchDistributordef train_fn(learning_rate):        # ...num_processes=2distributor = TorchDistributor(num_processes=num_processes, local_mode=True)distributor.run(train_fn, 1e-3)

### process 0 terminated with exit code 1[​](#process-0-terminated-with-exit-code-1 "Direct link to process-0-terminated-with-exit-code-1")

The following error can occur when using notebooks in Databricks or locally:

    process 0 terminated with exit code 1

To avoid this error, use `torch.multiprocessing.start_processes` with `start_method=fork` instead of `torch.multiprocessing.spawn`.

For example:

Python

    import torchdef train_fn(rank, learning_rate):    # required setup, e.g. setup(rank)        # ...num_processes = 2torch.multiprocessing.start_processes(train_fn, args=(1e-3,), nprocs=num_processes, start_method="fork")

### The server socket has failed to bind to port[​](#the-server-socket-has-failed-to-bind-to-port "Direct link to the-server-socket-has-failed-to-bind-to-port")

The following error appears when you restart the distributed training after interrupting the cell during training:

    The server socket has failed to bind to [::]:{PORT NUMBER} (errno: 98 - Address already in use).

To fix the issue, restart the cluster. If restarting does not solve the problem, there might be an error in the training function code.

You can run into additional issues with CUDA since `start_method=”fork”` is [not CUDA-compatible](https://github.com/pytorch/pytorch/blob/master/torch/multiprocessing/spawn.py#L173). Using any `.cuda` commands in any cell might lead to failures. To avoid these errors, add the following check before you call `torch.multiprocessing.start_method`:

Python

    if torch.cuda.is_initialized():    raise Exception("CUDA was initialized; distributed training will fail.") # or something similar
