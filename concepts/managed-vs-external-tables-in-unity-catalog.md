---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91c1ff05df717c36066b2190211fead63395e3bec0aa61aad8636bbde2c46884
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
    - unity-catalog-best-practices-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - managed-vs-external-tables-in-unity-catalog
    - MVETIUC
    - Managed Tables vs External Tables
    - Managed tables vs External tables
    - Managed tables vs external tables
    - Managed tables vs external tables|managed table
    - Managed vs External Tables
    - Managed vs. External Tables
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
    - file: unity-catalog-best-practices-databricks-on-aws.md
title: Managed vs External tables in Unity Catalog
description: Distinction between tables where Unity Catalog controls storage location and file lifecycle versus tables where the user specifies the storage location
tags:
  - unity-catalog
  - tables
  - databricks
timestamp: "2026-06-19T19:29:41.124Z"
---

## Managed vs [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)

In Unity Catalog, every registered securable object is centrally governed for access control, auditing, and lineage. However, for **tables** (and volumes) there is an additional distinction between *managed* and *external* assets that determines who controls the underlying data file storage location and lifecycle. This distinction does not apply to views, models, or functions. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

### Summary of differences

| Aspect | Managed table | External table |
|--------|--------------|----------------|
| Governance (access, auditing, lineage) | Unity Catalog controls | Unity Catalog controls |
| Storage location | Determined by Unity Catalog in the managed storage location of the containing schema, catalog, or [Metastore](/concepts/metastore.md) | Specified by the user; must be on a path defined by a Unity Catalog [External location](/concepts/external-location.md) |
| File lifecycle (optimization, organization, deletion) | Managed by Unity Catalog | Controlled by you or an external system |
| Supported formats | Delta or Apache Iceberg only | Delta, CSV, JSON, Avro, Parquet, ORC, and others |
| Behavior when dropped | Underlying data files are deleted | Metadata is removed; data files remain in place |
| Folder structure | Uses internal GUID-style folders (not simple `schema/table`); should only be accessed via Unity Catalog | User‑defined path; accessible directly by external systems |

Sources: ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md] ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

In all cases, the data files always remain in your cloud account – they are never transferred to Databricks or owned by Databricks. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

### Managed tables

A **managed table** is fully managed by Unity Catalog. This means Unity Catalog determines the storage location (the *managed storage location* defined on the containing schema, catalog, or [Metastore](/concepts/metastore.md)) and controls the file lifecycle including optimization, organization, and deletion. Managed tables are always stored in Delta or Apache Iceberg format. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

Databricks recommends using managed tables for **most workloads** because they:

- Simplify configuration, optimization, and governance.
- Unlock performance features such as auto compaction, auto optimize, faster metadata reads (metadata caching), and intelligent file size optimizations.
- Receive priority for new functionality (e.g., [predictive optimization](/concepts/delta-lake-predictive-optimization.md) and managed disaster recovery).
- Support read, write, and create access from external engines via the Unity REST API and the Iceberg REST Catalog – managed tables do **not** cause vendor lock-in. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md, unity-catalog-best-practices-databricks-on-aws.md]

**Best practice:** Use managed tables for all new lakehouse data – bronze, silver, and gold layers. Enable predictive optimization for frequently queried managed tables. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

### External tables

An **external table** is a table whose access from Databricks is governed by Unity Catalog, but whose underlying data file storage lifecycle is managed by you or by external systems. When you create an external table, you specify its cloud storage path, which must be covered by an [External location](/concepts/external-location.md) securable object. Because Unity Catalog does not manage the file lifecycle, dropping an external table removes only the table metadata from the [Metastore](/concepts/metastore.md); the data files remain intact. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md, unity-catalog-best-practices-databricks-on-aws.md]

**When to use external tables:**

- **Upgrading from Hive [Metastore](/concepts/metastore.md):** External tables provide a quick, one‑click upgrade path without moving data. Databricks recommends eventually migrating such tables to managed tables. ^[unity-catalog-best-practices-databricks-on-aws.md]
- **Regulatory or compliance requirements:** Data must remain in specific cloud storage paths. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **External systems need direct file access** – for example, systems that cannot use [OpenSharing](/concepts/opensharing.md) or that require non‑Delta/non‑Iceberg formats (Parquet, Avro, ORC, etc.). ^[unity-catalog-best-practices-databricks-on-aws.md]
- **Disaster recovery:** Managed tables cannot be registered across multiple metastores in the same cloud; external tables can be registered in another [Metastore](/concepts/metastore.md) if the data is copied independently. ^[unity-catalog-best-practices-databricks-on-aws.md]

**Important limitations:**

- Databricks strongly advises against registering the same external table in more than one [Metastore](/concepts/metastore.md) – schema changes in one [Metastore](/concepts/metastore.md) will not propagate, causing consistency issues. ^[unity-catalog-best-practices-databricks-on-aws.md]
- External tables do not benefit from managed‑table‑only features such as predictive optimization or auto compaction. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Direct external access to the underlying storage bypasses Unity Catalog access control, auditing, and lineage; prefer managed tables with OpenSharing when data must be shared across platforms. ^[unity-catalog-best-practices-databricks-on-aws.md]

**Best practice:** Reserve external tables only for data that must remain in specific paths. Create external tables using one external location per schema. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md, unity-catalog-best-practices-databricks-on-aws.md]

### Additional considerations

- **Governance:** Both managed and external tables are fully governed by Unity Catalog for access control, auditing, and lineage. The difference lies in who controls the underlying files. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]
- **Performance and features:** Managed tables are the primary beneficiaries of new Databricks optimizations. If your workload can use Delta or Iceberg format, managed tables are the recommended default. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md, unity-catalog-best-practices-databricks-on-aws.md]
- **Open access:** Both table types support access from external engines via the Unity REST API and the Iceberg REST Catalog, preventing lock‑in. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

### Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Central governance platform
- [Managed storage](/concepts/managed-storage-location.md) – Where managed table data is stored
- [External location](/concepts/external-location.md) – Required for creating external tables
- [Delta Lake](/concepts/delta-lake.md) – Primary format for managed tables
- Iceberg – Alternative format for managed tables
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) – Managed‑only feature
- [OpenSharing](/concepts/opensharing.md) – Recommended alternative to direct external access
- [Hive metastore](/concepts/built-in-hive-metastore.md) – Legacy [Metastore](/concepts/metastore.md) that external tables can help migrate from

### Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
- phase-6-design-delta-lake-architecture-databricks-on-aws.md
- unity-catalog-best-practices-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
2. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
3. [unity-catalog-best-practices-databricks-on-aws.md](/references/unity-catalog-best-practices-databricks-on-aws-2672bfeb.md)
