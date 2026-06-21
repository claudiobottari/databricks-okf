---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 06b5e28d4be02745e28bde405729b455ea03797159bbf42c6986ae6d48ca5e12
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - maven-coordinates-in-allowlist
    - MCIA
    - Maven coordinates
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Maven Coordinates in Allowlist
description: The ability to add Maven coordinates to the Unity Catalog allowlist using groupId:artifactId:version format, with support for wildcards to include all versions or all artifacts in a group.
tags:
  - maven
  - libraries
  - unity-catalog
timestamp: "2026-06-19T08:58:41.718Z"
---

# Maven Coordinates in Allowlist

**Maven Coordinates in Allowlist** refers to the process of adding Maven library references to the Unity Catalog allowlist, enabling those libraries to be installed on compute resources configured with standard access mode. The allowlist controls which libraries and init scripts can run on standard access mode compute in Databricks Runtime 13.3 LTS and above. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

The Unity Catalog allowlist is the mechanism that governs which libraries and init scripts can execute on standard access mode compute. By default, the allowlist is empty. To modify it, a user must have the `MANAGE ALLOWLIST` privilege. This feature cannot be disabled. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Maven coordinates are one of three artifact types that can be added to the allowlist, alongside JAR files stored in volumes or object storage, and init scripts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Prerequisites

Before adding Maven coordinates to the allowlist, a user must have `CAN ATTACH TO` and `CAN MANAGE` permissions set on the compute resource where the library will be installed. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Maven Coordinates

Users can add Maven coordinates to the allowlist through either [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. In Catalog Explorer, the allowlist management interface is accessed through the [Metastore](/concepts/metastore.md) details and permissions UI. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

To add a Maven coordinate in the allowlist dialog:

1. For **Type**, select **Maven**.
2. For **Source Type**, select **Coordinates**.
3. Enter coordinates in the following format: `groudId:artifactId:version`. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Coordination Format Options

The allowlist supports three levels of specificity when adding Maven coordinates: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- **Specific version**: `groupId:artifactId:version` — Allows a single library version.
- **All versions of an artifact**: `groupId:artifactId` — Allows all versions of a specific library.
- **All artifacts in a group**: `groupId` — Allows all artifacts published under a given group ID.

## Security and Governance

Managing Maven coordinates in the allowlist carries security implications. Users with `MANAGE ALLOWLIST` privileges can effectively control what code runs on standard access mode compute. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks recommends the following best practices: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant `MANAGE ALLOWLIST` only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators.
- Use specific paths and Maven coordinates rather than broad patterns.
- Review and audit allowlist additions regularly.
- Implement a formal approval process for allowlist additions in production environments.
- Test libraries in non-production environments before adding to production allowlists.

## Accessing the Allowlist UI

The Catalog Explorer option to manage the allowlist only displays for users with the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). Users who cannot access this UI should contact their [metastore admin](/concepts/metastore-admin-role.md) for assistance. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Standard Access Mode](/concepts/standard-access-mode.md)
- [Init Scripts in Allowlist](/concepts/init-script-allowlisting.md)
- [JAR Allowlist](/concepts/jar-library-allowlisting.md)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Compute Permissions](/concepts/can-manage-permission.md)

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
