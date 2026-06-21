---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de99a3d6eeb55eb8500142451b80f6587eba3da6db071c29bd278ce857a84eb0
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manage-allowlist-privilege
    - MAP
    - Map
    - map
    - MANAGE ALLOWLIST
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: MANAGE ALLOWLIST Privilege
description: A Unity Catalog privilege required to add or remove items from the allowlist; recommended to be granted only to metastore admins and trusted platform administrators.
tags:
  - unity-catalog
  - privileges
  - security
timestamp: "2026-06-19T22:05:37.897Z"
---

# MANAGE ALLOWLIST Privilege

The **MANAGE ALLOWLIST** privilege is a Unity Catalog privilege that controls who can modify the `allowlist` — the list of libraries and init scripts permitted to run on compute configured with standard access mode (formerly shared access mode). This privilege is granted at the [Metastore](/concepts/metastore.md) level and is required to add, review, or manage entries in the allowlist. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

In Databricks Runtime 13.3 LTS and above, the `allowlist` in Unity Catalog controls which libraries and init scripts can run on standard access mode compute. By default, the allowlist is empty. To modify it, users must have the `MANAGE ALLOWLIST` privilege. This feature cannot be disabled. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security Considerations

Understanding the security implications of the `MANAGE ALLOWLIST` privilege is critical for maintaining cluster isolation and protecting data on standard access mode compute. Proper allowlist management prevents users from adding arbitrary libraries and init scripts, reducing the likelihood of security issues, cluster instability, and other unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Users with `MANAGE ALLOWLIST` privileges can allowlist any path or Maven coordinate, effectively controlling what code can run on standard access mode compute. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Best Practices

Databricks recommends the following best practices for managing the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant the `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant `MANAGE ALLOWLIST` only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

As the [Metastore](/concepts/metastore.md) admin, periodically review items on the allowlist and verify that they come from trusted sources. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Using the Privilege

Users with the `MANAGE ALLOWLIST` privilege can add items to the allowlist using Catalog Explorer or the REST API. In Catalog Explorer, the allowlist management UI is accessed through the [Metastore](/concepts/metastore.md) details and permissions page. The **Allowed JARs/Init Scripts** option only displays for users who hold the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Items That Can Be Allowlisted

The `MANAGE ALLOWLIST` privilege enables users to add the following types of artifacts to the allowlist: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- **Init scripts** — stored in Unity Catalog volumes or object storage
- **JARs** — stored in Unity Catalog volumes or object storage
- **Maven coordinates** — specified in the format `groupId:artifactId:version`

### Path Permissions

When adding paths to the allowlist, prefix matching is used for artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). Permissions can be defined at the base path for the volume or storage container, a nested directory, or a single file. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Adding a path to the allowlist only means the path can be used for init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location. The principal used must have `READ VOLUME` permissions on the specified volume. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides the allowlist feature
- [Standard Access Mode](/concepts/standard-access-mode.md) — Compute mode that requires allowlisted libraries and init scripts
- [Init Scripts](/concepts/init-script-allowlisting.md) — Scripts that can be allowlisted for standard access mode compute
- Libraries — JARs and Maven artifacts that can be allowlisted
- [Metastore Admin](/concepts/metastore-admin-role.md) — Role that typically holds the MANAGE ALLOWLIST privilege
- READ VOLUME — Required permission for accessing allowlisted paths in volumes

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
