---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9591e0dfbbe3fea099b17f3ae102034cc429227b60dda972e08d87859d3fb9d
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - library-removal-notification-process
    - LRNP
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Library removal notification process
description: The multi-channel customer notification workflow Databricks follows before removing a library, including release notes, import warnings, and documentation updates.
tags:
  - databricks
  - notifications
  - deprecation
timestamp: "2026-06-18T15:09:41.522Z"
---

# Library Removal Notification Process

The **Library removal notification process** describes the steps Databricks follows to inform customers when a pre-installed library is planned for removal from [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). This process applies when a library meets the conditions for deprecation and removal.

## Deprecation Conditions

Databricks will remove a pre-installed library when the library reaches any of the following conditions:

- The library is no longer actively maintained. A library is considered not actively maintained when any of the following conditions are met:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Steps

When a library is planned for removal, Databricks takes the following steps to notify customers:

1. **Deprecation warning in release notes**: A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) release.

2. **Import notification**: A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.

3. **Documentation updates**: Databricks documentation that references the library is updated to indicate that the library is planned for removal.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuity of Use

To continue to use a library after it has been removed, you can either install the library manually or use an earlier version of [Databricks Runtime ML](/concepts/databricks-runtime-ml.md).^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime ML maintenance policy — The broader policy covering library support, updates, and deprecation
- [Top-tier Libraries in Databricks Runtime ML](/concepts/top-tier-libraries.md) — The subset of libraries with faster update cadence and advanced support
- [Library Deprecation Policy](/concepts/library-deprecation-policy.md) — The conditions under which libraries are removed from the top-tier list or pre-installed set

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
