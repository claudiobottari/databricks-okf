---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccd493a8d3eb6584d50228385520a6276315b51b0ebc4a363d07b3d24d48fd49
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-tables-for-rag-applications
    - OTFRA
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Tables for RAG Applications
description: Using online tables to host structured data for retrieval-augmented generation (RAG) applications, where a feature serving endpoint provides low-latency lookups integrated with LangChain agents.
tags:
  - databricks
  - rag
  - feature-serving
  - langchain
timestamp: "2026-06-19T18:14:36.893Z"
---

```markdown
---
title: Online Tables for RAG Applications
summary: Architecture pattern using online tables as structured data sources for retrieval-augmented generation applications via feature serving endpoints and LangChain tools.
sources:
  - databricks-online-tables-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:53:20.771Z"
updatedAt: "2026-06-19T14:53:20.771Z"
tags:
  - databricks
  - rag
  - langchain
  - generative-ai
aliases:
  - online-tables-for-rag-applications
  - OTFRA
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Online Tables for RAG Applications

**Online tables** are read-only, row-oriented copies of [[Delta Lake Table|Delta Tables]] that provide low-latency, high-throughput data access for online workloads. They are fully serverless and auto-scale capacity with request load, making them well-suited for [[Retrieval Augmented Generation (RAG)|Retrieval-Augmented Generation]] (RAG) applications that require fast lookups of structured data during inference. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Overview

Online tables are designed to work with [[Model Serving]], Feature Serving, and RAG applications where they enable fast data retrieval. They store data in row-oriented format optimized for online access, as opposed to the column-oriented format of standard Delta Tables. Online tables are created as a synchronized copy of a source Delta Table in [[Unity Catalog]]. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Using Online Tables with RAG Applications

RAG applications are a common use case for online tables. The typical workflow involves creating an online table for the structured data the RAG application needs, hosting it on a feature serving endpoint, and using that endpoint for lookups during inference. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Typical Steps

1. **Create a feature serving endpoint** that serves features from the online table.
2. **Create a tool** using LangChain or a similar package that queries the endpoint for relevant data.
3. **Use the tool in an agent** (such as a LangChain agent) to retrieve relevant data during the RAG workflow.
4. **Create a model serving endpoint** to host the application.

For step-by-step instructions and an example notebook, see the documentation on using features with structured RAG applications. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Creating an Online Table

You can create an online table using the Databricks UI (Catalog Explorer), the REST API, or the Databricks SDK. The source Delta Table must have a primary key defined. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Using the UI

1. In Catalog Explorer, navigate to the source Delta Table.
2. From the **Create** menu, select **Online table**.
3. Configure the online table with a name, primary key column(s), optional time series key, and sync mode.
4. Click **Confirm**.

The online table appears in Catalog Explorer under the specified catalog, schema, and name. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Sync Modes

| Mode | Description |
|------|-------------|
| **Snapshot** | Periodic full copy of the source table |
| **Triggered** | Incremental updates on demand |
| **Continuous** | Continuous incremental synchronization |

To support **Triggered** or **Continuous** sync modes, the source table must have [[Delta Change Data Feed (CDF)|Change Data Feed]] enabled. Source tables without change data feed support only the **Snapshot** mode. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Serving Online Table Data

### Feature Serving Endpoints

For models and applications hosted outside of Databricks, you can create a feature serving endpoint to serve features from online tables. The endpoint makes features available at low latency using a REST API. ^[databricks-online-tables-legacy-databricks-on-aws.md]

The process involves:

1. Creating a feature spec that references the source Delta Table.
2. Creating a feature serving endpoint using that spec.
3. Querying the endpoint via HTTP POST requests.

The feature serving endpoint automatically uses the online table for low-latency lookups. The source Delta Table and the online table must use the same primary key. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Model Serving with Automatic Feature Lookup

When you sync a feature table to an online table, models trained using features from that feature table automatically look up feature values from the online table during inference. No additional configuration is required. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Permissions

### User Permissions for Creating Online Tables

To create an online table, you need: ^[databricks-online-tables-legacy-databricks-on-aws.md]

- `SELECT` privilege on the source table
- `USE CATALOG` privilege on the destination catalog
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema

### Managing Synchronization

To manage the data synchronization pipeline of an online table, you must either be the owner of the online table or be granted the `REFRESH` privilege on it. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Endpoint Service Principal

A unique service principal is automatically created for each feature serving or model serving endpoint. This service principal has limited permissions required to query data from online tables, allowing endpoints to access data independently of the user who created the resource. The service principal persists for the lifetime of the endpoint. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only one online table is supported per source table.
- An online table and its source table can have at most 1000 columns.
- Columns of data types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys.
- Rows with null values in primary key columns are ignored.
- Foreign, system, and internal tables are not supported as source tables.
- Catalog, schema, and table names can only contain alphanumeric characters and underscores, and must not start with numbers. Dashes (`-`) are not allowed.
- String columns are limited to 64KB length.
- Column names are limited to 64 characters.
- Maximum row size is 2MB.
- During public preview, the combined size of all online tables in a Unity Catalog [[metastore|Metastore]] is 2TB uncompressed user data.
- Maximum read throughput for a [[metastore|Metastore]] is approximately 750 MB/sec.

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting

### Missing "Create online table" Option

Ensure the source table's Securable Kind is one of the supported types, including `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_FEATURE_STORE`, `TABLE_MATERIALIZED_VIEW`, and others. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Sync Mode Not Available

If **Triggered** or **Continuous** sync modes cannot be selected, the source table likely does not have Delta change data feed enabled, or it is a View or materialized view. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Update Failures or Offline Status

Common causes include: ^[databricks-online-tables-legacy-databricks-on-aws.md]

- The source table was deleted or recreated while the online table was synchronizing.
- The source table cannot be accessed through Serverless Compute due to firewall settings.
- The aggregate size of online tables exceeds the 2 TB metastore-wide limit. Note that the uncompressed row-oriented size can be significantly larger (up to 100x) than the compressed column-oriented size shown in Catalog Explorer.

To estimate the uncompressed size of a Delta table, use the following query from a Serverless SQL Warehouse:

```sql
SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- Feature Serving — Serving features from online tables via REST API.
- [[Model Serving]] — Deploying models that automatically use online tables for feature lookup.
- [[Unity Catalog]] — The governance layer for managing online tables.
- [[Delta Lake Table|Delta Tables]] — The source format for online tables.
- [[Delta Change Data Feed (CDF)|Change Data Feed]] — Required for incremental sync modes.
- [[Retrieval Augmented Generation (RAG)|Retrieval-Augmented Generation]] — The application pattern that benefits from online tables.
- [[FeatureEngineeringClient API|Feature Engineering]] — Creating feature specs for serving.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md
```

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
