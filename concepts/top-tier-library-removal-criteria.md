---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e3984354fd510af957162dcba9f3d78e92fdfa34f457b89e52185b7ea1c59f1
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-library-removal-criteria
    - TLRC
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Top-Tier Library Removal Criteria
description: "Specific conditions that trigger removal of a library from the top-tier list: no commits in 2 months and no releases in 6 months, significant usage drop, or replacement by newer packages."
tags:
  - databricks
  - library-management
  - governance
timestamp: "2026-06-19T14:54:05.313Z"
---

# Top-Tier Library Removal Criteria

**Top-Tier Library Removal Criteria** defines the conditions under which Databricks removes a library from its top-tier list or removes it entirely from pre-installation in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). These criteria are part of the Databricks Runtime ML maintenance policy and ensure that only actively maintained, widely used libraries receive advanced support and fast update cadences. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Overview

Databricks designates a subset of supported libraries as **top-tier libraries**. These libraries receive faster update cadence with each runtime release (barring dependency conflicts), advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

As of Databricks Runtime 18.0 ML, the top-tier libraries include:
- datasets
- [GraphFrames](/concepts/graphframes.md)
- [MLflow](/concepts/mlflow.md)
- PyTorch
- Scikit-learn
- [streaming](/concepts/mosaic-streaming.md)
- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [transformers](/concepts/mlflow-transformers-flavor.md) (Hugging Face)

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Removal from the Top-Tier List

Databricks may remove a library from the top-tier list under the following circumstances:

- The library has **no new commits in two months** and **no new releases in more than six months**. The library may be added back if active maintenance resumes.
- **Usage of the library drops significantly**.
- The library is **replaced** by new packages that fill major gaps.

Removal from the top-tier list does not necessarily mean removal from the runtime; the library may still be pre-installed but will no longer receive top-tier treatment. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Removal of Pre-Installed Libraries

Databricks will remove a pre-installed library from the runtime when the library reaches any of the following conditions:

- **No longer actively maintained**. A library is considered not actively maintained when any of these apply:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- **No stable release** found to be functional for the new runtime.

This removal applies to libraries that were previously pre-installed but no longer meet the maintenance criteria. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

When a library is planned for removal (either from the top-tier list or from pre-installation), Databricks provides the following notifications:

- A **deprecation warning** is added in the runtime release notes, indicating the library will be removed in the next major Databricks Runtime ML release.
- A **notification is displayed** when importing the library, indicating its planned removal.
- **Databricks documentation** that references the library is updated to indicate the planned removal.

These steps give users advance notice so they can adjust their workflows before the library is removed. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuing to Use a Removed Library

If a library has been removed from pre-installation, users can continue to use it by either:

- **Installing the library manually** into the runtime environment.
- **Using an earlier version** of Databricks Runtime ML that still includes the library.

These workarounds allow ongoing use despite the library no longer being pre-installed in the latest runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre-concluded ML environment that includes top-tier libraries.
- Databricks Runtime ML release notes – Where deprecation warnings are published.
- Library management on Databricks – How to install and manage libraries.
- [MLflow](/concepts/mlflow.md) – An example of a top-tier library.
- Hugging Face Transformers – Another top-tier library example.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
