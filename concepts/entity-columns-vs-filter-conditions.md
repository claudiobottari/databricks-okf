---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cff6bb9557542042757a779c994c4d9ea425f83e1631eb5f2b82caf103ae3ac
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - entity-columns-vs-filter-conditions
    - ECVFC
    - Filter Conditions
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Entity Columns vs Filter Conditions
description: A design pattern decision guide for choosing between entity columns (for different aggregation levels) and filter_condition on DeltaTableSource (for row filtering at the same aggregation level).
tags:
  - feature-engineering
  - best-practices
  - databricks
timestamp: "2026-06-19T14:57:34.577Z"
---

---
title: Entity Columns vs Filter Conditions
summary: Design pattern for deciding whether to use entity columns (for different aggregation levels) or filter_condition on DeltaTableSource (for filtering rows at the same aggregation level) when defining features from the same source table.
sources:
  - declarative-features-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:47:03.240Z"
updatedAt: "2026-06-18T15:12:43.960Z"
tags:
  - feature-engineering
  - best-practices
  - data-modeling
aliases:
  - entity-columns-vs-filter-conditions
  - ECVFC
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

# Entity Columns vs Filter Conditions

**Entity Columns vs Filter Conditions** is a decision guide for when to use `entity` columns (specified via the `entity` parameter on `create_feature` or `Feature`) versus `filter_condition` (specified on `DeltaTableSource`) when defining [declarative features](/concepts/declarative-feature-engineering-api.md) from the same source table. Choosing the correct mechanism ensures features are computed at the right granularity and avoids unnecessary data duplication. ^[declarative-features-databricks-on-aws.md]

## When to Use Entity Columns

Use `entity` when you need different **aggregation levels** for features that share the same source table. The entity columns define the grouping keys for the aggregation, and therefore the number of rows produced per unique combination of entities. ^[declarative-features-databricks-on-aws.md]

- **Customer-level features** (one row per customer): `entity=["customer_id"]`
- **Customer‑merchant features** (multiple rows per customer): `entity=["customer_id", "merchant_id"]`
- Different aggregation levels can safely coexist on the same `DeltaTableSource` by specifying different `entity` values on each feature definition. ^[declarative-features-databricks-on-aws.md]

## When to Use Filter Conditions

Use `filter_condition` (on `DeltaTableSource`) when you need to **filter rows** at the same aggregation level — that is, when the change does not alter the number of rows produced per entity. ^[declarative-features-databricks-on-aws.md]

- **High‑value transactions only**: `filter_condition="amount > 100"` (still aggregated per customer)
- **Completed orders only**: `filter_condition="status = 'completed'"` (still aggregated per customer)

Because the entity keys remain unchanged, all features built from that source share the same grouping, and the filter simply excludes rows that do not satisfy the condition before aggregation. ^[declarative-features-databricks-on-aws.md]

## Rule of Thumb

> If your change would result in a different number of rows per entity value, use different `entity` values on your feature definitions. If you're just filtering which rows contribute to the same aggregation, use `filter_condition` on the source. ^[declarative-features-databricks-on-aws.md]

This rule prevents subtle errors where a filter condition unintentionally changes the intended granularity of a feature, or where an overly broad entity list causes unnecessary joins during model training and serving. ^[declarative-features-databricks-on-aws.md]

## Example: Same Source, Different Needs

Suppose you have a `transactions` Delta table with columns `customer_id`, `merchant_id`, `amount`, `status`, and `transaction_time`.

- You want a **total spend per customer** over the last 30 days. This is a customer‑level feature → `entity=["customer_id"]`.
- You also want a **total spend per customer and merchant** over the same period. This changes the row count per customer → `entity=["customer_id", "merchant_id"]` (different entity).
- You want **total spend per customer from completed orders only**. The aggregation level is still per customer → use `filter_condition="status = 'completed'"` on the `DeltaTableSource`.

## Summary Table

| Scenario | Mechanism | Effect |
|----------|-----------|--------|
| Different aggregation level (different number of rows per entity) | `entity` parameter | Changes grouping keys for aggregation |
| Same aggregation level, different rows contributing | `filter_condition` on `DeltaTableSource` | Filters rows before aggregation, same grouping |
| Same source, multiple aggregation levels | Multiple feature definitions with different `entity` values | Coexists on same `DeltaTableSource` |

## Related Concepts

- [Declarative Features](/concepts/declarative-feature-engineering-api.md) — Overview of the declarative feature engineering API
- Feature — The core object representing a single feature definition
- [DeltaTableSource](/concepts/deltatablesource.md) — The data source specification that accepts `filter_condition`
- create_feature — One‑step define‑and‑register workflow
- materialize_features() API|Materialized Features — How features are materialized for training and serving
- Feature Engineering Best Practices — General guidance for feature development

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
