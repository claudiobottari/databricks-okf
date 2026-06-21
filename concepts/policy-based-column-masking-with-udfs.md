---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a960de34fda51cb45355028865c378d5f09a3e83decd7cd90a3bb24898338558
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-based-column-masking-with-udfs
    - PCMWU
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: Policy-based column masking with UDFs
description: Using User-Defined Functions (UDFs) as the masking logic in Unity Catalog column mask policies, enabling reusable masking strategies such as partial masking and full redaction.
tags:
  - unity-catalog
  - udf
  - column-masking
  - sql
timestamp: "2026-06-19T19:10:03.444Z"
---

## Policy-based column masking with UDFs

**Policy-based column masking with UDFs** is a Databricks Unity Catalog pattern that uses User-Defined Function (UDF)|UDFs, [Governed Tag|governed tags](/concepts/governed-tags.md), and [MATCH COLUMNS](/concepts/match-columns-with-and-conditions.md) clauses to apply column-level masking based on a column’s domain (owning team) and sensitivity level. It is typically combined with [Row Filter|row filters](/concepts/row-filter-policies.md) that restrict which rows each group can see, enabling a complete multi‑domain data access control solution for shared tables. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Components

The pattern relies on two governed tags applied to each sensitive column:
- A `domain` tag (e.g., `'hr'`, `'finance'`, `'marketing'`) that indicates which team owns the column.
- A `sensitivity` tag (e.g., `'internal'` or `'confidential'`) that determines the masking strength.

A third tag, `region`, is used for row‑filtering; it can be a key‑only tag (no value). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Masking UDFs

Two scalar UDFs define the masking logic:

| UDF | Input | Output |
|-----|-------|--------|
| `partial_mask(val STRING)` | Any string | First character followed by `***` (e.g., `'a***'`) |
| `redact(val STRING)` | Any string | Constant `'***REDACTED***'` |

A third UDF, `region_filter(region_val STRING, allowed_region STRING)`, returns `TRUE` when the row’s region matches the group’s allowed region and is used in row‑filter policies. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Policies

Two types of policies are created:

1. **Row‑filter policies** – One per region. They use `MATCH COLUMNS has_tag('region')` to identify the region column and pass the allowed region as a constant via `USING COLUMNS`. The policy is applied to the appropriate account group via `TO ...` (e.g., `TO us_team`).

2. **Column mask policies** – One per domain and sensitivity combination. Each policy uses `MATCH COLUMNS (has_tag_value('domain', '<domain>') AND has_tag_value('sensitivity', '<level>'))` to target only columns that match both tag values. The `EXCEPT` clause exempts the owning group from the mask (e.g., `TO account users EXCEPT hr_team`). Internal columns get the `partial_mask` UDF; confidential columns get the `redact` UDF. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Why the pattern works

Each column is assigned exactly one `domain` value and one `sensitivity` value, so every column is matched by at most one mask policy per user. The `EXCEPT` clause ensures that members of the owning domain group see the raw data, while all other users see the masked output. A user who belongs to multiple domain groups is excluded from all corresponding policies and sees all of those domains’ columns unmasked. There are no policy conflicts. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Extensibility

Adding a new domain (e.g., Legal) requires:
- A new account group (e.g., `legal_team`).
- A new allowed tag value for `domain` (e.g., `'legal'`).
- Two new column mask policies (internal and confidential) that reference the new group in the `EXCEPT` clause.
- Tags applied to the new columns.

No existing policies need to be modified. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4+ or serverless compute.
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` privilege on the UDFs.
- Pre‑existing account groups for each domain and region. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Related concepts

- Column Masking
- [Row Filter](/concepts/row-filter-policies.md)
- [MATCH COLUMNS](/concepts/match-columns-with-and-conditions.md)
- [EXCEPT clause (Unity Catalog)](/concepts/except-clause-in-unity-catalog-access-policies.md)
- has_tag_value function
- [Unity Catalog governed tags](/concepts/unity-catalog-system-governed-tags.md)

### Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
