---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b12d3875826a3f1bfb33fa8cbaa52bb87f88c3191f4f5f5abe32b183f26ac3d
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - except-clause-in-unity-catalog-access-policies
    - ECIUCAP
    - EXCEPT clause (Unity Catalog)
    - EXCEPT clause in access policies
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: EXCEPT clause in Unity Catalog access policies
description: Using EXCEPT in policy definitions to exempt specific groups from masking or filtering rules while applying the policy to all other principals, enabling owner-group exceptions.
tags:
  - unity-catalog
  - access-control
  - sql-patterns
timestamp: "2026-06-19T19:09:53.539Z"
---

# EXCEPT Clause in Unity Catalog Access Policies

The **EXCEPT clause** is a syntax element in Unity Catalog access policies — specifically in [Column Mask Policies](/concepts/column-mask-policies.md) — that exempts a specified group from the policy’s effect. It allows a policy to apply to a broad audience (such as all `account users`) while carving out a set of users who should see the raw data unmasked. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Syntax

In a `CREATE POLICY` statement, the `EXCEPT` clause appears after the `TO` principal list:

```sql
CREATE POLICY policy_name
ON SCHEMA schema_name
COLUMN MASK udf_name
TO `account users` EXCEPT `exempted_group`
FOR TABLES
MATCH COLUMNS ( ... ) AS m
ON COLUMN m;
```

The policy applies to every principal in the `TO` list **except** those who are members of the group named in the `EXCEPT` clause. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## How It Enables Domain‑Based Ownership

The EXCEPT clause is the key mechanism for implementing domain‑owned column masking across shared tables. In a typical multi‑domain scenario:

- Each column is tagged with a `domain` value (e.g., `'hr'`, `'finance'`, `'marketing'`) and a `sensitivity` value.
- A separate column mask policy is created for each domain–sensitivity combination.
- The policy is defined with `TO account users EXCEPT <owning_group>`. For example, the HR internal mask policy uses `TO account users EXCEPT hr_team`. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

Because the policy applies to everyone except the owning group, members of that group see the unmasked value, while all other users see the masked output. This pattern ensures that **each domain’s own team sees its columns in plain text**, but teams from other domains see only the appropriate mask level. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Multiple‑Group Membership

When a user belongs to multiple domain groups (e.g., `hr_team` and `marketing_team`), they are excluded from the policies of all the groups they are in. As a result, columns owned by any of those domains appear unmasked, while columns owned by other domains remain masked. No additional configuration is required. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Comparison with Row Filters

Row filter policies in Unity Catalog typically use `TO` without an `EXCEPT` clause, relying instead on static arguments or inline group checks inside the filter UDF. The EXCEPT clause is predominantly used with column mask policies to create an ownership exemption pattern. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Benefits

- **No policy conflicts**: Each column is matched by exactly one policy per user because columns carry a single domain tag. The EXCEPT clause then determines whether the policy applies to that user. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
- **Extensible**: Adding a new domain requires only a new group, new policies with the corresponding EXCEPT clause, and column tags. Existing policies are unaffected. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Related Concepts

- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Unity Catalog governed tags](/concepts/unity-catalog-system-governed-tags.md)
- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- Multi-domain column masking

## Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
