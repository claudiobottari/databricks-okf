---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad31d060e9c7681d261d68cdef6e229f957bfc708271f47a85b6db516225fdfb
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-installed-library-removal-criteria
    - PLRC
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Pre-Installed Library Removal Criteria
description: Conditions under which a pre-installed library is removed from Databricks Runtime ML, including lack of active maintenance (no commits in 3 months, no releases in 9 months, archived repository, or announced maintenance stop) or no functional stable release.
tags:
  - databricks
  - library-management
  - governance
timestamp: "2026-06-19T14:54:33.347Z"
---

# Pre-Installed Library Removal Criteria

**Pre-Installed Library Removal Criteria** defines the specific conditions under which Databricks removes a pre-installed library from [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). These criteria help users understand when a library will be deprecated and what steps to take before removal occurs.

## Overview

Databricks maintains a subset of supported libraries designated as [Top-Tier Libraries](/concepts/top-tier-libraries.md) that receive faster update cadences and advanced support. These libraries may be removed from the top-tier list or from the runtime itself when certain maintenance or usage conditions are met. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation Policy

Databricks may remove a library from the top-tier list in the following situations:

- If the library has no new commits in two months and no new releases in more than six months. Databricks may add back the removed library when active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- If usage of the library drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Libraries are replaced if new packages have been added to fill major gaps. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Pre-installed Library Removal Conditions

Databricks will remove a pre-installed library when the library reaches any of the following conditions:

- **The library is no longer actively maintained.** A library is considered not actively maintained when any of the following conditions are met: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - No new commits in three months and no new releases in more than nine months. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - The library's repository is archived. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
  - An announced stop in maintenance for that library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **No stable release is found to be functional** for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Process

When a library is planned for removal, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Databricks documentation that references the library is updated to indicate that the library is planned for removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Continuing After Removal

To continue to use a library after it has been removed, you can either: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- Install the library manually using standard package installation methods. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Use an earlier version of Databricks Runtime ML that still includes the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment that includes these libraries
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — Libraries receiving advanced support and faster updates
- [Library Deprecation Policy](/concepts/library-deprecation-policy.md) — The broader policy for library removal decisions
- Release notes — Where deprecation warnings are documented

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
