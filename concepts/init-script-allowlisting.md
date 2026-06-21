---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85aa95616b3bfd71780f9949799e4c48fa55d5fbbd28b29d505a25420f918015
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - init-script-allowlisting
    - ISA
    - Init Scripts in Allowlist
    - Init Scripts
    - Init scripts
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Init Script Allowlisting
description: The process of adding cluster init scripts to the Unity Catalog allowlist from Volumes or object storage, where the identity of the cluster owner is used for permissions in standard access mode.
tags:
  - init-scripts
  - unity-catalog
  - databricks
timestamp: "2026-06-19T08:58:43.688Z"
---

# Init Script Allowlisting

**Init script allowlisting** is Unity Catalog's control mechanism that determines which init scripts can run on compute configured with [Standard Access Mode](/concepts/standard-access-mode.md) (formerly shared access mode). In Databricks Runtime 13.3 LTS and above, the `allowlist` in Unity Catalog governs both libraries and init scripts, preventing arbitrary artifacts from executing on these clusters. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

By default the allowlist is empty. It cannot be disabled. Only users with the `MANAGE ALLOWLIST` privilege can modify the allowlist. See [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Adding an Init Script to the Allowlist

Init scripts can be added to the allowlist using [Catalog Explorer](/concepts/catalog-explorer.md) or the REST API. To add an init script via Catalog Explorer:

1. In your Databricks workspace, click **Catalog**.
2. Click the gear icon to open the [Metastore](/concepts/metastore.md) details and permissions UI.
3. Select **Allowed JARs/Init Scripts**.
4. Click **Add**.
5. For **Type**, select **Init Script**.
6. For **Source Type**, select **Volume** or the object storage protocol.
7. Specify the source path to add to the allowlist.

The **Add** option only displays for users with `MANAGE ALLOWLIST` on the [Metastore](/concepts/metastore.md). If the UI is not visible, contact your [Metastore](/concepts/metastore.md) admin. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

A directory or file can be added to the allowlist even if it has not yet been created. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## How Path Permissions Are Enforced

You can grant access to init scripts stored in Unity Catalog volumes or object storage. If you add a path for a directory rather than a file, allowlist permissions propagate to all contained files and subdirectories. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Prefix matching is used for all artifacts stored in volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` will not perform prefix matching for files prefixed with `prod-libraries`; instead all files and directories within that path are added to the allowlist. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Permissions can be defined at three levels:
- The base path for the volume or storage container.
- A directory nested at any depth from the base path.
- A single file.

Adding a path to the allowlist only permits the path to be used for init scripts or JAR installation. Databricks still checks for data access permissions on the specified location. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Identity Used for Access

- **Init scripts** stored in volumes use the identity of the cluster owner. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- For init scripts in object storage, Databricks recommends using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) with read and list permissions on the desired buckets.
- The principal must have `READ VOLUME` permission on the specified volume. See READ VOLUME privilege.

## Security and Operational Risks

Understanding allowlist security is critical for maintaining cluster isolation on standard access mode compute. Proper allowlist usage reduces the likelihood of security issues, cluster instability, and other unpredictable behavior. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks recommends these best practices:
- Grant `MANAGE ALLOWLIST` only to [Metastore](/concepts/metastore.md) admins and trusted platform administrators. For other users, grant it only on a temporary, as-needed basis.
- Review and audit allowlist additions regularly.
- Use specific paths rather than broad patterns.
- Configure storage locations with read-only permissions.
- Implement a formal approval process for allowlist additions in production environments.
- Test allowlisted init scripts in non-production environments before adding them to production allowlists.

[Metastore](/concepts/metastore.md) admins should periodically review items on the allowlist and verify they come from trusted sources, as allowlisted artifacts can access cluster resources and user data. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Separate Management of Init Scripts and JARs

Allowlist permissions for init scripts and JARs are managed separately. If the same storage location contains both types of objects, the location must be added to the allowlist for each type individually. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Standard Access Mode](/concepts/standard-access-mode.md)
- [Init scripts](/concepts/init-script-allowlisting.md)
- Unity Catalog volumes
- [Instance profiles](/concepts/instance-profile-databricks-on-aws.md)
- READ VOLUME privilege
- Library allowlisting

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
