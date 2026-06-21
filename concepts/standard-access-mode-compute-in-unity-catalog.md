---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 104c1be7a40d4cc3c938b8b891d095018093dfafdeb274ed670cf3dc1c390dce
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - standard-access-mode-compute-in-unity-catalog
    - SAMCIUC
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Standard Access Mode Compute in Unity Catalog
description: A compute access mode (formerly shared access mode) that enforces user isolation and requires allowlisted libraries and init scripts for non-default artifacts.
tags:
  - compute
  - unity-catalog
  - access-mode
timestamp: "2026-06-19T22:06:04.772Z"
---

# Standard Access Mode Compute in Unity Catalog

**Standard Access Mode Compute** (formerly known as shared access mode) is a compute configuration in Databricks that enables multiple users to share a cluster while maintaining Unity Catalog data governance. It provides user isolation for data access while allowing shared infrastructure utilization.

## Overview

Standard access mode compute allows multiple users to run workloads on the same compute resources while Unity Catalog enforces data access permissions based on each user's identity. Unlike dedicated access mode (formerly single user access mode), where a single principal's identity is used for all operations, standard mode uses the identity of the individual user or the library installer for access control decisions.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Libraries and Init Scripts on Standard Access Mode

Starting in Databricks Runtime 13.3 LTS and above, Unity Catalog provides an `allowlist` mechanism that controls which libraries and init scripts can run on standard access mode compute. This allows users to leverage these artifacts while maintaining security and isolation.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### The Allowlist

By default, the allowlist is empty. To modify it, users must have the `MANAGE ALLOWLIST` privilege. Items can be added to the allowlist using [Catalog Explorer](/concepts/catalog-explorer.md) or the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md). You can add a directory or file to the allowlist even if it hasn't been created yet.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Identity Resolution

When accessing libraries or init scripts on standard access mode compute:

- **Libraries** use the identity of the library installer.
- **Init scripts** use the identity of the cluster owner.

This differs from dedicated access mode, where the assigned principal's identity is used for all operations.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Prerequisites for Library Access

Libraries used as JDBC drivers or custom Spark data sources on Unity Catalog-enabled standard compute require `ANY FILE` permissions. Some installed libraries may store data of all users in a common temporary directory, potentially compromising user isolation.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and Operational Risks

Understanding the security implications of allowlists is critical for maintaining cluster isolation and protecting your data on standard access mode compute. Proper allowlist usage prevents users from adding arbitrary libraries and init scripts, reducing the likelihood of security issues, cluster instability, and other unpredictable behavior.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Best Practices for Allowlist Management

Databricks recommends the following practices for managing the allowlist:

- Grant the `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Items to the Allowlist

### Init Scripts

To add an init script to the allowlist:
1. For **Type**, select **Init Script**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path to add to the allowlist.

^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### JAR Files

To add a JAR to the allowlist:
1. For **Type**, select **JAR**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path to add to the allowlist.

^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Maven Coordinates

To add Maven coordinates to the allowlist:
1. For **Type**, select **Maven**.
2. For **Source Type**, select **Coordinates**.
3. Enter coordinates in the format `groupId:artifactId:version`.

Before adding Maven coordinates, you must have `CAN ATTACH TO` and `CAN MANAGE` permissions set on the compute where you want to install the library.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Path Permission Enforcement

Prefix matching is used for all artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` will not perform prefix matching for files prefixed with `prod-libraries`; instead, all files and directories within that path are added to the allowlist.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Permissions can be defined at the following levels:
1. The base path for the volume or storage container.
2. A directory nested at any depth from the base path.
3. A single file.

Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location. The principal used must have `READ VOLUME` permissions on the specified volume.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Storage Recommendations

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations can potentially modify code in library files or init scripts. For S3 storage, use instance profiles to manage access to JARs or init scripts.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution for Databricks
- [Dedicated Access Mode Compute](/concepts/dedicated-access-mode-for-ml-compute.md) – Single-user compute mode (formerly single user access mode)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) – The permission required to modify allowlists
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for managing Unity Catalog objects
- [Metastore Admin](/concepts/metastore-admin-role.md) – Administrator responsible for Unity Catalog [Metastore](/concepts/metastore.md) management
- READ VOLUME Privilege – Permission required to access volumes

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
