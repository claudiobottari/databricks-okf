---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25d47c34dc4c1eabb568629fc91076cad7cd3d3e2f9ab9796f541514e0f3106f
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lookup-tables-in-abac-policy-udfs
    - LTIAPU
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Lookup tables in ABAC policy UDFs
description: Using small lookup tables to express user-specific access rules that cannot be captured by the TO/EXCEPT clauses alone, leveraging broadcast hash joins for performance.
tags:
  - data-governance
  - abac
  - row-filtering
  - lookup-tables
  - unity-catalog
timestamp: "2026-06-19T17:47:06.441Z"
---

# Lookup tables in ABAC policy UDFs

**Lookup tables in ABAC policy UDFs** is a pattern for implementing [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in [Unity Catalog](/concepts/unity-catalog.md) where a user-defined function (UDF) queries a separate reference table to determine access rights at query time. This approach is used when access rules are too dynamic or fine-grained to be expressed solely through the policy's `TO`/`EXCEPT` clauses.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## When to use lookup tables

The preferred approach for targeting principals in ABAC policies is to use the `TO`/`EXCEPT` clauses directly on the policy definition. However, when access rules vary per user and cannot be expressed through these clauses alone — for example, when different users need access to different data values based on a priority level — a lookup table inside the UDF provides the necessary flexibility.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## How it works

The pattern involves three components:

1. **A lookup table** that maps principals to allowed values or access rules.
2. **A UDF** that checks the lookup table, typically using a subquery that references `session_user()`.
3. **A [row filter policy](/concepts/row-filter-policies.md)** that uses the UDF, passing column values from the protected table as parameters.

The UDF returns a boolean value indicating whether the current user has access to a given row based on the rules in the lookup table.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example

The following example uses a small lookup table `access_rules` to control which users can see records by priority level:^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
-- Create a small lookup table mapping principals to allowed priorities
CREATE TABLE access_rules (
  principal VARCHAR(255),
  priority VARCHAR(64)
);

INSERT INTO access_rules VALUES
  ('alice@company.com', '1-URGENT'),
  ('alice@company.com', '2-HIGH'),
  ('bob@company.com', '1-URGENT');
```

Then create a UDF that checks the lookup table and a policy that uses it:^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
CREATE FUNCTION priority_allowed(o_priority STRING) RETURNS BOOLEAN
RETURN EXISTS (
  SELECT 1 FROM access_rules
  WHERE principal = session_user() AND priority = o_priority
);

CREATE POLICY priority_filter
ON CATALOG operations
ROW FILTER priority_allowed
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag('priority') AS pri
USING COLUMNS (pri);
```

When a user named `alice@company.com` queries a table in the `operations` catalog, the policy calls `priority_allowed(priority_value)` for each row. The UDF checks the `access_rules` table: if Alice has a matching entry for that priority value, the row is returned; otherwise, it is filtered out.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Performance considerations

### Keep lookup tables small

The lookup table should be small enough that the query optimizer can convert the subquery into a broadcast hash join. Large lookup tables can degrade performance because the subquery is evaluated per-row.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Prefer TO/EXCEPT when possible

Using `TO`/`EXCEPT` clauses is the preferred approach for targeting principals, as it avoids the overhead of subquery evaluation. Reserve the lookup table pattern for cases where the access rules are too complex or dynamic to express through the policy's built-in principal targeting.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) – The type of ABAC policy that uses UDFs for row-level filtering
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The access control model that drives policy evaluation
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer providing ABAC capabilities
- ABAC Performance Considerations – Performance implications of different ABAC patterns
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) – Best practices for managing policy proliferation

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
