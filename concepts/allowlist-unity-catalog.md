---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1194985af896c47d61880841e77e68126e8843c838f6d1da80d6b7da0df42d0e
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlist-unity-catalog
    - A(C
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlist (Unity Catalog)
description: A Databricks Unity Catalog feature that controls which libraries (JARs, Maven artifacts) and init scripts can run on standard access mode compute, enhancing security and isolation.
tags:
  - unity-catalog
  - security
  - databricks
  - governance
timestamp: "2026-06-18T14:24:59.173Z"
---

# Allowlist (Unity Catalog)

The **allowlist** in [Unity Catalog](/concepts/unity-catalog.md) controls which libraries and init scripts can run on compute configured with **standard access mode** (formerly shared access mode). It is available in Databricks Runtime 13.3 LTS and above. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

By default, the allowlist is empty and cannot be disabled. To add or manage entries, you must have the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). See the [MANAGE ALLOWLIST](/concepts/manage-allowlist-privilege.md) privilege reference. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and operational risks

Understanding the implications of the allowlist is critical for maintaining cluster isolation and protecting data on standard access mode compute. Proper management prevents users from adding arbitrary libraries and init scripts, reducing the likelihood of security issues, cluster instability, and other unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Grant `MANAGE ALLOWLIST` only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant this privilege only on a temporary, as-needed basis. Databricks recommends the following best practices: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

Users with `MANAGE ALLOWLIST` can allowlist any path or Maven coordinate, effectively controlling what code can run. As the [Metastore](/concepts/metastore.md) admin, periodically review items and verify they come from trusted sources. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding items to the allowlist

You can add items using [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API (see [Artifact Allowlists API](https://docs.databricks.com/api/workspace/artifactallowlists)). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

In Catalog Explorer:
1. Click **Catalog**.
2. Click the gear icon to open the [Metastore](/concepts/metastore.md) details and permissions UI.
3. Click the [Metastore](/concepts/metastore.md) name.
4. Select **Allowed JARs/Init Scripts**.
5. Click **Add**.

This option only displays for users with `MANAGE ALLOWLIST` on the [Metastore](/concepts/metastore.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Add an init script

In the allowlist dialog:
1. **Type**: Select **Init Script**.
2. **Source Type**: Select **Volume** or the object storage protocol.
3. Specify the source path. See [Permissions on paths](#how-are-permissions-on-paths-enforced-in-the-allowlist). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Add a JAR

In the allowlist dialog:
1. **Type**: Select **JAR**.
2. **Source Type**: Select **Volume** or the object storage protocol.
3. Specify the source path. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Add Maven coordinates

Before adding Maven coordinates, you must have `CAN ATTACH TO` and `CAN MANAGE` permissions on the compute where the library will be installed. See Compute permissions. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

In the allowlist dialog:
1. **Type**: Select **Maven**.
2. **Source Type**: Select **Coordinates**.
3. Enter coordinates in the format `groupId:artifactId:version`.
   - You can include all versions by allowlisting `groupId:artifactId`.
   - You can include all artifacts in a group by allowlisting `groupId`. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## How are permissions on paths enforced in the allowlist?

You can grant access to JARs or init scripts stored in Unity Catalog volumes or object storage. If you add a directory rather than a file, allowlist permissions propagate to contained files and directories. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Prefix matching is used for all artifacts stored in volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` does not perform prefix matching for files prefixed with `prod-libraries`; instead, all files and directories within that exact path are added. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Permissions can be defined at the following levels:
1. The base path for the volume or storage container.
2. A directory nested at any depth.
3. A single file.

Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location. The principal used must have `READ VOLUME` on the corresponding volume. See the READ VOLUME privilege. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

In dedicated access mode (formerly single user access mode), the identity of the assigned principal (a user or group) is used. In standard access mode:
- Libraries use the identity of the library installer.
- Init scripts use the identity of the cluster owner.

No-isolation shared access mode does not support volumes but uses the same identity assignment as standard access mode. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations could modify code in library files or init scripts. For JARs or init scripts stored in S3, use instance profiles: create an IAM role with read and list permissions on your buckets, then launch a cluster with that instance profile. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Allowlist permissions for JARs and init scripts are managed separately. If you use the same location to store both types, you must add the location to the allowlist for each. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MANAGE ALLOWLIST](/concepts/manage-allowlist-privilege.md)
- [Standard Access Mode](/concepts/standard-access-mode.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Init scripts](/concepts/init-script-allowlisting.md)
- Libraries
- [Volumes](/concepts/ucvolumedataset.md)
- READ VOLUME
- Compute permissions

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
