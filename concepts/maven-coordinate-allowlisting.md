---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6befd937a6151468b460eba16579da64d52307dc45863f7f383d4de905df3cc
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - maven-coordinate-allowlisting
    - MCA
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Maven Coordinate Allowlisting
description: The process of adding Maven artifacts to the Unity Catalog allowlist using groupId:artifactId:version format, supporting wildcard patterns for all versions or all artifacts in a group.
tags:
  - maven
  - libraries
  - unity-catalog
timestamp: "2026-06-19T17:33:04.513Z"
---

# Maven Coordinate Allowlisting

**Maven Coordinate Allowlisting** is a feature in [Unity Catalog](/concepts/unity-catalog.md) that controls which Maven libraries can be installed on compute resources configured with [Standard Access Mode](/concepts/standard-access-mode.md) (formerly shared access mode). By adding Maven coordinates to the allowlist, administrators can permit users to leverage specific Maven artifacts while maintaining cluster isolation and security. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

In Databricks Runtime 13.3 LTS and above, the Unity Catalog allowlist governs which libraries and init scripts can run on standard access mode compute. The allowlist is empty by default, and this feature cannot be disabled. To modify the allowlist, users must have the `MANAGE ALLOWLIST` privilege. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Maven Coordinates to the Allowlist

Before adding Maven coordinates to the allowlist, you must have `CAN ATTACH TO` and `CAN MANAGE` permissions set on the compute where you intend to install the library. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Using Catalog Explorer

To add Maven coordinates through Catalog Explorer:

1. In your Databricks workspace, click **Catalog**.
2. Click the gear icon to open [Metastore](/concepts/metastore.md) settings.
3. Click the [Metastore](/concepts/metastore.md) name to open the [Metastore](/concepts/metastore.md) details and permissions UI.
4. Select **Allowed JARs/Init Scripts**.
5. Click **Add**.

This option only displays for users with the `MANAGE ALLOWLIST` privilege on the [Metastore](/concepts/metastore.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Coordinate Format

In the allowlist dialog, configure the following:

1. For **Type**, select **Maven**.
2. For **Source Type**, select **Coordinates**.
3. Enter coordinates in the following format: `groupId:artifactId:version`.

The allowlist supports three levels of granularity:

- **Specific version**: `groupId:artifactId:version` — allows only that exact library version.
- **All versions of an artifact**: `groupId:artifactId` — allows all versions of the specified library.
- **All artifacts in a group**: `groupId` — allows all artifacts within the specified Maven group.

^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and Operational Risks

Understanding the security implications of allowlists is critical for maintaining cluster isolation and protecting data on standard access mode compute. Proper allowlist usage prevents users from adding arbitrary libraries, reducing the likelihood of security issues, cluster instability, and other unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Users with `MANAGE ALLOWLIST` privileges can allowlist any Maven coordinate, effectively controlling what code can run on standard access mode compute. Databricks recommends the following best practices: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

- Grant the `MANAGE ALLOWLIST` privilege only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific Maven coordinates rather than broad patterns.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries in non-production environments before adding them to production allowlists.

As the [Metastore](/concepts/metastore.md) admin, periodically review items on the allowlist and verify that they come from trusted sources. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Important Considerations

Libraries used as JDBC drivers or custom Spark data sources on Unity Catalog-enabled standard compute require `ANY FILE` permissions. Additionally, some installed libraries store data of all users in one common temp directory, which might compromise user isolation. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides allowlist capabilities
- [Standard Access Mode](/concepts/standard-access-mode.md) — The compute access mode that requires allowlisted libraries
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) — The privilege required to modify the allowlist
- [Init Script Allowlisting](/concepts/init-script-allowlisting.md) — Allowlisting init scripts alongside Maven libraries
- [JAR Allowlisting](/concepts/jar-library-allowlisting.md) — Allowlisting JAR files stored in volumes or object storage

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
