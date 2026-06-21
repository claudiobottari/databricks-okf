---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 501a78f801e19b70468361c5a4b44b48b11e1ac0bd6a89cb1246b9fe7d7de9b7
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filtering-with-region-based-policies
    - RFWRP
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: Row filtering with region-based policies
description: Applying row-level filters via Unity Catalog policies that restrict data visibility based on geographic region, using UDFs that compare a tagged column value against an allowed region constant.
tags:
  - unity-catalog
  - row-filtering
  - access-control
  - data-governance
timestamp: "2026-06-19T19:09:41.875Z"
---

# Row Filtering with Region-Based Policies

**Row filtering with region-based policies** is a pattern in Databricks [Unity Catalog](/concepts/unity-catalog.md) that restricts which rows of a table are visible to different groups based on the geographic region associated with each row. This pattern is often combined with domain-aware column masking to implement both row-level and column-level access controls from a single set of governed tags. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Overview

Region-based row filtering uses [Row Filter Policy|row filter policies](/concepts/row-filter-policies.md) and a User-Defined Function (UDF) to compare a column that identifies the row’s region (for example, `emp_region`) against a static constant representing the region a group is authorized to see. Each row filter policy targets one group and passes the allowed region as a constant via `USING COLUMNS`. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

The core mechanism works as follows:

1. A column in the table (e.g., `emp_region`) is tagged with a key-only tag such as `region`. The tag value is left empty because the policy only needs to identify the column, not check a specific value. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
2. A UDF accepts the row’s region value and an allowed region constant, and returns `TRUE` when they match. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
3. A row filter policy is created for each region, targeting a specific group (for example, `us_team` or `eu_team`). The policy uses `MATCH COLUMNS` with `has_tag('region')` to identify the region column, and `USING COLUMNS` to supply the column and the allowed region constant. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Key Components

### Governed Tags

A region tag must be applied to the column that holds the region identifier. For example:

```sql
ALTER TABLE employee_records
  ALTER COLUMN emp_region SET TAGS ('region' = '');
```

The key is `region`; the value is empty because the policy only needs to identify the column. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Row Filter UDF

The UDF accepts two arguments: the column value from each row and a static allowed region string. It returns `TRUE` when they are equal.

```sql
CREATE OR REPLACE FUNCTION abac_tutorial.domain_demo.region_filter(
  region_val STRING,
  allowed_region STRING
)
RETURNS BOOLEAN
RETURN region_val = allowed_region;
```

^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Row Filter Policies

Create one policy per region, targeting the appropriate group. Each policy uses `MATCH COLUMNS` with `has_tag('region') AS region_col` to bind the tagged column, and `USING COLUMNS` to pass both the column and the allowed region constant.

```sql
CREATE POLICY region_filter_us
ON SCHEMA abac_tutorial.domain_demo
ROW FILTER abac_tutorial.domain_demo.region_filter
TO `us_team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS region_col
USING COLUMNS (region_col, 'us');

CREATE POLICY region_filter_eu
ON SCHEMA abac_tutorial.domain_demo
ROW FILTER abac_tutorial.domain_demo.region_filter
TO `eu_team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS region_col
USING COLUMNS (region_col, 'eu');
```

^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Alternative Approach Using Identity Functions

Instead of passing the allowed region as a static constant, you can embed the group-to-region mapping directly inside the UDF using identity functions such as `is_account_group_member()`. This approach uses a single policy with no static values, but it moves the mapping logic into the UDF. Choose whichever approach fits your organization. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Integration with Domain-Based Column Masking

Region-based row filtering is typically combined with Column Masking policies that apply different masking rules based on a column’s `domain` and `sensitivity` tags. In such a combined setup, a user in a group like `hr_team` in the US region sees HR columns unmasked (via `EXCEPT` clauses on column masks) and only rows where `emp_region = 'us'` (via the row filter). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

The row filter and column mask policies are created independently on the same table; both are enforced at query time. There is no conflict because each policy targets a distinct access control dimension (rows versus columns). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC) – Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- [Row Filter Policy](/concepts/abac-row-filter-policy.md)
- Column Masking
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog – Data Governance](/concepts/unity-catalog-governance.md)
- [User-Defined Functions (UDF) – Databricks](/concepts/abac-user-defined-functions-udfs.md)

## Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
