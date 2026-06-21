---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 339559e0420c90f254f220a1c1d058319ac789b4d5c2044719be8e6c8c40b5d5
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-maintenance-definition-for-libraries
    - AMDFL
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Active Maintenance Definition for Libraries
description: "Criteria Databricks uses to determine if a library is actively maintained: commits within 3 months and releases within 9 months, no archived repository, and no announced stop of maintenance."
tags:
  - databricks
  - library-management
  - maintenance
timestamp: "2026-06-19T09:54:40.149Z"
---

---
title: Active Maintenance Definition for Libraries
summary: Definition of "active maintenance" as used by Databricks to determine when a pre-installed library is no longer supported, based on commit activity, release frequency, repository status, and maintenance announcements.
sources:
  - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:00:00.000Z"
updatedAt: "2026-06-18T10:00:00.000Z"
tags:
  - databricks
  - library-management
  - deprecation
  - maintenance-policy
aliases:
  - active-maintenance-definition-for-libraries
  - AMD
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Active Maintenance Definition for Libraries

**Active Maintenance Definition for Libraries** refers to the criteria that [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) uses to determine whether a pre-installed library is still actively maintained. This definition directly governs when a library is considered for removal from the runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Definition

A library is considered **not actively maintained** — and therefore a candidate for removal — when **any** of the following conditions is met: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. **No new commits in three months and no new releases in more than nine months.** ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
2. **The library’s repository is archived.** ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
3. **An announced stop in maintenance for that library.** ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

A library is considered **actively maintained** when none of the above conditions apply. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## How the Definition Is Used

For pre-installed libraries in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), Databricks applies the active maintenance definition as part of its [Library Deprecation Policy](/concepts/library-deprecation-policy.md). When a library meets the definition of "not actively maintained," Databricks may remove it from the runtime in a future release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Distinction from Top-Tier Library Status

The definition of active maintenance for library removal is separate from the criteria used to manage [Top-Tier Libraries](/concepts/top-tier-libraries.md). Top-tier libraries may be removed from the top-tier list if they have no new commits in two months and no new releases in more than six months, or if usage drops significantly. However, removal from the top-tier list does not automatically mean the library is removed from the runtime — only that it is no longer given accelerated update cadence and advanced support. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Notification Before Removal

When a pre-installed library is identified for removal based on the active maintenance definition, Databricks provides advance notice: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Databricks documentation that references the library is updated to indicate that the library is planned for removal. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Users who need to continue using a removed library can install it manually or use an earlier version of Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment for machine learning workloads on Databricks.
- [Top-Tier Libraries](/concepts/top-tier-libraries.md) — Libraries that receive accelerated updates and advanced support.
- [Library Deprecation Policy](/concepts/library-deprecation-policy.md) — The broader policy governing library removal.
- Databricks Runtime release notes — Where deprecation warnings are published.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
