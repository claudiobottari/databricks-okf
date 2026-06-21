---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00edb18ef8a6f2c3b789e9e68b23069eb4fe800d1ec519a423a502a45b04f0c5
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-removal-and-re-addition-policy
    - Re-addition Policy and Top-Tier Removal
    - TRARP
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Top-Tier Removal and Re-addition Policy
description: Conditions under which Databricks may remove a library from top-tier status (2 months no commits, 6 months no releases, significant usage drop, or replacement by newer packages) and the possibility of reinstatement when active maintenance resumes.
tags:
  - databricks
  - library-management
  - policy
timestamp: "2026-06-19T09:54:56.741Z"
---

# Top-Tier Removal and Re-addition Policy

The **Top-Tier Removal and Re-addition Policy** describes the conditions under which Databricks may remove a library from the top-tier list in Databricks Runtime ML, and the circumstances under which a previously removed library may be reinstated as a top-tier library. This policy applies to the subset of libraries designated as "top-tier" within the Databricks Runtime ML environment.

## Library Support Policy

Databricks Runtime ML includes a variety of popular ML and DL libraries. The libraries are updated with each release to include new features and fixes. Databricks has designated a subset of the supported libraries as top-tier libraries. For these libraries, Databricks provides a faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts). Databricks also provides advanced support, testing, and embedded optimizations for top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Top-tier libraries are added or removed only with major releases. The full list of current top-tier libraries includes: datasets, GraphFrames, MLflow, PyTorch, Scikit-learn, streaming, TensorBoard, and transformers. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Removal Conditions

Databricks may remove a library from the top-tier list under the following situations:

- **Inactivity**: If the library has no new commits in two months and no new releases in more than six months. Databricks may add back the removed library when active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Low usage**: If usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Replacement**: Libraries are replaced if new packages have been added to fill major gaps. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Additionally, Databricks will remove a pre-installed library when the library reaches any of the following conditions for being no longer actively maintained:

- No new commits in three months and no new releases in more than nine months.
- The library's repository is archived.
- An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Re-addition Policy

When a library has been removed from the top-tier list due to inactivity, Databricks may add the removed library back to the top-tier list when active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Notifications

When a library is planned for removal, Databricks takes the following steps to notify customers:

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
- Databricks documentation that references the library is updated to indicate that the library is planned for removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Continuation After Removal

To continue to use a library after it has been removed, you can either install the library manually or use an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime environment containing top-tier ML/DL libraries.
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) – The subset of libraries with faster update cadence and advanced support.
- Library Support Policy – The broader policy governing library lifecycle in Databricks Runtime ML.
- [Library Deprecation](/concepts/library-deprecation-policy.md) – The process for removing libraries from the runtime.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
