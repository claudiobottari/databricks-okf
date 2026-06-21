---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2377272886706c1b373645dddfd5b1be01a3eefb2153053a6b9f2debbf9a68e8
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-owner-permissions-for-shared-assets
    - SOPFSA
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Share Owner Permissions for Shared Assets
description: A 'does not exist' error on a shared asset indicates the share owner lacks sufficient permissions on the asset; requires verifying permissions on all shared objects.
tags:
  - delta-sharing
  - permissions
  - access-control
  - troubleshooting
timestamp: "2026-06-19T23:14:39.479Z"
---

# Share Owner Permissions for Shared Assets

**Share Owner Permissions for Shared Assets** refers to the access control requirements that a data provider must fulfill when sharing data assets through [Delta Sharing](/concepts/delta-sharing.md) on Databricks. The share owner must have sufficient permissions on every asset included in a share; otherwise, recipients may encounter errors when trying to access the shared data.

## Permission Requirements

When a data provider shares a data asset—such as a table, view, materialized view, or streaming table—the share owner must have the necessary permissions on that asset. If the share owner lacks sufficient permissions, the asset may appear inaccessible to recipients. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

For specific asset types, the provider must also have read-write access to the asset they are trying to share. Without this access, materialization of views, materialized views, or streaming tables may fail with the error `DS_MATERIALIZATION_QUERY_FAILED`. The error message indicates that the provider does not have read-write access to the shared data asset. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Common Error: "Does Not Exist"

If a recipient clicks on a shared asset and encounters an object "does not exist" error, the most likely cause is that the share owner on the provider side does not have sufficient permissions on the asset. The recipient should contact the data provider to verify that the share owner has the required permissions on all shared assets. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Resolution

To resolve permission-related sharing issues, the data provider should:

1. Verify that the share owner has the required permissions on all shared assets.
2. Ensure the provider has read-write access to the asset for materialization when sharing views, materialized views, or streaming tables.

For detailed information about the permissions required for a share owner to share a data asset and how to grant recipient access, see the official documentation on Grant recipient access to share and the Create share requirements. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- Share Owner — The user or principal responsible for managing a share
- Grant recipient access to share — Process for granting data access to recipients
- Data Asset Materialization — Temporary materialization required for views and streaming tables
- DS_MATERIALIZATION_QUERY_FAILED — Error indicating insufficient provider permissions

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
