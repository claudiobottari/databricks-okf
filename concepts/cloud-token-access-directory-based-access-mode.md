---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a48a3180751d7d5f6b79f228158becc1d6155bc5274e585ed0228fbaf5d2e8c3
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloud-token-access-directory-based-access-mode
    - CTA(AM
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Cloud Token Access (Directory-based Access Mode)
description: A mechanism where Databricks uses temporary, path-scoped cloud credentials to give recipients direct read access to shared Delta table files, bypassing the need for long-lived bearer tokens.
tags:
  - delta-sharing
  - security
  - performance
timestamp: "2026-06-19T09:37:43.778Z"
---

# Cloud Token Access (Directory-Based Access Mode)

**Cloud Token Access** (also called **directory-based access mode** in the [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) protocol) is a mechanism where Databricks issues temporary, path-scoped cloud credentials that grant recipients direct read access to the underlying files of a shared [Delta table](/concepts/delta-lake-table.md). This bypasses the sharing server for data transfer, improving query performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

When cloud tokens are used, recipients can read Delta table files directly from the source cloud storage instead of having data proxied through the OpenSharing server. For [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), this results in performance comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How Cloud Token Access Works

### Databricks-to-Databricks Sharing

Cloud tokens are exchanged directly between [Unity Catalog](/concepts/unity-catalog.md) metastores without using long-lived bearer tokens. The recipient's workspace generates scoped credentials to read the shared table data. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Open (OpenSharing)

The OpenSharing server includes the table's cloud storage location together with `accessModes: ["url", "dir"]` in its list and metadata responses. Open recipients can call the [Generate Temporary Table Credentials](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#generate-temporary-table-credential) endpoint (defined in the Delta Sharing protocol) to obtain credentials and read directly from cloud storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Eligibility Conditions

The following asset types are **not** supported for cloud token access: views, materialized views, foreign tables, streaming tables, volumes, notebooks, Python UDFs, and AI models. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Databricks Sharing

Cloud tokens are used when **all** of the following conditions are true:

- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without** a partition filter.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Open Sharing

Cloud tokens (directory-based access mode) are used when **all** of the following conditions are true:

- The shared object is a **managed or external Delta table**.
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared **without** a partition filter.
- The table is **not** a CCv2 table.
- The table **does not** use default storage.

^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When cloud token access is used, recipients receive credentials that are scoped to the **root directory of the shared Delta table**. This grants read access to both the data files and the Delta log. The Delta log contains the commit history for each table version, information about the committer, and deleted data that has not been vacuumed. ^[create-shares-for-opensharing-databricks-on-aws.md]

Because the credentials are temporary and path-scoped, the risk of broad exposure is limited. However, providers should be aware that the Delta log exposes historical metadata, including records of deleted data that may still be physically present until vacuumed. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol that underpins cloud token access.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that manages shares and recipients.
- [OpenSharing](/concepts/opensharing.md) — The cross-platform sharing protocol used for Databricks-to-Open sharing.
- [Delta Table](/concepts/delta-lake-table.md) — The table format that qualifies for cloud token access.
- Partition Filters — When applied, cloud token access is not used; data is served through the sharing server instead.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — Sharing between two Databricks workspaces.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — Sharing to non-Databricks recipients.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
