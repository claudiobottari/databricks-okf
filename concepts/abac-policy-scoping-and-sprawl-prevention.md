---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4e879b2d43afe39868b45c27c233dff7799452b4855ca77f24a691b104f7dad
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-scoping-and-sprawl-prevention
    - Sprawl Prevention and ABAC Policy Scoping
    - APSASP
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: ABAC Policy Scoping and Sprawl Prevention
description: Attaching policies at catalog or schema level rather than table level, starting with a small number of broad policies, and periodically consolidating overlapping ones to avoid complex authorization checks.
tags:
  - abac
  - policy-management
  - performance
timestamp: "2026-06-19T09:09:18.490Z"
---

# ABAC Policy Scoping and Sprawl Prevention

**ABAC policy scoping and sprawl prevention** refers to the set of best practices for designing, placing, and managing [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md) to minimize policy proliferation while maintaining effective governance. ABAC is designed to reduce the number of access control rules, not increase them. If teams create too many tags and policies, the result is hard to manage and audit.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Scoping Principles

### Define policies at the highest applicable scope

Attach policies at the catalog or schema level when possible. Table-level policies are rare and should be the exception. Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When you add new tables, existing policies apply as long as their tags match the policy's conditions.^[best-practices-for-abac-policies-databricks-on-aws.md]

For [ABAC GRANT Policy](/concepts/abac-grant-policy.md) on models, attach policies at the smallest scope that covers the targets, but only at catalog or schema level — policies cannot be attached directly to models.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Preventing Policy Sprawl

### Analyze before creating

Analyze your governance requirements before creating policies. Start with a small number of broad policies, such as PII masking across a catalog or regional row filtering. Avoid creating a separate policy for every edge case.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Consolidate overlapping policies

Review policies periodically and consolidate overlapping ones. Large numbers of policies and complex conditions can slow authorization checks.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Use tag inheritance for safe defaults

Apply default tag values at the parent catalog or schema so descendants inherit them. Override the inherited tag only on the specific objects that need a different value. This reduces the need for separate policies targeting individual objects.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Standardizing Tags to Control Sprawl

Establish a consistent tagging taxonomy before creating policies. Agree on tag key names, allowed values, and naming conventions across teams. A small, well-defined set of tags is easier to manage than a proliferation of ad-hoc tags.^[best-practices-for-abac-policies-databricks-on-aws.md]

For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`.^[best-practices-for-abac-policies-databricks-on-aws.md]

Tagging is a security boundary in ABAC. If a user can change tags on a data asset, they can change which policies apply to it. Wrong or missing tags can leave data unprotected or inaccessible because policies only apply when the right tags are in place.

- Restrict tag creation and modification to authorized data stewards or governance admins. See [Governed Tags](/concepts/governed-tags.md) for how to configure tag permissions.
- Audit tag changes regularly using the [Audit Log System Table](/concepts/audit-log-system-table-requirements.md).

^[best-practices-for-abac-policies-databricks-on-aws.md]

## Avoiding Mixing Policy Types

For a given privilege on a securable, choose either GRANT policies or direct grants, not both. Mixing them makes it harder to audit effective access and can produce unexpected results because the effective privileges on an object are the union of direct grants and any applicable GRANT policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Use direct grants for `USE CATALOG` and `USE SCHEMA`, GRANT policies for `EXECUTE`. GRANT policies do not grant the `USE CATALOG` and `USE SCHEMA` prerequisites required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Auditing for Sprawl

Audit both direct grants and ABAC GRANT policies together. A user's effective privileges on a data object are the union of both. When reviewing access, check both surfaces — auditing only one can hide unintended permissions.^[best-practices-for-abac-policies-databricks-on-aws.md]

Use [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) to determine what applies to a specific table or schema. Document your tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Fallback Rules for Unclassified Data

Don't assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms for unclassified data:

- Apply a default restrictive tag (like `classification : unverified`) to new objects until a data steward reviews them.
- Create a policy that restricts access to objects with the default tag.

For a detailed example, see the common pattern on preventing access until sensitive columns are tagged.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Prefer TO/EXCEPT for Principal Targeting

For row filter and column mask policies, use the policy's `TO` and `EXCEPT` clauses to define which users and groups the policy applies to. This keeps UDF logic simple. The `EXCEPT` clause excludes specific users from the policy entirely so they are not subject to any filtering or masking. When complex conditional logic is required, identity functions like `is_account_group_member()` inside UDFs remain a valid option.^[best-practices-for-abac-policies-databricks-on-aws.md]

For GRANT policies, `TO` and `EXCEPT` are the only mechanisms for targeting principals because GRANT policies do not use UDFs.^[best-practices-for-abac-policies-databricks-on-aws.md]

Use groups in `TO` and `EXCEPT`, not individual users. Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The core access control model
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that supports ABAC
- [Governed Tags](/concepts/governed-tags.md) — Tags used in ABAC policy conditions
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based grant policies for models
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — System table for auditing tag changes

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
