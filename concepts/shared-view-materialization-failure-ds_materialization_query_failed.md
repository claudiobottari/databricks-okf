---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e85742f9c941379769db4815da768a57126b04721e68c85a2cc7e537207a2422
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-view-materialization-failure-ds_materialization_query_failed
    - SVMF(
    - SVM
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Shared View Materialization Failure (DS_MATERIALIZATION_QUERY_FAILED)
description: Error when sharing views, materialized views, or streaming tables because the provider lacks read-write access to the asset or the materialization workspace is misconfigured.
tags:
  - delta-sharing
  - materialized-views
  - permissions
  - troubleshooting
timestamp: "2026-06-19T23:14:10.468Z"
---

# Shared View Materialization Failure (`DS_MATERIALIZATION_QUERY_FAILED`)

**`DS_MATERIALIZATION_QUERY_FAILED`** is an error that occurs when a recipient tries to query a shared view, [materialized view](/concepts/materialized-views-in-databricks.md), or streaming table via [OpenSharing](/concepts/opensharing.md) ([Delta Sharing](/concepts/delta-sharing.md)) on Databricks, and the provider’s side is unable to materialize the asset for the share.

## Error Message

The full error message reads:

> `"DS_MATERIALIZATION_QUERY_FAILED": "The shared asset could not be materialized due to the asset not being accessible in the materialization workspace. Please ask data provider to contact :re[DB] support to override the materialization workspace."` ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Causes

The most common cause is that the data provider does not have **read‑write access** to the asset they are trying to share. When a view, materialized view, or streaming table is shared, Databricks must temporarily materialize the asset in the provider’s storage (the asset’s parent schema or catalog storage location). If the provider lacks the necessary permissions on that storage location, the materialization fails. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

A separate but related error, **Network access error during data materialization**, occurs when the storage location has network restrictions (e.g., firewalls, private links) that prevent Databricks serverless compute from accessing it. That error displays a different message (see below). If the network access error is the actual problem, the provider must allowlist the serverless compute IPs for their region. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Recommended Fix

The recipient should contact the data provider and ask them to verify that they have **read‑write access** to the shared data asset. The provider must also ensure that the share owner has the correct permissions on the asset and its underlying storage. If the issue persists after confirming access, the provider may need to contact Databricks support (using the `:re[DB]` reference in the error) to override the materialization workspace. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

If the network access error is the actual cause (i.e., the error message mentions “There was an issue accessing the data provider’s cloud storage”), the provider must configure their firewall to allowlist the serverless compute IPs for their region. See serverless compute firewall configuration for guidance. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md)
- [Materialized view](/concepts/materialized-views-in-databricks.md)
- Streaming table
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- Data provider permissions
- [Network access error during data materialization](/concepts/network-access-for-serverless-materialization-in-delta-sharing.md)

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
