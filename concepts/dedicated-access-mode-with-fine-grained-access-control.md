---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8825a4dc933b6e9ed495e2d6dc23c862efada4b174816645756f30721298aa53
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dedicated-access-mode-with-fine-grained-access-control
    - DAMWFAC
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Dedicated access mode with fine-grained access control
description: Restrictions and caveats when querying tables with row filters or column masks from dedicated access compute resources, including serverless FGAC enforcement and Cloud Fetch storage implications.
tags:
  - compute
  - unity-catalog
  - security
  - architecture
timestamp: "2026-06-19T20:16:55.414Z"
---

# Dedicated access mode with fine‑grained access control

**Dedicated access mode with fine‑grained access control** refers to the ability to query tables that have [Row filters](/concepts/row-filter-policies.md) or [Column masks](/concepts/column-mask-policies.md) applied from a [Dedicated access mode](/concepts/dedicated-access-mode-for-ml-compute.md) compute resource on Databricks. This capability is available only on specific runtime versions and has runtime‑dependent limitations on which operations are supported. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Overview

Row filters and column masks are [Unity Catalog](/concepts/unity-catalog.md) access controls that restrict which rows and column values a user can see at query time. When a table has such policies applied, queries must be routed through a mechanism that can enforce them. On dedicated access compute resources (for example, a user‑isolated cluster), Databricks uses [Serverless compute](/concepts/serverless-gpu-compute.md) to enforce these fine‑grained access controls (FGAC). ^[row-filters-and-column-masks-databricks-on-aws.md]

## Runtime requirements

- **Databricks Runtime 15.3 or below**: Tables with row filters or column masks **cannot** be accessed from a dedicated access compute resource. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Databricks Runtime 15.4 LTS or above**: Dedicated access mode is supported **only if the workspace is enabled for serverless compute**. Without a serverless compute entitlement, the query will fail. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Read vs. write support

The operations permitted on a table with row filters or column masks depend on the runtime version:

| Runtime version | Supported operations |
|----------------|----------------------|
| 15.4 LTS – 16.2 | Read‑only (`SELECT`, `MERGE INTO` is **not** supported) |
| 16.3 or above | Read and write — including `INSERT`, `UPDATE`, `DELETE`, and `MERGE INTO` (provided the write pattern is supported by the policy) |

^[row-filters-and-column-masks-databricks-on-aws.md]

Write operations on Databricks Runtime 16.3+ must still follow the supported patterns documented for the specific policy type (e.g., `MERGE INTO` is listed as a supported pattern). ^[row-filters-and-column-masks-databricks-on-aws.md]

## FGAC enforcement and Cloud Fetch

When a table with row filters or column masks is queried from dedicated access mode, Databricks uses serverless compute to evaluate the policy at runtime. All Fine‑grained access control (FGAC) limitations and considerations apply, including the use of Cloud Fetch to write temporary result sets to internal workspace storage. ^[row-filters-and-column-masks-databricks-on-aws.md]

> **S3 bucket versioning consideration**  
> If the workspace’s internal storage bucket (typically an S3 bucket) has versioning enabled, Cloud Fetch can cause exponential storage growth. See the [advanced configurations documentation](https://docs.databricks.com/aws/en/integrations/jdbc/capability#advanced-configurations) for recommendations on mitigating this issue. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Related concepts

- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – The table‑level access controls that dedicated-mode queries enforce.
- [Dedicated access mode](/concepts/dedicated-access-mode-for-ml-compute.md) – The compute mode that isolates a single user.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure used to enforce FGAC.
- [Fine‑grained access control on dedicated compute](/concepts/dynamic-views-for-fine-grained-access-control.md) – The broader documentation page covering all FGAC considerations.
- Cloud Fetch – The mechanism used to materialize temporary result sets.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer providing row- and column-level security.

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)
