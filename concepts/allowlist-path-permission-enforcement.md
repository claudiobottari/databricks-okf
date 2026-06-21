---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ddd5e0af00edba0cfb45dad171fddc966b9eb226a099f481131e7446b26baa0
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlist-path-permission-enforcement
    - APPE
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlist Path Permission Enforcement
description: The mechanism by which allowlist entries use prefix matching on paths in Unity Catalog volumes or object storage, supporting permissions at base path, nested directory, or single file levels, with trailing slashes controlling prefix matching scope.
tags:
  - unity-catalog
  - permissions
  - paths
timestamp: "2026-06-19T17:32:44.157Z"
---

# Allowlist Path Permission Enforcement

**Allowlist Path Permission Enforcement** refers to the rules by which Databricks validates access to JARs and init scripts that have been added to the Unity Catalog allowlist. The allowlist controls which libraries and init scripts can run on standard access mode compute. When a path is allowlisted, Databricks still enforces independent data-access permissions to ensure that the principal using the artifact has the right to read the underlying files. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Prefix Matching and Scope

Permission enforcement for allowlisted paths uses **prefix matching**. If a directory path is added (rather than a single file), the allowlist permission propagates to all contained files and subdirectories. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` does **not** match files that begin with `prod-libraries`; instead it adds all files and directories **within** `/Volumes/prod-libraries/` to the allowlist. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Permissions can be defined at any of the following granularity levels:

1. The base path for the volume or storage container.
2. A directory nested at any depth from the base path.
3. A single file. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Identity Used for Access Checks

The principal whose permissions are checked depends on the compute access mode:

- **Dedicated access mode** (formerly single user access mode): the identity of the assigned principal (a user or group) is used. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- **Standard access mode**: for libraries, the identity of the library installer is used; for init scripts, the identity of the cluster owner is used. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- **No-isolation shared access mode**: does not support volumes but follows the same identity assignment as standard access mode. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

The principal must have `READ VOLUME` permission on the volume containing the allowlisted artifact. Databricks recommends configuring all object storage privileges related to init scripts and libraries with **read-only** permissions to prevent unauthorized modification of code. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Storage in Volumes vs. Object Storage

Allowlisted paths can point to files stored in Unity Catalog volumes or external object storage (such as S3). When object storage is used, Databricks recommends using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) to manage access. The instance profile should be set up with read and list permissions on the desired buckets, and the cluster should be launched with that instance profile. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Important Notes

- Adding a path to the allowlist only means the path **can be used** for init scripts or JAR installation; it does **not** grant data access. Separate permissions (e.g., `READ VOLUME`) are still enforced. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- Allowlist permissions for JARs and init scripts are managed separately. If the same location stores both types of objects, you must add the location to the allowlist for **each type**. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Allowlist](/concepts/unity-catalog-allowlist.md)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)
- READ VOLUME privilege
- [Standard Access Mode](/concepts/standard-access-mode.md)
- [Dedicated access mode](/concepts/dedicated-access-mode-for-ml-compute.md)
- [Init scripts](/concepts/init-script-allowlisting.md)
- Libraries
- [Instance profiles](/concepts/instance-profile-databricks-on-aws.md)

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
