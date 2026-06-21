---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81cc712ea3e65efdd3ba34f3908beeab2eb4203b10d4389b41fe46a4ccea8daf
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - network-access-for-serverless-materialization-in-delta-sharing
    - NAFSMIDS
    - Network access error during data materialization
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Network Access for Serverless Materialization in Delta Sharing
description: Shared view materialization uses serverless compute in the provider's region, which may be blocked by storage-layer firewalls or private links; requires allowlisting serverless compute IPs.
tags:
  - delta-sharing
  - serverless
  - networking
  - firewall
timestamp: "2026-06-19T23:14:10.706Z"
---

# Network Access for Serverless Materialization in [Delta Sharing](/concepts/delta-sharing.md)

**Network Access for Serverless Materialization in Delta Sharing** refers to the connectivity requirements and configuration needed when sharing views, materialized views, or streaming tables via [Delta Sharing](/concepts/delta-sharing.md). These shared assets require temporary materialization on the provider's side using serverless compute, which must be able to access the underlying cloud storage.

## Overview

When a data provider shares a view, materialized view, or streaming table through [Delta Sharing](/concepts/delta-sharing.md), the data is temporarily materialized on the provider's side before being served to recipients. This materialization process uses Databricks serverless compute in the provider's region. The materialization storage location is the asset's parent schema or catalog storage location. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Network Access Error

If the storage location for the materialized data has network restrictions — such as a firewall or private link — that prevent Databricks serverless compute from accessing it, queries on the shared asset will fail with the following error:

```
There was an issue accessing the data provider's cloud storage. Shared view materialization uses the Serverless compute of data provider's region to perform the materialization. Please contact the data provider to allowlist Serverless compute IPs of their corresponding region to access the view's dependent tables storage location.
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Resolution

The data provider must allowlist serverless compute IP addresses for their corresponding region to access the view's dependent tables storage location. This involves configuring the firewall to permit traffic from Databricks serverless compute IP ranges. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

For detailed configuration instructions, see Serverless compute firewall configuration. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.
- Serverless Compute — The compute infrastructure used for materialization.
- Serverless compute firewall configuration — How to configure network access for serverless compute.
- DS_MATERIALIZATION_QUERY_FAILED — A related error when the materialization workspace cannot access the shared asset.
- Shared Views in Delta Sharing — Views that require materialization before sharing.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Pre-computed views that may require network access during sharing.

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
