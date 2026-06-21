---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1be2a129aad0fb450e6601caa5428a48372de56d569701485519093e788fb07e
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-installation-on-databricks
    - HIOD
  citations:
    - file: horovod-databricks-on-aws.md
title: Horovod Installation on Databricks
description: The process of upgrading or downgrading Horovod on Databricks Runtime ML clusters, requiring manual uninstallation, recompilation with CUDA libraries, and wheel installation.
tags:
  - databricks
  - installation
  - horovod
timestamp: "2026-06-19T10:47:58.647Z"
---

# Horovod Installation on Databricks

**Horovod** is a distributed training framework for TensorFlow, Keras, and PyTorch. Databricks supports distributed deep learning using HorovodRunner and the `horovod.spark` package. However, Horovod and HorovodRunner are now deprecated; releases after Databricks Runtime 15.4 LTS ML will not have Horovod pre-installed. For distributed training, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovod-databricks-on-aws.md]

## Requirements

Using Horovod on Databricks requires [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). ^[horovod-databricks-on-aws.md]

## Installing or Upgrading Horovod

Horovod comes pre-installed on Databricks Runtime ML. To install a different version (upgrade or downgrade), you must manually recompile Horovod. ^[horovod-databricks-on-aws.md]

### Step 1: Uninstall the current version

```bash
%pip uninstall -y horovod
```

^[horovod-databricks-on-aws.md]

### Step 2: Install CUDA development libraries (GPU clusters only)

If using a GPU-accelerated cluster, install the required CUDA libraries to compile Horovod. Leave package versions unchanged for compatibility. ^[horovod-databricks-on-aws.md]

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

### Step 3: Download and compile the desired Horovod version

Clone the Horovod source code at the desired tag and compile with the appropriate flags. Remove flags for extensions you do not need (e.g., `HOROVOD_WITH_PYTORCH`). ^[horovod-databricks-on-aws.md]

**CPU version:**
```bash
%sh
HOROVOD_VERSION=v0.21.3 # Change as necessary
git clone --recursive https://github.com/horovod/horovod.git --branch ${HOROVOD_VERSION}
cd horovod
rm -rf build/ dist/
HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 \
  # For Databricks Runtime 8.4 ML and below, replace with /databricks/conda/envs/databricks-ml/bin/python
  sudo /databricks/python3/bin/python setup.py bdist_wheel
readlink -f dist/horovod-*.whl
```

^[horovod-databricks-on-aws.md]

**GPU version:** Same commands as CPU version, but ensure the GPU extensions are enabled via the environment variables shown above (e.g., `HOROVOD_WITH_TENSORFLOW=1`, `HOROVOD_WITH_PYTORCH=1`). ^[horovod-databricks-on-aws.md]

### Step 4: Reinstall Horovod from the built wheel

Use the wheel path from the previous step. The example below uses version 0.21.3. ^[horovod-databricks-on-aws.md]

```bash
%pip install --no-cache-dir /databricks/driver/horovod/dist/horovod-0.21.3-cp38-cp38-linux_x86_64.whl
```

^[horovod-databricks-on-aws.md]

## Troubleshooting

**Problem:** Importing `horovod.{torch|tensorflow}` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built` ^[horovod-databricks-on-aws.md]

**Solution:** This error usually indicates that Horovod was installed before the required deep learning library (PyTorch or TensorFlow). Horovod must be compiled *after* the library is present. ^[horovod-databricks-on-aws.md]

To fix:

1. Verify you are on a Databricks Runtime ML cluster.
2. Ensure that the PyTorch or TensorFlow package is already installed.
3. Uninstall Horovod: `%pip uninstall -y horovod`.
4. Install `cmake`: `%pip install cmake`.
5. Reinstall Horovod following the steps above. ^[horovod-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The recommended alternative for PyTorch distributed training.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – The recommended alternative for TensorFlow distributed training.
- [HorovodRunner](/concepts/horovodrunner.md) – The Databricks API for running Horovod jobs (deprecated).
- [horovod.spark](/concepts/horovodspark.md) – Spark ML integration with Horovod (deprecated).
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The required runtime for Horovod.

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
