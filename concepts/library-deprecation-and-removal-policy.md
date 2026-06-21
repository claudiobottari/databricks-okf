---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 531232ba099d59ed19829f258c84d897f7d0cb1049abe2bf64e3e1fa1e87155c
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - library-deprecation-and-removal-policy
    - Removal Policy and Library Deprecation
    - LDARP
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Library Deprecation and Removal Policy
description: Policies governing when pre-installed or top-tier libraries are deprecated and removed from Databricks Runtime ML, including triggers such as inactivity, low usage, or replacement by superior packages.
tags:
  - databricks
  - library-management
  - deprecation
timestamp: "2026-06-19T14:54:04.982Z"
---

# Library Deprecation and Removal Policy

**Library Deprecation and Removal Policy** refers to the formal process by which Databricks determines when to remove a pre-installed library from Databricks Runtime ML and how it notifies customers about planned removals. This policy covers both top-tier libraries and all pre-installed libraries in the runtime.

## Library Support Policy

Databricks designates a subset of supported libraries as **top-tier libraries**. These receive a faster update cadence, advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The current top-tier libraries include:
- [datasets](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
- [GraphFrames](https://docs.databricks.com/aws/en/integrations/graphframes/)
- [MLflow](https://docs.databricks.com/aws/en/mlflow/)
- [PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch)
- [Scikit-learn](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn)
- [streaming](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming)
- [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard)
- [transformers](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Policy

### Conditions for Removing a Library from the Top-Tier List

Databricks may remove a library from the top-tier list under the following circumstances: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library has no new commits in two months and no new releases in more than six months. Databricks may add back the removed library when active maintenance resumes.
- Usage of the library drops significantly.
- Libraries are replaced if new packages have been added to fill major gaps.

### Conditions for Removing a Pre-Installed Library

Databricks will remove a pre-installed library when the library reaches any of the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- **The library is no longer actively maintained.** A library is considered not actively maintained when any of the following conditions are met:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

## Customer Notification Process

When a library is planned for removal, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
- Databricks documentation that references the library is updated to indicate that the library is planned for removal.

## Continuing to Use a Removed Library

To continue to use a library after it has been removed, you can either install the library manually or use an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment containing pre-installed ML and DL libraries.
- Databricks Runtime ML Release Notes — Where deprecation warnings are published.
- [Library Installation on Databricks](/concepts/manual-library-installation-on-databricks.md) — How to manually install libraries not included in the runtime.
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — The subset of libraries with enhanced support and faster update cadence.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
