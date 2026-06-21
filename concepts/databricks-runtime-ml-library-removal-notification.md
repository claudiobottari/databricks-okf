---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0e937879a8f66e58c3ee7cde5c6a6e2a8e8847bbe69894a462430d4a9b9269d
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-library-removal-notification
    - DRMLRN
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Databricks Runtime ML Library Removal Notification
description: The multi-channel notification process Databricks uses to inform customers before removing a library, including release notes, import warnings, and documentation updates.
tags:
  - databricks
  - machine-learning
  - library-management
  - communication
timestamp: "2026-06-19T18:15:16.783Z"
---

# Databricks Runtime ML Library Removal Notification

The **Databricks Runtime ML Library Removal Notification** is a formal notification process that Databricks follows when a pre-installed library is scheduled for removal from [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). This process provides advance notice to users through multiple channels before a library is actually removed.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Channels

When a library is planned for removal, Databricks provides notifications through the following channels:^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. **Release notes**: A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
2. **Import notification**: A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
3. **Documentation updates**: Databricks documentation that references the library is updated to indicate that the library is planned for removal.

## Library Removal Conditions

Databricks will remove a pre-installed library when the library reaches any of the following conditions:^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library is no longer actively maintained. A library is considered not actively maintained when any of the following conditions are met:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

## Deprecation of Top-Tier Libraries

In addition to regular library removal, Databricks may also remove a library from the [Top-Tier Libraries](/concepts/top-tier-libraries.md) list under the following circumstances:^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- If the library has no new commits in two months and no new releases in more than six months. (Databricks might add back the removed library when active maintenance resumes.)
- If usage of the library drops significantly.
- Libraries are replaced if new packages have been added to fill major gaps.

## Example: TensorFlow Removal

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries.^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuation of Use

To continue using a library after it has been removed from Databricks Runtime ML, users have two options:^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. Install the library manually on the current runtime version.
2. Use an earlier version of Databricks Runtime ML that still includes the library.

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The machine learning-optimized runtime environment
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — Designated libraries with faster update cadence and advanced support
- Databricks Runtime ML Release Notes — Official release documentation containing deprecation notices
- [Library Installation on Databricks](/concepts/manual-library-installation-on-databricks.md) — Instructions for manually installing libraries

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
