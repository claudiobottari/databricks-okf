---
title: "Get started: Serverless GPU compute with H100 GPUs | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-api-h100-starter
ingestedAt: "2026-06-18T08:08:41.822Z"
---

This notebook demonstrates how to use Databricks Serverless GPU compute with H100 accelerators. You'll learn how to connect to H100 GPUs and run distributed workloads using the `serverless_gpu` Python library.

The `serverless_gpu` library enables seamless execution of GPU workloads directly from Databricks notebooks. It provides decorators and runtime utilities for distributed GPU computing. To learn more, see the [Serverless GPU API documentation](https://api-docs.databricks.com/python/serverless_gpu/index.html).

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

To run this notebook, you need access to Databricks Serverless GPU compute with H100 accelerators.

1.  From the compute selector, select **Serverless GPU**.
2.  In the "Environment" tab on the right side, select **8xH100** for your accelerator. This option uses 8 H100 chips on a single node.
3.  Choose **AI v5** environment from the right panel that contains all the required libraries to run this notebook example.
4.  Click **Apply**.

## When to use H100 GPUs[​](#when-to-use-h100-gpus "Direct link to When to use H100 GPUs")

Compared to A10s, H100s offer larger floating-point operations per second (FLOPS) and high-bandwidth memory (HBM). Use H100s for large model **training** where high throughput and/or large GPU memory is needed.

## Verify GPU connection[​](#verify-gpu-connection "Direct link to Verify GPU connection")

Use the `nvidia-smi` command to confirm that you're connected to 8 H100 GPUs. This command displays GPU information including model, memory, and utilization.

Output

    Thu Jan 15 17:56:54 2026+-----------------------------------------------------------------------------------------+| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     ||-----------------------------------------+------------------------+----------------------+| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC || Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. ||                                         |                        |               MIG M. ||=========================================+========================+======================||   0  NVIDIA H100 80GB HBM3          On  |   00000000:53:00.0 Off |                    0 || N/A   26C    P0             70W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   1  NVIDIA H100 80GB HBM3          On  |   00000000:64:00.0 Off |                    0 || N/A   28C    P0             68W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   2  NVIDIA H100 80GB HBM3          On  |   00000000:75:00.0 Off |                    0 || N/A   26C    P0             71W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   3  NVIDIA H100 80GB HBM3          On  |   00000000:86:00.0 Off |                    0 || N/A   29C    P0             68W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   4  NVIDIA H100 80GB HBM3          On  |   00000000:97:00.0 Off |                    0 || N/A   27C    P0             67W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   5  NVIDIA H100 80GB HBM3          On  |   00000000:A8:00.0 Off |                    0 || N/A   26C    P0             67W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   6  NVIDIA H100 80GB HBM3          On  |   00000000:B9:00.0 Off |                    0 || N/A   26C    P0             69W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------+|   7  NVIDIA H100 80GB HBM3          On  |   00000000:CA:00.0 Off |                    0 || N/A   26C    P0             67W /  700W |       0MiB /  81559MiB |      0%      Default ||                                         |                        |             Disabled |+-----------------------------------------+------------------------+----------------------++-----------------------------------------------------------------------------------------+| Processes:                                                                              ||  GPU   GI   CI              PID   Type   Process name                        GPU Memory ||        ID   ID                                                               Usage      ||=========================================================================================||  No running processes found                                                             |+-----------------------------------------------------------------------------------------+

## Hello World example[​](#hello-world-example "Direct link to Hello World example")

This example demonstrates how to run a distributed function across multiple GPUs using the `@distributed` decorator.

The annotated function below runs on 8 processes, one per GPU on the node the notebook is attached to.

The function uses the `runtime` module to access the local and global GPU ranks.

Python

    from serverless_gpu import distributedfrom serverless_gpu import runtime as rt@distributed(    gpus=8,    gpu_type='h100',)def hello_world(name: str) -> list[int]:    if rt.get_local_rank() == 0:        print('hello world', name)    return rt.get_global_rank()result = hello_world.distributed('SGC')

Python

    assert result == [0, 1, 2, 3, 4, 5, 6, 7]

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [Serverless GPU API documentation](https://api-docs.databricks.com/python/serverless_gpu/index.html)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Get started: Serverless GPU compute with H100 GPUs
