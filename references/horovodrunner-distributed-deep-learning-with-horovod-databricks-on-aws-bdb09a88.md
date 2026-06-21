---
title: "HorovodRunner: distributed deep learning with Horovod | Databricks on AWS"
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner
ingestedAt: "2026-06-18T08:02:58.505Z"
---

important

Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow.

Learn how to perform distributed training of machine learning models using HorovodRunner to launch Horovod training jobs as Spark jobs on Databricks.

## What is HorovodRunner?[​](#what-is-horovodrunner "Direct link to What is HorovodRunner?")

HorovodRunner is a general API to run distributed deep learning workloads on Databricks using the [Horovod](https://github.com/horovod/horovod) framework. By integrating Horovod with Spark's [barrier mode](https://issues.apache.org/jira/browse/SPARK-24374), Databricks is able to provide higher stability for long-running deep learning training jobs on Spark. HorovodRunner takes a Python method that contains deep learning training code with Horovod hooks. HorovodRunner pickles the method on the driver and distributes it to Spark workers. A Horovod MPI job is embedded as a Spark job using the barrier execution mode. The first executor collects the IP addresses of all task executors using `BarrierTaskContext` and triggers a Horovod job using `mpirun`. Each Python MPI process loads the pickled user program, deserializes it, and runs it.

![HorovodRunner](https://docs.databricks.com/aws/en/assets/images/horovod-runner-0638a234281824845e9162f2cca8d8a9.png)

## Distributed training with HorovodRunner[​](#distributed-training-with-horovodrunner "Direct link to Distributed training with HorovodRunner")

HorovodRunner lets you launch Horovod training jobs as Spark jobs. The HorovodRunner API supports the methods shown in the table. For details, see the [HorovodRunner API documentation](https://databricks.github.io/spark-deep-learning/#sparkdl.HorovodRunner).

The general approach to developing a distributed training program using HorovodRunner is:

1.  Create a `HorovodRunner` instance initialized with the number of nodes.
2.  Define a Horovod training method according to the methods described in [Horovod usage](https://github.com/horovod/horovod#usage), making sure to add any import statements inside the method.
3.  Pass the training method to the `HorovodRunner` instance.

For example:

Python

    hr = HorovodRunner(np=2)def train():  import tensorflow as tf  hvd.init()hr.run(train)

To run HorovodRunner on the driver only with `n` subprocesses, use `hr = HorovodRunner(np=-n)`. For example, if there are 4 GPUs on the driver node, you can choose `n` up to `4`. For details about the parameter `np`, see the [HorovodRunner API documentation](https://databricks.github.io/spark-deep-learning/#api-documentation). For details about how to pin one GPU per subprocess, see the [Horovod usage guide](https://github.com/horovod/horovod#usage).

A common error is that TensorFlow objects cannot be found or pickled. This happens when the library import statements are not distributed to other executors. To avoid this issue, include all import statements (for example, `import tensorflow as tf`) _both_ at the top of the Horovod training method and inside any other user-defined functions called in the Horovod training method.

## Record Horovod training with Horovod Timeline[​](#record-horovod-training-with-horovod-timeline "Direct link to record-horovod-training-with-horovod-timeline")

Horovod has the ability to record the timeline of its activity, called [Horovod Timeline](https://horovod.readthedocs.io/en/latest/timeline.html).

important

Horovod Timeline has a significant impact on performance. Inception3 throughput can decrease by ~40% when Horovod Timeline is enabled. To speed up HorovodRunner jobs, do not use Horovod Timeline.

You cannot view the Horovod Timeline while training is in progress.

To record a Horovod Timeline, set the `HOROVOD_TIMELINE` environment variable to the location where you want to save the timeline file. Databricks recommends using a location on shared storage so that the timeline file can be easily retrieved. For example, you can use [DBFS local file APIs](https://docs.databricks.com/aws/en/dbfs/) as shown:

Python

    timeline_dir = "/dbfs/ml/horovod-timeline/%s" % uuid.uuid4()os.makedirs(timeline_dir)os.environ['HOROVOD_TIMELINE'] = timeline_dir + "/horovod_timeline.json"hr = HorovodRunner(np=4)hr.run(run_training_horovod, params=params)

Then, add timeline specific code to the beginning and end of the training function. The following example notebook includes example code that you can use as a workaround to view training progress.

#### Horovod timeline example notebook

To download the timeline file, use the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/), and then use the Chrome browser's `chrome://tracing` facility to view it. For example:

![Horovod timeline](https://docs.databricks.com/aws/en/assets/images/mnist-timeline-2f43586369684bc8573ceae09687437a.png)

## Development workflow[​](#development-workflow "Direct link to development-workflow")

These are the general steps in migrating single node deep learning code to distributed training. The [Examples: Migrate to distributed deep learning with HorovodRunner](#examples) in this section illustrate these steps.

1.  **Prepare single node code:** Prepare and test the single node code with TensorFlow, Keras, or PyTorch.
2.  **Migrate to Horovod:** Follow the instructions from [Horovod usage](https://github.com/horovod/horovod#usage) to migrate the code with Horovod and test it on the driver:
    1.  Add `hvd.init()` to initialize Horovod.
    2.  Pin a server GPU to be used by this process using `config.gpu_options.visible_device_list`. With the typical setup of one GPU per process, this can be set to local rank. In that case, the first process on the server will be allocated the first GPU, second process will be allocated the second GPU and so forth.
    3.  Include a shard of the dataset. This dataset operator is very useful when running distributed training, as it allows each worker to read a unique subset.
    4.  Scale the learning rate by number of workers. The effective batch size in synchronous distributed training is scaled by the number of workers. Increasing the learning rate compensates for the increased batch size.
    5.  Wrap the optimizer in `hvd.DistributedOptimizer`. The distributed optimizer delegates gradient computation to the original optimizer, averages gradients using allreduce or allgather, and then applies the averaged gradients.
    6.  Add `hvd.BroadcastGlobalVariablesHook(0)` to broadcast initial variable states from rank 0 to all other processes. This is necessary to ensure consistent initialization of all workers when training is started with random weights or restored from a checkpoint. Alternatively, if you're not using `MonitoredTrainingSession`, you can execute the `hvd.broadcast_global_variables` operation after global variables have been initialized.
    7.  Modify your code to save checkpoints only on worker 0 to prevent other workers from corrupting them.
3.  **Migrate to HorovodRunner:** HorovodRunner runs the Horovod training job by invoking a Python function. You must wrap the main training procedure into a single Python function. Then you can test HorovodRunner in local mode and distributed mode.

## Update the deep learning libraries[​](#update-the-deep-learning-libraries "Direct link to Update the deep learning libraries")

If you upgrade or downgrade TensorFlow, Keras, or PyTorch, you must reinstall Horovod so that it is compiled against the newly installed library. For example, if you want to upgrade TensorFlow, Databricks recommends using the init script from the [TensorFlow installation instructions](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow) and appending the following TensorFlow specific Horovod installation code to the end of it. See [Horovod installation instructions](https://github.com/horovod/horovod#install) to work with different combinations, such as upgrading or downgrading PyTorch and other libraries.

Bash

    add-apt-repository -y ppa:ubuntu-toolchain-r/testapt update# Using the same compiler that TensorFlow was built to compile Horovodapt install g++-7 -yupdate-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_CUDA_HOME=/usr/local/cuda pip install horovod==0.18.1 --force-reinstall --no-deps --no-cache-dir

## Examples: Migrate to distributed deep learning with HorovodRunner[​](#examples-migrate-to-distributed-deep-learning-with-horovodrunner "Direct link to examples-migrate-to-distributed-deep-learning-with-horovodrunner")

The following examples, based on the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset, demonstrate how to migrate a single-node deep learning program to distributed deep learning with HorovodRunner.

*   [Deep learning using TensorFlow with HorovodRunner for MNIST](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-tensorflow-keras)
*   [Adapt single node PyTorch to distributed deep learning](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-pytorch)

## Limitations[​](#limitations "Direct link to Limitations")

*   When working with workspace files, HorovodRunner will not work if `np` is set to greater than 1 and the notebook imports from other relative files. Consider using [horovod.spark](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark) instead of `HorovodRunner`.
*   If you come across errors like `WARNING: Open MPI accepted a TCP connection from what appears to be a another Open MPI process but cannot find a corresponding process entry for that peer`, this indicates a problem with network communication among nodes in your cluster. To resolve this error, add the following snippet in your training code to use the primary network interface.

Python

    import osos.environ["OMPI_MCA_btl_tcp_if_include"]="eth0"os.environ["NCCL_SOCKET_IFNAME"]="eth0"
