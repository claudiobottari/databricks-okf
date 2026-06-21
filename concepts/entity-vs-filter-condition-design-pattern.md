---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46e9d8c44046a488d07cfeb8cc3769601b2aeab8129bc807935a29f9bc02f982
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - entity-vs-filter-condition-design-pattern
    - EVFCDP
    - entity-vs-filter-condition-decision-guide
    - EVFCDG
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Entity vs Filter Condition Design Pattern
description: "Decision guide for structuring feature definitions: use entity columns for different aggregation levels (e.g., customer-level vs customer-merchant) and filter_condition for filtering rows within the same aggregation level."
tags:
  - feature-engineering
  - design-patterns
  - data-modeling
timestamp: "2026-06-19T09:57:29.994Z"
---

# Entity vs Filter Condition Design Pattern

The **Entity vs Filter Condition Design Pattern** is a decision guide for [Declarative Feature Engineering on Databricks](/concepts/declarative-feature-engineering-apis.md) that helps practitioners choose between two mechanisms — `entity` columns and `filter_condition` on a `DeltaTableSource` — when defining Feature objects from the same source table. Applying the correct mechanism ensures that feature definitions remain clear, performant, and semantically correct. ^[declarative-features-databricks-on-aws.md]

## Overview

When you derive multiple features from a single Delta table, you often need to restrict which rows contribute to each feature or change the granularity of aggregation. The design pattern draws a clean boundary between two concerns:

- **Aggregation level** – the set of columns that define the grouping key (one row per combination of entity column values).
- **Row filtering** – a condition that selects which rows of the source table are included in the aggregation, without changing the grouping key.

The pattern states that you should use `entity` to control the aggregation level and `filter_condition` to filter rows when the aggregation level remains unchanged. ^[declarative-features-databricks-on-aws.md]

## When to Use `entity`

Use the `entity` parameter (on `create_feature` or `Feature`) when you need **different aggregation levels** across features that share the same `DeltaTableSource`. ^[declarative-features-databricks-on-aws.md]

| Scenario | `entity` value | Result |
|----------|----------------|--------|
| Customer-level features (one row per customer) | `entity=["customer_id"]` | Each customer produces one aggregated row. |
| Customer–merchant features (multiple rows per customer) | `entity=["customer_id", "merchant_id"]` | Each customer–merchant pair produces one aggregated row. |

Different features can share the same `DeltaTableSource` while specifying different `entity` values. This allows, for example, a feature that aggregates across all of a customer's transactions alongside a feature that aggregates per merchant for the same customer. ^[declarative-features-databricks-on-aws.md]

## When to Use `filter_condition`

Use `filter_condition` on the `DeltaTableSource` when you need to **filter rows at the same aggregation level**. The filtering does not change the number of rows per entity value—it only determines which source rows are fed into the aggregation function. ^[declarative-features-databricks-on-aws.md]

| Scenario | `filter_condition` | Aggregation unchanged |
|----------|---------------------|-----------------------|
| High-value transactions only | `filter_condition="amount > 100"` | Still aggregated per customer |
| Completed orders only | `filter_condition="status = 'completed'"` | Still aggregated per customer |

The `filter_condition` applies to the source rows before aggregation, so it is a convenient way to compute statistics on a subset of the data while keeping the grouping key identical across features. ^[declarative-features-databricks-on-aws.md]

## Rule of Thumb

> If your change would result in a **different number of rows per entity value**, use different `entity` values on your feature definitions. If you are just **filtering which rows contribute to the same aggregation**, use `filter_condition` on the source. ^[declarative-features-databricks-on-aws.md]

In other words, `entity` changes **granularity**; `filter_condition` changes **membership** within the same granularity.

## Example

The following example creates two features from a `transactions` source table. The first uses a custom aggregation level to produce per-merchant aggregates; the second uses a `filter_condition` to compute statistics only for completed transactions while grouping by the original entity key. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import (
    DeltaTableSource, AggregationFunction, Sum, Count
)

fe = FeatureEngineeringClient()

source = DeltaTableSource(
    catalog_name="main",
    schema_name="ecommerce",
    table_name="transactions",
)

# Different entity level: per (customer, merchant)
feature_per_merchant = fe.create_feature(
    catalog_name="main",
    schema_name="ecommerce",
    source=source,
    entity=["customer_id", "merchant_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Sum(input="amount"), ...),
    name="amount_sum_per_merchant",
)

# Same entity level, but filter rows: only completed orders
feature_completed_orders = fe.create_feature(
    catalog_name="main",
    schema_name="ecommerce",
    source=DeltaTableSource(
        catalog_name="main",
        schema_name="ecommerce",
        table_name="transactions",
        filter_condition="status = 'completed'",
    ),
    entity=["customer_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Count(input="transaction_id"), ...),
    name="completed_orders_count",
)
```

## Related Concepts

- [Declarative Feature Engineering on Databricks](/concepts/declarative-feature-engineering-apis.md) – The broader API framework that includes `entity` and `filter_condition`.
- [DeltaTableSource](/concepts/deltatablesource.md) – The data source object that accepts `filter_condition`.
- Feature – The object representing a single feature definition.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Defines the windowed aggregation logic applied after filtering.
- Entity columns – The group-by columns used during feature computation.
- [Feature Materialization](/concepts/feature-materialization.md) – How features are persisted for serving and training.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
