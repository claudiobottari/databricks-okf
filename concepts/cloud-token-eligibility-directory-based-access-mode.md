---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab44300301753f8a3b34998b6aa4ce21eab017009d6330704211bf1394c81e0c
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloud-token-eligibility-directory-based-access-mode
    - CTE(AM
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Cloud Token Eligibility (Directory-Based Access Mode)
description: A mechanism that uses temporary, path-scoped cloud credentials to give recipients direct read access to shared Delta table files without long-lived bearer tokens.
tags:
  - delta-sharing
  - security
  - access-control
timestamp: "2026-06-18T11:23:48.691Z"
---

# Cloud Token Eligibility (Directory-Based Access Mode)

**Cloud Token Eligibility** determines whether Databricks uses temporary, path-scoped cloud credentials (cloud tokens) to give recipients direct read access to shared Delta table files. In the Databricks-to-Open sharing protocol, this is also called *directory-based access mode*. ^[create-shares-for-opensharing-databricks-on-aws.md]

Cloud tokens are temporary credentials that allow recipients to read directly from cloud storage, bypassing the OpenSharing server for data transfer. This can improve query performance for large tables because data flows directly from storage to the recipient’s compute environment. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Which Shared Objects Qualify

Cloud tokens are only used for **Delta tables** that meet specific conditions. Views, materialized views, foreign tables, streaming tables, volumes, notebooks, Python UDFs, and AI models are **not eligible** for cloud token access. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Databricks Sharing

Cloud tokens are used when **all** of the following are true: ^[create-shares-for-opensharing-databricks-on-aws.md]

- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without a partition filter**.

For Databricks-to-Databricks shares, cloud tokens are exchanged directly between Unity Catalog metastores without long-lived bearer tokens, resulting in performance comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Open Sharing

Cloud tokens (directory-based access mode) are used when **all** of the following are true: ^[create-shares-for-opensharing-databricks-on-aws.md]

- The shared object is a **managed or external Delta table**.
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without a partition filter**.
- The table is **not a CCv2 table**.
- The table **does not use default storage**.

For Databricks-to-Open sharing, the OpenSharing server includes the table’s cloud storage location and `accessModes: ["url", "dir"]` in list and metadata responses. Open recipients can call the [Generate Temporary Table Credentials](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#generate-temporary-table-credential) endpoint to obtain credentials and read directly from cloud storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When cloud token access is used, recipients receive credentials scoped to the **root directory** of the shared Delta table. This grants read access to both the data files and the Delta log. The Delta log contains:

- The commit history for each table version.
- Information about the committer.
- Deleted data that has not been vacuumed.

Because the Delta log may expose metadata and deleted data, providers should carefully consider whether to enable history sharing for tables containing sensitive information. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Interaction with Partition Filters

Partition filters **disqualify** a table from cloud token eligibility. When partitions are specified (including parameterized partitions using `CURRENT_RECIPIENT()`), the sharing server must evaluate which partitions apply to each recipient, and cloud token access is not used. The same applies to both sharing protocols. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Best Practices

- Enable history sharing (`WITH HISTORY`) for eligible tables to maximize performance via cloud tokens.
- Be aware of the security implications of sharing the Delta log — if your table contains deleted data that has not been vacuumed, recipients may be able to read it via cloud token access.
- Use table partitions or parameterized partitions when you need to limit data per recipient, but note that this will disable cloud token access.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for data sharing
- [OpenSharing](/concepts/opensharing.md) — The Databricks-to-Open sharing implementation
- Cloud Tokens — Temporary credentials for direct storage access
- Delta Log — Transaction log containing table history and metadata
- Table Partitions — Partition specifications that affect token eligibility
- [Managed Tables](/concepts/managed-tables-in-databricks.md) vs External Tables — Both types can qualify for cloud tokens
- [History Sharing](/concepts/table-history-sharing.md) — Required for cloud token access
- Generate Temporary Table Credentials — REST API endpoint for open recipients

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
