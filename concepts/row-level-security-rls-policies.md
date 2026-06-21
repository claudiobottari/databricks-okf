---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 516374d6c9fdae0569f541015046f3f981a4dff459d6c855fc7e2f95dc3cb9e7
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-security-rls-policies
    - RS(P
    - Row-Level Security Policies
    - Row Level Security RLS
    - Row-Level Security
    - Row-Level Security (RLS)
    - Row-level Security
    - Row-level Security (RLS)
    - Row-level security
    - Row‑Level Security
    - row and column-level security
    - row-level security
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Row-Level Security (RLS) Policies
description: Databricks security feature for filtering rows that is incompatible with external metadata sources
tags:
  - databricks
  - security
  - delta-lake
timestamp: "2026-06-19T10:05:37.741Z"
---

# Row-Level Security (RLS) Policies

**Row-Level Security (RLS) Policies** are a data governance mechanism that restricts which rows in a database table are visible to a given user or query. RLS policies filter data at the row level based on user attributes, group membership, or other conditions, ensuring that users only see the data they are authorized to access.

## Overview

Row-Level Security policies allow organizations to implement fine-grained access control on database tables without requiring separate views or application-level filtering. When a query is executed against a table with an RLS policy, the policy automatically appends a filter condition to the query, limiting the rows returned to those that satisfy the policy's criteria. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## How RLS Policies Work

RLS policies are defined as filter conditions that are evaluated at query time. The policy specifies:

- **Scope**: The table or view where the policy is applied
- **Principals**: The users, groups, or roles subject to the policy
- **Filter condition**: A Boolean expression that determines which rows are visible

When a user queries a table protected by an RLS policy, the system transparently injects the filter condition into the query execution plan. Users who are not exempt from the policy only see rows that satisfy the filter condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Compatibility Considerations

### External Metadata Support

RLS policies have specific compatibility requirements with external metadata systems. The `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error condition indicates that certain table types with Row-Level Security policies are not supported when using external metadata. Specifically, tables with RLS policies may encounter this error when external metadata is enabled. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Error Message

When an unsupported operation is attempted on a table with RLS policies, the system returns:

```
DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE
<tableType> with Row-level Security (RLS) policies.
```

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Supported Table Types

RLS policies are supported on standard Delta tables. However, when using external metadata, only streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are supported. Standard tables with RLS policies may not be compatible with external metadata configurations. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Column Mask Policies](/concepts/column-mask-policies.md) — A complementary data governance mechanism that restricts visibility at the column level rather than the row level
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — A broader access control framework that can include row-level and column-level policies
- [Delta Lake](/concepts/delta-lake.md) — The storage layer where RLS policies are commonly applied
- [External Metadata](/concepts/external-metadata-api.md) — A feature that may have compatibility limitations with RLS policies
- Streaming Tables — A table type that supports RLS policies with external metadata
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Another table type compatible with RLS policies in external metadata scenarios

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
