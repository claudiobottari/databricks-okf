---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5afcea0e8ee4abc49d2ead3aca16369c0c89223876a2541d8d4d2edc268a2bf4
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyarrow-compatibility-constraint-for-horovodspark
    - PCCFH
    - pyarrow-compatibility-constraint-with-horovodspark
    - PCCWH
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: PyArrow Compatibility Constraint for horovod.spark
description: horovod.spark does not support pyarrow versions 11.0 and above, requiring manual installation of a compatible version on Databricks Runtime 15.0 ML and above.
tags:
  - compatibility
  - pyarrow
  - horovod
timestamp: "2026-06-19T10:48:41.856Z"
---

# PyArrow Compatibility Constraint for horovod.spark

**PyArrow Compatibility Constraint for horovod.spark** refers to the requirement that the `horovod.spark` package must be used with a version of PyArrow below 11.0. Versions 11.0 and above are not supported and cause runtime failures. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Cause

The incompatibility is a known issue tracked in the Horovod project (see [GitHub Issue #3829](https://github.com/horovod/horovod/issues/3829)). PyArrow versions 11.0 and later introduced changes that break the internals of `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Impact on Databricks Runtime

Databricks Runtime 15.0 ML includes PyArrow version 14.0.1 by default, which is incompatible with `horovod.spark`. Users of Databricks Runtime 15.0 ML or any later runtime that ships PyArrow 11.0+ must manually downgrade PyArrow to a version below 11.0 before using `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Resolution

Manually install a compatible version of PyArrow, such as version 10.0.1 or another release below 11.0. For example:

```
pip install pyarrow==10.0.1
```

This step must be performed in the cluster’s library configuration or within the notebook before importing `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## General Dependency Caveat

Databricks installs the `horovod` package together with its dependencies. If you upgrade or downgrade any of those dependencies — including PyArrow — there may be further compatibility issues. Always test the resulting environment thoroughly. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [horovod.spark](/concepts/horovodspark.md) – The distributed deep learning estimator API for Spark.
- [HorovodRunner](/concepts/horovodrunner.md) – Deprecated alternative to `horovod.spark`.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The ML-focused runtime version that includes `horovod`.
- [TorchDistributor](/concepts/torchdistributor.md) – Recommended replacement for distributed PyTorch training on Databricks.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – Recommended replacement for distributed TensorFlow training on Databricks.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
