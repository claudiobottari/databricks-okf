---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d95caae2aeab40036ad180b97e9e39f704ba85925ab533242b10b810df51b0c9
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-tag-governance-and-standardization
    - Standardization and ABAC Tag Governance
    - ATGAS
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Tag Governance and Standardization
description: Establishing a consistent, controlled tagging taxonomy for ABAC policies with restricted tag permissions
tags:
  - data-governance
  - abac
  - tagging
  - unity-catalog
timestamp: "2026-06-19T22:13:17.596Z"
---

---SOURCE: best-practices-for-abac-policies-databricks-on-aws.md ---

---
title: ABAC Tag Governance and Standardization
summary: Best practices for establishing consistent tagging taxonomies, naming conventions, and controlled tag values in ABAC policy design
sources:
  - best-practices-for-abac-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:08:58.879Z"
updatedAt: "2026-06-19T14:09:04.890Z"
tags:
  - abac
  - tag-governance
  - unity-catalog
  - data-governance
aliases:
  - abac-tag-governance-and-standardization
  - Standardization and ABAC Tag Governance
  - ATGAS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## ABAC Tag Governance and Standardization

**ABAC Tag Governance and Standardization** refers to the set of practices for managing the tagging taxonomy, policy scope, and operational discipline that underpin effective [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in [Unity Catalog](/concepts/unity-catalog.md). Because ABAC policies use tags on data assets as conditions for row filters, column masks, and dynamic grants, consistent and well-governed tag usage is essential for security, auditability, and performance.

### Overview

Tags are a security boundary in ABAC: if users can change tags on a data asset, they can alter which policies apply to it. Missing or incorrect tags may leave sensitive data unprotected or accidentally lock out legitimate users. Good tag governance therefore includes standardising tag keys and values, restricting who can create or modify tags, using automation for fallback mechanisms, and auditing changes.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Standardize Attributes and Naming

Before creating any ABAC policy, teams should agree on a consistent tagging taxonomy. This means defining tag key names, allowed values, and naming conventions across the organisation. A small, well-defined set of tags is easier to manage than a proliferation of ad-hoc tags. For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`.^[best-practices-for-abac-policies-databricks-on-aws.md]

Tag creation and modification must be restricted to authorised data stewards or governance administrators. Databricks provides [Governed Tags](/concepts/governed-tags.md) to configure these permissions, and tag changes should be audited regularly using the audit log system table.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Set Fallback Rules for Unclassified Data

Do not assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms for unclassified data. A common pattern is to:

- Apply a default restrictive tag (e.g., `classification: unverified`) to new objects until a data steward reviews them.
- Create a policy that restricts access to objects bearing this default tag.

For a detailed example, see [Prevent access until sensitive columns are tagged](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns#prevent-untagged).^[best-practices-for-abac-policies-databricks-on-aws.md]

### Define Policies at the Highest Applicable Scope

To reduce maintenance overhead, attach ABAC policies at the catalog or schema level whenever possible. Table-level policies are rare and should be the exception. Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When new tables are added, existing policies apply automatically as long as their tags match the policy’s conditions.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Avoid Policy Sprawl

ABAC is designed to reduce the number of access control rules, not increase them. If teams create too many tags and policies, the result is hard to manage and audit. Recommended practices include:

- Analyzing governance requirements before creating policies.
- Starting with a small number of broad policies, such as PII masking across a catalog or regional row filtering.
- Avoiding a separate policy for every edge case.
- Reviewing policies periodically and consolidating overlapping ones.

Large numbers of policies and complex conditions can slow authorization checks. See Performance Considerations for ABAC for details.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Audit Direct Grants and ABAC GRANT Policies Together

A user’s effective privileges on a data object are the union of both direct grants and [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (Beta). When reviewing access, check both surfaces. Auditing only one surface can hide unintended permissions.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Prefer TO/EXCEPT for Principal Targeting

For [Row Filters and Column Masks (ABAC)|row filter and column mask policies](/concepts/row-filter-policies.md), use the policy’s `TO` and `EXCEPT` clauses to define which users and groups the policy applies to. This keeps the underlying UDF logic simple. The `EXCEPT` clause excludes specific users from the policy entirely so they are not subject to any filtering or masking. When complex conditional logic is required, identity functions like `is_account_group_member()` inside UDFs remain a valid option. For GRANT policies (Beta), `TO` and `EXCEPT` are the only mechanisms for targeting principals because GRANT policies do not use UDFs.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Plan for Dynamic Policy Evaluation

ABAC policies evaluate at query time based on the user’s identity, group memberships, and the tags on the data object in the policy’s scope. This dynamism can make it harder for data consumers and table owners to understand which access rules apply to a given table. To mitigate this:

- Use `SHOW EFFECTIVE POLICIES` to determine what applies to a specific table.
- Document the tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually.
- If transparency is critical for a specific table, consider using table-level row filters and column masks for that isolated case instead, after checking for conflicts.^[best-practices-for-abac-policies-databricks-on-aws.md]

### Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
