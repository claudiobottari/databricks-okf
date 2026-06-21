---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e944c8e92a07b4052b311a65dba056d338b0177fa335075d89dcc1fdcac741d
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-custom-installation-on-databricks
    - HCIOD
  citations:
    - file: horovod-databricks-on-aws.md
title: Horovod Custom Installation on Databricks
description: Process to install a different version of Horovod on Databricks Runtime ML by uninstalling, recompiling from source, and reinstalling as a wheel.
tags:
  - installation
  - databricks
  - devops
timestamp: "2026-06-19T19:05:24.097Z"
---

# Horovod Custom Installation on Databricks

**Horovod** is a distributed training framework for TensorFlow, Keras, and PyTorch. Databricks provides pre-installed Horovod on Databricks Runtime ML clusters, along with the **HorovodRunner** API and the `horovod.spark` package. However, Horovod and HorovodRunner are now **deprecated** — releases after Databricks Runtime 15.4 LTS ML will not include Horovod pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovod-databricks-on-aws.md]

## Prerequisites

- A cluster running **Databricks Runtime ML** (not the standard runtime).
- For GPU-accelerated clusters: CUDA development libraries must be installed to recompile Horovod with GPU support. ^[horovod-databricks-on-aws.md]

## Steps to Install a Custom Version of Horovod

If you need a version of Horovod different from the one pre-installed on your ML cluster, you must recompile Horovod from source. The following steps cover both CPU and GPU clusters.

### 1. Uninstall the Current Horovod

Use `%pip` in a notebook cell to remove the pre-installed package:

```bash
%pip uninstall -y horovod
```

^[horovod-databricks-on-aws.md]

### 2. Install CUDA Development Libraries (GPU Clusters Only)

On a GPU‑accelerated cluster, install the CUDA toolkits required for compilation. The commands below install specific versions to ensure compatibility:

```bash
%sh
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
dpkg -i ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
apt-get update
apt-get install --allow-downgrades --no-install-recommends -y \
  cuda-nvml-dev-11-0=11.0.167-1 \
  cuda-nvcc-11-0=11.0.221-1 \
  cuda-cudart-dev-11-0=11.0.221-1 \
  cuda-libraries-dev-11-0=11.0.3-1 \
  libnccl-dev=2.11.4-1+cuda11.5 \
  libcusparse-dev-11-0=11.1.1.245-1
```

^[horovod-databricks-on-aws.md]

### 3. Download and Compile Horovod from Source

Clone the desired version from GitHub. Replace `v0.21.3` with the version you need. The compilation flags enable support for MPI, TensorFlow, and PyTorch. Remove flags for frameworks you do not use.

**CPU cluster** – omit the CUDA‑related flags:

```bash
%sh
HOROVOD_VERSION=v0.21.3  # Change as necessary
git clone --recursive https://github.com/horovod/horovod.git --branch ${HOROVOD_VERSION}
cd horovod
rm -rf build/ dist/
HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 \
  sudo /databricks/python3/bin/python setup.py bdist_wheel
readlink -f dist/horovod-*.whl
```

**GPU cluster** – the same commands apply; the previously installed CUDA libraries will be used automatically during compilation.

^[horovod-databricks-on-aws.md]

> **Note**: For Databricks Runtime 8.4 ML and below, replace `/databricks/python3/bin/python` with `/databricks/conda/envs/databricks-ml/bin/python`.

### 4. Reinstall Horovod from the Built Wheel

Use `%pip` with the wheel path printed by the previous `readlink` command. The example uses version 0.21.3:

```bash
%pip install --no-cache-dir /databricks/driver/horovod/dist/horovod-0.21.3-cp38-cp38-linux_x86_64.whl
```

^[horovod-databricks-on-aws.md]

## Troubleshooting

**Problem**: Importing `horovod.torch` or `horovod.tensorflow` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built`.  
**Solution**: This occurs when Horovod was installed **before** the required framework (PyTorch or TensorFlow) was present. Because Horovod is compiled at install time, the framework‑specific extension is skipped if the framework is missing. To fix:

1. Verify the cluster is running **Databricks Runtime ML**.
2. Ensure PyTorch or TensorFlow is already installed.
3. Uninstall Horovod: `%pip uninstall -y horovod`.
4. Install `cmake`: `%pip install cmake`.
5. Reinstall Horovod following steps 3 and 4 above.

^[horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The deprecated API for distributed deep learning with Horovod on Databricks.
- [TorchDistributor](/concepts/torchdistributor.md) – The recommended alternative for distributed PyTorch training.
- [Distributed Training with TensorFlow (tf.distribute.Strategy)](/concepts/distributed-training-with-tensorflow-2.md) – The recommended alternative for distributed TensorFlow training.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The cluster type required for pre‑installed Horovod and custom compilation.

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
