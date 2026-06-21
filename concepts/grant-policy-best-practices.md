---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ed54bf70125088cc1d60b630f82cef076b65b7aef0c806d1c0d9a0174ace54f
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-best-practices
    - GPBP
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Best Practices
description: "Recommendations for designing maintainable GRANT policies: use groups not individuals, attach at smallest scope, use tag inheritance with EXCEPT for exceptions, avoid mixing with direct grants."
tags:
  - unity-catalog
  - best-practices
  - administration
timestamp: "2026-06-19T13:50:20.024Z"
---

---
title: GRANT Policy Best Practices
summary: "Recommendations for designing maintainable GRANT policies: use groups not individuals, attach at smallest scope, use tag inheritance with safe defaults, avoid mixing with direct grants, and use direct grants for prerequisite permissions."
sources:
  - abac-grant-policies-for-models-beta-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - unity-catalog
  - abac
  - best-practices
  - databricks
aliases:
  - grant-policy-best-practices
  - GPBP
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# GRANT Policy Best Practices

This page provides best practices for designing, implementing, and maintaining [GRANT policies](/concepts/abac-grant-policy.md) in Unity Catalog. GRANT policies dynamically grant privileges to securable objects whose governed tags match a condition, evaluated at every access check. Following these recommendations helps create policies that are easier to maintain, audit, and reason about. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Use Groups, Not Individual Users

Always use groups in the `TO` and `EXCEPT` clauses of your GRANT policies rather than individual users. Adding or removing users from a group named in a policy changes who the policy applies to without requiring edits to the policy itself. This approach simplifies administration and reduces the risk of misconfiguration. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Attach Policies at the Smallest Scope

Attach policies at the narrowest scope that contains the securables the policy should apply to. A broader scope brings unrelated securables into the policy's tag-matching logic and may grant access where you didn't intend. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Use Tag Inheritance for Safe Defaults

Apply default tag values at the parent catalog or schema so descendants inherit them. Override the inherited tag only on the specific objects that need a different value. Combine this approach with the `EXCEPT` clause to handle controlled exceptions to a policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Don't Mix GRANT Policies and Direct Grants

For a given privilege on a securable, choose either GRANT policies or direct grants, not both. GRANT policies union with direct grants, meaning a principal can hold a privilege through either mechanism. Mixing them on the same securable makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Use Direct Grants for Prerequisite Permissions

GRANT policies do not grant the `USE CATALOG` and `USE SCHEMA` prerequisites required to access a model. Grant those permissions directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — The core concept of attribute-based access control policies
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution providing ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Tags used in GRANT policy conditions to determine access
- [System Tags](/concepts/system-tags.md) — Predefined tags provided by Databricks

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
