---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10cb139f7aa3e2808af78ee7312189428dfc2a7763f7643677c6e43ac02484e1
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlist-security-best-practices
    - ASBP
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlist Security Best Practices
description: Recommended practices for managing the Unity Catalog allowlist, including granting MANAGE ALLOWLIST sparingly, using specific paths, read-only storage, and formal approval processes.
tags:
  - security
  - best-practices
  - unity-catalog
timestamp: "2026-06-19T22:05:39.342Z"
---

# Allowlist Security Best Practices

**Allowlist security best practices** are guidelines for managing the Unity Catalog allowlist, which controls which libraries and init scripts can run on standard access mode compute. Proper allowlist management reduces security risks, cluster instability, and unpredictable behavior associated with arbitrary code execution on shared compute infrastructure. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

In Databricks Runtime 13.3 LTS and above, the `allowlist` in [Unity Catalog](/concepts/unity-catalog.md) controls which libraries and init scripts can run on [Standard Access Mode Compute](/concepts/standard-access-mode-compute.md). The allowlist is empty by default and cannot be disabled. Only users with the `MANAGE ALLOWLIST` privilege can modify it. Understanding the security implications of allowlists is critical for maintaining cluster isolation and protecting data on standard access mode compute. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Privilege Management

Be deliberate about who receives `MANAGE ALLOWLIST` privileges. Users with this privilege can allowlist any path or Maven coordinate, effectively controlling what code runs on standard access mode compute. Databricks recommends granting `MANAGE ALLOWLIST` only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it only on a temporary, as-needed basis. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Regular Review and Audit

As [Metastore](/concepts/metastore.md) admin, periodically review items on the allowlist and verify they come from trusted sources. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Use Specific Paths and Coordinates

Use specific paths and Maven coordinates rather than broad patterns. When adding Maven coordinates, specify `groupId:artifactId:version` for precise version control. Broader patterns like `groupId:artifactId` (all versions) or `groupId` (all artifacts) increase the attack surface. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Configure Read-Only Storage Locations

Configure all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions can potentially modify code in library files or init scripts. Databricks recommends using [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) to manage access to JARs or init scripts stored in S3: create an IAM role with read and list permissions on desired buckets, then launch a cluster with that instance profile. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Implement Formal Approval Processes

Implement a formal approval process for allowlist additions in production environments. Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Understanding Path Permissions

When adding paths to the allowlist, prefix matching is used for all artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` adds all files and directories within that path, not files prefixed with `prod-libraries`. Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still checks for data access permissions. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

The principal must have `READ VOLUME` permission on the specified [Unity Catalog Volumes|volume](/concepts/unity-catalog-volumes-for-ml-data.md). In dedicated access mode, the assigned principal's identity is used. In standard access mode, libraries use the identity of the library installer, and init scripts use the identity of the cluster owner. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Separate Allowlists for JARs and Init Scripts

Allowlist permissions for JARs and init scripts are managed separately. If you use the same location to store both types of objects, you must add the location to the allowlist for each type. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Additional Security Considerations

Some installed libraries store data of all users in one common temp directory, which might compromise user isolation on standard access mode compute. Additionally, libraries used as JDBC drivers or custom Spark data sources on Unity Catalog-enabled standard compute require `ANY FILE` permissions. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution providing allowlist capabilities.
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) — The privilege required to modify the allowlist.
- [Standard Access Mode Compute](/concepts/standard-access-mode-compute.md) — The compute configuration where allowlists apply.
- [Init Scripts](/concepts/init-script-allowlisting.md) — Scripts that can be allowlisted for standard access mode.
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — Recommended mechanism for managing S3 access to stored artifacts.
- Unity Catalog Volumes — Storage location for allowlisted artifacts.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
