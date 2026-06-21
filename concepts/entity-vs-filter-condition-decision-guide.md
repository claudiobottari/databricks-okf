---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: beb967ee928b74c69e7770259e54d554978a10b4f6f030e58f05db48c06a0146
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - entity-vs-filter-condition-decision-guide
    - EVFCDG
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Entity vs Filter Condition Decision Guide
description: Design pattern distinguishing when to use entity columns for different aggregation levels vs filter conditions for row-level filtering at the same aggregation level
tags:
  - feature-engineering
  - design-patterns
  - data-modeling
timestamp: "2026-06-19T18:18:06.678Z"
---

# Entity vs Filter Condition Decision Guide

When defining features from a single [DeltaTableSource](/concepts/deltatablesource.md) in the [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) framework, you can control which rows contribute to a feature's aggregation in two ways: the `entity` parameter (on `create_feature`) and the `filter_condition` parameter (on `DeltaTableSource`). Choosing the right one depends on whether you need different aggregation levels or merely filtered rows at the same aggregation level. ^[declarative-features-databricks-on-aws.md]

## Use `entity` for Different Aggregation Levels

Set different `entity` values on your feature definitions when you need features at distinct granularities. For example, a customer-level feature uses `entity=["customer_id"]` (one row per customer), while a customer-merchant feature uses `entity=["customer_id", "merchant_id"]` (multiple rows per customer). Multiple feature definitions can share the same `DeltaTableSource` but specify different `entity` arrays to produce different aggregation levels. ^[declarative-features-databricks-on-aws.md]

## Use `filter_condition` for Filtering Rows at the Same Aggregation Level

Apply `filter_condition` on the `DeltaTableSource` when you want to restrict which rows participate in the aggregation without changing the grouping keys. For instance, "high-value transactions only" (`filter_condition="amount > 100"`) or "completed orders only" (`filter_condition="status = 'completed'"`) still aggregates per customer — the entity column stays the same. The filter simply limits the rows that feed into the computation. ^[declarative-features-databricks-on-aws.md]

## Rule of Thumb

If your change would result in a different number of rows per entity value, use different `entity` values on your feature definitions. If you are merely filtering which rows contribute to the same aggregation, use `filter_condition` on the source. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The overarching API for defining and computing features.
- [DeltaTableSource](/concepts/deltatablesource.md) — The primary source type for declarative features.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — Defines the computation applied to filtered rows.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — General workflow for creating training data.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
