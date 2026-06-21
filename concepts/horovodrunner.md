---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca3076fc6cd00e10b116ffa69fe71dd4c7137b25ca2d784ed23b326aba8fb8fd
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
    - horovod-databricks-on-aws.md
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - horovodrunner
    - Horovod Runner
    - HorovodRunner API
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
    - file: horovod-databricks-on-aws.md
      start: 3
      end: 5
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 3
      end: 5
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 12
      end: 14
    - file: horovod-databricks-on-aws.md
      start: 9
      end: 11
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 18
      end: 23
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 25
      end: 30
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 32
      end: 33
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 35
      end: 37
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 53
      end: 55
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 57
      end: 58
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 60
      end: 61
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 62
      end: 68
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 70
      end: 72
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 76
      end: 80
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 82
      end: 86
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 104
      end: 106
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 107
      end: 109
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
      start: 110
      end: 114
    - file: horovod-databricks-on-aws.md
      start: 17
      end: 19
    - file: horovod-databricks-on-aws.md
      start: 19
      end: 31
    - file: horovod-databricks-on-aws.md
      start: 37
      end: 40
    - file: horovod-databricks-on-aws.md
      start: 41
      end: 45
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: HorovodRunner
description: A Databricks API for distributed deep learning using Horovod that allows adapting single-node PyTorch code to distributed training with minimal changes.
tags:
  - distributed-training
  - databricks
  - deep-learning
timestamp: "2026-06-19T21:58:57.095Z"
---

# HorovodRunner

**HorovodRunner** is a general API for running distributed deep learning training workloads on Databricks using the [Horovod](https://github.com/horovod/horovod) framework. It provides a method to launch Horovod training jobs as Spark jobs by integrating Horovod with Spark's barrier execution mode, offering higher stability for long-running deep learning jobs. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

> **Deprecation notice**: Horovod and HorovodRunner are now deprecated. Releases after Databricks Runtime 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovod-databricks-on-aws.md#L3-L5, horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L3-L5]

## Overview

HorovodRunner takes a Python method containing deep learning training code with Horovod hooks. It pickles the method on the driver and distributes it to Spark workers. A Horovod MPI job is embedded as a Spark job using barrier execution mode. The first executor collects IP addresses of all task executors using `BarrierTaskContext` and triggers a Horovod job using `mpirun`. Each Python MPI process loads the pickled user program, deserializes it, and runs it. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L12-L14]

![HorovodRunner architecture diagram showing the flow from driver to Spark workers](https://docs.databricks.com/aws/en/assets/images/horovod-runner-0638a234281824845e9162f2cca8d8a9.png)^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Requirements

HorovodRunner requires **Databricks Runtime ML** for the pre-installed Horovod package. ^[horovod-databricks-on-aws.md#L9-L11]

## Distributed training with HorovodRunner

The general approach to developing a distributed training program using HorovodRunner is:

1. Create a `HorovodRunner` instance initialized with the number of nodes.
2. Define a Horovod training method according to [Horovod usage guidelines](https://github.com/horovod/horovod#usage), making sure to add any import statements inside the method.
3. Pass the training method to the `HorovodRunner` instance. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L18-L23]

Example:

```python
hr = HorovodRunner(np=2)
def train():
    import tensorflow as tf
    hvd.init()
hr.run(train)
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L25-L30]

To run HorovodRunner on the driver only with `n` subprocesses, use `hr = HorovodRunner(np=-n)`. For example, if there are 4 GPUs on the driver node, you can choose `n` up to `4`. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L32-L33]

### Common Error: Pickling TensorFlow Objects

A common error is that TensorFlow objects cannot be found or pickled. This happens when library import statements are not distributed to other executors. To avoid this issue, include all import statements (for example, `import tensorflow as tf`) *both* at the top of the Horovod training method and inside any other user-defined functions called in the Horovod training method. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L35-L37]

## Development workflow

To migrate single-node deep learning code to distributed training with HorovodRunner, follow the recommended three-step workflow: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L53-L55]

### Step 1: Prepare single node code

Prepare and test the single node code with TensorFlow, Keras, or PyTorch. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L57-L58]

### Step 2: Migrate to Horovod

Follow [Horovod usage instructions](https://github.com/horovod/horovod#usage) to migrate the code with Horovod and test it on the driver: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L60-L61]

1. **Add `hvd.init()`** to initialize Horovod.
2. **Pin a server GPU** to be used by this process using `config.gpu_options.visible_device_list`. With the typical setup of one GPU per process, this can be set to local rank. The first process on the server will be allocated the first GPU, second process will be allocated the second GPU, and so forth.
3. **Include a shard of the dataset.** This dataset operator allows each worker to read a unique subset, which is useful for distributed training.
4. **Scale the learning rate** by the number of workers. The effective batch size in synchronous distributed training is scaled by the number of workers. Increasing the learning rate compensates for the increased batch size.
5. **Wrap the optimizer** in `hvd.DistributedOptimizer`. The distributed optimizer delegates gradient computation to the original optimizer, averages gradients using allreduce or allgather, and then applies the averaged gradients.
6. **Add `hvd.BroadcastGlobalVariablesHook(0)`** to broadcast initial variable states from rank 0 to all other processes. This ensures consistent initialization of all workers when training is started with random weights or restored from a checkpoint. If not using `MonitoredTrainingSession`, execute `hvd.broadcast_global_variables` after global variables have been initialized.
7. **Modify your code** to save checkpoints only on worker 0 to prevent other workers from corrupting them. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L62-L68]

### Step 3: Migrate to HorovodRunner

HorovodRunner runs the Horovod training job by invoking a Python function. You must wrap the main training procedure into a single Python function. Then you can test HorovodRunner in local mode and distributed mode. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L70-L72]

## Record Horovod training with Horovod Timeline

Horovod has the ability to record its activity timeline, called [Horovod Timeline](https://horovod.readthedocs.io/en/latest/timeline.html). However, Horovod Timeline has a significant performance impact — Inception3 throughput can decrease by approximately 40% when enabled. To speed up HorovodRunner jobs, do not use Horovod Timeline. You cannot view the timeline while training is in progress. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L76-L80]

To record a Horovod Timeline, set the `HOROVOD_TIMELINE` environment variable to the location where you want to save the timeline file. Databricks recommends using a location on shared storage such as DBFS local file APIs:

```python
timeline_dir = "/dbfs/ml/horovod-timeline/%s" % uuid.uuid4()
os.makedirs(timeline_dir)
os.environ['HOROVOD_TIMELINE'] = timeline_dir + "/horovod_timeline.json"
hr = HorovodRunner(np=4)
hr.run(run_training_horovod, params=params)
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L82-L86]

## Limitations

- When working with workspace files, HorovodRunner will not work if `np` is set to greater than 1 and the notebook imports from other relative files. Consider using `horovod.spark` instead. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L104-L106]
- Errors like `WARNING: Open MPI accepted a TCP connection from what appears to be another Open MPI process but cannot find a corresponding process entry for that peer` indicate a problem with network communication among nodes in your cluster. To resolve this, add the following snippet in your training code: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L107-L109]

