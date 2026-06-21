---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 539f625b42e167e65a085bb7df1f673f8f151bce540e5ce381df88d514cb4583
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-sprawl-prevention
    - APSP
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Policy Sprawl Prevention
description: Avoiding excessive tags and policies by starting with a small set of broad policies, consolidating overlapping ones, and periodic review.
tags:
  - attribute-based-access-control
  - policy-design
  - governance
timestamp: "2026-06-19T17:40:46.258Z"
---

```yaml
---
title: ABAC Policy Sprawl Prevention
summary: Strategies to avoid excessive tags and policies by starting with broad policies, consolidating overlapping ones, and analyzing governance requirements upfront.
sources:
  - best-practices-for-abac-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:32:40.991Z"
updatedAt: "2026-06-18T14:32:40.991Z"
tags:
  - abac
  - governance
  - policy-management
aliases:
  - abac-policy-sprawl-prevention
  - APSP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Policy Sprawl Prevention

**ABAC Policy Sprawl Prevention** refers to the set of design and governance practices that keep the number of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) rules in [Unity Catalog](/concepts/unity-catalog.md) manageable, auditable, and performant. ABAC is intended to *reduce* the number of access control rules compared to traditional role-based approaches, but without deliberate planning, teams can unintentionally create a proliferation of tags and policies that become difficult to manage and audit. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Overview

Policy sprawl in ABAC arises when teams create too many distinct tags, values, or policies — often one per edge case — rather than designing a small, well-defined set of reusable rules. This defeats the purpose of attribute-based control and introduces two major risks:

- **Manageability and audit difficulty** — A large number of policies and overlapping conditions are hard to review, modify, and reason about.
- **Performance degradation** — Complex policies and large policy sets can slow authorization checks. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Preventing sprawl requires front-loading governance analysis and following a consistent taxonomy, attaching policies at the highest possible scope, and regularly consolidating overlapping rules.

## Best Practices

### 1. Standardize Attributes and Naming

Establish a consistent tagging taxonomy *before* creating any policies. Agree on tag key names, allowed values, and naming conventions across teams. A small, well-defined set of tags is easier to manage than a proliferation of ad-hoc tags.

For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags such as `is_sensitive`, `data_class`, and `pii_level`. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Because tagging is a security boundary in ABAC — a user who can change tags can change which policies apply — restrict tag creation and modification to authorized data stewards or governance admins, and audit tag changes regularly. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 2. Define Policies at the Highest Applicable Scope

Attach policies at the catalog or schema level whenever possible. Table-level policies should be rare exceptions. Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When new tables are added, existing policies apply automatically as long as their tags match the policy's conditions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 3. Start Small and Prefer Broad Policies

Analyze governance requirements before creating policies. Start with a small number of broad policies — for example, [PII masking policies|PII masking](/concepts/column-mask-policies.md) across a catalog, or regional [row filtering](/concepts/row-filter-policies.md). Avoid creating a separate policy for every edge case. Review policies periodically and consolidate overlapping ones. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 4. Use TO/EXCEPT for Principal Targeting

For [row filter](/concepts/row-filter-policies.md) and [column mask](/concepts/column-mask-policies.md) policies, use the policy's `TO` and `EXCEPT` clauses to define which users and groups the policy applies to. This keeps any user-defined function (UDF) logic simple. For [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (Beta), `TO` and `EXCEPT` are the only mechanisms for targeting principals because GRANT policies do not use UDFs. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 5. Set Fallback Rules for Unclassified Data

Do not assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms:

- Apply a default restrictive tag (such as `classification : unverified`) to new objects until a data steward reviews them.
- Create a policy that restricts access to objects carrying the default tag.

For a detailed example, see the common pattern [Prevent access until sensitive columns are tagged](/concepts/prevent-access-until-sensitive-columns-are-tagged.md). ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 6. Audit Direct Grants and ABAC GRANT Policies Together

A user's effective privileges on a data object are the union of direct grants and ABAC GRANT policies. When reviewing access, check both surfaces — auditing only one can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### 7. Plan for Dynamic Policy Evaluation

ABAC policies are dynamic: they evaluate at query time based on the user's identity, group memberships, and the tags on the data object in the policy scope. This can make it harder for data consumers and table owners to understand which rules apply.

- Use `SHOW EFFECTIVE POLICIES` to determine what applies to a specific table.
- Document the tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually.
- If transparency is critical for a specific table, consider using [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) for that isolated case, while addressing possible conflicts first. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Consequences of Policy Sprawl

- **Hard to manage and audit** — A large number of policies and complex conditions make it difficult to understand who has access to what and why.
- **Slow authorization checks** — Too many policies or overly complex conditions can degrade query performance. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Governed Tags](/concepts/governed-tags.md)
- [System Tags](/concepts/system-tags.md)

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
