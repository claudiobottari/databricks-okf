---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9376b8304be955d057fbb6177b747474a573415d56748f374a28220d2dbd3b2
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-abac-grant-policies
    - BPFAGP
    - Best Practices for ABAC Policies
    - Best practices for ABAC policies
    - Performance considerations for ABAC policies
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Best Practices for ABAC GRANT Policies
description: Design recommendations for GRANT policies including using groups over individual users, attaching at smallest scope, using tag inheritance, and avoiding mixing with direct grants.
tags:
  - data-governance
  - best-practices
  - access-control
  - unity-catalog
timestamp: "2026-06-19T17:24:00.283Z"
---

# Best Practices for ABAC GRANT Policies

**ABAC (Attribute-Based Access Control) GRANT policies** dynamically grant Unity Catalog privileges to securable objects whose governed tags match a condition. Following best practices helps maintain clean, auditable, and predictable access control.

## Use Groups Instead of Individual Users

Always use **groups** in the `TO` and `EXCEPT` clauses of a GRANT policy, not individual users or service principals. Adding or removing users from a group named in a policy changes who the policy applies to without requiring edits to the policy itself. This simplifies maintenance and reduces the risk of configuration drift. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Attach Policies at the Smallest Scope

Attach policies at the **narrowest scope that covers the target securable objects**. A broader scope (for example, attaching at the catalog level when only one schema needs the policy) brings unrelated securables into the policy's tag-matching logic and may grant access where unintended. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Use Tag Inheritance for Safe Defaults

Apply default tag values at the parent catalog or schema so that descendant securable objects inherit them. Override the inherited tag only on the specific objects that need a different value. Combine this pattern with the `EXCEPT` clause to handle controlled exceptions to a policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Avoid Mixing GRANT Policies and Direct Grants for the Same Privilege

For a given privilege on a securable object, choose either GRANT policies or direct grants — **not both**. GRANT policies union with direct grants, so mixing them on the same securable makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Use Direct Grants for Prerequisite Permissions

GRANT policies do not grant the `USE CATALOG` and `USE SCHEMA` prerequisites required to access a model. Grant those prerequisite permissions **directly**, and use a GRANT policy to scope `EXECUTE` on individual models by tag. This separation keeps prerequisite access simple and tag-based model access dynamic. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Existing Grants Before Adopting Policies

Before using GRANT policies as the primary way to control `EXECUTE` on models, determine whether any direct grants already in place might override the policy. Use `SHOW EFFECTIVE POLICIES` to list every GRANT policy whose scope covers the models in a schema or catalog, and use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Understand Evaluation Semantics

The effective privileges on an object are the **union** of direct grants and any applicable GRANT policies. A more selective GRANT policy does not prevent a principal from holding `EXECUTE` through a direct grant on the model, its parent schema, or its parent catalog. Design policies with this union behavior in mind. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Core concepts including governed tags and built-in functions like `has_tag` and `has_tag_value`
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Overview of permission types and inheritance
- [Governed Tags](/concepts/governed-tags.md) — Tag management for ABAC policies
- [System Tags](/concepts/system-tags.md) — Predefined tags available for policy conditions
- [Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md) — Related ABAC policy types that restrict data content rather than access
- MLflow Model Lifecycle in Unity Catalog — How models are registered and managed

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
