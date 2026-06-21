---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52b710096164c4fd8362e829617bf67857c8f8cc613bad17249e35334f2b8537
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecation-notification-process
    - DNP
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Deprecation Notification Process
description: The multi-channel notification process Databricks follows when planning to remove a library, including release notes warnings, import-time notifications, and documentation updates.
tags:
  - databricks
  - library-management
  - communication
timestamp: "2026-06-19T14:53:51.607Z"
---

```markdown
---
title: Deprecation Notification Process
summary: The multi-step process Databricks follows to notify customers before removing a library, including release notes, import warnings, and documentation updates.
sources:
  - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:41:59.113Z"
updatedAt: "2026-06-18T11:41:59.113Z"
tags:
  - databricks
  - deprecation
  - notifications
aliases:
  - deprecation-notification-process
  - DNP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Deprecation Notification Process

The **Deprecation Notification Process** describes the steps Databricks takes to notify customers when a pre-installed library is planned for removal from [[Databricks Runtime ML]]. This process applies to libraries that are no longer actively maintained or have no functional stable release for a new runtime version. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Triggers for Deprecation

Databricks may remove a pre-installed library when it reaches any of the following conditions: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- The library is no longer actively maintained. A library is considered not actively maintained when any of the following conditions are met:
  - No new commits in three months and no new releases in more than nine months.
  - The library's repository is archived.
  - An announced stop in maintenance for that library.
- No stable release is found to be functional for the new runtime.

Additionally, Databricks might remove a library from the [[top-tier libraries]] list (a subset of supported libraries with faster update cadence and advanced support) in the following situations: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- If the library has no new commits in two months and no new releases in more than six months. Databricks might add back the removed library when active maintenance resumes.
- If usage of the library drops significantly.
- Libraries are replaced if new packages have been added to fill major gaps.

## Notification Steps

When a library is planned for removal, Databricks takes the following steps to notify customers: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

1. **Deprecation warning in release notes** — A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
2. **Import notification** — A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
3. **Documentation updates** — Databricks documentation that references the library is updated to indicate that the library is planned for removal.

## Continuing to Use a Deprecated Library

To continue to use a library after it has been removed from Databricks Runtime ML, you can either: ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

- Install the library manually on your cluster.
- Use an earlier version of Databricks Runtime ML that still includes the library.

## Related Concepts

- [[Databricks Runtime ML]] — The runtime environment that includes pre-installed ML and DL libraries.
- [[Top-tier libraries]] — Libraries with faster update cadence and advanced support.
- Library support policy — The policy governing library updates and maintenance.
- Runtime release notes — Where deprecation warnings are first published.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
```

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
