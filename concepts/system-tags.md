---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8fb05307c60a7964ff3e867503001bdb6a14819824ab1c1f0a200f86c3cdd24
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - system-tags
    - system tag
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: System Tags
description: Predefined tags provided by Databricks (e.g., ai.model_creator) that can be referenced in GRANT policy conditions alongside user-created governed tags.
tags:
  - data-governance
  - unity-catalog
  - tagging
  - system
timestamp: "2026-06-19T17:23:38.385Z"
---

# System Tags

**System Tags** are predefined tags created by Databricks that are automatically applied to securable objects in Unity Catalog. Unlike user-defined governed tags, system tags cannot be created, modified, or deleted by users. They provide built-in metadata about objects that can be used in attribute-based access control (ABAC) policies.

## Overview

System tags are a type of tag within Unity Catalog that Databricks manages and applies to certain securable objects automatically. They are part of the broader tagging infrastructure that supports [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md). System tags are distinct from governed tags, which users create and manage themselves. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Purpose

System tags enable ABAC GRANT policies to dynamically grant privileges based on automatically assigned metadata. For example, a GRANT policy can use a system tag like `ai.model_creator` to grant `EXECUTE` on all foundation models from a specific provider, such as Anthropic, without requiring separate grants for each individual model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Examples

One documented system tag is `ai.model_creator`, which is applied to Databricks-hosted foundation models in the `system.ai` schema. This tag indicates which organization created a given model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

For instance, a GRANT policy can match `has_tag_value('ai.model_creator', 'anthropic')` to grant `EXECUTE` on all Anthropic-hosted foundation models in `system.ai`, including models that may be added in the future. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Usage in ABAC GRANT Policies

System tags can be referenced in the `WHEN` condition of a [GRANT Policy](/concepts/grant-policies-beta.md). The policy evaluates the condition against the system tags on each securable object in the policy's scope every time access is checked. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Example GRANT policy using a system tag:

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

This policy grants `EXECUTE` on every model in `system.ai` that carries the `ai.model_creator` system tag with value `anthropic`, without requiring a separate grant per model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Comparison with Governed Tags

| Feature | System Tags | Governed Tags |
|---------|-------------|---------------|
| Created by | Databricks (automatic) | Users (manual) |
| Modified by | Not modifiable | Users |
| Deleted by | Not deletable | Users |
| Use in ABAC policies | Supported | Supported |

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

System tags are read-only. Users cannot create, alter, or delete them. They appear alongside governed tags when using tag-matching functions like `has_tag_value()` in GRANT policy conditions, but users have no control over which system tags exist or how they are assigned to objects. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [GRANT Policy](/concepts/grant-policies-beta.md)
- [Governed Tags](/concepts/governed-tags.md)
- ABAC Built-in Functions
- [Unity Catalog](/concepts/unity-catalog.md)
- [Foundation Model Access in Unity Catalog](/concepts/foundation-model-unity-catalog-permissions.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
