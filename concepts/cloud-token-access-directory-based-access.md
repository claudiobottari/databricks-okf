---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e71811a9c03965c393a2f9d96373aba0e14fd036759d49e73876cbfeffe6ad0e
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloud-token-access-directory-based-access
    - CTA(A
    - Cloud Tokens and Directory-Based Access
    - Directory-Based Access
    - cloud-token-access-directory-based-access-mode
    - CTA(AM
    - cloud-token-eligibility-directory-based-access-mode
    - CTE(AM
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Cloud Token Access (Directory-Based Access)
description: A mechanism using temporary, path-scoped cloud credentials to give recipients direct read access to shared Delta table files. Applicable to Databricks-to-Databricks and Databricks-to-Open sharing under specific conditions (full history, no partition filter, etc.). Grants read access to data files and the Delta log.
tags:
  - delta-sharing
  - security
  - cloud-storage
timestamp: "2026-06-19T18:02:12.419Z"
---

# Cloud Token Access (Directory-Based Access)

**Cloud Token Access** (also called **directory-based access mode** in the Databricks-to-Open sharing protocol) is a mechanism used by Databricks OpenSharing to give recipients temporary, path-scoped cloud credentials that grant direct read access to the underlying files of shared Delta tables. Instead of proxying all data through a server, the provider issues short-lived cloud tokens that allow the recipient to read table files directly from cloud storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Cloud tokens are temporary credentials that are scoped to the root directory of a shared Delta table. They provide a high‑performance data access path because the recipient reads the files directly from the provider’s cloud bucket without routing through an intermediate server. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Eligibility

Cloud token access is only available for certain types of shared objects and depends on the sharing protocol used.

### Databricks‑to‑Databricks Sharing

Cloud tokens are used when **all** of the following conditions are true:

- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without** a partition filter.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks‑to‑Open Sharing

Cloud tokens (directory‑based access mode) are used when **all** of the following conditions are true:

- The shared object is a **managed or external Delta table**.
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without** a partition filter.
- The table is **not** a CCv2 table.
- The table does **not** use [Default Storage](/concepts/workspace-default-storage-path.md).

^[create-shares-for-opensharing-databricks-on-aws.md]

### Ineligible Object Types

The following asset types **do not** support cloud token access:

- Views and dynamic views
- Materialized views
- Foreign tables (including foreign Iceberg tables)
- Streaming tables
- Volumes
- Notebooks
- Python UDFs
- AI models

^[create-shares-for-opensharing-databricks-on-aws.md]

## How It Works

For **Databricks‑to‑Databricks shares**, cloud tokens are exchanged directly between Unity Catalog metastores without the use of long‑lived bearer tokens. This results in performance that is comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

For **Databricks‑to‑Open sharing**, the OpenSharing server includes the table’s cloud storage location and the `accessModes: ["url", "dir"]` field in list and metadata responses. Open recipients can call the Generate Temporary Table Credentials endpoint (as defined in the [Delta Sharing Protocol](/concepts/delta-sharing.md)) to obtain credentials and read directly from cloud storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When cloud token access is used, recipients receive credentials that are scoped to the **root directory** of the shared Delta table. This grant includes read access to:

- All data files within the table directory.
- The **Delta log** for each table version.

> **Important:** The Delta log contains the commit history for each table version, information about the committer, and **deleted data that has not been vacuumed**. Providers should be aware that sharing the full table history exposes this metadata to the recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The overall data sharing framework on Databricks.
- [Delta Sharing Protocol](/concepts/delta-sharing.md) – The open protocol that defines how temporary credentials are generated.
- [Delta Table](/concepts/delta-lake-table.md) – The data format eligible for cloud token access.
- [Default Storage](/concepts/workspace-default-storage-path.md) – A storage configuration that may exclude a table from cloud token eligibility.
- Partition Filters – A sharing option that disables cloud token access when applied.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that controls cloud token exchange in Databricks‑to‑Databricks sharing.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
