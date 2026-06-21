---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d33f35e614b84e39badaa7773c8b0401f81db12d14d88b7c4fcac062a5a43d5
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported-operations-on-abac-protected-tables
    - UOOAT
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: Unsupported Operations on ABAC-Protected Tables
description: Operations like time travel queries, deep/shallow cloning, OpenSharing, and AI Search index creation that fail on ABAC-secured tables unless the principal is exempt from all applicable policies.
tags:
  - abac
  - limitations
  - unsupported-operations
  - databricks
timestamp: "2026-06-19T20:16:41.521Z"
---

# Unsupported Operations on ABAC-Protected Tables

**Unsupported Operations on ABAC-Protected Tables** are operations that cannot be performed on tables secured by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies unless the executing principal is explicitly exempted from those policies. These operations fail by design rather than bypassing enforcement, following ABAC's fail-closed security model.

## Overview

ABAC (Attribute-Based Access Control) employs a Fail-Closed Design where Databricks defaults to denying access if it cannot verify security. Certain operations are inherently incompatible with [Row Filter and Column Mask Policy](/concepts/row-filter-and-column-mask-policies.md) enforcement because they cannot be safely applied during query execution. For these operations to succeed, the executing principal must be listed in the `EXCEPT` clause of every applicable ABAC policy. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Operations Requiring Exemption

The following operations fail when attempted against ABAC-protected tables unless the executing principal is exempt from all relevant policies:

- **Accessing ABAC-secured tables from unsupported compute versions** – Specifically, compute running Databricks Runtime versions below 16.4. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
- **Time travel queries** – These bypass row filter enforcement. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
- **Deep and shallow cloning** – Clone operations on ABAC-protected tables. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
- **OpenSharing** – Where the share owner must be exempt from the policy and have the required [OpenSharing](/concepts/opensharing.md) permissions. Note that the policy does not govern the recipient's access. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
- **AI Search index creation and syncing** – AI Search index building workflows. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

Additional operations such as Pipeline Refreshes, backup processes, and other administrative workflows also fall under this restriction. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Failure Behavior

When an unsupported operation is attempted against an ABAC-protected table, the query fails closed (access is denied) to prevent unprotected data exposure. This protects sensitive data from being accessed without the intended policy enforcement. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Resolution

To perform these operations, the executing principal must be listed in the `EXCEPT` clause of every ABAC policy that applies to the table. Exempt principals are not subject to the policy, so Databricks can safely allow the operation without needing to enforce row filters or column masks. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- Fail-Closed Design – The security model underlying this restriction.
- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) – How policies are evaluated and enforced.
- [Row Filter and Column Mask Policy](/concepts/row-filter-and-column-mask-policies.md) – The enforcement mechanism for ABAC policies.
- Policies for Exempting Principals – How to configure exemptions for unsupported operations.
- Unsupported Compute Versions – Specific version requirements for ABAC enforcement.

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
