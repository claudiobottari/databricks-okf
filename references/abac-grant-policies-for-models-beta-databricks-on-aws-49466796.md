---
title: ABAC GRANT policies for models (Beta) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies
ingestedAt: "2026-06-18T08:03:24.588Z"
---

Beta

ABAC GRANT policies are in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). In Beta, GRANT policies can grant the `EXECUTE` privilege on models, attached at the catalog or schema level. Additional privileges and securable types will be supported in future releases.

This page describes ABAC GRANT policies, which dynamically grant Unity Catalog privileges to securable objects whose governed tags match a condition. It covers how to create, edit, list, and delete them in Catalog Explorer, SQL, and the Databricks SDK, how GRANT policies interact with direct grants, and the current Beta scope and limitations.

For an overview of ABAC and core concepts, including governed tags and built-in functions such as `has_tag` and `has_tag_value`, see [Core concepts for attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts).

## Compute requirements[​](#compute-requirements "Direct link to compute-requirements")

Creating, modifying, or dropping GRANT policies with SQL requires a [classic compute cluster](https://docs.databricks.com/aws/en/compute/use-compute) running Databricks Runtime 18.3 or above.

## What is a GRANT policy[​](#what-is-a-grant-policy "Direct link to what-is-a-grant-policy")

A GRANT policy is an attribute-based access control policy that dynamically grants Unity Catalog privileges to [securable objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#securable-objects) whose governed tags match the policy's condition. Unity Catalog evaluates the policy's `WHEN` condition against the governed tags on each securable object in the policy's scope every time access is checked, and grants the privilege on every securable object that matches.

In comparison, direct `GRANT` statements assign privileges on securable objects identified by their three-level namespace (`catalog.schema.object`).

In Beta, GRANT policies support one privilege on one securable type: `EXECUTE` on models. Both customer-registered MLflow models and Databricks\-hosted foundation models in `system.ai` are covered. See [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) for how MLflow models are registered in Unity Catalog, and [Access generative AI and LLM models from Unity Catalog](https://docs.databricks.com/aws/en/generative-ai/pretrained-models) for Databricks\-hosted foundation models.

GRANT policies can reference either [governed tags you create yourself](https://docs.databricks.com/aws/en/admin/governed-tags/) or [system tags](https://docs.databricks.com/aws/en/database-objects/tags#system-tags) predefined by Databricks in their conditions.

For example, the following policy uses the `lifecycle` governed tag applied to customer-registered MLflow models in `production.ml_models`. The policy grants `EXECUTE` only on models tagged `lifecycle = 'production'`:

SQL

    CREATE POLICY grant_production_model_accessON SCHEMA production.ml_modelsCOMMENT 'Grant EXECUTE on production MLflow models'TO `analysts`GRANT EXECUTE FOR MODELSWHEN has_tag_value('lifecycle', 'production');

The following policy grants `EXECUTE` on Anthropic-hosted foundation models in `system.ai` to `data_scientists`, except `contractors`, by matching the `ai.model_creator` system tag. Every model that carries `ai.model_creator = 'anthropic'` is covered, without a separate grant per model:

SQL

    CREATE POLICY grant_anthropic_foundation_modelsON SCHEMA system.aiCOMMENT 'Grant EXECUTE on Anthropic foundation models'TO `data_scientists`EXCEPT `contractors`GRANT EXECUTE FOR MODELSWHEN has_tag_value('ai.model_creator', 'anthropic');

The equivalent access using direct grants requires one statement per model in `system.ai`, reissued as Databricks adds new Anthropic models:

SQL

    GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-sonnet-4-6` TO `data_scientists`;GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-opus-4-7` TO `data_scientists`;GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-haiku-4-5` TO `data_scientists`;

GRANT policies differ from row filter and column mask policies in two ways:

*   Row filter and column mask policies restrict the content of data a user can already access. GRANT policies determine whether the user can access the object at all.
*   Row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask. GRANT policies do not use UDFs. The condition is expressed inline in the policy definition.

## How GRANT policies interact with direct grants[​](#how-grant-policies-interact-with-direct-grants "Direct link to how-grant-policies-interact-with-direct-grants")

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when any of the following is true:

*   A GRANT policy attached to the model's catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model.
*   A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal, whether granted directly, through group membership, or through other administrative privileges.

Because access is the union of these sources, a more selective GRANT policy does not mean that an excluded principal lacks `EXECUTE`. The principal can still hold the privilege through a direct grant on the model, or its parent schema or catalog. If you intend to use GRANT policies as the primary way to control `EXECUTE` on models, first determine whether any direct grants already in place might override the policy:

*   Use [`SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) (or `ON CATALOG <parent_catalog>`) to list every GRANT policy whose scope covers the models in that schema or catalog. `SHOW EFFECTIVE POLICIES` does not support `ON MODEL` directly. The equivalent REST API is `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true` (Python SDK: `w.policies.list_policies(..., include_inherited=True)`).
*   Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. The equivalent REST API for direct grants on a securable object is `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get(...)`); for the union of direct and inherited grants, use `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get_effective(...)`).

## Create a GRANT policy[​](#create-a-grant-policy "Direct link to create-a-grant-policy")

You can create a GRANT policy through the Catalog Explorer UI, with the [`CREATE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy) SQL statement, or with the Databricks SDK.

To create a GRANT policy, you must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object.

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Select the catalog or schema where you want to attach the policy. GRANT policies in Beta can only be attached at the catalog or schema level.
3.  Click the **Policies** tab.
4.  Click **New policy**.
5.  Under **Policy identification**, enter a **Policy name** and an optional **Description**.
6.  Under **Principals and scope**:
    *   In **Applied to**, select the principals (users, groups, or service principals) that the policy applies to.
    *   In **Except for**, optionally select principals to exclude from the policy.
    *   In **Scope**, confirm the catalog or schema where the policy is attached.
7.  Under **Policy type**, select **Grant access**.
8.  Under **Securable objects**, select **Model**. Model is the only securable type supported for GRANT policies in Beta. The other types in the list (Table, Volume, Schema, Catalog) cannot be combined with **Grant access**.
9.  Under **Condition**, choose how to scope the policy to models in the selected catalog or schema:
    *   **No condition** applies the policy to all models under the selected catalog or schema.
    *   **Securables matching any of these tags** applies the policy only to models that carry at least one of the selected governed tags.
    *   **Securables matching a custom expression** lets you write a tag-based expression to determine which models the policy applies to. See [Conditions and built-in functions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#conditions-and-built-in-functions) for the available condition functions.
10.  Under **Privileges**, select **EXECUTE**. EXECUTE is the only privilege supported for models in Beta.
11.  Click **Show code** to review the equivalent SQL statement before saving, then click **Create policy**.

## Edit a GRANT policy[​](#edit-a-grant-policy "Direct link to edit-a-grant-policy")

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Select the catalog or schema the policy is attached to.
3.  Click the **Policies** tab.
4.  Select the policy you want to edit.
5.  Update any fields you want to change.
6.  Click **Update policy**.

## Delete a GRANT policy[​](#delete-a-grant-policy "Direct link to delete-a-grant-policy")

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Select the catalog or schema the policy is attached to.
3.  Click the **Policies** tab.
4.  Select the policy.
5.  Click **Delete policy**.

## Show policies[​](#show-policies "Direct link to show-policies")

Use [`SHOW POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) to list the policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes, such as catalog-level policies that affect a schema.

SQL

    SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA } securable_name

