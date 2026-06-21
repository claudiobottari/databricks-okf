---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02df86da7dfa51d3b3bb727fc83ec16f08c00151b5e008da2d6010821b50fd9b
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-tagging-taxonomy-and-governance
    - Governance and ABAC Tagging Taxonomy
    - ATTAG
    - Tag Taxonomy and Naming Conventions
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Tagging Taxonomy and Governance
description: Establishing consistent, controlled tag taxonomies with standardized key names and allowed values, and restricting tag modification to authorized stewards.
tags:
  - attribute-based-access-control
  - data-governance
  - tagging
timestamp: "2026-06-19T17:40:58.471Z"
---

```markdown
---
title: ABAC Tagging Taxonomy and Governance
summary: Best practices for standardizing tag key names, allowed values, and naming conventions for ABAC policies, including restricting tag modification to authorized stewards.
sources:
  - best-practices-for-abac-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:52:49.745Z"
updatedAt: "2026-06-19T14:52:00.000Z"
tags:
  - abac
  - governance
  - tagging
aliases:
  - abac-tagging-taxonomy-and-governance
  - Government-and-ABAC-Tagging-Taxonomy
  - ATTAG
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Tagging Taxonomy and Governance

**ABAC Tagging Taxonomy and Governance** refers to the structured approach for defining, managing, and governing the tags that drive [[Attribute-Based Access Control (ABAC)]] policies in [[Unity Catalog]]. A well-designed tagging taxonomy is essential for ABAC to function as a reliable security boundary, because tags determine which policies apply to which data assets. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Establishing a Tagging Taxonomy

Before creating ABAC policies, organizations should establish a consistent tagging taxonomy. This involves agreeing on tag key names, allowed values, and naming conventions across teams. A small, well-defined set of tags is easier to manage than a proliferation of ad-hoc tags. ^[best-practices-for-abac-policies-databricks-on-aws.md]

For example, use a single `sensitivity` tag with controlled values such as `public`, `internal`, `confidential`, and `restricted` rather than multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Tags as a Security Boundary

Tagging is a security boundary in ABAC. If a user can change tags on a data asset, they can change which policies apply to it. Wrong or missing tags can leave data unprotected or inaccessible because policies only apply when the right tags are in place. ^[best-practices-for-abac-policies-databricks-on-aws.md]

To maintain tag integrity:

- Restrict tag creation and modification to authorized data stewards or governance admins. See [[Governed Tags]] for how to configure tag permissions.
- Audit tag changes regularly using the [[Audit Log System Table Requirements|audit log system table]]. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Fallback Rules for Unclassified Data

Organizations should not assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms for unclassified data. Recommended practices include:

- Applying a default restrictive tag (such as `classification : unverified`) to new objects until a data steward reviews them.
- Creating a policy that restricts access to objects with the default tag.

For a detailed example, see [[Prevent access until sensitive columns are tagged]]. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Policy Scope and Sprawl Management

### Define Policies at the Highest Applicable Scope

Attach policies at the catalog or schema level when possible. Table-level policies should be rare and the exception. Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When new tables are added, existing policies apply as long as their tags match the policy's conditions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Avoid Policy Sprawl

ABAC is designed to reduce the number of access control rules, not increase them. If teams create too many tags and policies, the result is hard to manage and audit. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Best practices to avoid sprawl:

- Analyze governance requirements before creating policies.
- Start with a small number of broad policies, such as PII masking across a catalog or regional row filtering.
- Avoid creating a separate policy for every edge case.
- Review policies periodically and consolidate overlapping ones.

Large numbers of policies and complex conditions can slow authorization checks. See ABAC Performance Considerations for details. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Principal Targeting and Auditing

### Prefer `TO` and `EXCEPT` for Principal Targeting

For [[Row Filter Policies|row filter]] and column mask policies, use the policy's `TO` and `EXCEPT` clauses to define which users and groups the policy applies to. This keeps UDF logic simple. The `EXCEPT` clause excludes specific users from the policy entirely so they are not subject to any filtering or masking. When complex conditional logic is required, identity functions like `is_account_group_member()` inside UDFs remain a valid option. ^[best-practices-for-abac-policies-databricks-on-aws.md]

For [[ABAC GRANT policies]] (Beta), `TO` and `EXCEPT` are the only mechanisms for targeting principals because GRANT policies do not use UDFs. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Audit Direct Grants and ABAC GRANT Policies Together

A user's effective privileges on a data object are the union of both direct grants and ABAC GRANT policies (Beta). When reviewing access, check both surfaces. Auditing only one can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Planning for Dynamic Policy Evaluation

ABAC policies are dynamic. Unlike table-level row filters and column masks, which are directly visible on the table definition, ABAC policies evaluate at query time based on the user's identity, group memberships, and the tags on the data object in the policy scope. This can make it harder for data consumers and table owners to understand which access rules apply to a given table. ^[best-practices-for-abac-policies-databricks-on-aws.md]

To manage this complexity:

- Use `SHOW EFFECTIVE POLICIES` to determine what applies to a specific table.
- Document your tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually.
- If transparency is critical for a specific table, consider using [[table-level row filters and column masks]] for that isolated case instead, after addressing possible conflicts. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [[Attribute-Based Access Control (ABAC)]] — The access control model driven by tags and conditions
- [[Unity Catalog]] — The governance layer providing ABAC capabilities
- [[Governed Tags]] — Tags that drive ABAC policy evaluation
- [[System Tags]] — Predefined tags provided by Databricks
- [[ABAC GRANT Policy]] — Dynamic privilege grants based on tag conditions
- [[Row Filter Policies]] — ABAC policies that restrict data rows
- [[Column Mask Policies]] — ABAC policies that mask sensitive columns
- ABAC Performance Considerations — Performance implications of ABAC policy design

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
```

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
