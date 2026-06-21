---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17a8876860aeaa796d14e1b0340560e61477cca126a0f86226826939bee39d1d
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodrunner-pickling-and-import-constraints
    - Import Constraints and HorovodRunner Pickling
    - HPAIC
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: HorovodRunner Pickling and Import Constraints
description: Requirement that all import statements must be included inside the Horovod training method (and any called functions) to avoid pickling errors during distribution to Spark executors.
tags:
  - python
  - distributed-training
  - debugging
timestamp: "2026-06-19T10:48:26.973Z"
---

---
title: "HorovodRunner Pickling and Import Constraints"
summary: "Explains how HorovodRunner pickles and distributes training methods to Spark workers, common import-related errors, and best practices for placing import statements to avoid pickling failures."
---

# HorovodRunner Pickling and Import Constraints

> **Deprecation note:** Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

**HorovodRunner Pickling and Import Constraints** refers to the series of requirements and common pitfalls that arise when using HorovodRunner to distribute deep learning training code across Spark workers. Because HorovodRunner relies on Python’s pickling mechanism to serialize the training method on the driver and deserialize it on each executor, import statements and module dependencies are often the source of runtime failures.

## How HorovodRunner Pickles Training Code

HorovodRunner takes a Python method that contains the training logic with Horovod hooks. The method is **pickled on the driver** and then distributed to Spark workers via Spark’s barrier execution mode. Each Python MPI process that is launched by `mpirun` loads the pickled user program, deserializes it, and runs it. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Because the pickling happens at the driver and the deserialization occurs on the executors, any object that is not serializable or any reference that is not available in the remote process’s module namespace will cause an error.

## Common Import-Related Errors

A frequent error when using HorovodRunner is that TensorFlow objects (or other deep learning framework objects) **cannot be found or pickled**. This happens when library import statements are placed only at the top of the notebook cell or in a module that is not available on the executor’s Python path. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

The root cause is that the pickled method does not carry the module’s import context. When the serialized code is deserialized on a remote worker, the worker’s Python environment may not have the same module imported, leading to `NameError` or `AttributeError` for objects like `tf.Session`, `tf.keras.Model`, or PyTorch tensors.

## Mitigation: Placement of Import Statements

To avoid pickling failures, **all import statements must be included inside the Horovod training method** (i.e., the function passed to `HorovodRunner.run()`). Additionally, if the training method calls any user‑defined helper functions, those functions must also contain the necessary import statements at their top. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

The recommended pattern is:

```python
def train():
    import tensorflow as tf    # <-- inside the method
    import horovod.tensorflow as hvd
    # ... rest of training code

hr = HorovodRunner(np=2)
hr.run(train)
```

This ensures that each MPI process that deserializes the function also imports the required libraries before executing any code that references them.

## Additional Considerations

### Workspace Files and Relative Imports

HorovodRunner does not work when `np` is set to greater than 1 **and** the notebook imports from other relative workspace files. In such cases, consider using `horovod.spark` instead. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Network Environment Variables

If errors like `WARNING: Open MPI accepted a TCP connection from what appears to be another Open MPI process...` occur, it indicates a network communication issue among nodes. The training code should set environment variables to use the primary network interface:

```python
import os
os.environ["OMPI_MCA_btl_tcp_if_include"] = "eth0"
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [Distributed deep learning on Databricks](/concepts/distributed-deep-learning-on-databricks.md) – Overview of distributed training options.
- [TorchDistributor](/concepts/torchdistributor.md) – Recommended alternative for PyTorch distributed training.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – Recommended alternative for TensorFlow distributed training.
- [Horovod](/concepts/horovod.md) – The underlying distributed training framework.
- [Spark Barrier Execution Mode](/concepts/spark-barrier-execution-mode.md) – The Spark feature used by HorovodRunner.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
