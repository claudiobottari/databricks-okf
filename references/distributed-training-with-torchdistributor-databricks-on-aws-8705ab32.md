---
title: Distributed training with TorchDistributor | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor
ingestedAt: "2026-06-18T08:13:24.313Z"
---

This article describes how to perform distributed training on PyTorch ML models using [TorchDistributor](https://github.com/apache/spark/blob/master/python/pyspark/ml/torch/distributor.py).

TorchDistributor is an open-source module in PySpark that helps users do distributed training with PyTorch on their Spark clusters, so it lets you launch PyTorch training jobs as Spark jobs. Under-the-hood, it initializes the environment and the communication channels between the workers and utilizes the CLI command `torch.distributed.run` to run distributed training across the worker nodes.

The [TorchDistributor API](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.torch.distributor.TorchDistributor.html) supports the methods shown in the following table.

## Requirements[​](#requirements "Direct link to Requirements")

*   Spark 3.4
*   Databricks Runtime 13.0 ML or above

## Development workflow for notebooks[​](#development-workflow-for-notebooks "Direct link to Development workflow for notebooks")

If the model creation and training process happens entirely from a notebook on your local machine or a [Databricks Notebook](https://docs.databricks.com/aws/en/notebooks/), you only have to make minor changes to get your code ready for distributed training.

1.  **Prepare single node code:** Prepare and test the single node code with PyTorch, PyTorch Lightning, or other frameworks that are based on PyTorch/PyTorch Lightning like, the HuggingFace Trainer API.
    
2.  **Prepare code for standard distributed training:** You need to [convert your single process training to distributed training](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). Have this distributed code all encompassed within one training function that you can use with the `TorchDistributor`.
    
3.  **Move imports within training function:** Add the necessary imports, such as `import torch`, within the training function. Doing so allows you to avoid common pickling errors. Furthermore, the `device_id` that models and data are be tied to is determined by:
    
    Python
    
        device_id = int(os.environ["LOCAL_RANK"])
    
4.  **Launch distributed training:** Instantiate the `TorchDistributor` with the desired parameters and call `.run(*args)` to launch training.
    

The following is a training code example:

Python

    from pyspark.ml.torch.distributor import TorchDistributordef train(learning_rate, use_gpu):  import torch  import torch.distributed as dist  import torch.nn.parallel.DistributedDataParallel as DDP  from torch.utils.data import DistributedSampler, DataLoader  backend = "nccl" if use_gpu else "gloo"  dist.init_process_group(backend)  device = int(os.environ["LOCAL_RANK"]) if use_gpu  else "cpu"  model = DDP(createModel(), **kwargs)  sampler = DistributedSampler(dataset)  loader = DataLoader(dataset, sampler=sampler)  output = train(model, loader, learning_rate)  dist.cleanup()  return outputdistributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)distributor.run(train, 1e-3, True)

## Migrate training from external repositories[​](#migrate-training-from-external-repositories "Direct link to Migrate training from external repositories")

If you have an existing distributed training procedure stored in an external repository, you can easily migrate to Databricks by doing the following:

1.  **Import the repository:** Import the external repository as a [Databricks Git folder](https://docs.databricks.com/aws/en/repos/).
2.  **Create a new notebook** Initialize a new Databricks Notebook within the repository.
3.  **Launch distributed training** In a notebook cell, call `TorchDistributor` like the following:

Python

    from pyspark.ml.torch.distributor import TorchDistributortrain_file = "/path/to/train.py"args = ["--learning_rate=0.001", "--batch_size=16"]distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)distributor.run(train_file, *args)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

A common error for the notebook workflow is that objects cannot be found or pickled when running distributed training. This can happen when the library import statements are not distributed to other executors.

To avoid this issue, include all import statements (for example, `import torch`) _both_ at the top of the training function that is called with `TorchDistributor(...).run(<func>)` and inside any other user-defined functions called in the training method.

### CUDA failure: `peer access is not supported between these two devices`[​](#cuda-failure-peer-access-is-not-supported-between-these-two-devices "Direct link to cuda-failure-peer-access-is-not-supported-between-these-two-devices")

This is a potential error on the G5 suite of GPUs on AWS. To resolve this error, add the following snippet in your training code:

Python

    import osos.environ["NCCL_P2P_DISABLE"] = "1"

### NCCL failure: `ncclInternalError: Internal check failed.`[​](#nccl-failure-ncclinternalerror-internal-check-failed "Direct link to nccl-failure-ncclinternalerror-internal-check-failed")

When you encounter this error during multi-node training, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication.

To resolve this error, add the following snippet in your training code to use the primary network interface.

Python

    import osos.environ["NCCL_SOCKET_IFNAME"] = "eth0"

### Gloo failure: `RuntimeError: Connection refused`[​](#gloo-failure-runtimeerror-connection-refused "Direct link to gloo-failure-runtimeerror-connection-refused")

You may potentially run into this error when using Gloo for distributed training on CPU instances. To resolve this error, add the following snippet in your training code:

Python

    import osos.environ["GLOO_SOCKET_IFNAME"] = "eth0"

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

The following notebook examples demonstrate how to perform distributed training with PyTorch.

#### End-to-end distributed training on Databricks notebook

#### Distributed fine-tuning a Hugging Face model notebook

#### Distributed training on a PyTorch File notebook

#### Distributed training using PyTorch Lightning notebook
