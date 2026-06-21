---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d0be7fe2632fad1d3583dd139140576497f6d0d29a3493de771415dabb6ddeb
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - unity-catalog-setup-guide-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-metastore
    - UCM
    - Create a Unity Catalog Metastore
    - Create a Unity Catalog metastore
    - Manage Unity Catalog Metastores
    - Manage Unity Catalog metastores
    - Unified Catalog Metastore
    - Unity Catalog metastores
    - Create and link metastores
    - Unified Catalog Metastore|metastore
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md; enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
    - file: manage-unity-catalog-metastores-databricks-on-aws.md; unity-catalog-setup-guide-databricks-on-aws.md
title: Unity Catalog Metastore
description: The top-level container for data in Unity Catalog that registers metadata about securable objects and permissions, exposing a three-level namespace.
tags:
  - unity-catalog
  - data-governance
  - metastore
timestamp: "2026-06-19T17:57:34.745Z"
---

# Unity Catalog [Metastore](/concepts/metastore.md)

The **Unity Catalog metastore** is the top-level container for all data assets, metadata, and access policies in [Unity Catalog](/concepts/unity-catalog.md). It is scoped to a single cloud region and holds every securable object registered in Unity Catalog — catalogs, schemas, tables, volumes, functions, storage credentials, external locations, connections, shares, providers, recipients, and clean rooms. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md] Each [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`) by which data can be organized and governed. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Key Characteristics

- **Regional scope**: Create one [Metastore](/concepts/metastore.md) per AWS region where your organization operates. Multiple workspaces in the same region can share a single [Metastore](/concepts/metastore.md), giving them the same view of data and enabling centralized access control. ^[create-a-unity-catalog-metastore-databricks-on-aws.md; enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Top-level securable**: The [Metastore](/concepts/metastore.md) itself is a securable object on which administrative privileges (such as `CREATE CATALOG` and `CREATE STORAGE CREDENTIAL`) can be granted. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]
- **Managed storage (optional)**: You can attach an S3 bucket as the metastore-level storage root for [Managed Table](/concepts/unity-catalog-managed-tables.md) and Volume data. This storage root can be overridden at the [Catalog and Schema](/concepts/catalog-and-schema.md) levels. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- **Metastore admin**: The user who creates the [Metastore](/concepts/metastore.md) becomes its owner ([Metastore](/concepts/metastore.md) admin). Databricks recommends transferring this role to a group. [Metastore](/concepts/metastore.md) admins can create top-level objects and manage access across all workspaces attached to the [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Creating a [Metastore](/concepts/metastore.md)

To create a [Metastore](/concepts/metastore.md), you must be a Databricks account admin. The process involves:

1. **Optional**: In your AWS account, create an S3 bucket to serve as the metastore-level managed storage location. The bucket must be in the same region as the workspaces that will access the data, and cannot use dot notation in the bucket name. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
2. **Optional**: Create an IAM role in AWS with a trust policy that grants Databricks access to the S3 bucket. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
3. In the Databricks account console, navigate to **Catalog** > **Create metastore**, provide a name, region, and optionally the S3 bucket path and IAM role name. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
4. Assign one or more workspaces to the [Metastore](/concepts/metastore.md) to enable Unity Catalog for those workspaces. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
5. Transfer the [Metastore](/concepts/metastore.md) admin role to a group. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
6. Enable CORS on the S3 bucket to permit Databricks-managed uploads to managed volumes. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

For workspaces enabled automatically on or after November 8, 2023, these steps are not required — Databricks creates and assigns a [Metastore](/concepts/metastore.md) automatically. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Enabling a Workspace for Unity Catalog

Enabling a workspace for Unity Catalog means assigning a [Metastore](/concepts/metastore.md) to that workspace. This allows users in the workspace to access data governed by the [Metastore](/concepts/metastore.md), enables automatic audit logging, and centralizes identity management through the account console. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

- Workspaces can be assigned to a [Metastore](/concepts/metastore.md) at creation time or later via the account console. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- Consider workspace-catalog bindings to limit catalog access by workspace boundaries. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- Enabling Unity Catalog is irreversible; identity management must thereafter use account-level SCIM provisioning. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Managing Metastores

### Auto-Assignment of New Workspaces

Account admins can enable automatic [Metastore](/concepts/metastore.md) assignment for new workspaces in the [Metastore](/concepts/metastore.md)'s region. When enabled, new workspaces are automatically attached, a workspace catalog is created, and workspace admins receive default privileges to create metastore-level securable objects. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### Adding or Removing Managed Storage

- **Add storage**: Create an external location in Unity Catalog that points to the S3 bucket, grant yourself `CREATE MANAGED STORAGE` on that location, then set the S3 bucket path in the [Metastore](/concepts/metastore.md) configuration from the account console. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- **Remove storage**: Removing the [Metastore](/concepts/metastore.md) storage root pushes the storage root down to existing catalogs that do not have their own storage root, creating an external location named `prior_metastore_root_location` if needed. Subsequently, every new catalog must provide a dedicated storage location. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### [Metastore](/concepts/metastore.md) Admins

Assigning a [Metastore](/concepts/metastore.md) admin is optional but recommended for delegating governance tasks such as creating catalogs, managing the init script allowlist, or receiving shared data via [OpenSharing](/concepts/opensharing.md). [Metastore](/concepts/metastore.md) admins can be assigned or changed from the account console. ^[manage-unity-catalog-metastores-databricks-on-aws.md; unity-catalog-setup-guide-databricks-on-aws.md]

### Deleting a [Metastore](/concepts/metastore.md)

Deleting a [Metastore](/concepts/metastore.md) is irreversible. All objects managed by the [Metastore](/concepts/metastore.md) become inaccessible from Databricks workspaces. Managed table data and metadata are auto-deleted after 30 days; external table data in cloud storage is not affected. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Related Concepts

- [Catalog](/concepts/unity-catalog.md) – The top-level data container within a [Metastore](/concepts/metastore.md).
- Schema – The second-level container within a catalog.
- Table – The primary structured data object.
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) – Authentication information for cloud storage access.
- [External location](/concepts/external-location.md) – A path in cloud storage paired with a storage credential.
- Volume – A securable object for unstructured data.
- [OpenSharing](/concepts/opensharing.md) – Mechanism for sharing data across metastores or organizations.
- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table whose storage location is determined by Unity Catalog.
- Workspace – A Databricks environment that can be attached to a [Metastore](/concepts/metastore.md).

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md
- enable-a-workspace-for-unity-catalog-databricks-on-aws.md
- manage-unity-catalog-metastores-databricks-on-aws.md
- unity-catalog-securable-objects-reference-databricks-on-aws.md
- unity-catalog-setup-guide-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
2. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
3. create-a-unity-catalog-metastore-databricks-on-aws.md; enable-a-workspace-for-unity-catalog-databricks-on-aws.md
4. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
5. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
6. manage-unity-catalog-metastores-databricks-on-aws.md; unity-catalog-setup-guide-databricks-on-aws.md
