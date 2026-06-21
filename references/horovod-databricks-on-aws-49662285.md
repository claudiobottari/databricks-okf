---
title: Horovod | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod
ingestedAt: "2026-06-18T08:02:56.572Z"
---

important

Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow.

[Horovod](https://github.com/horovod/horovod) is a distributed training framework for TensorFlow, Keras, and PyTorch. Databricks supports distributed deep learning training using HorovodRunner and the `horovod.spark` package. For Spark ML pipeline applications using Keras or PyTorch, you can use the `horovod.spark` [estimator API](https://spark.apache.org/docs/latest/ml-pipeline.html#estimators).

## Requirements[​](#requirements "Direct link to Requirements")

Databricks Runtime ML.

## Use Horovod[​](#use-horovod "Direct link to Use Horovod")

The following articles provide general information about distributed deep learning with Horovod and example notebooks illustrating how to use HorovodRunner and the `horovod.spark` package.

*   [HorovodRunner: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner)
*   [HorovodRunner examples](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner-examples)
*   [`horovod.spark`: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark)

## Install a different version of Horovod[​](#install-a-different-version-of-horovod "Direct link to Install a different version of Horovod")

To upgrade or downgrade Horovod from the pre-installed version in your ML cluster, you must recompile Horovod by following these steps:

1.  Uninstall the current version of Horovod.

    %pip uninstall -y horovod

1.  If using a GPU-accelerated cluster, install CUDA development libraries required to compile Horovod. To ensure compatibility, leave the package versions unchanged.

    %shwget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pinmv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pubadd-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.debdpkg -i ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.debapt-get updateapt-get install --allow-downgrades --no-install-recommends -y \cuda-nvml-dev-11-0=11.0.167-1 \cuda-nvcc-11-0=11.0.221-1 \cuda-cudart-dev-11-0=11.0.221-1 \cuda-libraries-dev-11-0=11.0.3-1 \libnccl-dev=2.11.4-1+cuda11.5\libcusparse-dev-11-0=11.1.1.245-1

1.  Download the desired version of Horovod's source code and compile with the appropriate flags. If you don't need any of the extensions (such as `HOROVOD_WITH_PYTORCH`), you can remove those flags.

*   CPU
*   GPU

    %shHOROVOD_VERSION=v0.21.3 # Change as necessarygit clone --recursive https://github.com/horovod/horovod.git --branch ${HOROVOD_VERSION}cd horovodrm -rf build/ dist/HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 \# For Databricks Runtime 8.4 ML and below, replace with /databricks/conda/envs/databricks-ml/bin/pythonsudo /databricks/python3/bin/python setup.py bdist_wheelreadlink -f dist/horovod-*.whl

1.  Use `%pip` to reinstall Horovod by specifying the Python wheel path from the previous command's output. `0.21.3` is shown in this example.

    %pip install --no-cache-dir /databricks/driver/horovod/dist/horovod-0.21.3-cp38-cp38-linux_x86_64.whl

## Troubleshoot Horovod installation[​](#troubleshoot-horovod-installation "Direct link to Troubleshoot Horovod installation")

**Problem**: Importing `horovod.{torch|tensorflow}` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built`

**Solution**: Horovod comes pre-installed on Databricks Runtime ML, so this error typically occurs if updating an environment goes wrong. The error indicates that Horovod was installed before a required library (PyTorch or TensorFlow). Since Horovod is compiled during installation, `horovod.{torch|tensorflow}` will not get compiled if those packages aren't present during the installation of Horovod. To fix the issue, follow these steps:

1.  Verify that you are on a Databricks Runtime ML cluster.
2.  Ensure that the PyTorch or TensorFlow package is already installed.
3.  Uninstall Horovod (`%pip uninstall -y horovod`).
4.  Install `cmake` (`%pip install cmake`).
5.  Reinstall `horovod`.
