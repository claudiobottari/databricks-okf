---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c81ee5bf49777d2f0dad9694f707dfcbbbe0b0885b367a98f0e0ffcec9980b3
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-library-deprecation-policy
    - DRMLDP
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Databricks Runtime ML Library Deprecation Policy
description: The criteria and process by which Databricks removes pre-installed libraries from Databricks Runtime ML, including conditions like inactivity, low usage, or replacement.
tags:
  - databricks
  - machine-learning
  - library-management
  - lifecycle
timestamp: "2026-06-19T18:15:23.245Z"
---

---
title: Databricks Runtime ML Library Deprecation Policy
summary: Policy defining when Databricks removes a library from top-tier status (inactivity, low usage, or replacement) or entirely from pre-installation (loss of active maintenance, no functional stable release), with multi-step customer notification procedures.
sources:
  - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:54:41.573Z"
updatedAt: "2026-06-19T09:54:41.573Z"
tags:
  - databricks
  - library-deprecation
  - machine-learning
aliases:
  - databricks-runtime-ml-library-deprecation-policy
  - DRMLDP
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks Runtime ML Library Deprecation Policy

**Databricks Runtime ML Library Deprecation Policy** defines the conditions under which pre-installed machine learning and deep learning libraries are removed from [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) and the steps Databricks takes to notify customers before removal. The policy covers both changes to the list of top-tier libraries and the full set of pre-installed libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Top-Tier Libraries

A subset of supported libraries is designated as *top-tier*. For these libraries, Databricks provides a faster update cadence — updating to the latest package releases with each runtime release (barring dependency conflicts) — and offers advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major runtime releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The current top-tier libraries are:

- datasets (Hugging Face)
- [GraphFrames](/concepts/graphframes.md)
- [MLflow](/concepts/mlflow.md)
- PyTorch
- Scikit-learn
- [streaming](/concepts/mosaic-streaming.md) (Databricks streaming utilities)
- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [transformers](/concepts/mlflow-transformers-flavor.md) (Hugging Face)

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

> **Note:** Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

For a complete list of all libraries included in each runtime version, see the Databricks Runtime ML release notes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Triggers

### Removal from the Top-Tier List

Databricks may remove a library from the top-tier list if any of the following conditions are met:

- The library has **no new commits in two months** and **no new releases in more than six months**. (The library may be reinstated when active maintenance resumes.)
- **Usage of the library drops significantly.**
- The library is **replaced** because new packages have been added to fill major gaps.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Removal of a Pre-Installed Library

Databricks will remove a pre-installed library (regardless of top-tier status) when the library reaches any of these conditions:

- The library is **no longer actively maintained**, meaning:
  - No new commits in three months **and** no new releases in more than nine months, **or**
  - The library’s repository is archived, **or**
  - An announced stop in maintenance for that library.
- **No stable release is found to be functional** for the new runtime.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Customer Notification Process

When a library is planned for removal, Databricks takes the following steps to notify customers:

1. A **deprecation warning** is added to the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
2. A **notification is displayed when importing the library**, indicating that the library will be removed in the next major Databricks Runtime ML release.
3. **Databricks documentation** that references the library is updated to indicate that the library is planned for removal.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuing to Use a Removed Library

After a library has been removed from a Databricks Runtime ML version, you can continue to use it by either:

- **Installing the library manually** (e.g., via `%pip install` or `%conda install`), or
- **Using an earlier version** of Databricks Runtime ML that still includes the library.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that includes pre-installed ML/DL libraries.
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — The subset of libraries that receive accelerated updates and advanced support.
- [MLflow](/concepts/mlflow.md) — A top-tier library for experiment tracking and model management.
- PyTorch — A top-tier deep learning framework.
- Databricks Runtime ML release notes — Where deprecation warnings are announced.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
