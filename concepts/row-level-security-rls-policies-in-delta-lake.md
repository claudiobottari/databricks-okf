---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7316c0d58fd1a8136aeca23c72ce9da977bb44ddee2e667eb28a70fd8df8c1d0
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-security-rls-policies-in-delta-lake
    - RS(PIDL
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Row-level Security (RLS) policies in Delta Lake
description: A Delta table security feature that filters rows at query time per user permissions, unsupported by external metadata sources.
tags:
  - delta-lake
  - security
  - data-governance
timestamp: "2026-06-19T18:24:41.321Z"
---

# Row-level Security (RLS) Policies in Delta Lake

**Row-level Security (RLS) policies** in Delta Lake are a data governance feature that restricts which rows a user can access in a table based on filter conditions defined at the table level. RLS policies are applied transparently to queries, ensuring that users only see the data they are authorized to view.

## Overview

RLS policies allow administrators to define row-level access controls directly on Delta Lake tables. When a policy is applied, every query against the table automatically filters rows according to the policy conditions, without requiring changes to the query itself. This provides a centralized way to enforce data access restrictions. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Compatibility with External Metadata

Delta Lake tables that have RLS policies applied are not supported as sources for [External Metadata](/concepts/external-metadata-api.md) operations. When attempting to use a table with RLS policies as an external metadata source, the system returns a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error with the `ROW_FILTER` sub-condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

The error message indicates that the table type with Row-level Security (RLS) policies is not supported for external metadata operations. Only streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are supported as external metadata sources. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Column Mask (CM) Policies](/concepts/column-mask-policies.md) — Another data governance feature that restricts access at the column level, also unsupported for external metadata sources
- [External Metadata](/concepts/external-metadata-api.md) — A feature that allows querying metadata from external systems
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- Data Governance — The broader framework for managing data access and security

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
