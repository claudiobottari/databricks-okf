---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c12c6c1fce5a2204cdd0623d259ca8f1a9da9cfa84b4afab9e72c4beb06fe63d
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - standard-access-mode-compute
    - SAMC
    - Access modes (compute)
    - standard compute
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Standard Access Mode Compute
description: A Databricks compute access mode (formerly shared access mode) where the allowlist restricts what libraries and init scripts can run, using the library installer's identity for libraries and the cluster owner's identity for init scripts.
tags:
  - compute
  - access-modes
  - unity-catalog
timestamp: "2026-06-19T17:32:41.992Z"
---

# Standard Access Mode Compute

**Standard Access Mode Compute** (formerly known as shared access mode) is a Databricks compute configuration designed for multi-user collaboration with strong data isolation and access control. It enables multiple users to share the same compute resources while maintaining data security through fine-grained permissions enforced by [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Standard access mode compute supports concurrent workloads from multiple users while ensuring user isolation through an allowlist that restricts which libraries and init scripts can execute. When libraries or init scripts are used on standard access mode compute, Databricks enforces specific security controls to prevent unauthorized code execution and data access. The allowlist is managed through Unity Catalog and cannot be disabled; by default it is empty.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Library and Init Script Allowlist

All libraries and init scripts used on standard access mode compute must be explicitly allowed through the Unity Catalog allowlist. This controls which JARs, Maven coordinates, and init scripts can run on this compute. Only users with the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md) can modify the allowlist. This privilege should be granted sparingly, as it grants control over what code can execute on standard access mode compute.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Managing the Allowlist

Items can be added to the allowlist through [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. The supported artifact types and source types are:^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- **Init Scripts** – Source types: Volume or object storage protocols.
- **JARs** – Source types: Volume or object storage protocols.
- **Maven Coordinates** – Format `groupId:artifactId:version`, with support for wildcards at the group and artifact level (e.g., `groupId:artifactId` for all versions, `groupId` for all artifacts in a group).

### Path-Based Permissions

Path permissions use prefix matching. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` applies to all files within that directory but does not match files prefixed with `prod-libraries`. You can define permissions at the base path, a nested directory, or a single file. Adding a path to the allowlist only means the path can be used; Databricks still checks data access permissions.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Identity Resolution

In standard access mode, the principal used for permission checks depends on the artifact type:^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- For **libraries**, the identity of the library installer is used.
- For **init scripts**, the identity of the cluster owner is used.

The principal must have `READ VOLUME` permissions on the specified volume.

## Security Considerations

### Risks

Some installed libraries may store data from all users in a common temporary directory, which can compromise user isolation on standard access mode compute. Additionally, libraries used as JDBC drivers or custom Spark data sources on Unity Catalog-enabled standard compute require `ANY FILE` permissions.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Best Practices

The source recommends the following:^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant `MANAGE ALLOWLIST` only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

### Storage Configuration

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations could potentially modify code in library files or init scripts. Using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) to manage access to JARs or init scripts stored in S3 is also recommended. Allowlist permissions for JARs and init scripts are managed separately; if the same location stores both types of objects, the location must be added to the allowlist for each type.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Comparison with Other Access Modes

- **[Dedicated Access Mode](/concepts/dedicated-access-mode-for-ml-compute.md)** (formerly single user access mode) – Uses the identity of the assigned principal (a user or group) for permission checks, rather than the library installer or cluster owner.
- **[No-Isolation Shared Access Mode](/concepts/no-isolation-shared-clusters.md)** – Does not support volumes, but uses the same identity assignment as standard access mode.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance system that enforces access control policies on standard access mode compute.
- [Metastore Admin](/concepts/metastore-admin-role.md) – The role responsible for managing the allowlist.
- [Compute Permissions](/concepts/can-manage-permission.md) – Required for installing libraries (e.g., `CAN ATTACH TO`, `CAN MANAGE`).
- READ VOLUME – The permission required to access volumes containing allowlisted artifacts.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for managing the allowlist.
- REST API – Programmatic interface for allowlist management.
- [Instance profiles](/concepts/instance-profile-databricks-on-aws.md) – Recommended for managing access to JARs or init scripts stored in S3.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
