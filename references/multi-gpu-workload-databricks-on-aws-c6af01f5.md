---
title: Multi-GPU workload | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training
ingestedAt: "2026-06-18T08:08:23.889Z"
---

You can launch distributed workloads across multiple GPUs on a single node using the [Serverless GPU Python API](https://api-docs.databricks.com/python/serverless_gpu/index.html). The API provides a simple, unified interface that abstracts away the details of GPU provisioning, environment setup, and workload distribution. With minimal code changes, you can seamlessly move from single-GPU training to multi-GPU distributed execution from the same notebook.

note

Distributed training requires an 8xH100 accelerator, which provisions a single node with 8 GPUs. When using the `@distributed` decorator, set `gpus=8` and `gpu_type='H100'`.

## Supported frameworks[​](#supported-frameworks "Direct link to Supported frameworks")

The `@distributed` API integrates with major distributed training libraries:

*   **PyTorch Distributed Data Parallel (DDP)** — Standard multi-GPU data parallelism.
*   **Fully Sharded Data Parallel (FSDP)** — Memory-efficient training for large models.
*   **DeepSpeed** — Microsoft's optimization library for large model training.

## serverless\_gpu API vs. TorchDistributor[​](#serverless_gpu-api-vs-torchdistributor "Direct link to serverless_gpu API vs. TorchDistributor")

The following table compares the `serverless_gpu` `@distributed` API with [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor):

The `serverless_gpu` API is the recommended approach for new deep learning workloads on Databricks. TorchDistributor remains available for workloads tightly coupled with Spark clusters.

## Quick start[​](#quick-start "Direct link to Quick start")

The serverless GPU API for distributed training is preinstalled when you are connected to a serverless GPU within Databricks notebooks and jobs. We recommend [GPU environment 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/four-gpu#base-environment) and above. To use it for distributed training, import and use the `distributed` decorator to distribute your training function.

Wrap the model training code in a function and decorate the function with the `@distributed` decorator. The decorated function becomes the entrypoint for distributed execution — all training logic, data loading, and model initialization should be defined inside this function.

warning

The `gpu_type` parameter in `@distributed` must match the accelerator type your notebook is connected to. For example, `@distributed(gpus=8, gpu_type='H100')` requires that your notebook is connected to an H100 accelerator. Using a mismatched accelerator type (such as connecting to A10 while specifying H100) will cause the workload to fail.

The code snippet below shows the basic usage of `@distributed`:

Python

    # Import the distributed decoratorfrom serverless_gpu import distributed# Decorate your training function with @distributed and specify the number of GPUs and GPU type@distributed(gpus=8, gpu_type='H100')def run_train():    ...

Below is a full example that trains a multilayer perceptron (MLP) model on 8 H100 GPUs from a notebook:

1.  Set up your model and define utility functions.
    
    Python
    
        # Define the modelimport osimport torchimport torch.distributed as distimport torch.nn as nndef setup():    torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))    dist.init_process_group("nccl")def cleanup():    dist.destroy_process_group()class SimpleMLP(nn.Module):    def __init__(self, input_dim=10, hidden_dim=64, output_dim=1):        super().__init__()        self.net = nn.Sequential(            nn.Linear(input_dim, hidden_dim),            nn.ReLU(),            nn.Dropout(0.2),            nn.Linear(hidden_dim, hidden_dim),            nn.ReLU(),            nn.Dropout(0.2),            nn.Linear(hidden_dim, output_dim)        )    def forward(self, x):        return self.net(x)
    
2.  Import the _serverless\_gpu_ library and the _distributed_ module.
    
    Python
    
        import serverless_gpufrom serverless_gpu import distributed
    
3.  Wrap the model training code in a function and decorate the function with the `@distributed` decorator.
    
    Python
    
        @distributed(gpus=8, gpu_type='H100')def run_train(num_epochs: int, batch_size: int) -> None:    import mlflow    import torch.optim as optim    from torch.nn.parallel import DistributedDataParallel as DDP    from torch.utils.data import DataLoader, DistributedSampler, TensorDataset    # 1. Set up multi-GPU environment    setup()    device = torch.device(f"cuda:{int(os.environ['LOCAL_RANK'])}")    # 2. Apply the Torch distributed data parallel (DDP) library for data-parellel training.    model = SimpleMLP().to(device)    model = DDP(model, device_ids=[device])    # 3. Create and load dataset.    x = torch.randn(5000, 10)    y = torch.randn(5000, 1)    dataset = TensorDataset(x, y)    sampler = DistributedSampler(dataset)    dataloader = DataLoader(dataset, sampler=sampler, batch_size=batch_size)    # 4. Define the training loop.    optimizer = optim.Adam(model.parameters(), lr=0.001)    loss_fn = nn.MSELoss()    for epoch in range(num_epochs):        sampler.set_epoch(epoch)        model.train()        total_loss = 0.0        for step, (xb, yb) in enumerate(dataloader):            xb, yb = xb.to(device), yb.to(device)            optimizer.zero_grad()            loss = loss_fn(model(xb), yb)            # Log loss to MLflow metric            mlflow.log_metric("loss", loss.item(), step=step)            loss.backward()            optimizer.step()            total_loss += loss.item() * xb.size(0)        mlflow.log_metric("total_loss", total_loss)        print(f"Total loss for epoch {epoch}: {total_loss}")    cleanup()
    
4.  Execute the distributed training by calling the distributed function with user-defined arguments.
    
    Python
    
        run_train.distributed(num_epochs=3, batch_size=1)
    
5.  When executed, an MLflow run link is be generated in the notebook cell output. Click the MLflow run link or find it in the **Experiment** panel to see the run results.
    

## Distributed execution details[​](#distributed-execution-details "Direct link to Distributed execution details")

Serverless GPU API consists of several key components:

*   Compute manager: Handles resource allocation and management
*   Runtime environment: Manages Python environments and dependencies
*   Launcher: Orchestrates job execution and monitoring

When running in distributed mode:

*   The function is serialized and distributed across the specified number of GPUs
*   Each GPU runs a copy of the function with the same parameters
*   The environment is synchronized across all GPUs
*   Results are collected and returned from all GPUs

The API supports popular parallel training libraries such as [Distributed Data Parallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel) (DDP), [Fully Sharded Data Parallel](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) (FSDP), [DeepSpeed](https://github.com/deepspeedai/DeepSpeed).

You can find more real distributed training scenarios using the various libraries in [notebook examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training).

## FAQs[​](#faqs "Direct link to FAQs")

### Where should the data loading code be placed?[​](#where-should-the-data-loading-code-be-placed "Direct link to Where should the data loading code be placed?")

When using the [Serverless GPU API](https://api-docs.databricks.com/python/serverless_gpu/index.html) for distributed training, move data loading code inside the [@distributed](https://api-docs.databricks.com/python/serverless_gpu/api/serverless_gpu.html#serverless_gpu.launcher.distributed) decorator. The dataset size can exceed the maximum size allowed by pickle, so it is recommended to generate the dataset inside the decorator, as shown below:

Python

    from serverless_gpu import distributed# this may cause pickle errordataset = get_dataset(file_path)@distributed(gpus=8, gpu_type='H100')def run_train():  # good practice  dataset = get_dataset(file_path)  ....

For file-based data stored in Unity Catalog volumes, use `UCVolumeDataset` from `serverless_gpu.data`, which streams files with local caching and partitions them across ranks and workers automatically. To checkpoint distributed training to a volume, use `UCVolumeWriter` and `UCVolumeReader`. See [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading) and [Model checkpointing](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability#model-checkpointing).

## Learn more[​](#learn-more "Direct link to Learn more")

For the API reference, refer to the [Serverless GPU Python API](https://api-docs.databricks.com/python/serverless_gpu/index.html) documentation.
