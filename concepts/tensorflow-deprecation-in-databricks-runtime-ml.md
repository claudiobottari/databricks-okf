---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51e42c39fab34dbeeac2b35559e8c8b8155cc61243de0d39c42c857255364647
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorflow-deprecation-in-databricks-runtime-ml
    - TDIDRM
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: TensorFlow deprecation in Databricks Runtime ML
description: The removal of TensorFlow and spark-tensorflow-connector from the top-tier library list starting with Databricks Runtime 18.0 ML.
tags:
  - databricks
  - tensorflow
  - deprecation
timestamp: "2026-06-18T15:09:54.994Z"
---

# TensorFlow deprecation in Databricks Runtime ML

**TensorFlow deprecation in Databricks Runtime ML** refers to the status change of TensorFlow and the `spark-tensorflow-connector` from top-tier to non–top-tier libraries, beginning with Databricks Runtime 18.0 ML. This decision signals a reduction in support priority and may lead to eventual removal from pre-installed libraries under the standard library deprecation policy. User’s can still use TensorFlow after deprecation by installing it manually or by using an older runtime version. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Background

[Databricks Runtime ML](/concepts/databricks-runtime-ml.md) ships a curated set of machine learning and deep learning libraries. A subset of these are designated as **top-tier libraries**, which receive faster updates, advanced support, testing, and embedded optimizations. Starting with Databricks Runtime 18.0 ML, TensorFlow and `spark-tensorflow-connector` are no longer included in the top-tier list. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Top-tier libraries are added or removed only with major releases. The remaining top-tier libraries continue to include PyTorch, Scikit-learn, [transformers](/concepts/mlflow-transformers-flavor.md), [MLflow](/concepts/mlflow.md), and others. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Deprecation triggers

Databricks may remove a library from the top-tier list when one or more of the following conditions are met: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library has no new commits in two months **and** no new releases in more than six months.
- Usage of the library drops significantly.
- New packages fill major gaps, replacing the existing library.

After leaving the top-tier list, a library may be **removed entirely** from pre-installed libraries if it: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- Is no longer actively maintained (no commits in three months **and** no releases in nine months, the repository is archived, or maintenance has been announced as stopped).
- Has no stable release found functional for the new runtime.

## Notification process

When a library is planned for removal, Databricks follows a three-step notification process: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. A deprecation warning is added to the runtime release notes, stating that the library will be removed in the next major Databricks Runtime ML release.
2. A notification is displayed when importing the library, indicating the same planned removal.
3. Databricks documentation that references the library is updated to indicate the planned removal.

As of Databricks Runtime 18.0 ML, TensorFlow is no longer top-tier; customers should watch for these notifications in future releases to anticipate complete removal.

## Continuing to use TensorFlow

Even if TensorFlow is removed from pre-installed libraries in a future runtime, users have two options to continue working with it: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- **Install the library manually** — use `%pip install tensorflow` or cluster library installation to add TensorFlow to a Databricks Runtime ML cluster that no longer includes it.
- **Use an earlier version of Databricks Runtime ML** — switch to a runtime version that still ships TensorFlow as part of the base image.

## Impact on existing workflows

Existing notebooks or pipelines that rely on TensorFlow will continue to work as long as they use a runtime that includes the library or the library is installed manually. However, users migrating to newer major runtime versions should plan for the absence of pre-installed TensorFlow and consider migrating to supported deep-learning frameworks such as PyTorch, which remains a top-tier library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The curated runtime environment for ML and DL workloads.
- PyTorch — One of the top-tier deep learning libraries remaining after TensorFlow’s deprecation.
- Library Support Policy — Full description of top-tier criteria and update cadence.
- [MLflow](/concepts/mlflow.md) — Another top-tier library for experiment tracking and model management.
- Transformers — Top-tier library for natural language processing models.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