```python
import os
os.environ["OMPI_MCA_btl_tcp_if_include"]="eth0"
os.environ["NCCL_SOCKET_IFNAME"]="eth0"
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md#L110-L114]

## Installing a different version of Horovod

To upgrade or downgrade Horovod from the pre-installed version in your ML cluster, you must recompile Horovod: ^[horovod-databricks-on-aws.md#L17-L19]

1. Uninstall the current version: `%pip uninstall -y horovod`
2. If using a GPU-accelerated cluster, install CUDA development libraries required to compile Horovod.
3. Download the desired version of Horovod's source code and compile with the appropriate flags.
4. Use `%pip` to reinstall Horovod by specifying the Python wheel path. ^[horovod-databricks-on-aws.md#L19-L31]

## Troubleshooting

**Problem**: Importing `horovod.{torch|tensorflow}` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built`

**Solution**: This error typically occurs when updating an environment goes wrong. It indicates Horovod was installed before a required library (PyTorch or TensorFlow). Since Horovod is compiled during installation, `horovod.{torch|tensorflow}` will not get compiled if those packages aren't present. To fix: ^[horovod-databricks-on-aws.md#L37-L40]

1. Verify you are on a Databricks Runtime ML cluster.
2. Ensure the PyTorch or TensorFlow package is already installed.
3. Uninstall Horovod (`%pip uninstall -y horovod`).
4. Install `cmake` (`%pip install cmake`).
5. Reinstall `horovod`. ^[horovod-databricks-on-aws.md#L41-L45]

## Related concepts

- [Horovod](/concepts/horovod.md) — The distributed training framework that HorovodRunner builds upon
- [TorchDistributor](/concepts/torchdistributor.md) — The recommended replacement for distributed PyTorch training
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) — General concept of scaling ML training across multiple nodes
- [Barrier execution mode](/concepts/spark-barrier-execution-mode.md) — Spark execution mode used by HorovodRunner
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime that includes pre-installed Horovod
- MNIST — Common dataset used in HorovodRunner example notebooks
- DBFS — Shared storage location for Horovod Timeline files

## Examples

The following examples demonstrate how to migrate single-node deep learning programs to distributed training with HorovodRunner using the MNIST dataset:

- [Deep learning using TensorFlow with HorovodRunner for MNIST](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-tensorflow-keras) ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]
- [Adapt single node PyTorch to distributed deep learning](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-pytorch) ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
- horovod-databricks-on-aws.md
- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
2. [horovod-databricks-on-aws.md:3-5](/references/horovod-databricks-on-aws-49662285.md)
3. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:3-5](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
4. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:12-14](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
5. [horovod-databricks-on-aws.md:9-11](/references/horovod-databricks-on-aws-49662285.md)
6. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:18-23](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
7. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:25-30](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
8. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:32-33](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
9. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:35-37](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
10. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:53-55](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
11. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:57-58](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
12. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:60-61](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
13. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:62-68](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
14. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:70-72](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
15. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:76-80](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
16. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:82-86](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
17. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:104-106](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
18. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:107-109](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
19. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md:110-114](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
20. [horovod-databricks-on-aws.md:17-19](/references/horovod-databricks-on-aws-49662285.md)
21. [horovod-databricks-on-aws.md:19-31](/references/horovod-databricks-on-aws-49662285.md)
22. [horovod-databricks-on-aws.md:37-40](/references/horovod-databricks-on-aws-49662285.md)
23. [horovod-databricks-on-aws.md:41-45](/references/horovod-databricks-on-aws-49662285.md)
24. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
25. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
