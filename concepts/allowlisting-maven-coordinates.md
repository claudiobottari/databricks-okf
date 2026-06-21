---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 407ecb57f3ba6ace49b76cb676a2e5a0bfd1d1e7f2dc3aad56fce48ee525bd0f
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allowlisting-maven-coordinates
    - AMC
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Allowlisting Maven Coordinates
description: The process of adding Maven coordinates (groupId:artifactId:version) to the Unity Catalog allowlist, including wildcard patterns for versions and group IDs.
tags:
  - maven
  - libraries
  - unity-catalog
timestamp: "2026-06-19T22:05:51.255Z"
---

# Allowlisting Maven Coordinates

**Allowlisting Maven Coordinates** is the process of registering specific Maven artifacts (JAR libraries) in the Unity Catalog allowlist so that they can be installed on compute with standard access mode (formerly shared access mode). The allowlist is a security control that prevents arbitrary libraries from running on shared compute, and by default it is empty. Only users with the `MANAGE ALLOWLIST` privilege can add entries to it. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Required Permissions

Before a Maven coordinate can be added to the allowlist, the user must have **CAN ATTACH TO** and **CAN MANAGE** permissions on the target compute resource where the library will be installed. These compute permissions are separate from the `MANAGE ALLOWLIST` privilege required to modify the allowlist itself. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Maven Coordinates

Maven coordinates can be added to the allowlist through [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. The procedure in Catalog Explorer is as follows:

1. In the allowlist dialog, set **Type** to **Maven**.
2. Set **Source Type** to **Coordinates**.
3. Enter the coordinates in the format `groupId:artifactId:version`.

The allowlist supports three levels of granularity:
- **A specific version**: `groupId:artifactId:version` (e.g., `com.example:my-lib:1.0.0`)
- **All versions of an artifact**: `groupId:artifactId` (e.g., `com.example:my-lib`)
- **All artifacts in a group**: `groupId` (e.g., `com.example`)

Broad patterns (group-only or group+artifact without version) allow any version or any artifact within the specified group. Use the most specific pattern possible to reduce security risk. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security Considerations

Adding Maven coordinates to the allowlist grants permission for the corresponding JAR to be used on standard access mode compute. Because allowlisted libraries can access cluster resources and user data, Databricks recommends:
- Granting `MANAGE ALLOWLIST` only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators.
- Using specific group-artifact-version coordinates rather than broad patterns.
- Periodically reviewing and auditing allowlisted entries.
- Testing libraries in non-production environments before allowlisting in production. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Also note that JDBC drivers and custom Spark data sources on Unity Catalog‑enabled standard compute require **`ANY FILE`** permissions in addition to the allowlist entry. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Allowlist](/concepts/unity-catalog-allowlist.md) — Central control for libraries and init scripts on standard access mode.
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) — Required to modify the allowlist.
- [Standard Access Mode](/concepts/standard-access-mode.md) — Compute mode that enforces the allowlist.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for managing Unity Catalog objects and the allowlist.
- [Maven coordinates](/concepts/maven-coordinates-in-allowlist.md) — Standard identifier format for Java/Scala libraries.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
