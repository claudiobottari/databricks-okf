---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5530cfca9b600d505f9bcb814745a79a977df89aba84d9ebcd103f2605c2c606
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodrunner-pickling-and-import-requirements
    - Import Requirements and HorovodRunner Pickling
    - HPAIR
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: HorovodRunner Pickling and Import Requirements
description: HorovodRunner pickles the training method on the driver and distributes it to Spark workers, requiring all import statements to be included inside the training method to avoid pickling errors.
tags:
  - python
  - spark
  - debugging
timestamp: "2026-06-19T19:05:48.009Z"
---

# HorovodRunner Pickling and Import Requirements

**HorovodRunner Pickling and Import Requirements** refers to the constraints on how Python imports and dependencies must be structured for distributed training with [HorovodRunner](/concepts/horovodrunner.md). Because HorovodRunner pickles the user’s training method on the driver and distributes it to Spark workers, any import statements needed by the method must be present inside the method itself to avoid serialization failures. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

> **Note:** Horovod and HorovodRunner are now deprecated. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## The Pickling Mechanism

HorovodRunner integrates Horovod with Spark’s barrier execution mode. It pickles the user-provided Python method on the driver and distributes the serialized object to Spark workers. The first executor collects the IP addresses of all task executors using `BarrierTaskContext` and triggers a Horovod job with `mpirun`. Each Python MPI process then loads the pickled user program, deserializes it, and runs it. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Because the training method is pickled on the driver and unpickled on remote workers, all objects referenced by the method—including imported modules—must be available in the serialized closure. If import statements are placed only at the top level of the notebook or script, they may not be included in the pickled representation. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Import Requirements

To avoid pickling errors, include **all import statements inside the Horovod training method itself**, as well as inside any user-defined functions called by that method. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

For example:

```python
def train():
    import tensorflow as tf   # Required: import inside the method
    import horovod.tensorflow as hvd
    hvd.init()
    # ... training logic ...

hr = HorovodRunner(np=2)
hr.run(train)
```

This pattern applies to any library used in the training logic, including TensorFlow, Keras, PyTorch, or custom modules. The same rule holds for helper functions defined outside the training method but called from within it: those helper functions must also contain their own import statements. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Common Errors and Solutions

A frequent error is that TensorFlow objects cannot be found or pickled. This occurs when the library import statements are not distributed to other executors—typically because the imports are placed only at the top of the notebook or script. The solution is to move the imports into the training method as described above. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Another common issue involves workspace files: if `np` is set to greater than 1 and the notebook imports from other relative files, HorovodRunner will not work. In such cases, consider using [horovod.spark](/concepts/horovodspark.md) instead. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Verifying Pickling Correctness

During development, test HorovodRunner in local mode first (by setting a negative `np` value, for example `HorovodRunner(np=-4)` on a multi‑GPU driver node) before running in distributed mode. This helps isolate pickling issues without involving multiple Spark executors. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The deprecated API for distributed deep learning with Horovod.
- Distributed Deep Learning with Horovod – General approach for migrating single-node code.
- [TorchDistributor](/concepts/torchdistributor.md) – Recommended replacement for PyTorch distributed training.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – Recommended replacement for TensorFlow distributed training.
- [Spark Barrier Execution Mode](/concepts/spark-barrier-execution-mode.md) – The underlying execution model used by HorovodRunner.
- Pickle Serialization – General concept of Python object serialization.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
