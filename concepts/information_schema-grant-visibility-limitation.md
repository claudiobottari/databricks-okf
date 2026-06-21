---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a11fed75c434ee93aab2186f5ada6f6b841f19d94c718baa5fdd78f34b1e3f74
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - information_schema-grant-visibility-limitation
    - IGVL
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: INFORMATION_SCHEMA Grant Visibility Limitation
description: Users with the MANAGE privilege on an object cannot view all grants for that object via INFORMATION_SCHEMA — only their own grants are shown. This is a known behavior gap slated for correction.
tags:
  - unity-catalog
  - information-schema
  - visibility
  - bugs
timestamp: "2026-06-19T19:27:39.091Z"
---

# INFORMATION_SCHEMA Grant Visibility Limitation

The **INFORMATION_SCHEMA Grant Visibility Limitation** is a known shortcoming in [Unity Catalog](/concepts/unity-catalog.md)'s permissions model where `INFORMATION_SCHEMA` queries do not return a complete view of all grants on an object for users who hold the `MANAGE` privilege on that object. Instead, such users see only their own grants when querying `INFORMATION_SCHEMA`. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Behavior

Users with the [`MANAGE` privilege](/en/data-governance/unity-catalog/manage-privileges/) on a Unity Catalog securable object normally have the authority to view and manage all grants on that object. However, when they query `INFORMATION_SCHEMA` to list grants, the system currently returns **only the user’s own grants**, not the full set of grants for the object. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

This limitation does **not** apply to other methods of viewing grants. Users with the `MANAGE` privilege (as well as [Metastore](/concepts/metastore.md) admins, object owners, and catalog/schema owners) can use the [`SHOW GRANTS` SQL command](/en/sql/language-manual/sql-ref-privileges) or [Catalog Explorer](/concepts/catalog-explorer.md) to see all grants on an object. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Future Correction

The documentation notes that this `INFORMATION_SCHEMA` behavior is a temporary limitation and **will be corrected in the future**. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Workaround

If you hold the `MANAGE` privilege on an object and need to see all grants, use one of the following alternatives instead of querying `INFORMATION_SCHEMA`:

- Run the `SHOW GRANTS ON <securable_type> <securable_name>` SQL command. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]
- Navigate to the object in **Catalog Explorer** and view the **Permissions** tab. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Permissions Model](/concepts/unity-catalog-permissions-model.md) – Background on privilege inheritance and the `MANAGE` privilege.
- [MANAGE Privilege](/concepts/manage-privilege.md) – The privilege that grants full administrative control over an object’s permissions.
- INFORMATION_SCHEMA – The system schema that provides metadata about securable objects and privileges.
- SHOW GRANTS Command – SQL syntax for viewing grants outside `INFORMATION_SCHEMA`.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for viewing and managing privileges.

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
