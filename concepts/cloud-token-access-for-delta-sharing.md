---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88e9c6e089b34a65a0e33389f2ad8fa32d295dd5e7936c1cf23ac89794518dc6
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloud-token-access-for-delta-sharing
    - CTAFDS
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Cloud Token Access for Delta Sharing
description: Temporary, path-scoped cloud credentials that give recipients direct read access to shared Delta table files, improving performance by avoiding server-side materialization.
tags:
  - delta-sharing
  - security
  - performance
timestamp: "2026-06-19T14:38:31.500Z"
---

# Cloud Token Access for Delta Sharing

**Cloud Token Access** is a security mechanism in [Delta Sharing](/concepts/delta-sharing.md) that provides recipients with temporary, path-scoped cloud credentials to access shared Delta table files directly from cloud storage. This approach, also known as *directory-based access mode* in the Databricks-to-Open sharing protocol, enables high-performance data access without requiring long-lived bearer tokens or complex credential management. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Cloud tokens are temporary credentials that Databricks generates to give recipients direct read access to shared Delta table files. When cloud token access is enabled, recipients receive credentials scoped to the root directory of the shared Delta table, granting read access to both the data files and the Delta log. The Delta log contains the commit history for each table version, information about the committer, and deleted data that has not been vacuumed. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Eligibility

Not all shared objects qualify for cloud token access. The eligibility criteria differ based on the sharing protocol used.

### Databricks-to-Databricks Sharing

Cloud tokens are used in Databricks-to-Databricks sharing when **all** of the following conditions are met:

- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared without a partition filter.

Cloud tokens are exchanged directly between Unity Catalog metastores without long-lived bearer tokens, resulting in performance comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Open Sharing

Cloud tokens (directory-based access mode) are used in Databricks-to-Open sharing when **all** of the following conditions are met:

- The shared object is a **managed or external Delta table**.
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared without a partition filter.
- The table is not a CCv2 table.
- The table does not use default storage.

The OpenSharing server includes the table's cloud storage location and `accessModes: ["url", "dir"]` in list and metadata responses. Open recipients can call the [Generate Temporary Table Credentials](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#generate-temporary-table-credential) endpoint to obtain credentials and read directly from cloud storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Unsupported Objects

Views, materialized views, foreign tables, streaming tables, volumes, notebooks, Python UDFs, and AI models are not supported for cloud token access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When cloud token access is used, recipients receive credentials scoped to the root directory of the shared Delta table. This provides read access to the data files and the Delta log. The Delta log contains the commit history for each table version, information about the committer, and deleted data that has not been vacuumed. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Performance

For Databricks-to-Databricks shares, cloud tokens are exchanged directly between Unity Catalog metastores without long-lived bearer tokens, resulting in performance comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open data sharing protocol
- [OpenSharing](/concepts/opensharing.md) — The Databricks-to-Open sharing model
- [Recipient Properties](/concepts/recipient-properties.md) — Partition filtering via recipient properties
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer
- Delta log — The transaction log for Delta tables

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
