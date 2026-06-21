---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75b07bad130171210248266c1ec6cd06ac7fa6f00cc19bd0b46dd9a5617d89ce
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-domain-column-masking-with-sensitivity-tiers
    - MCMWST
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: Multi-domain column masking with sensitivity tiers
description: A pattern for applying column-level masks that vary by both domain ownership and sensitivity classification, using AND conditions in MATCH COLUMNS to target specific combinations of governed tags.
tags:
  - data-governance
  - unity-catalog
  - column-masking
  - access-control
timestamp: "2026-06-19T19:09:31.534Z"
---

# Multi-domain column masking with sensitivity tiers

**Multi-domain column masking with sensitivity tiers** is a [Unity Catalog](/concepts/unity-catalog.md) pattern for implementing attribute-based access control (ABAC) on a shared table. It uses [Governed Tags](/concepts/governed-tags.md) to mark each column with two attributes — a domain (owning team) and a sensitivity level — and then applies [column masking](/concepts/delta-lake-column-masking.md) policies that match columns by both tags using AND conditions in `MATCH COLUMNS`. An `EXCEPT` clause exempts the owning domain group so members see unmasked data, while others see a mask that varies by sensitivity level. The pattern is often combined with [row filtering](/concepts/row-filters-in-unity-catalog.md) to further restrict rows by region. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Overview

In organizations where multiple teams (e.g., HR, Finance, Marketing) share a central table such as `employee_records`, each team must see its own columns unmasked but other teams’ sensitive data must be protected. A single sensitivity tag is not enough because the same sensitivity level (e.g., “internal”) may require different masks for different teams. Domain-aware masking solves this by pairing a `domain` tag (which column a team owns) with a `sensitivity` tag (how aggressively to mask for outside users). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## How it works

### Governed tags

Two governed tags are created:

- `domain` — set to `hr`, `finance`, or `marketing` (or any business group name).  
- `sensitivity` — set to `internal` or `confidential`.  

Tag values are plain text and may be replicated globally; they must not contain personal or sensitive information. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

Each sensitive column receives exactly one `domain` value and exactly one `sensitivity` value. A region tag (`region`) is used for row filtering. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Column mask policies

One column mask policy is created per domain–sensitivity combination (e.g., `mask_internal_hr`, `mask_confidential_hr`, `mask_internal_finance`, etc.). Each policy:

- Targets `account users` with an `EXCEPT` clause for the owning domain group.
- Uses `MATCH COLUMNS` with an AND condition:  
  `has_tag_value('domain', '<value>') AND has_tag_value('sensitivity', '<value>')`.
- Calls a UDF to produce the mask:
  - **Internal** columns → `partial_mask()` (first character + `***`).  
  - **Confidential** columns → `redact()` (`***REDACTED***`).

Because each column has exactly one domain and one sensitivity, it matches exactly one policy per user. There are no conflicts. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Row filter policies (optional)

Row filter policies restrict rows based on region. A UDF `region_filter` compares the column value with a static allowed region. Each policy targets one group (e.g., `us_team`) and uses `MATCH COLUMNS has_tag('region') AS region_col` then `USING COLUMNS (region_col, 'us')`. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Group membership

A user who belongs to multiple domain groups (e.g., `hr_team` AND `marketing_team`) is excluded from both sets of policies, so both domains’ columns are unmasked. All other columns are masked according to their sensitivity level. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Example scenario

The tutorial uses an `employee_records` table with columns tagged as:

| Column | domain | sensitivity |
|--------|--------|-------------|
| `employee_name` | hr | internal |
| `ssn` | hr | confidential |
| `email` | marketing | internal |
| `customer_list` | marketing | confidential |
| `cost_center` | finance | internal |
| `salary_band` | finance | confidential |
| `emp_region` | region | (key only) |

A member of `hr_team` + `us_team` sees HR columns unmasked, Marketing columns masked (email partially, customer_list redacted), Finance columns masked, and only US rows. A member of `finance_team` + `eu_team` sees Finance columns unmasked, all others masked, and only EU rows. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Benefits

- **Scalability**: Adding a new domain requires only a new group, a new tag value, and two new policies. Existing policies do not need to change. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]  
- **No conflicts**: Each column is matched by exactly one policy per user. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]  
- **Multi‑group support**: Users in multiple domain groups see all their domains’ data unmasked automatically via the `EXCEPT` clauses. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]  
- **Flexibility**: The domain tag can be named `team`, `department`, or `business_unit`; the logic is unchanged. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Related concepts

- [Attribute-based access control (ABAC) with Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Column masking](/concepts/delta-lake-column-masking.md)
- [Row filtering](/concepts/row-filter-policies.md)
- MATCH COLUMNS clause
- [EXCEPT clause in access policies](/concepts/except-clause-in-unity-catalog-access-policies.md)
- has_tag function
- has_tag_value function
- User-defined functions (UDFs) for masking
- is_account_group_member function

## Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
