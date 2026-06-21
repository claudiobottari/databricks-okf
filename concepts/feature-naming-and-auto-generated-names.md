---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30fccde472585b488ab8fdeb2982ce4682728a29ddbfc66b77270c228997c42c
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-naming-and-auto-generated-names
    - Auto-Generated Names and Feature Naming
    - FNAAN
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Naming and Auto-Generated Names
description: A naming convention system where features can be explicitly named or auto-named based on function, window, and column properties for traceability.
tags:
  - feature-engineering
  - best-practices
  - naming
timestamp: "2026-06-19T14:57:49.069Z"
---

# Feature Naming and Auto-Generated Names

**Feature Naming and Auto-Generated Names** refers to the conventions and mechanisms for assigning names to features defined through Databricks' Declarative Feature Engineering APIs. When defining features, users can either provide an explicit name or rely on the system to automatically generate a name based on the function and window parameters. ^[declarative-features-databricks-on-aws.md]

## Auto-Generated Names

If a feature is created using `create_feature` or constructed as a `Feature` object without providing a `name` parameter, the system automatically generates a name. The auto-generated name follows a pattern derived from the aggregation function, the input column, and the window specification. ^[declarative-features-databricks-on-aws.md]

For example, in the quickstart, a feature defined with `Sum(input="amount")` and `SlidingWindow(window_duration=timedelta(days=7), slide_duration=timedelta(days=1))` receives the auto-generated name `amount_sum_sliding_7d_1d`. ^[declarative-features-databricks-on-aws.md]

The auto-generated naming scheme is intended to provide a readable, deterministic identifier that reflects the feature’s computation. This helps developers quickly understand what a feature represents without having to look up its definition. ^[declarative-features-databricks-on-aws.md]

## Best Practices

Databricks recommends the following guidelines for feature naming: ^[declarative-features-databricks-on-aws.md]

- **Use descriptive names for business-critical features.** Once a feature is used in production, a clear, human-readable name makes it easier to manage, audit, and reuse across teams. ^[declarative-features-databricks-on-aws.md]
- **Follow consistent naming conventions across teams.** Standardizing naming patterns (e.g., `metric_aggregation_window`) reduces confusion when features are shared across different projects. ^[declarative-features-databricks-on-aws.md]
- **Use auto-generated names as you begin developing features.** During early prototyping, auto-generated names are sufficient and save effort. Explicit, descriptive names can be assigned later when the feature is promoted to production. ^[declarative-features-databricks-on-aws.md]

## Relation to the Feature Development Workflow

In the declarative feature lifecycle, naming is handled differently depending on the workflow:

| Workflow | Naming approach |
|----------|-----------------|
| Local feature construction (`Feature` object) | Name can be omitted; auto-generated until `register_feature` is called. |
| `create_feature` (define and register in one step) | Name can be explicitly provided or left to auto-generation. |

Regardless of the approach, once a feature is registered in Unity Catalog, its name becomes a persistent identifier used in training sets, materialization, and serving. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) – The broader API set that includes feature naming.
- Feature – The entity class that holds a feature definition, including its name (explicit or auto-generated).
- create_feature – The API method that registers a feature and can accept an optional name.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog where features are stored and identified by name.
- [Training Set](/concepts/training-set-feature-store.md) – A collection of features referenced by their names during model training.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
