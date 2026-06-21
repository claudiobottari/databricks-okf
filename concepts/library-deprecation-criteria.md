---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd191a6f29d6d940287e6a77282ee42370004461e4b898fb2952352ac816f441
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - library-deprecation-criteria
    - LDC
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Library deprecation criteria
description: Conditions under which Databricks removes a top-tier or pre-installed library, including inactivity metrics, lack of maintenance, and low usage.
tags:
  - databricks
  - deprecation
  - libraries
timestamp: "2026-06-18T15:09:39.837Z"
---

# Library Deprecation Criteria

**Library deprecation criteria** are the conditions under which Databricks may remove a library from the top‑tier list or uninstall a pre‑installed library in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). These criteria help maintain a reliable, actively supported set of libraries in each runtime release.

## Top‑Tier Library Removal

A top‑tier library may be removed from the designated list (but not necessarily uninstalled) if any of the following situations occur:

- The library has no new commits in two months and no new releases in more than six months. If active maintenance resumes, the library may be added back. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- New packages have been added to fill major gaps, which may replace the existing library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Pre‑Installed Library Removal

A pre‑installed library is removed when it reaches any of the following conditions:

- The library is no longer actively maintained. A library is considered not actively maintained when any of these is true:
  - No new commits in three months and no new releases in more than nine months.
  - The library’s repository is archived.
  - An announced stop in maintenance for that library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- No stable release is found to be functional for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

Before a library is removed, Databricks takes the following steps to notify customers:

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, stating that the library will be removed in the next major release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Documentation referencing the library is updated to indicate its planned removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuing Use After Removal

If a library has been removed, users can continue to use it by either installing the library manually or by using an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — The subset of libraries that receive faster updates and advanced support.
- Databricks Runtime ML maintenance policy — The overall policy covering support, updates, and deprecation.
- Databricks Runtime ML release notes — Where deprecation warnings are published.
- [Manual library installation in Databricks](/concepts/manual-library-installation-on-databricks.md) — How to add libraries after they have been removed.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
