---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02969dc35cf49df5cf397ff66d45818e00a528a7ab151456cdad2ba46ed350b1
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-and-system-tags
    - System Tags and Governed Tags
    - GTAST
    - Governed Tags Management
    - System governed tags
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Governed Tags and System Tags
description: Tag metadata used in GRANT policy conditions — governed tags are user-defined, system tags are predefined by Databricks — to determine which securable objects a policy applies to.
tags:
  - governance
  - unity-catalog
  - tagging
  - databricks
timestamp: "2026-06-19T08:47:02.543Z"
---

# Governed Tags and System Tags

**Governed Tags** and **System Tags** are two categories of metadata tags in Unity Catalog that can be used in attribute-based access control (ABAC) policies, including [ABAC GRANT Policy](/concepts/abac-grant-policy.md) conditions. Governed tags are user-defined, while system tags are predefined by Databricks. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Governed Tags

Governed tags are tags that you create yourself and apply to securable objects in Unity Catalog. They are fully under your control — you define the tag keys, values, and which objects they apply to. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

These tags are used in ABAC policy conditions to dynamically determine access. For example, a governed tag like `lifecycle` with value `production` can be applied to MLflow models, and a GRANT policy can grant `EXECUTE` only on models carrying that tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example Usage

The following GRANT policy uses the `lifecycle` governed tag applied to customer-registered MLflow models in `production.ml_models`. The policy grants `EXECUTE` only on models tagged `lifecycle = 'production'`:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## System Tags

System tags are tags predefined by Databricks that are automatically applied to certain securable objects. They provide built-in metadata that can be referenced in ABAC policy conditions without requiring manual tag creation or maintenance. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Foundation Model Access

System tags are particularly useful for managing access to Databricks-hosted foundation models in `system.ai`. For example, the `ai.model_creator` system tag identifies which company created a foundation model. The following policy grants `EXECUTE` on all Anthropic-hosted foundation models to `data_scientists`, except `contractors`:

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

This approach covers every model that carries `ai.model_creator = 'anthropic'` without requiring a separate grant per model. As Databricks adds new Anthropic models, they are automatically covered by the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Using Tags in ABAC Policies

Both governed tags and system tags can be referenced in GRANT policy conditions using built-in functions such as `has_tag()` and `has_tag_value()`. Unity Catalog evaluates the policy's `WHEN` condition against the tags on each securable object in the policy's scope every time access is checked. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Policies that use tags to dynamically grant privileges
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform providing tag and ABAC capabilities
- [Data Classification](/concepts/data-classification.md) — Automatic detection and tagging of sensitive columns
- [ABAC Policies from Data Classification](/concepts/abac-policies-from-data-classification.md) — Creating masking policies from classification tags
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns based on tag conditions

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
