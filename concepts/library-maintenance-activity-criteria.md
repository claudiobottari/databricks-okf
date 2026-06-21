---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a5161f945bf829f949e122e168393e5a721c1a58b8247467f892feaed112862
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - library-maintenance-activity-criteria
    - LMAC
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Library Maintenance Activity Criteria
description: Specific metrics used by Databricks to determine if a library is actively maintained, based on commit frequency and release cadence (e.g., no commits in 2-3 months, no releases in 6-9 months).
tags:
  - databricks
  - library-management
  - maintenance
timestamp: "2026-06-19T18:15:19.600Z"
---

# Library Maintenance Activity Criteria

**Library Maintenance Activity Criteria** define the conditions under which Databricks updates, deprecates, or removes pre‑installed libraries in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). These criteria cover two main areas: the support policy for top‑tier libraries and the deprecation policy for any pre‑installed library.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Top‑Tier Library Support

Databricks designates a subset of supported libraries as **top‑tier libraries**. For these libraries, Databricks provides a faster update cadence—updating to the latest package releases with each runtime release, subject to dependency conflicts—along with advanced support, testing, and embedded optimizations. Top‑tier libraries are added or removed only with major Databricks Runtime ML releases.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The current list of top‑tier libraries includes:
- `datasets`
- `GraphFrames`
- `MLflow`
- `PyTorch`
- `Scikit‑learn`
- `streaming`
- `TensorBoard`
- `transformers`

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark‑tensorflow‑connector are **no longer** top‑tier libraries.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Policy

Databricks may remove a library from the top‑tier list—or deprecate a pre‑installed library—under the following conditions:

- **Inactivity:** The library has no new commits in two months and no new releases in more than six months. Databricks may restore top‑tier status if active maintenance resumes.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Low usage:** Usage of the library drops significantly.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Replacement:** New packages are added that fill major gaps, making the library redundant.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Removal Criteria for Pre‑installed Libraries

A pre‑installed library is removed from the runtime when any of the following is true:

- The library is **no longer actively maintained**, defined as any of:
  - No new commits in three months **and** no new releases in more than nine months.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - The library’s repository is archived.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - An announced stop in maintenance for that library.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- No stable release is found to be functional for the new runtime.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

When a library is planned for removal, Databricks follows a multi‑step notification process to give customers advance warning:

1. A deprecation warning is added in the runtime release notes, stating that the library will be removed in the next major Databricks Runtime ML release.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
2. A notification is displayed when importing the library, indicating the same planned removal.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
3. Databricks documentation that references the library is updated to mark it as planned for removal.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Customers who need to continue using a removed library can either install it manually or use an earlier version of Databricks Runtime ML.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime environment in which these library policies apply.
- [MLflow](/concepts/mlflow.md) – A top‑tier library for experiment tracking and model management.
- PyTorch – A top‑tier deep learning framework.
- [transformers](/concepts/mlflow-transformers-flavor.md) – A top‑tier library from Hugging Face for natural language processing.
- Databricks Runtime release notes – Where deprecation notices are published.
- [Manual library installation](/concepts/manual-library-installation-on-databricks.md) – Fallback method for using deprecated or removed libraries.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
