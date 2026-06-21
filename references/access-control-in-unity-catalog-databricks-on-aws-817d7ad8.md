---
title: Access control in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/
ingestedAt: "2026-06-18T08:03:41.073Z"
---

Access control in Unity Catalog is built on the following complementary models:

*   **Privileges and ownership** control _who_ can access _what_, using grants on securable objects.
*   **Attribute-based policies (ABAC)** control _what_ data users can access, using governed tags and centralized policies.
*   **Table-level filtering and masking** control _what_ data users can see within tables using table-specific filters and views.
*   **Workspace-level restrictions** control _where_ users can access data, by limiting objects to specific workspaces.

These models work together to enforce secure, fine-grained access across your data environment.

## When to use each access control mechanism[​](#when-to-use-each-access-control-mechanism "Direct link to when-to-use-each-access-control-mechanism")

Workspace bindings, privileges, and ABAC policies all evaluate access at different levels, and they are designed to be used together. The following table compares them across common access control criteria:

note

Databricks recommends using attribute-based access control (ABAC) to centralize and scale access control based on governed tags. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet.

## Permissions model[​](#permissions-model "Direct link to Permissions model")

*   *   [Permissions concepts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts)
    *   Understand the Unity Catalog object hierarchy, privilege inheritance, and how access flows from parent to child objects.
*   *   [Privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference)
    *   View detailed descriptions of every privilege in Unity Catalog.
*   *   [Admin roles](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges)
    *   Learn about account admin, workspace admin, and metastore admin roles and their scopes.

## Manage access[​](#manage-access "Direct link to Manage access")

*   *   [Manage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/)
    *   Grant, revoke, and inspect privileges on Unity Catalog objects using Catalog Explorer and SQL.
*   *   [Access requests](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/access-request-destinations)
    *   Configure destinations for access requests on Unity Catalog securable objects, including email, Slack, Teams, and webhooks.
*   *   [Workspace-catalog binding](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding)
    *   Restrict which workspaces can access specific catalogs, external locations, and storage credentials.

## Fine-grained data access[​](#fine-grained-data-access "Direct link to Fine-grained data access")

*   *   [Attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)
    *   Define centralized, tag-driven policies that dynamically filter and mask data across your catalog.
*   *   [Row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/)
    *   Apply per-table row and column filters using UDFs to control what data users see at query time.
