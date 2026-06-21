---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c1d1c5d9826cecc11aa542217e8feef9b04394435c096e63b3a2bb06fc1674c
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-for-column-classification
    - GTFCC
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: Governed tags for column classification
description: A governed tag system in Unity Catalog that associates key-value metadata (e.g., domain, sensitivity) with columns, which can be queried by policy MATCH COLUMNS clauses to dynamically target columns.
tags:
  - unity-catalog
  - data-classification
  - tagging
timestamp: "2026-06-19T19:09:53.855Z"
---

# Governed Tags for Column Classification

**Governed tags for column classification** is a pattern in [Unity Catalog](/concepts/unity-catalog.md) that uses [Governed Tags](/concepts/governed-tags.md) to label table columns with metadata such as ownership domain and sensitivity level, enabling automated [column masking](/concepts/delta-lake-column-masking.md) and [row filtering](/concepts/row-filters-in-unity-catalog.md) policies based on those tags. This approach allows organizations to implement fine-grained, attribute-based access control ([ABAC](/concepts/abac-attribute-based-access-control.md)) without maintaining separate policies for each column.

## Overview

Governed tags are metadata labels that can be applied to columns in Unity Catalog tables. When used for column classification, each column is assigned one or more tag key-value pairs that describe its characteristics — for example, which team owns the column (`domain = 'hr'`) and how sensitive the data is (`sensitivity = 'confidential'`). Policies can then use [MATCH COLUMNS](/concepts/match-columns-with-and-conditions.md) clauses with functions like has_tag() and has_tag_value() to target columns by their tags, and apply masking or filtering automatically. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Common Classification Dimensions

Two common classification dimensions used with governed tags are domain and sensitivity:

- **Domain** (or team, department, business unit): Identifies which group owns each column. For example, `domain = 'hr'`, `domain = 'finance'`, or `domain = 'marketing'`. The tag name is arbitrary; the key idea is that each column is assigned to exactly one owning group. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
- **Sensitivity**: Controls how aggressively data is masked for users outside the owning group. Common values include `internal` (partial mask, e.g., first character + `***`) and `confidential` (full redaction, e.g., `***REDACTED***`). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Policy Implementation

Policies use AND conditions in `MATCH COLUMNS` to target columns by both domain and sensitivity level simultaneously. Each column has exactly one `domain` value and one `sensitivity` value, so each column is matched by exactly one policy per user. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Exception Clause

The `EXCEPT` clause is key to the pattern. Each mask policy applies to all users except the domain group that owns the targeted columns. If a user is in the owning group, the policy does not apply and they see raw data. If they are not, the policy applies and the data is masked. Users in multiple domain groups see all of their domains' columns unmasked. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

### Example Policies

For internal-level columns, partial masking is applied to users outside the owning domain:

```sql
CREATE POLICY mask_internal_hr
ON SCHEMA abac_tutorial.domain_demo
COLUMN MASK abac_tutorial.domain_demo.partial_mask
TO `account users` EXCEPT `hr_team`
FOR TABLES
MATCH COLUMNS (
  has_tag_value('domain', 'hr')
  AND has_tag_value('sensitivity', 'internal')
) AS m
ON COLUMN m;
```

^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

For confidential-level columns, full redaction is applied:

```sql
CREATE POLICY mask_confidential_finance
ON SCHEMA abac_tutorial.domain_demo
COLUMN MASK abac_tutorial.domain_demo.redact
TO `account users` EXCEPT `finance_team`
FOR TABLES
MATCH COLUMNS (
  has_tag_value('domain', 'finance')
  AND has_tag_value('sensitivity', 'confidential')
) AS m
ON COLUMN m;
```

^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Scalability

Adding a new domain requires: ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
1. A new account group (e.g., `legal_team`)
2. A new allowed value for the `domain` tag (e.g., `legal`)
3. Two new policies (one for internal, one for confidential)
4. Tags on the new columns

No existing policies need to change, making the pattern scalable as the organization grows. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Prerequisites

- Databricks Runtime 16.4 or above, or serverless compute
- Account admin or workspace admin permissions (to create governed tags)
- `MANAGE` permission on the target catalog or schema
- `EXECUTE` on the UDFs used for masking and filtering

^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Security Considerations

Tag data is stored as plain text and may be replicated globally. Tag names, values, or descriptors should not contain personal or sensitive information that could compromise the security of your resources. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Related Concepts

- [Column masking](/concepts/delta-lake-column-masking.md) — Applying transformations to column values based on user identity
- [Row filtering](/concepts/row-filter-policies.md) — Filtering rows based on user identity and data attributes
- [Governed Tags](/concepts/governed-tags.md) — The metadata tagging system used for classification
- [MATCH COLUMNS](/concepts/match-columns-with-and-conditions.md) — SQL syntax for targeting columns by tag values
- Unity Catalog ABAC — Attribute-based access control in Unity Catalog

## Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
