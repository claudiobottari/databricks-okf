---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40443342290a27cd508cc3b6ea8d792dc4baa3c56c8878f428b825abad93e684
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-online-tables-legacy
    - DOT(
    - Databricks online table (legacy)
    - Online Table (legacy)
    - Online Tables (Legacy)
    - Online tables (legacy)
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Databricks Online Tables (Legacy)
description: Serverless, read-only copies of Delta Tables stored in row-oriented format, optimized for low-latency online access and designed for use with Model Serving, Feature Serving, and RAG applications.
tags:
  - databricks
  - online-tables
  - feature-store
  - data-serving
timestamp: "2026-06-19T18:15:17.051Z"
---

Here is the wiki page on "Databricks Online Tables (Legacy)".

## Databricks Online Tables (Legacy)

**Databricks Online Tables (Legacy)** are fully managed, serverless, read-only copies of a Delta Table, stored in a row-oriented format optimized for low-latency, high-throughput online access. They are designed to serve feature data to [Model Serving](/concepts/model-serving.md), Feature Serving, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications, enabling fast data lookups by key. An online table is a one-to-one copy of its source Delta table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Online tables are in Public Preview. They are fully serverless, meaning they auto-scale throughput capacity with the request load and provide low latency and high throughput access to data of any scale. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Requirements

To create an online table, the following prerequisites must be met:

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). A Unity Catalog [Metastore](/concepts/metastore.md) must be set up, and a catalog must be created. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A model must be registered in Unity Catalog to access online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A Databricks admin must accept the Serverless Terms of Service in the account console. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Creating and Managing Online Tables

Online tables can be created via the [Catalog Explorer](/concepts/catalog-explorer.md) UI, the REST API, or the Databricks SDK.

**Creating via the UI:** This is a one-step process. Navigate to the source Delta table in Catalog Explorer and select **Create online table**. The source table must have a primary key. In the creation dialog, you configure the **Name**, **Primary Key** column(s), an optional **Time Series Key** (which ensures only the latest row per primary key is stored), and a **Sync mode**. ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Sync Modes:** The available sync modes are **Snapshot**, **Triggered**, and **Continuous**. To support Triggered or Continuous sync modes, the source table must have Change Data Feed (CDF) enabled. ^[databricks-online-tables-legacy-databricks-on-aws.md]

- In **Snapshot** mode, the online table is a point-in-time copy.
- In **Triggered** mode, updates are applied on-demand or on a schedule.
- In **Continuous** mode, the online table is continuously synchronized with the source. ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Managing via the UI:** The online table page in Catalog Explorer shows the **Data Ingest** status. You can trigger a manual update by clicking **Sync now**, or schedule periodic updates via the pipeline management page. ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Deleting:** An online table can be deleted from its page in Catalog Explorer or via the API. Deleting stops all ongoing data synchronization and releases resources. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Serving Online Table Data

Data from online tables can be served via a **Feature Serving Endpoint**. This is done by:

1.  Creating a [Feature Spec](/concepts/featurespec.md) that references the source Delta table and its primary key. ^[databricks-online-tables-legacy-databricks-on-aws.md]
2.  Creating a Feature Serving Endpoint using that Feature Spec. The endpoint provides low-latency REST API access to the feature values, automatically using the online table for lookups. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Use Cases

Online tables are used for two primary scenarios:

- **Model Serving:** When a model is trained using features from a feature table, it automatically looks up feature values from the corresponding online table during inference, requiring no additional configuration. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **RAG Applications:** For structured data needed by a RAG application, you create an online table and host it on a feature serving endpoint. The RAG application uses this endpoint for fast data lookups. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Permissions

- **Creating an online table** requires `SELECT` privilege on the source table, `USE CATALOG` on the destination catalog, and `USE SCHEMA` and `CREATE TABLE` on the destination schema. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Managing the pipeline** requires ownership of the online table or the `REFRESH` privilege. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Service Principals:** A unique service principal is automatically created for a Feature Serving or Model Serving endpoint. This principal has limited permissions to query data from online tables, ensuring endpoint functionality even if the creator leaves the workspace. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Limitations

Several limitations apply during the Public Preview:

- **Naming and Structure:** Catalog, schema, and table names can only contain alphanumeric characters and underscores. Dashes (`-`) are not allowed. Column names are limited to 64 characters. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Data Types:** Columns of type ARRAY, MAP, or STRUCT cannot be used as primary keys. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Source Table:** Only one online table is supported per source table. The source and online tables can have at most 1000 columns. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Size:** The maximum row size is 2MB. String type columns are limited to 64KB. The combined size of all online tables in a [Metastore](/concepts/metastore.md) is 2TB (uncompressed user data). ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Throughput:** Maximum read throughput for a [Metastore](/concepts/metastore.md) is approximately 750 MB/sec. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Troubleshooting

- **"Create online table" option missing:** The source table may not be a supported type. Check the "Securable Kind" in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Sync mode selection issues:** The source table may not have Change Data Feed enabled, or it might be a view or materialized view. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Update fails / status shows offline:** Click the pipeline ID link in the overview tab. Common causes include the source table being deleted or recreated, firewall blocking access, or the total online table size exceeding the 2TB limit. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- Feature Serving

### Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
