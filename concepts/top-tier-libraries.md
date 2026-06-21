---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f11cfb8762359636a1a11a4df985e578157e1a01dafa56862dd3af88c25892f6
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-libraries
    - top-tier-libraries-in-databricks-runtime-ml
    - TLIDRM
    - Pre-installed libraries in Databricks Runtime ML
    - top-tier-library-support-in-databricks-runtime-ml
    - TLSIDRM
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Top-Tier Libraries
description: A subset of Databricks Runtime ML libraries receiving faster updates, advanced support, testing, and embedded optimizations.
tags:
  - databricks
  - libraries
  - support-policy
timestamp: "2026-06-18T11:41:52.063Z"
---

# Top-Tier Libraries

**Top-tier libraries** are a subset of the libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) that receive prioritized support, faster updates, and embedded optimizations from Databricks. These libraries are updated to the latest package releases with each runtime release, barring dependency conflicts. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Support Policy

Databricks designates a subset of supported libraries as top-tier libraries. For these libraries, Databricks provides: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts).
- Advanced support, testing, and embedded optimizations.
- Additions or removals only with major releases.

## Current Top-Tier Libraries

The full list of top-tier libraries includes: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- datasets — For loading and processing data, including Hugging Face datasets
- [GraphFrames](/concepts/graphframes.md) — For graph processing and analysis
- [MLflow](/concepts/mlflow.md) — For managing the machine learning lifecycle
- PyTorch — For deep learning model training
- Scikit-learn — For classical machine learning algorithms
- [streaming](/concepts/mosaic-streaming.md) — For streaming data processing
- [TensorBoard](/concepts/tensorboard-on-databricks.md) — For visualization and experiment tracking
- [transformers](/concepts/mlflow-transformers-flavor.md) — For Hugging Face transformer models

For a complete list of all libraries included in each runtime version, see the Databricks Runtime ML release notes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Changes in Recent Releases

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Policy

Databricks may remove a library from the top-tier list under the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library has no new commits in two months and no new releases in more than six months. Databricks may add back the removed library when active maintenance resumes.
- Usage of the library drops significantly.
- New packages are added to fill major gaps, replacing existing libraries.

Databricks will remove a pre-installed library when the library reaches any of the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library is no longer actively maintained, defined as:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

### Notification Process

When a library is planned for removal, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
- Databricks documentation that references the library is updated to indicate that the library is planned for removal.

### Continuing to Use Removed Libraries

To continue to use a library after it has been removed, you can either install the library manually or use an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The machine learning runtime environment
- Library Management — Installing and managing libraries in Databricks
- [MLflow](/concepts/mlflow.md) — A top-tier library for ML lifecycle management
- PyTorch — A top-tier deep learning framework
- Hugging Face Transformers — A top-tier library for transformer models

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
