---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 809396527f4903354f8bee4cbb0801dd183357e7e431ccce3b9ea3916361afb7
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorflow-deprecation-from-top-tier
    - TDFT
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: TensorFlow Deprecation from Top-Tier
description: Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries.
tags:
  - databricks
  - tensorflow
  - deprecation
timestamp: "2026-06-18T11:42:33.024Z"
---

# TensorFlow Deprecation from Top-Tier

**TensorFlow Deprecation from Top-Tier** refers to the removal of TensorFlow and `spark-tensorflow-connector` from the list of top-tier libraries in Databricks Runtime ML, beginning with Databricks Runtime 18.0 ML. This change affects the level of support, update cadence, and embedded optimizations these libraries receive from Databricks.

## Background

Databricks Runtime ML includes a variety of popular machine learning and deep learning libraries. A subset of these libraries are designated as **top-tier libraries**, for which Databricks provides a faster update cadence — updating to the latest package releases with each runtime release — as well as advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The full list of top-tier libraries prior to the deprecation included:
- datasets
- GraphFrames
- MLflow
- PyTorch
- Scikit-learn
- streaming
- TensorBoard
- transformers
- TensorFlow
- spark-tensorflow-connector

## Deprecation Event

Starting with Databricks Runtime 18.0 ML, **TensorFlow** and **spark-tensorflow-connector** are no longer top-tier libraries. This means they are removed from the subset of libraries that receive Databricks' fastest update cadence, advanced support, testing, and embedded optimizations. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Reasons for Deprecation

Databricks may remove a library from the top-tier list under several conditions, any of which could apply to TensorFlow:

- If the library has **no new commits in two months** and **no new releases in more than six months**. Databricks might add back the removed library when active maintenance resumes.
- If **usage of the library drops significantly**.
- If the library is **replaced** by new packages that fill major gaps.

These conditions are evaluated on a per-library basis as part of Databricks' library support policy for Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

When a library is planned for removal from top-tier status, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. A **deprecation warning** is added in the runtime release notes, indicating the library will be removed in the next major Databricks Runtime ML release.
2. A **notification** is displayed when importing the library, indicating the planned removal.
3. **Databricks documentation** that references the library is updated to indicate the planned removal.

For TensorFlow, these notifications appeared in the Databricks Runtime 18.0 ML release notes and related documentation.

## Impact

With the deprecation from top-tier status, TensorFlow and `spark-tensorflow-connector` no longer receive: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- **Fast update cadence** — Updates to the latest package releases with each runtime release are no longer guaranteed.
- **Advanced support** — Databricks' dedicated support for these libraries is reduced.
- **Testing** — These libraries are no longer part of Databricks' standard integration test suite for new runtime releases.
- **Embedded optimizations** — Performance optimizations specific to the Databricks Runtime environment are no longer provided.

However, the libraries remain available as pre-installed packages in Databricks Runtime ML for continued usage. They are simply removed from the top-tier designation.

## Continuing to Use TensorFlow

To continue using TensorFlow after its deprecation from top-tier status, you can: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- **Install the library manually** using `pip install tensorflow` or `%pip install tensorflow` within a notebook.
- **Use an earlier version** of Databricks Runtime ML that still includes TensorFlow as a top-tier library (versions prior to 18.0 ML).

## Related Concepts

- Library support policy — The overarching policy governing top-tier library designation and deprecation
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment where these libraries are distributed
- [MLflow](/concepts/mlflow.md) — Another top-tier library that remains in the supported set
- PyTorch — A top-tier library that continues to receive advanced support as an alternative to TensorFlow
- [TensorBoard](/concepts/tensorboard-on-databricks.md) — A top-tier library that remains supported for visualization
- Transformers — A top-tier library that remains supported for NLP workloads

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
