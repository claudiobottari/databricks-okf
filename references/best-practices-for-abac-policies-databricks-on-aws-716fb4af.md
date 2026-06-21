---
title: Best practices for ABAC policies | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/best-practices
ingestedAt: "2026-06-18T08:03:17.067Z"
---

Consider the following best practices for ABAC policy design and tag governance.

## Standardize attributes and naming[​](#standardize-attributes-and-naming "Direct link to standardize-attributes-and-naming")

Establish a consistent tagging taxonomy before creating policies. Agree on tag key names, allowed values, and naming conventions across teams. A small, well-defined set of tags is easier to manage than a proliferation of ad-hoc tags.

For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`.

Tagging is a security boundary in ABAC. If a user can change tags on a data asset, they can change which policies apply to it. Wrong or missing tags can leave data unprotected or inaccessible because policies only apply when the right tags are in place.

*   Restrict tag creation and modification to authorized data stewards or governance admins. See [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/) for how to configure tag permissions.
*   Audit tag changes regularly using the [audit log system table](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs).

## Set fallback rules for unclassified data[​](#set-fallback-rules-for-unclassified-data "Direct link to set-fallback-rules-for-unclassified-data")

Don't assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms for unclassified data:

*   Apply a default restrictive tag (like `classification : unverified`) to new objects until a data steward reviews them.
*   Create a policy that restricts access to objects with the default tag.

For a detailed example, see [Prevent access until sensitive columns are tagged](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns#prevent-untagged).

## Define policies at the highest applicable scope[​](#define-policies-at-the-highest-applicable-scope "Direct link to define-policies-at-the-highest-applicable-scope")

Attach policies at the catalog or schema level when possible. Table-level policies are rare and should be the exception.

Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When you add new tables, existing policies apply as long as their tags match the policy's conditions.

## Avoid policy sprawl[​](#avoid-policy-sprawl "Direct link to avoid-policy-sprawl")

ABAC is designed to reduce the number of access control rules, not increase them. If teams create too many tags and policies, the result is hard to manage and audit.

*   Analyze your governance requirements before creating policies.
*   Start with a small number of broad policies, such as PII masking across a catalog or regional row filtering.
*   Avoid creating a separate policy for every edge case.
*   Review policies periodically and consolidate overlapping ones.

Large numbers of policies and complex conditions can slow authorization checks. See [Performance considerations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance) for details.

## Audit direct grants and ABAC GRANT policies together[​](#audit-direct-grants-and-abac-grant-policies-together "Direct link to audit-direct-grants-and-abac-grant-policies-together")

tip

A user's effective privileges on a data object are the union of both direct grants and ABAC GRANT policies (Beta). When reviewing access, check both direct grants and ABAC GRANT policies. Auditing only one surface can hide unintended permissions. See [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).

## Prefer TO/EXCEPT for principal targeting[​](#prefer-toexcept-for-principal-targeting "Direct link to prefer-toexcept-for-principal-targeting")

For row filter and column mask policies, use the policy's `TO` and `EXCEPT` clauses to define which users and groups the policy applies to. This keeps UDF logic simple. The `EXCEPT` clause excludes specific users from the policy entirely so they are not subject to any filtering or masking. When complex conditional logic is required, identity functions like `is_account_group_member()` inside UDFs remain a valid option.

For GRANT policies (Beta), `TO` and `EXCEPT` are the only mechanisms for targeting principals because GRANT policies do not use UDFs.

For details, see [Approach for targeting principals](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#targeting-principals).

## Plan for dynamic policy evaluation[​](#plan-for-dynamic-policy-evaluation "Direct link to plan-for-dynamic-policy-evaluation")

ABAC policies are dynamic. Unlike table-level row filters and column masks, which are directly visible on the table definition, ABAC policies evaluate at query time based on the user's identity and group memberships, and the tags on the data object in the policy scope. This can make it harder for data consumers and table owners to understand which access rules apply to a given table.

*   Use [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) to determine what applies to a specific table.
*   Document your tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually.
*   If transparency is critical for a specific table, consider using [table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/abac-vs-rls-cm) for that isolated case instead. Make sure to address possible conflicts first.

## Learn more[​](#learn-more "Direct link to learn-more")
