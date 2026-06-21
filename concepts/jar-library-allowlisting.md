---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 894bc6fc83c170e9d569f3fec7feabdcdb2f0565ee625e0bf1962a86cfcb82bf
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-library-allowlisting
    - JLA
    - Library allowlisting
    - JAR Allowlist
    - JAR Allowlisting
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: JAR Library Allowlisting
description: The process of adding JAR artifacts to the Unity Catalog allowlist from Volumes or object storage, where the identity of the library installer is used for permissions in standard access mode.
tags:
  - jars
  - libraries
  - unity-catalog
timestamp: "2026-06-19T08:59:07.808Z"
---

```markdown
---
title: JAR Library Allowlisting
summary: A Unity Catalog security feature that controls which JAR libraries can be installed on standard access mode compute clusters through a metastore-level allowlist managed by the `MANAGE ALLOWLIST` privilege.
sources:
  - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - unity-catalog
  - security
  - compute
  - libraries
aliases:
  - jar-allowlist
  - library-allowlisting
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# JAR Library Allowlisting

**JAR library allowlisting** is a [[Unity Catalog]] security feature that controls which JAR files can be used on [[standard access mode]] compute clusters (formerly shared access mode). The allowlist is a metastore-level list managed by principals who hold the `MANAGE ALLOWLIST` privilege. By default, the allowlist is empty and cannot be disabled. Users without this privilege cannot see the allowlist UI and must contact their [[Metastore Admin Role|metastore admin]] for assistance. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Overview

The allowlist restricts the libraries that can run on standard access mode compute, reducing the risk of security issues, cluster instability, and other unpredictable behavior. To modify the allowlist, a user must have the `MANAGE ALLOWLIST` privilege on the [[metastore|Metastore]]. The allowlist can be managed using [[Catalog Explorer]] or the Databricks Artifact Allowlists API. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding a JAR to the Allowlist

A JAR can be added to the allowlist using Catalog Explorer or the REST API. The source path can point to a directory or a single file. The path can be specified even if the file or directory hasn't been created yet. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Using Catalog Explorer

To add a JAR via the UI: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. In your Databricks workspace, click **Catalog**.
2. Click the gear icon to open the [[metastore|Metastore]] details and permissions UI.
3. Select **Allowed JARs/Init Scripts**.
4. Click **Add**.
5. For **Type**, select **JAR**.
6. For **Source Type**, select **Volume** or the object storage protocol (e.g., `s3://`).
7. Specify the source path to add to the allowlist.

### Using the REST API

The allowlist can also be managed programmatically via the `ArtifactAllowlists` API endpoint. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding Maven Coordinates to the Allowlist

Maven libraries can also be allowlisted using coordinates. Before adding Maven coordinates, you must have `CAN ATTACH TO` and `CAN MANAGE` permissions on the compute where you intend to install the library. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

To add Maven coordinates via Catalog Explorer: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

1. Follow steps 1–4 above.
2. For **Type**, select **Maven**.
3. For **Source Type**, select **Coordinates**.
4. Enter coordinates in one of the following formats:
   - `groupId:artifactId:version` – allowlists a specific version.
   - `groupId:artifactId` – allowlists all versions of that artifact.
   - `groupId` – allowlists all artifacts in that group.

## Permissions on Paths

Path-based allowlist entries support prefix matching. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` adds all files and directories within that volume but does not match files prefixed with `prod-libraries` outside that exact path. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Paths can be specified at the following granularity levels: ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- The base path for a volume or storage container.
- A directory nested at any depth.
- A single file.

Adding a path to the allowlist only permits the path to be used for library installation. It does not grant data access. The caller must still have `READ VOLUME` permission on the volume (for paths in Unity Catalog volumes) or appropriate object storage permissions. For S3, Databricks recommends using [[Instance Profile (Databricks on AWS)|instance profiles]] with a read-only IAM role. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

On standard access mode clusters, JAR library installation uses the identity of the library installer, while init scripts use the identity of the cluster owner. In dedicated access mode (formerly single user mode), the identity of the assigned principal (user or group) is used. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Security and Operational Risks

The allowlist is a critical security control. Users with `MANAGE ALLOWLIST` privileges can allowlist any path or Maven coordinate, effectively controlling what code can run on standard access mode compute. Databricks recommends that [[metastore|Metastore]] admins periodically review allowlisted items and verify they come from trusted sources. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security governance as other sensitive components. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Some installed libraries may store data of all users in a common temp directory, which can compromise user isolation on shared clusters. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Best Practices

- Grant `MANAGE ALLOWLIST` only to [[metastore|Metastore]] admins and trusted platform administrators. For others, grant it only on a temporary, as-needed basis. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- Review and audit allowlist additions regularly.
- Use specific paths and Maven coordinates rather than broad patterns.
- Configure storage locations for allowlisted artifacts with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

Additionally, allowlist permissions for JARs and init scripts are managed separately. If the same location stores both types of objects, the location must be added to the allowlist for each type individually. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [[Standard Access Mode]] – The compute access mode that enforces Unity Catalog allowlists.
- [[Unity Catalog Metastore]] – The top-level container for Unity Catalog metadata and privileges.
- [[MANAGE ALLOWLIST Privilege|MANAGE ALLOWLIST]] – The privilege required to modify the allowlist.
- Unity Catalog Volumes – Storage locations that can be referenced in allowlist paths.
- [[Init Script Allowlisting]] – Similar feature for cluster init scripts.
- Databricks Library Management – Broader topic of installing libraries on clusters.
- Maven Coordinates – Format used to identify Maven artifacts.
- Data Governance – The overarching security model.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
```

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
