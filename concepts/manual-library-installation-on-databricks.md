---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bf0d2f4f2637d31a2faf35b54ec4a019221e4438b4c8dfd2bc5057e3626bfd6
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-library-installation-on-databricks
    - MLIOD
    - Library Installation on Databricks
    - Manual library installation in Databricks
    - Libraries on Databricks
    - Library installation on compute
    - Manual library installation
    - cluster library installation
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Manual Library Installation on Databricks
description: The fallback option to continue using a library after it has been removed from Databricks Runtime ML by installing it manually or using an earlier runtime version.
tags:
  - databricks
  - library-management
  - workflow
timestamp: "2026-06-19T14:54:14.090Z"
---

# Manual Library Installation on Databricks

**Manual library installation** on Databricks is a workaround that allows users to install a library themselves after it has been removed from the pre‑installed set of libraries in a Databricks Runtime ML version. This approach provides continuity for workflows that depend on libraries that are no longer shipped with new runtime releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Background

Databricks Runtime ML includes a curated set of popular machine learning and deep learning libraries that are updated with each release. Over time, Databricks may deprecate and remove a library from the runtime due to factors such as lack of active maintenance, significant drop in usage, or replacement by a newer package that fills a major gap. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Deprecation Notification Process

When a library is planned for removal, Databricks notifies customers through multiple channels:

- A deprecation warning is added in the runtime release notes, indicating the library will be removed in the next major Databricks Runtime ML release.
- A notification is displayed when importing the library, warning that it will be removed in the next major release.
- Databricks documentation that references the library is updated to indicate the planned removal.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Post-Removal Options

After a library has been removed from the runtime, users have two options to continue using it:

- **Install the library manually** – Use standard package management tools (such as `pip` or `conda`) to add the library to the cluster environment.
- **Use an earlier version of Databricks Runtime ML** – Keep using a runtime version that still includes the library pre‑installed.

The manual installation path is explicitly noted as a fallback in the Databricks Runtime ML maintenance policy. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Conditions for Library Removal

Databricks will remove a pre-installed library when it reaches any of the following conditions:

- The library is no longer actively maintained, as determined by:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime ML maintenance policy – Describes how libraries are supported, updated, and deprecated.
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) – The subset of libraries that receive faster updates and advanced support.
- [Library Deprecation Policy](/concepts/library-deprecation-policy.md) – The conditions under which a library is removed from the runtime.
- [Pre-installed libraries in Databricks Runtime ML](/concepts/top-tier-libraries-in-databricks-runtime-ml.md) – List of libraries shipped by default.
- Cluster library management – How to install libraries manually on Databricks clusters.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
