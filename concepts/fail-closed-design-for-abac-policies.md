---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 656512c5495e56b07a39b06ff69b4cd24c37705760ad76768bcff5136ee83ad2
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fail-closed-design-for-abac-policies
    - FDFAP
    - Fail-closed design
    - fail-closed design
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: Fail-Closed Design for ABAC Policies
description: Security model where Databricks denies access to ABAC-secured tables if it cannot safely verify and enforce all applicable policies, including on unsupported compute, specific operations, or when policy dependencies are removed.
tags:
  - abac
  - security
  - fail-closed
  - databricks
timestamp: "2026-06-19T20:15:59.630Z"
---

# Fail-Closed Design for ABAC Policies

**Fail-Closed Design for ABAC Policies** refers to the security principle that Databricks applies to [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) policy enforcement: access to an ABAC-secured table is denied unless Databricks can safely verify and enforce all applicable policies. This prevents unintended data exposure when policy dependencies are missing, compute environments are unsupported, or operations are incompatible with row filters or column masks. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Overview

ABAC policy evaluation follows a two‑stage process. During query execution, [Unity Catalog](/concepts/unity-catalog.md) evaluates policies based on the user’s identity, group memberships, and governed tags on the securable object, then sends the effective row filter or column mask to the Databricks Runtime. The runtime enforces the filter or mask by rewriting the query plan as a secure view. Because different users may see different results from the same query, the system must guarantee that enforcement occurs correctly for every principal. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

The fail‑closed design ensures that when enforcement cannot be guaranteed, access is blocked rather than allowed without protection. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Unsupported Compute Versions

ABAC policies require Databricks Runtime 16.4 or above, or serverless compute. If a user attempts to access an ABAC‑secured table from an unsupported runtime version, the query fails closed (access is denied) to prevent unprotected data exposure. On dedicated access mode, Databricks delegates enforcement to serverless compute to guarantee fine‑grained access controls are applied. To allow users on older runtimes to access these tables, they must be explicitly exempted from the policies. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Unsupported Operations on Protected Data

Certain operations are incompatible with row filters or column masks. These operations fail rather than bypass enforcement. To run them, the principal must be listed in the `EXCEPT` clause of every ABAC policy that applies to the table. Exempt principals are not subject to the policy, so Databricks does not need to enforce it and can safely allow the operation. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

Operations that require the executing principal to be exempt include:

- Accessing ABAC‑secured tables from compute running Databricks Runtime versions below 16.4.
- Time travel queries.
- Deep and shallow cloning.
- OpenSharing (the share owner must be exempt and have the required OpenSharing permissions; the policy does not govern the recipient’s access).
- AI Search index creation and syncing.

For a full list, see the requirements and limitations documentation. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Removed Policy Dependencies

ABAC policies depend on [Governed Tags](/concepts/governed-tags.md) and User‑Defined Functions (UDFs). If any of these dependencies are removed while a policy still references them, queries against tables in the policy’s scope fail. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Governed Tag Deletion

If a governed tag that an ABAC policy references is deleted, all queries against the object where the policy is attached and its child objects fail with an `INVALID_PARAMETER_VALUE.UC_ABAC_UNKNOWN_TAG_POLICY` error. This occurs even if the tag was not applied to the queried tables. When a governed tag is deleted, it becomes an ungoverned tag: the allowed value restrictions are removed, and anyone with `APPLY TAG` can modify values without the `ASSIGN` privilege. The UI and API do not prevent deleting a governed tag that is referenced in an ABAC policy. To resolve the error, either restore the deleted tag, or update or delete the policy that references it. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Deleting a Column That Is Tagged

Databricks prevents deleting a column that has a governed tag applied. To drop the column, a user with `ASSIGN` on the tag and `APPLY TAG` on the object must first remove the tag, then the column can be deleted. This is relevant for declarative pipelines and other automated workflows that modify table schemas. If a pipeline attempts to drop a tagged column, the operation fails. To unblock the pipeline, a user with the required tag permissions must remove the tag, run the pipeline so the schema change succeeds, and then reapply the tag to the relevant columns. If the tag is not reapplied, queries against the data will fail because the policy is still in scope but the expected tag is no longer on the object. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Policy‑Referenced Function Deletion

If a UDF referenced by a policy is deleted while the policy is still in scope, queries against tables in that scope fail with an `UC_DEPENDENCY_DOES_NOT_EXIST` error. To resolve, either restore the function or update the policy to reference a different UDF. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md)
- [Row Filter](/concepts/row-filter-policies.md)
- Column Mask
- [Unity Catalog](/concepts/unity-catalog.md)
- Databricks Runtime
- [Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md)
- [Governed Tags](/concepts/governed-tags.md)
- User-Defined Functions (UDFs)
- Fail-Closed Design (general security principle)

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