The result includes the policy name, policy type, and the catalog or schema where each policy is defined. GRANT policies are returned with policy type `GRANT` alongside any row filter and column mask policies attached at the same scope. The `table` column is populated only for table-scoped policies (row filter and column mask); for GRANT policies attached to a catalog or schema, it is `NULL`.

Example:

SQL

    SHOW EFFECTIVE POLICIES ON SCHEMA system.ai;

`SHOW GRANTS` does not include privileges granted via a GRANT policy. To see all `EXECUTE` access on a model, combine `SHOW GRANTS` output for the model with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent schema or catalog.

## Describe a policy[​](#describe-a-policy "Direct link to describe-a-policy")

Use [`DESCRIBE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-describe-policy) to view the details of a specific GRANT policy. Requires `MANAGE` on the target securable object or object ownership.

SQL

    { DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name

The result shows the policy's properties as key-value pairs, including name, securable object type, securable object name, principals, privileges, and the `WHEN` condition.

Example:

SQL

    DESCRIBE POLICY grant_anthropic_foundation_models ON SCHEMA system.ai;

## Policy quotas[​](#policy-quotas "Direct link to policy-quotas")

These quotas are separate from the [quotas for row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements#policy-quotas).

## Audit logging[​](#audit-logging "Direct link to audit-logging")

GRANT policy create, alter, and drop operations are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as row filter and column mask policies. See [Audit logging](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies#audit-logging) for example audit log queries.

## Best practices[​](#best-practices "Direct link to best-practices")

The following recommendations help you design GRANT policies that are easier to maintain, audit, and reason about.

*   **Use groups in `TO` and `EXCEPT`, not individual users.** Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy.
*   **Attach policies at the smallest scope that covers the targets.** Use the narrowest scope that contains the securables the policy should apply to. A broader scope brings unrelated securables into the policy's tag-matching, and may grant access where you didn't intend.
*   **Use tag inheritance for safe defaults.** Apply default tag values at the parent catalog or schema so descendants inherit them. Override the inherited tag only on the specific objects that need a different value. Combine this with `EXCEPT` to handle controlled exceptions to a policy.
*   **Don't mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose either GRANT policies or direct grants, not both. GRANT policies union with direct grants, so mixing them on the same securable makes it harder to reason about who has access and to audit changes.
*   **Use direct grants for `USE CATALOG` and `USE SCHEMA`, GRANT policies for `EXECUTE`.** GRANT policies do not grant the `USE CATALOG` and `USE SCHEMA` prerequisites required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag.

## Limitations[​](#limitations "Direct link to limitations")

*   Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` are not supported by GRANT policies and must be granted directly.
*   The prerequisite permissions `USE SCHEMA` and `USE CATALOG`, which a user needs to reach a model, are not supported by GRANT policies and must be granted directly.
*   A policy can be attached to the catalog or the schema, not to the model.
*   `SHOW GRANTS` does not return privileges granted by a GRANT policy.
*   `INFORMATION_SCHEMA` does not include GRANT policies.
*   Deleting a model or a model version is not covered by GRANT policies. See [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) for how to delete model versions and models.
*   You cannot use Delta Sharing to share models that have GRANT policies defined on them.

## More information[​](#more-information "Direct link to more-information")

See also [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).
