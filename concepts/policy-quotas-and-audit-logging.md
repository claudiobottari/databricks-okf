---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d08ed0638d54c61eb740389f718035795fd2fcea196cca2b99e54b3aecb7ce5
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-quotas-and-audit-logging
    - Audit Logging and Policy Quotas
    - PQAAL
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Policy Quotas and Audit Logging
description: GRANT policies have separate quotas from row filter/column mask policies, and CRUD operations are logged under standard policy audit actions (createPolicy, deletePolicy, getPolicy, listPolicies).
tags:
  - unity-catalog
  - administration
  - monitoring
timestamp: "2026-06-19T13:50:25.861Z"
---

# Policy Quotas and Audit Logging

**Policy Quotas and Audit Logging** refers to the usage limits and operational tracking mechanisms that apply to [ABAC GRANT Policies](/concepts/abac-grant-policy.md) in Unity Catalog. These quotas and logs are distinct from those associated with row filter and column mask policies.

## Overview

Unity Catalog enforces separate quotas for GRANT policies — attribute-based policies that dynamically grant privileges based on governed tags — and for row filter/column mask policies. All create, alter, and drop operations on GRANT policies are recorded in the system audit logs under the same action types used for row filter and column mask policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Policy Quotas

Quotas for GRANT policies are independent from the quotas applied to [Row Filter and Column Mask Policies](/concepts/row-filter-policies.md).^[abac-grant-policies-for-models-beta-databricks-on-aws.md] Specific numerical limits are not detailed in the source material; administrators should consult the Databricks documentation for current quota values.

## Audit Logging

GRANT policy lifecycle events are captured in the Databricks audit log. The following operations are logged under the same action identifiers as row filter and column mask policies: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- `createPolicy` — when a GRANT policy is created
- `deletePolicy` — when a GRANT policy is deleted
- `getPolicy` — when a GRANT policy's details are retrieved
- `listPolicies` — when GRANT policies are listed

For example audit log queries, see the Databricks documentation on [Audit logging for policies](/concepts/audit-logging-for-abac-policy-operations.md).^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — The policy type governed by these quotas and logs
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- Unity Catalog audit logging
- [Governed Tags](/concepts/governed-tags.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
