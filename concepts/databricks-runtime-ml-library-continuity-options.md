---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0510f62835b4527f364c6b506c344525c9ad07e321faafbb1f642cf5b940cb0b
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-library-continuity-options
    - DRMLCO
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Databricks Runtime ML Library Continuity Options
description: "Options available to customers after a library is removed from Databricks Runtime ML pre-installation: manually install the library or use an earlier runtime version."
tags:
  - databricks
  - migration
  - library-management
timestamp: "2026-06-19T09:54:48.921Z"
---

Here is the wiki page for "Databricks Runtime ML Library Continuity Options".

---

## Databricks Runtime ML Library Continuity Options

**Databricks Runtime ML Library Continuity Options** refers to the policies and practices governing how machine learning libraries are maintained, updated, and eventually deprecated within Databricks Runtime ML. Understanding these options helps teams plan for library transitions and ensure long-term reproducibility of their ML workloads.

### Top-Tier Libraries and Support Policy

Databricks designates a subset of pre-installed libraries as **top-tier libraries**. For these libraries, Databricks provides a faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts). Top-tier libraries also receive advanced support, testing, and embedded optimizations. The list of top-tier libraries changes only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The full list of top‑tier libraries includes:

- `datasets`
- `GraphFrames`
- `MLflow`
- `PyTorch`
- `Scikit-learn`
- `streaming`
- `TensorBoard`
- `transformers`

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top‑tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

For a complete list of all libraries included in each runtime version, see the release notes for Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Library Deprecation Policy

Databricks may remove a library from the top‑tier list under any of the following conditions:

- The library has no new commits in two months and no new releases in more than six months. Databricks might restore it when active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- New packages fill major gaps and replace the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

A pre-installed library will be removed entirely when any of the following conditions are met:

- The library is no longer actively maintained (no new commits in three months and no new releases in more than nine months, or the repository is archived, or maintenance is announced to stop). ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- No stable release is found to be functional for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

When a library is planned for removal, Databricks takes these notification steps:

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, indicating that the library will be removed in the next major release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Documentation referencing the library is updated to indicate the planned removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Continuity Options After Removal

If a library has been removed from Databricks Runtime ML and you still need it, you have two primary continuity options:

- **Install the library manually** on the cluster using `%pip install` or library installation mechanisms. This allows you to continue using the library even if it is no longer pre-installed. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Use an earlier version of Databricks Runtime ML** that still includes the library. This can be a temporary workaround while you migrate to alternative libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

These options give teams flexibility to maintain existing codebases while planning upgrades.

### Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre-configured environment for ML workloads.
- [Top-tier Libraries in Databricks Runtime ML](/concepts/top-tier-libraries-in-databricks-runtime-ml.md) – The subset that receives accelerated updates.
- [MLflow](/concepts/mlflow.md) – A top-tier library for experiment tracking and model management.
- PyTorch – A top-tier deep learning framework.
- Transformers – A top-tier library from Hugging Face.
- [Manual Library Installation on Databricks](/concepts/manual-library-installation-on-databricks.md) – How to install packages on a cluster.
- Databricks Runtime Release Notes – Official release details for each runtime version.

### Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
