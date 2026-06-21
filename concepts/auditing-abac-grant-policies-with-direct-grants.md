---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d8622441f2eaf9451cace8c22b5401913e29055bdf8330a042e64fd904eb7a1
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auditing-abac-grant-policies-with-direct-grants
    - AAGPWDG
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Auditing ABAC GRANT Policies with Direct Grants
description: Auditing both direct grants and ABAC GRANT policies together since effective privileges are the union of both.
tags:
  - attribute-based-access-control
  - auditing
  - security
timestamp: "2026-06-19T17:41:29.239Z"
---

# Auditing ABAC GRANT Policies with Direct Grants

**Auditing ABAC GRANT policies together with direct grants** is a governance best practice that ensures a complete view of a principal's effective privileges on a securable object. Because Unity Catalog evaluates access as the union of direct `GRANT` statements and any applicable ABAC GRANT policies, reviewing only one of those surfaces can leave unintended permissions hidden. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Why audit both

A user's effective privileges on a data object are the combination of direct grants (privileges explicitly assigned using `GRANT` on the object, its parent schema, or its parent catalog) and ABAC GRANT policies (attribute-based policies that dynamically grant privileges based on tag conditions). If you audit only direct grants, you may miss privileges that a GRANT policy confers. Conversely, if you audit only GRANT policies, you may overlook privileges that a direct grant provides, which could override or supplement the more selective policy. The risk is especially high when GRANT policies are used as the primary access control mechanism but existing direct grants remain in place. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## How to audit

The source document recommends using `SHOW EFFECTIVE POLICIES` to determine which ABAC policies apply to a specific table. This command lists every ABAC GRANT policy whose scope covers the objects in a given schema or catalog. For direct grants, Unity Catalog offers standard `SHOW GRANTS` commands and the effective permissions API (the source document does not provide exact syntax for the latter but acknowledges that both surfaces must be checked). ^[best-practices-for-abac-policies-databricks-on-aws.md]

> For detailed command syntax and examples, see the [ABAC GRANT Policy](/concepts/abac-grant-policy.md) page.

## Best practice from the source

The source document includes this explicit tip:

> *"When reviewing access, check both direct grants and ABAC GRANT policies. Auditing only one surface can hide unintended permissions."* ^[best-practices-for-abac-policies-databricks-on-aws.md]

This recommendation is part of a broader set of ABAC best practices that also includes standardizing tags, defining policies at the highest applicable scope, and avoiding policy sprawl. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) – attribute-based policies that dynamically grant privileges
- [Direct Grants](/concepts/grant-policy-vs-direct-grant.md) – static `GRANT` statements in Unity Catalog
- Effective Privileges – the union of all privilege sources
- [Unity Catalog](/concepts/unity-catalog.md) – the governance layer that enforces both mechanisms
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – the broader access control model
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) – command for inspecting applicable ABAC policies

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
