---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7cbdc93de6910ea7b94a62a6a341bbf63af07030603c4880078c79fcaaf55598
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privileges-for-external-lineage
    - PFEL
    - privileges-for-external-lineage-management
    - PFELM
  citations:
    - file: external-lineage-databricks-on-aws.md:L3-L8
    - file: external-lineage-databricks-on-aws.md:L25-L33
    - file: external-lineage-databricks-on-aws.md:L25-L27
    - file: external-lineage-databricks-on-aws.md:L28-L29
    - file: external-lineage-databricks-on-aws.md:L30-L31
    - file: external-lineage-databricks-on-aws.md:L32-L33
    - file: external-lineage-databricks-on-aws.md:L10-L12
    - file: external-lineage-databricks-on-aws.md:L70-L71
    - file: external-lineage-databricks-on-aws.md:L72-L73
title: Privileges for External Lineage
description: The set of Unity Catalog privileges required to create external metadata objects and configure lineage relationships, including CREATE EXTERNAL METADATA, MODIFY, SELECT, and MODIFY privileges depending on the role of the object.
tags:
  - unity-catalog
  - security
  - permissions
timestamp: "2026-06-19T18:47:16.521Z"
---

# Privileges for External Lineage

**Privileges for External Lineage** are the Unity Catalog permissions required to add external metadata objects and configure lineage relationships that extend the automatically captured Databricks runtime lineage. These privileges control the ability to represent entities from external systems (e.g., Salesforce, Tableau) in Unity Catalog and connect them to catalog objects such as tables, models, or paths. ^[external-lineage-databricks-on-aws.md:L3-L8]

## Required Privileges

To add external lineage metadata outside of the automatic capture by Databricks, a user or service principal must be granted specific metastore‑ and object‑level privileges depending on the task. The following table summarises the required privileges:

| Task | Required Privilege | Scope |
|------|-------------------|-------|
| Create an external metadata securable object | `CREATE EXTERNAL METADATA` | [Metastore](/concepts/metastore.md) |
| Specify lineage relationships from an external metadata object | `MODIFY` | The external metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object (e.g., a table consuming the external data) | Read privilege on the UC object (e.g., `SELECT` on a table) | The target Unity Catalog object |
| Specify an upstream lineage relationship from a Unity Catalog object (e.g., a table that is the source for the external object) | Write privilege on the UC object (e.g., `MODIFY` on a table) | The source Unity Catalog object |

These privileges are enforced when using the Catalog Explorer UI, the External Metadata API, the External Lineage API, or the Databricks SDK for Python to manually add external lineage. ^[external-lineage-databricks-on-aws.md:L25-L33]

## Creating External Metadata Objects

Before any external lineage relationship can be recorded, an external metadata object must exist in Unity Catalog. The principal performing this action must have the `CREATE EXTERNAL METADATA` privilege on the [Metastore](/concepts/metastore.md). This object represents an entity in an external system, such as a dashboard in Tableau or a table in MySQL. ^[external-lineage-databricks-on-aws.md:L25-L27]

## Configuring Lineage Relationships

Once an external metadata object exists, configuring a lineage relationship between it and a Unity Catalog object (or another external metadata object) requires:

- **`MODIFY` privilege on the external metadata object** – to specify the relationship itself. ^[external-lineage-databricks-on-aws.md:L28-L29]
- **Appropriate read or write privilege on the target or source Unity Catalog object**, depending on the direction of the relationship:
  - For a **downstream** relationship (the external object is consumer), the principal needs a read privilege such as `SELECT` on the downstream UC object. ^[external-lineage-databricks-on-aws.md:L30-L31]
  - For an **upstream** relationship (the external object is producer), the principal needs a write privilege such as `MODIFY` on the upstream UC object. ^[external-lineage-databricks-on-aws.md:L32-L33]

These privileges ensure that only authorised users can link external entities to catalog objects and that lineage relationships respect existing access controls.

## Automatic Lineage via Lakeflow Connect

Databricks also supports automatic external lineage through Lakeflow Connect managed ingestion pipelines. When using Lakeflow Connect, source lineage from external tables to Unity Catalog destination tables is recorded automatically. The privilege requirements for that automatic workflow are not detailed in the same requirements section; administrators should consult the Lakeflow Connect documentation for any additional permissions required. ^[external-lineage-databricks-on-aws.md:L10-L12]

## Limitations

- External lineage created through these privileges is **not recorded** in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md:L70-L71]
- A [Metastore](/concepts/metastore.md) can have at most **10,000 external metadata objects** and **100,000 external lineage relationships**. ^[external-lineage-databricks-on-aws.md:L72-L73] These limits are documented in the Databricks resource limits guide.

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md)
- [External Metadata API](/concepts/external-metadata-api.md)
- [External Lineage API](/concepts/external-lineage-api.md)
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- [Metastore](/concepts/metastore.md)
- Lakeflow Connect

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. external-lineage-databricks-on-aws.md:L3-L8
2. external-lineage-databricks-on-aws.md:L25-L33
3. external-lineage-databricks-on-aws.md:L25-L27
4. external-lineage-databricks-on-aws.md:L28-L29
5. external-lineage-databricks-on-aws.md:L30-L31
6. external-lineage-databricks-on-aws.md:L32-L33
7. external-lineage-databricks-on-aws.md:L10-L12
8. external-lineage-databricks-on-aws.md:L70-L71
9. external-lineage-databricks-on-aws.md:L72-L73
