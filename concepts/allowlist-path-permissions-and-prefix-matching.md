---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5d4f5ab67771ab6e50252adb5274059d3cbea0f48cafb9dbae098a8c35af724
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlist-path-permissions-and-prefix-matching
    - Prefix Matching and Allowlist Path Permissions
    - APPAPM
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlist Path Permissions and Prefix Matching
description: Rules governing how file paths and directories are matched in the allowlist, including prefix matching, trailing slash semantics, and the requirement for READ VOLUME permissions on volumes.
tags:
  - unity-catalog
  - permissions
  - paths
timestamp: "2026-06-19T22:07:32.001Z"
---

# Allowlist Path Permissions and Prefix Matching

**Allowlist Path Permissions and Prefix Matching** describes how Unity Catalog allowlist permissions propagate to contained files and directories when a directory path (rather than a single file) is added to the allowlist. The mechanism uses prefix matching, with a trailing slash (`/`) to limit the scope of matching.

## Path Permission Propagation

When you add a path for a directory rather than a file to the Unity Catalog allowlist, the permissions propagate to all files and directories contained within that directory. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Prefix Matching Behavior

Prefix matching is used for all artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` will **not** perform prefix matching for files that begin with the string `prod-libraries`. Instead, all files and directories within `/Volumes/prod-libraries/` are added to the allowlist as a set. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Permission Levels

You can define permissions at any of the following granularities: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- The base path for the volume or storage container.
- A directory nested at any depth from the base path.
- A single file.

## Data Access Checks

Adding a path to the allowlist means only that the path is permitted for use with init scripts or JAR installation. Databricks still enforces standard data-access permissions on the specified location. The principal used must have `READ VOLUME` permission on the volume. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Identity Assignment

- In dedicated access mode (formerly single user access mode), the identity of the assigned principal (a user or group) is used for the data access check. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- In standard access mode (formerly shared access mode):
  - Libraries use the identity of the library installer.
  - Init scripts use the identity of the cluster owner. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- No-isolation shared access mode does not support volumes, but uses the same identity assignment as standard access mode. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security Recommendations

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on those locations could potentially modify the code in library files or init scripts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Use instance profiles to manage access to JARs or init scripts stored in S3. To set this up, create an IAM role with read and list permissions on the desired buckets, then launch a cluster with that instance profile. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Separate Allowlist for JARs and Init Scripts

Allowlist permissions for JARs and init scripts are managed separately. If you use the same location to store both types of objects, you must add the location to the allowlist for each type. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- Unity Catalog volumes
- [Standard Access Mode](/concepts/standard-access-mode.md)
- [Init scripts](/concepts/init-script-allowlisting.md)
- [Library installation on compute](/concepts/manual-library-installation-on-databricks.md)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
