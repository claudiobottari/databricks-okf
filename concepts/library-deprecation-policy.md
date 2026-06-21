---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52cb07c439e19bb7ddb46b09ceb673023d2a960f88a4a24989700b2d7b819bfd
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - library-deprecation-policy
    - LDP
    - Library Deprecation
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Library Deprecation Policy
description: Defines conditions under which Databricks removes libraries from top-tier or pre-installed status, including inactivity, low usage, or replacement.
tags:
  - databricks
  - libraries
  - deprecation
  - lifecycle
timestamp: "2026-06-18T11:41:57.869Z"
---

# Library Deprecation Policy

**Library Deprecation Policy** defines the conditions under which Databricks removes pre-installed libraries from [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) and the notification process for affected customers. This policy applies both to libraries removed from the top-tier library list and to libraries removed entirely from runtime installations.

## Top-Tier Library Removal

Databricks designates a subset of supported libraries as top-tier libraries, which receive a faster update cadence, advanced testing, and embedded optimizations. Top-tier libraries may be removed from the top-tier list under the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library has no new commits in two months and no new releases in more than six months. Databricks might add back the removed library when active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Libraries are replaced if new packages have been added to fill major gaps. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

For example, starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Pre-Installed Library Removal

Databricks removes a pre-installed library when the library reaches any of the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- **Library is no longer actively maintained.** A library is considered not actively maintained when any of the following conditions are met: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - No new commits in three months and no new releases in more than nine months. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - The library's repository is archived. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - An announced stop in maintenance for that library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **No stable release is found to be functional for the new runtime.** ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

When a library is planned for removal, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Databricks documentation that references the library is updated to indicate that the library is planned for removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuing to Use a Removed Library

To continue to use a library after it has been removed from Databricks Runtime ML, you can either install the library manually or use an earlier version of Databricks Runtime ML that still includes the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment that includes pre-installed ML and DL libraries
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — Libraries that receive accelerated updates and advanced support
- Release Notes — Where deprecation warnings are first communicated

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
