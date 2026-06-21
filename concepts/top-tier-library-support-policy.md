---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: becb02707e652a416b515fdd37d03f978770767b3acef1a30c11559d67097652
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-library-support-policy
    - TLSP
    - Library Support Policy
    - Library support policy
    - library support policy
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Top-tier Library Support Policy
description: Databricks designates a subset of libraries as 'top-tier' with faster update cadence, advanced support, testing, and embedded optimizations, updated with each runtime release.
tags:
  - libraries
  - release-management
  - machine-learning
timestamp: "2026-06-19T14:53:21.192Z"
---

# Top-tier Library Support Policy

**Top-tier Library Support Policy** defines the subset of pre-installed libraries in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) that receive accelerated updates, advanced testing, and embedded optimizations from Databricks. This policy helps users identify which libraries are actively maintained and prioritized within the runtime environment.

## Overview

Databricks Runtime ML includes a wide variety of popular machine learning and deep learning libraries. Among them, Databricks designates a subset as **top-tier libraries**. For these libraries, Databricks provides a faster update cadence — updating to the latest package releases with each runtime release, barring dependency conflicts — as well as advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major runtime releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Current Top-tier Libraries

As of the latest documentation, the following libraries are designated as top-tier:

- datasets (Hugging Face)
- [GraphFrames](/concepts/graphframes.md)
- [MLflow](/concepts/mlflow.md)
- PyTorch
- Scikit-learn
- [streaming](/concepts/mosaic-streaming.md)
- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [transformers](/concepts/mlflow-transformers-flavor.md) (Hugging Face)

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Note: Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Policy

Databricks may remove a library from the top-tier list in the following situations:

- The library has no new commits in two months and no new releases in more than six months. Databricks may later add the library back if active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- New packages have been added to fill major gaps, leading to replacement. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

A pre-installed library may be removed entirely when it reaches any of the following conditions:

- The library is no longer actively maintained, defined as: no new commits in three months and no new releases in more than nine months; the library's repository is archived; or an announced stop in maintenance. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- No stable release is found to be functional for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Customer Notification Process

When a library is planned for removal, Databricks takes the following steps:

- A deprecation warning is added in the runtime release notes, stating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, indicating the planned removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Databricks documentation that references the library is updated to indicate the planned removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

To continue using a library after it has been removed, users can either install the library manually or use an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Recommendations

- For production workloads, prefer using top-tier libraries to benefit from the latest updates, optimizations, and support. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Monitor Databricks Runtime ML release notes for deprecation notices and plan upgrades accordingly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- If a library is removed, evaluate manual installation or consider migrating to a supported alternative. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- [MLflow](/concepts/mlflow.md)
- PyTorch
- [transformers](/concepts/mlflow-transformers-flavor.md)
- Release notes for Databricks Runtime ML

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
