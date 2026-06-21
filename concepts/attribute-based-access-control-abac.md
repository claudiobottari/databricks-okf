---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4fabbb5db53452bb59492c9a40c94519fca85b56f03a3d63ed4424af37690af
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - attribute-based-access-control-abac
    - AAC(
    - ABAC|Attribute-Based Access Control (ABAC)
    - ABAC|attribute-based access control (ABAC)
    - Attribute-Based Access Control
    - Attribute-Based Access Control (ABAC) Overview
    - Attribute-Based Access Control (ABAC) policies
    - Attribute-based access control
    - Attribute‑Based Access Control (ABAC)
    - attribute‑based access control (ABAC)
    - ABAC Policies|attribute-based access control (ABAC)
    - Core concepts for attribute-based access control (ABAC)
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: access-control-in-unity-catalog-databricks-on-aws.md
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Attribute-Based Access Control (ABAC)
description: Dynamic, fine-grained access policies based on attributes of data and users, enabling row-level filtering and column-level masking without managing permissions table by table.
tags:
  - data-governance
  - access-control
  - security
timestamp: "2026-06-19T19:01:39.605Z"
---

# Attribute-Based Access Control (ABAC)

**Attribute-Based Access Control (ABAC)** is a dynamic access control model in Unity Catalog where access decisions are based on policies evaluated against attributes associated with securable objects, rather than per-object grants. ABAC uses governed tags and centralized policies to enable fine-grained, scalable access control across data and AI assets. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Access control in Unity Catalog is built on complementary models including privileges and ownership, attribute-based policies (ABAC), table-level filtering and masking, and workspace-level restrictions. These models work together to enforce secure, fine-grained access across your data environment.^[access-control-in-unity-catalog-databricks-on-aws.md] Databricks recommends using ABAC to centralize and scale access control based on governed tags.^[access-control-in-unity-catalog-databricks-on-aws.md]

## How ABAC Works

ABAC in Unity Catalog is built on three core components that work together to define and enforce access rules dynamically: governed tags, policies, and user-defined functions (UDFs).^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Governed Tags

Governed tags are the attributes that ABAC policies evaluate. They are key-value pairs defined at the account level that represent characteristics such as sensitivity, classification, or business domain. By default, securables inherit tags from their parent catalog or schema. You can override inherited tags at every level except the column level — column tags do not inherit from the parent table and must be applied directly.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Governed tags are defined at the account level, which allows the same tag taxonomy to be used across an entire data estate, including across multiple metastores.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] After classification, tags can integrate directly with ABAC policies, allowing you to apply governance controls based on what the data actually contains rather than managing access object by object.^[get-started-with-unity-catalog-databricks-on-aws.md]

### Policies

Policies are attached to securable objects in Unity Catalog to define access control rules based on tag conditions. Each policy specifies the scope of the securable object, the principals it applies to (and those who are exempt), the action it enforces, and the conditions based on tags.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

ABAC supports three policy types:

1. **Row Filter Policies**: Restrict which rows a user can see in a table based on column values identified by tags. The policy references a UDF that evaluates each row; rows where the function returns `FALSE` are excluded from query results.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

2. **Column Mask Policies**: Control what values a user sees for specific columns identified by tags. The policy references a UDF that takes the column value as input and returns the original value or a masked version.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

3. **GRANT Policies (Beta)**: Dynamically grant a Unity Catalog privilege when their tag-based condition matches a securable object's tags. Currently scoped to `EXECUTE` on models.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Conditions are tag-based expressions that use built-in functions such as `has_tag()` and `has_tag_value()`, which check whether a given tag is present on the target data object, either directly or through tag inheritance.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### User-Defined Functions (UDFs)

Row filter and column mask policies use user-defined functions (UDFs) to implement their filtering or masking logic. SQL UDFs are recommended for better performance. Python UDFs are also supported, though the query optimizer cannot inline or optimize them the way it can SQL UDFs.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of ABAC

- **Reusable policies based on attributes**: A single policy can apply to multiple data objects that match the same attribute-based conditions, rather than being tied to one specific object.
- **Automatic application to new objects**: When new data objects are created within scope and tagged, existing ABAC policies apply without additional configuration.
- **Consistent enforcement within a scope**: Policies attached at the catalog or schema level are evaluated dynamically against matching data objects in that scope.
- **Lower ongoing maintenance**: Changes can be made by updating policy logic or governed tags, rather than revisiting each individual object.
- **Centralized governance**: Governance teams can manage controls across larger parts of the data estate with fewer policy definitions.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer that provides ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Attributes used in ABAC policy conditions
- [Data Classification](/concepts/data-classification.md) — AI-driven tagging that integrates with ABAC
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Alternative per-object approach to row and column security

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- access-control-in-unity-catalog-databricks-on-aws.md
- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
3. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
