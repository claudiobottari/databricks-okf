---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fb6acf35e51bfa702417a82b48444d621be218f9d8ac2970fc9ac1325442bbb
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - init-script-and-jar-allowlisting
    - JAR Allowlisting and Init Script
    - ISAJA
    - Allowlist for Libraries and Init Scripts
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Init Script and JAR Allowlisting
description: The process of adding init scripts or JAR files to the Unity Catalog allowlist via Catalog Explorer or REST API, supporting sources from Unity Catalog volumes or object storage.
tags:
  - init-scripts
  - jars
  - libraries
timestamp: "2026-06-19T17:33:30.230Z"
---

# Init Script and JAR Allowlisting

**Init Script and JAR Allowlisting** is a Unity Catalog access control mechanism that controls which libraries and init scripts can run on compute configured with standard access mode (formerly shared access mode). The allowlist prevents users from adding arbitrary artifacts to clusters, reducing the risk of security issues, cluster instability, and unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

In Databricks Runtime 13.3 LTS and above, Unity Catalog provides an `allowlist` that governs which JARs, Maven coordinates, and init scripts can execute on standard access mode compute. If a library or init script is not on the allowlist, it cannot be used. By default, the allowlist is empty, and the feature cannot be disabled. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Users can add items to the allowlist that point to paths that do not yet exist, enabling future provisioning of artifacts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Libraries with Special Permission Requirements

Libraries used as JDBC drivers or custom Spark data sources on Unity Catalog-enabled standard compute require `ANY FILE` permissions. Additionally, some installed libraries store data of all users in a common temporary directory, which may compromise user isolation. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and Operational Risks

Proper allowlist usage is critical for maintaining cluster isolation and protecting data on standard access mode compute. Users with `MANAGE ALLOWLIST` privileges can allowlist any path or Maven coordinate, effectively controlling what code runs on standard access mode compute. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. Databricks recommends that [Metastore](/concepts/metastore.md) admins periodically review allowlist contents and verify artifacts come from trusted sources. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Best Practices

Databricks recommends the following practices for managing the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

## Managing the Allowlist

### Prerequisites

To modify the allowlist, users must have the `MANAGE ALLOWLIST` privilege. See [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) for details. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Items can be added to the allowlist using [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Adding Items in Catalog Explorer

To open the allowlist dialog in Catalog Explorer: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. Click the **Catalog** icon.
2. Click the gear icon to open settings.
3. Click the [Metastore](/concepts/metastore.md) name to open the [Metastore](/concepts/metastore.md) details and permissions UI.
4. Select **Allowed JARs/Init Scripts**.
5. Click **Add**.

This option only appears for users with the `MANAGE ALLOWLIST` privilege. If the UI is not accessible, contact a [metastore admin](/concepts/metastore-admin-role.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Adding an Init Script

To add an init script to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **Init Script**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path.

### Adding a JAR

To add a JAR to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **JAR**.
2. For **Source Type**, select **Volume** or the object storage protocol.
3. Specify the source path.

### Adding Maven Coordinates

Before adding Maven coordinates, the user must have `CAN ATTACH TO` and `CAN MANAGE` permissions on the target compute. See Compute permissions. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

To add Maven coordinates: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. For **Type**, select **Maven**.
2. For **Source Type**, select **Coordinates**.
3. Enter coordinates in the format `groupId:artifactId:version`.

Wildcard patterns are supported:
- `groupId:artifactId` — includes all versions of a library.
- `groupId` — includes all artifacts in a group.

## Path Permission Enforcement

When paths are added to the allowlist, prefix matching is used for all artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` adds all files and directories within that path without performing prefix matching on names beginning with `prod-libraries`. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Permissions can be defined at three levels: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. The base path for the volume or storage container.
2. A directory nested at any depth.
3. A single file.

Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still enforces data access permissions for the specified location. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Identity and Access Requirements

The principal used must have `READ VOLUME` permissions on the specified volume. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Identity assignment varies by access mode:
- **Dedicated access mode** (formerly single user access mode): Uses the identity of the assigned principal (user or group).
- **Standard access mode**: Libraries use the identity of the library installer; init scripts use the identity of the cluster owner.
- **No-isolation shared access mode**: Does not support volumes but uses the same identity assignment as standard access mode.

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations could potentially modify code in library files or init scripts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

For S3 storage, Databricks recommends using instance profiles to manage access. See Configure S3 access with an instance profile. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Separate Permissions for JARs and Init Scripts

Allowlist permissions for JARs and init scripts are managed separately. If the same location is used to store both types of objects, the location must be added to the allowlist for each type. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides the allowlist capability.
- [Standard Access Mode](/concepts/standard-access-mode.md) — The compute access mode that requires allowlisting.
- [Init scripts](/concepts/init-script-allowlisting.md) — Custom scripts that run during cluster initialization.
- [Libraries on Databricks](/concepts/manual-library-installation-on-databricks.md) — Overview of installing and managing libraries.
- [Metastore admin privileges](/concepts/metastore-admin-ownership-privileges.md) — The administrative role that can manage the allowlist.
- Unity Catalog volumes — Managed storage volumes for Unity Catalog.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
