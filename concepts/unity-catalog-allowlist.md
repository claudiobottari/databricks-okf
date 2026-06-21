---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a90255f61bffe9ebaad7ad8ace5b123715b78eb7ba7ccc890fb40d8aa8dfe043
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-allowlist
    - UCA
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Unity Catalog Allowlist
description: A security control in Unity Catalog that specifies which JARs, Maven coordinates, and init scripts are permitted to run on standard access mode compute in Databricks.
tags:
  - unity-catalog
  - security
  - access-control
timestamp: "2026-06-19T22:05:41.469Z"
---

# Unity Catalog Allowlist

The **Unity Catalog Allowlist** is a security feature on Databricks that controls which libraries (JARs, Maven artifacts) and init scripts can be installed on compute configured with **standard access mode** (formerly shared access mode). By default, the allowlist is empty, meaning no libraries or init scripts can be used on standard access mode compute until explicitly allowed. This feature cannot be disabled. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

Introduced in Databricks Runtime 13.3 LTS and later, the allowlist governs which artifacts can run on standard access mode compute, preventing users from adding arbitrary libraries and init scripts. This reduces the likelihood of security issues, cluster instability, and other unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

You can add a directory or file to the allowlist even if it has not been created yet. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and Operational Risks

The allowlist is a critical control for maintaining cluster isolation and protecting data on standard access mode compute. Users with the `MANAGE ALLOWLIST` privilege can allowlist any path or Maven coordinate, effectively controlling what code can run on standard access mode compute. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. Databricks recommends the following best practices: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant the `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

## Prerequisites

To modify the allowlist, you must have the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). See [MANAGE ALLOWLIST](/concepts/manage-allowlist-privilege.md) for details. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Before adding Maven coordinates to the allowlist, you must have `CAN ATTACH TO` and `CAN MANAGE` permissions set on the compute where you want to install the library. See Compute permissions for details. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Items to the Allowlist

Items can be added to the allowlist using [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

To open the dialog in Catalog Explorer: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. Click **Catalog** in your Databricks workspace.
2. Click the gear icon to access settings.
3. Click the [Metastore](/concepts/metastore.md) name to open the [Metastore](/concepts/metastore.md) details and permissions UI.
4. Select **Allowed JARs/Init Scripts**.
5. Click **Add**.

> This option only displays for users with the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Init Scripts

To add an init script to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **Init Script**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path to add to the allowlist.

### JAR Files

To add a JAR to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **JAR**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path to add to the allowlist.

### Maven Coordinates

To add Maven coordinates to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **Maven**.
2. For **Source Type**, select **Coordinates**.
3. Enter coordinates in the following format: `groupId:artifactId:version`.

You can include all versions of a library by allowlisting `groupId:artifactId`, or all artifacts in a group by allowlisting `groupId`. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Path-Based Permissions

When adding paths to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- **Directories**: Permissions propagate to contained files and subdirectories.
- **Trailing slash**: Prevents prefix matching at a given directory level (e.g., `/Volumes/prod-libraries/` adds all files and directories within that path without matching prefixes).
- **Files**: Can be added individually.
- **Directories at any depth**: Can be added from the volume base path.

You can define permissions at three levels: the base path for the volume or storage container, a nested directory at any depth, or a single file. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Permissions Enforcement

Adding a path to the allowlist only means the path can be used for either init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location. The principal used must have `READ VOLUME` permissions on the specified volume. See READ VOLUME for details. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Identity assignment varies by access mode: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- **Dedicated access mode** (formerly single user): Uses the identity of the assigned principal (a user or group).
- **Standard access mode**: Libraries use the identity of the library installer; init scripts use the identity of the cluster owner.
- **No-isolation shared access mode**: Does not support volumes but uses the same identity assignment as standard access mode.

Databricks recommends configuring all object storage privileges related to init scripts and libraries with **read-only** permissions. Users with write permissions on these locations can potentially modify code in library files or init scripts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

For S3 storage, using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) is recommended to manage access. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

> Allowlist permissions for JARs and init scripts are managed separately. If you use the same location for both types of objects, you must add the location to the allowlist for each. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Important Notes

- Libraries used as JDBC drivers or custom Spark data sources on Unity Catalog–enabled standard compute require `ANY FILE` permissions. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- Some installed libraries store data of all users in a common temp directory, potentially compromising user isolation. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- Storage locations for allowlisted artifacts should be configured with read-only permissions to prevent code modification. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Standard Access Mode Compute](/concepts/standard-access-mode-compute.md)
- Unity Catalog Volumes
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)
- [Compute Permissions](/concepts/can-manage-permission.md)
- [Init Scripts](/concepts/init-script-allowlisting.md)
- [Libraries on Databricks](/concepts/manual-library-installation-on-databricks.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- READ VOLUME
- [Metastore Admin](/concepts/metastore-admin-role.md)

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
