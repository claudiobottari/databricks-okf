---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82477bd3aea0127a6263d4466b6f122cd2ba04486457acd3c33124757dfdfc9e
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlist-path-prefix-matching
    - APPM
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlist Path Prefix Matching
description: The mechanism by which allowlist permissions propagate to contained files and directories, with trailing slashes controlling whether prefix matching is performed at a given directory level.
tags:
  - unity-catalog
  - security
  - paths
timestamp: "2026-06-19T14:00:21.862Z"
---

# Allowlist Path Prefix Matching

**Allowlist Path Prefix Matching** is a permission enforcement mechanism in [Unity Catalog](/concepts/unity-catalog.md) for artifacts stored in volumes or object storage. When a directory path is added to the allowlist, permissions automatically propagate to all files and subdirectories contained within that directory. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

The allowlist in [Unity Catalog](/concepts/unity-catalog.md) controls which libraries and init scripts can run on standard access mode compute. For artifacts stored in Unity Catalog volumes or object storage, prefix matching determines how permissions apply across directory structures. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Controlling Prefix Matching with Trailing Slashes

To prevent prefix matching at a specific directory level, include a trailing slash (`/`) in the allowlist path. For example, adding `/Volumes/prod-libraries/` to the allowlist does **not** perform prefix matching for files prefixed with `prod-libraries`. Instead, all files and directories **within** `/Volumes/prod-libraries/` are explicitly added to the allowlist. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Permission Levels for Path-Based Allowlisting

You can define permissions at the following levels:

1. **Base path** for the volume or storage container.
2. **A directory** nested at any depth from the base path.
3. **A single file**.

Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Access Requirements

The principal used must have `READ VOLUME` permissions on the specified volume. In dedicated access mode (formerly single user access mode), the identity of the assigned principal (a user or group) is used. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

In standard access mode:
- Libraries use the identity of the library installer.
- Init scripts use the identity of the cluster owner.

No-isolation shared access mode does not support volumes but uses the same identity assignment as standard access mode. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Best Practices

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations can potentially modify code in library files or init scripts. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks recommends using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) to manage access to JARs or init scripts stored in S3. This involves:
1. Creating an IAM role with read and list permissions on desired buckets.
2. Launching a cluster with the instance profile.

Allowlist permissions for JARs and init scripts are managed separately. If you use the same location to store both types of objects, you must add the location to the allowlist for each. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- Allowlist — The Unity Catalog control mechanism for libraries and init scripts
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) — The privilege required to modify the allowlist
- Unity Catalog Volumes — Storage locations for allowlisted artifacts
- [Standard Access Mode Compute](/concepts/standard-access-mode-compute.md) — The compute type requiring allowlisted artifacts
- [Init Scripts](/concepts/init-script-allowlisting.md) — Scripts that run during cluster initialization
- [Library Installation on Databricks](/concepts/manual-library-installation-on-databricks.md) — How JARs and Maven packages are installed

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
