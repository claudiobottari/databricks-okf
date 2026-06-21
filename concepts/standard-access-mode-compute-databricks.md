---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a81113162f3a49e2705a18356980ea83589f2e7e6fb2fa4d5fd7beb03b4d3702
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - standard-access-mode-compute-databricks
    - SAMC(
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Standard access mode compute (Databricks)
description: A cluster access mode where identity of the library installer or cluster owner is used for access control; allowlisted libraries and init scripts are required to run on this mode with Unity Catalog.
tags:
  - databricks
  - compute
  - security
  - clusters
timestamp: "2026-06-18T14:24:53.408Z"
---

---

title: Standard access mode compute (Databricks)
summary: A compute configuration that enforces cluster isolation and Unity Catalog governance, with an allowlist controlling which libraries and init scripts can run.
sources:
  - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T13:05:00.000Z"
updatedAt: "2026-06-18T13:05:00.000Z"
tags:
  - databricks
  - compute
  - security
  - unity-catalog
aliases:
  - shared access mode compute
  - standard access mode
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# Standard access mode compute (Databricks)

**Standard access mode compute** (formerly called *shared access mode*) is a Databricks compute configuration designed for multi-user workloads where cluster isolation and [Unity Catalog](/concepts/unity-catalog.md) governance are required. It allows multiple users to run workloads on the same cluster while enforcing data access controls through Unity Catalog.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

A core requirement of standard access mode is that all libraries and init scripts running on the cluster must be explicitly allowlisted in Unity Catalog. This [Allowlist (Unity Catalog)](/concepts/allowlist-unity-catalog.md) controls which artifacts can be installed or executed, reducing security risks and preventing arbitrary code from running on the cluster.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and operational risks

Because allowlisted artifacts can access cluster resources and user data, they should be subject to the same security and governance controls as other sensitive components. Users with the `MANAGE ALLOWLIST` privilege can allowlist any path or Maven coordinate, effectively controlling what code runs on standard access mode compute. Databricks recommends that this privilege be granted only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators, and only on a temporary, as-needed basis for others.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Best practices include: granting `MANAGE ALLOWLIST` sparingly, reviewing and auditing allowlist additions regularly, using specific paths and Maven coordinates rather than broad patterns, configuring storage locations with read-only permissions, implementing a formal approval process for production allowlists, and testing artifacts in non-production environments before adding them to the production allowlist.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Allowlist management

The allowlist is managed through [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. By default, the allowlist is empty. To modify it, a user must have the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). This feature is always enabled and cannot be disabled.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Adding items to the allowlist

Users with `MANAGE ALLOWLIST` can add the following types of artifacts:

- **Init scripts** – Shell scripts that run during cluster startup.
- **JARs** – Java libraries stored in Unity Catalog volumes or object storage.
- **Maven coordinates** – Libraries from Maven repositories, specified in `groupId:artifactId:version` format. You can allowlist all versions of a library by omitting the version (`groupId:artifactId`) or all artifacts in a group (`groupId`).^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

To add an item in Catalog Explorer, navigate to the [Metastore](/concepts/metastore.md) details and permissions UI, select **Allowed JARs/Init Scripts**, and click **Add**. For each entry, select the type, source type (Volume or object storage protocol), and specify the path or coordinates.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Path permissions

When adding a path to the allowlist, prefix matching is used. To prevent prefix matching at a given directory level, include a trailing slash (`/`). Permissions can be defined at three levels: the base path for the volume or storage container, a nested directory, or a single file. Adding a path to the allowlist only permits the path to be used; Databricks still checks for data access permissions.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Access to allowlisted artifacts is enforced differently depending on the artifact type and the user identity:

- Libraries use the identity of the library installer.
- Init scripts use the identity of the cluster owner.
- For both JARs and init scripts stored in Unity Catalog volumes, the principal must have `READ VOLUME` permission on the volume.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks recommends using instance profiles with read-only permissions for object storage locations that contain allowlisted artifacts, and testing libraries and init scripts in non-production environments before adding them to production allowlists.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Differences from dedicated access mode

In dedicated access mode (formerly *single user access mode*), the identity of the assigned principal (a user or group) is used for all data access. In standard access mode, identity is determined per-run for libraries and init scripts as described above. Additionally, standard access mode enforces user isolation between concurrent users on the same cluster, while dedicated access mode assigns the cluster to a single user.^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Allowlist (Unity Catalog)](/concepts/allowlist-unity-catalog.md)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Init scripts on Databricks
- [Libraries on Databricks](/concepts/manual-library-installation-on-databricks.md)
- [Maven coordinates](/concepts/maven-coordinates-in-allowlist.md)
- [Instance profiles](/concepts/instance-profile-databricks-on-aws.md)
- [Dedicated access mode compute](/concepts/dedicated-access-mode-for-ml-compute.md)

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
