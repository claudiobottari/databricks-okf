---
title: Core concepts for attribute-based access control (ABAC) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts
ingestedAt: "2026-06-18T08:03:20.659Z"
---

Attribute-based access control (ABAC) is an access-control model that uses **governed tags** and policies to grant permissions based on object attributes rather than per-object grants. This page defines the building blocks: governed tags, the three ABAC policy types (row filter, column mask, and GRANT policies), the permissions required to configure them, and the separation of duties ABAC enables across teams.

See [Attribute-based access control in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) for an overview of all ABAC topics, including tutorials, policy management, best practices, and limitations.

## What is ABAC?[​](#what-is-abac "Direct link to what-is-abac")

**Attribute-based access control (ABAC)** is a dynamic access control model where access decisions are based on policies evaluated against attributes associated with securable objects. In Unity Catalog, these attributes are represented through [governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/). These governed tags are used in policy conditions to match data objects within a given scope, such as a catalog or a schema. This allows a single policy to apply automatically across multiple data objects that meet its conditions.

For example, an ABAC policy might mask all columns tagged `PII` for tables within schemas tagged `HR`. As new data objects are created and tagged, the policy applies automatically without requiring separate policy definitions for each object.

ABAC supports row and column-level security through **row filter policies** and **column mask policies** on tables, materialized views, and streaming tables. Row filter policies restrict which rows a user can see. Column mask policies control how column values are presented to users. For a comparison with [table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/), see [When to use ABAC vs table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/abac-vs-rls-cm).

ABAC also supports dynamic privilege grants through **GRANT policies** (Beta), currently scoped to `EXECUTE` on models. See [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).

In Unity Catalog, attributes are implemented as [governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/). Governed tags are key-value pairs defined at the account level and applied to Unity Catalog securable objects such as catalogs, schemas, tables, columns, models, and volumes, in addition to workspace objects. They represent characteristics such as sensitivity, classification, or business domain.

By default, securables inherit tags from their parent catalog or schema. You can override inherited tags at every level except the column level: column tags do not inherit from the parent table and must be applied directly.

![Governed tags hierarchy diagram](https://docs.databricks.com/aws/en/assets/images/governed-tags-hierarchy-2740348868f29ddf0611089d4684adec.png)

Governed tags can be referenced in [policy](#policies) conditions using built-in functions like `has_tag()` and `has_tag_value()`, which check whether a given tag is present on the target data object, either directly or through tag inheritance.

Governed tags are defined at the account level. This means that you can use the same tag taxonomy across your entire data estate in an account, including across multiple metastores.

For more information, see [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/) and [Apply tags to Unity Catalog securable objects](https://docs.databricks.com/aws/en/database-objects/tags).

## Policies[​](#policies "Direct link to policies")

Policies are attached to [securable objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#securable-objects) in Unity Catalog to define access control rules based on tag conditions. Below is an example:

SQL

    CREATE FUNCTION mask_pii(val STRING) RETURNS STRING    RETURN '***';CREATE POLICY mask_pii_for_hrON CATALOG catalog_aCOLUMN MASK mask_piiTO `account users` EXCEPT `HR admins`FOR TABLESWHEN has_tag('HR')MATCH COLUMNS has_tag('PII') AS pii_colON COLUMN pii_col;

Each policy specifies:

*   **Scope**: The securable object where the policy is attached, specified by the `ON` clause. Attaching a policy to a securable object means the policy conditions are evaluated for all objects of the type specified in the `FOR` clause, across that object and all of its descendants.
    *   For row filter and column mask policies, supported policy scopes are `CATALOG`, `SCHEMA`, or `TABLE`. For GRANT policies (Beta), supported policy scopes are `CATALOG` and `SCHEMA`.
    *   Tables, including streaming tables and materialized views, are the only supported securable object type for row filter and column mask policies, specified using the `FOR TABLES` clause. GRANT policies (Beta) support models only, specified using `GRANT EXECUTE FOR MODELS`. See [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).
    *   A policy attached at a catalog evaluates against all tables in that catalog. A policy attached at a schema evaluates against all tables in that schema. A policy attached at a table evaluates only against that table.

note

Databricks recommends attaching policies at the highest applicable level, usually the catalog, to maximize governance efficiency. See [Best practices for ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/best-practices).

*   **Principals**: Who the policy applies to and who is exempt. The `TO` clause specifies the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause excludes specific principals from this policy.
*   **Actions**: Whether the policy applies a row filter, a column mask, or a privilege grant. Row filter and column mask policies use a [user-defined function (UDF)](#udfs) to implement the filtering or masking logic. GRANT policies (Beta) do not use UDFs. See [Policy types](#policy-types).
*   **Conditions**: Tag-based expressions that determine which tables or columns the policy targets. See [Conditions and built-in functions](#conditions-and-built-in-functions).

Policies are created and managed through the UI or programmatically with [SQL statements](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy), such as `CREATE POLICY`, `DROP POLICY`, `SHOW POLICIES`, or `DESCRIBE POLICY`, [REST APIs](https://docs.databricks.com/api/workspace/policies), [Databricks SDKs](https://databricks-sdk-py.readthedocs.io/en/stable/workspace/catalog/policies.html), or [Terraform](https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/policy_info). See [Create and manage ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) for the full syntax and examples.

### Policy types[​](#policy-types "Direct link to policy-types")

ABAC supports three policy types: row filter policies, column mask policies, and GRANT policies (Beta). Row filter and column mask policies require [UDFs](https://docs.databricks.com/aws/en/udf/unity-catalog) to implement the filtering or masking logic. GRANT policies don't use UDFs, and instead grant privileges when their tag-based condition matches the target object's attributes.

#### Row filter policies[​](#row-filter-policies "Direct link to Row filter policies")

Row filter policies restrict which rows a user can see in a table based on values in columns identified by tags that match the [Conditions and built-in functions](#conditions-and-built-in-functions). The policy references a UDF that evaluates each row. Rows where the function returns `FALSE` are excluded from query results. Arguments are passed to the UDF through the `USING COLUMNS` clause.

_Example use case:_ For a sales catalog, ensure the EMEA team sees only EMEA sale records across all tables that have a column tagged `region`.

SQL

    CREATE FUNCTION filter_by_region(region STRING, allowed STRING) RETURNS BOOLEAN    RETURN region = allowed;CREATE POLICY regional_access_emeaON CATALOG salesROW FILTER filter_by_regionTO `emea team`FOR TABLESMATCH COLUMNS has_tag('region') AS rgnUSING COLUMNS (rgn, 'EMEA');

#### Column mask policies[​](#column-mask-policies "Direct link to Column mask policies")

Column mask policies control what values a user sees for specific columns identified by tags that match the [Conditions and built-in functions](#conditions-and-built-in-functions). The policy references a UDF that takes the column value as input and returns the original value or a masked version. The masked column value is bound automatically as the first argument from the `ON COLUMN` clause, and additional arguments can be passed through `USING COLUMNS`. The return type must match or be castable to the column's data type.

_Example use case:_ Mask SSN columns tagged with `pii : ssn` so that users see `***-**-XXXX` (last four digits only) unless they are in a compliance group exempt from the policy.

SQL

    CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING    RETURN CONCAT('***-**-', RIGHT(ssn, show_last));CREATE POLICY mask_ssn_columnsON CATALOG hr_catalogCOLUMN MASK mask_ssnTO `account users` EXCEPT `compliance team`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_colON COLUMN ssn_colUSING COLUMNS (4);

The `USING COLUMNS` clause passes arguments to the UDF. It accepts aliases for columns that match a tag-based expression, or constant values (quoted strings, numeric literals, boolean values (`TRUE`/`FALSE`), or `NULL`), supplied in the order the function expects them. For column mask policies, these are additional arguments beyond the masked column (which is bound automatically from `ON COLUMN`). This allows a single UDF to be reused across policies with different parameters.

SQL UDFs are recommended for better performance. Python UDFs registered in Unity Catalog are also supported, though the query optimizer cannot inline or optimize them the way it can SQL UDFs. See [Performance considerations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance) for guidance on UDF language selection.

#### GRANT policies (Beta)[​](#grant-policies-beta "Direct link to GRANT policies (Beta)")

GRANT policies dynamically grant a Unity Catalog privilege when their tag-based condition matches a securable object's tags. Each time a user attempts to access a securable object, Unity Catalog identifies all GRANT policies whose scope covers the object, checks whether the user is in the `TO` list and not in the `EXCEPT` list, and evaluates the policy's `WHEN` condition against the tags on the securable, including inherited tags. If the policy applies, Unity Catalog grants the privilege. GRANT policies use the same [evaluation model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation) as row filter and column mask policies, except they do not use UDFs. The condition is expressed inline in the policy definition.

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal has the privilege if a GRANT policy in scope applies to that principal or a direct `GRANT` of the same privilege applies. GRANT policies only add access. They cannot revoke access that was granted directly.

### Conditions and built-in functions[​](#conditions-and-built-in-functions "Direct link to conditions-and-built-in-functions")

Conditions are tag-based expressions that determine which tables and columns a policy targets within its scope.

*   **Table conditions** (`WHEN` clause): Boolean expressions that match tables based on their tags. If omitted, defaults to `TRUE`, meaning the policy applies to all tables in scope.
*   **Column conditions** (`MATCH COLUMNS` clause): One or more comma-separated boolean expressions that identify which columns the policy targets. Each expression can be a single built-in function like `has_tag('pii')`, or a combination using logical operators like `has_tag_value('pii', 'ssn') AND has_tag('sensitive')`. Each expression can be assigned an alias (specified after `AS`) that can be referenced in the `ON COLUMN` and `USING COLUMNS` clauses. A policy can include up to 3 column expressions, and all must match for the policy to apply.

Both clause types use the following built-in functions, evaluated by Unity Catalog against securable metadata:

Tags don't propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches column-level tags, not tags on the parent table or its ancestors.

note

The `has_tag` and `has_tag_value` functions use snake\_case naming. The older camelCase forms (`hasTag`, `hasTagValue`) continue to work but aren't recommended. Databricks plans to deprecate camelCase forms when creating new policies. Existing policies aren't affected.

_Example: using two column conditions._ A `customers` schema has tables with an email column tagged `pii : email` and a consent column tagged `consent_to_contact`. The policy masks email addresses unless the customer has consented to be contacted. It uses two column conditions:

1.  `has_tag_value('pii', 'email')` identifies the column that contains email addresses (the column to mask).
2.  `has_tag('consent_to_contact')` identifies the column that contains consent information (used by the UDF to decide whether to mask).

SQL

    CREATE FUNCTION mask_email_by_consent(email STRING, consent BOOLEAN)RETURNS STRINGRETURN CASE  WHEN consent = true THEN email  ELSE '****@****.***'END;CREATE POLICY mask_email_with_consentON SCHEMA customersCOLUMN MASK mask_email_by_consentTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'email') AS m,  has_tag('consent_to_contact') AS cON COLUMN mUSING COLUMNS (c);

This policy only applies to tables that have both a column tagged `pii : email` and a column tagged `consent_to_contact`. If a table does not have columns matching both conditions, the policy does not apply and the data is returned unmasked.

### User-defined functions (UDFs)[​](#user-defined-functions-udfs "Direct link to user-defined-functions-udfs")

Row filter and column mask policies use user-defined functions (UDFs) to implement their filtering or masking logic. See [User-defined functions (UDFs) in Unity Catalog](https://docs.databricks.com/aws/en/udf/unity-catalog) for how to create and manage UDFs, and [Common patterns for row filtering and column masking](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns) for examples.

## Separation of duties and permissions[​](#separation-of-duties-and-permissions "Direct link to separation-of-duties-and-permissions")

Setting up ABAC involves several steps, each with its own permission requirements. Organizations can distribute these tasks across specialized groups depending on how they choose to separate duties. For example, an organization can define a tag taxonomy centrally, then have data stewards classify data, governance admins write policies, data creators create objects within governed scopes, and data consumers access the governed objects.

![Separation of duties for ABAC](https://docs.databricks.com/aws/en/assets/images/abac-separation-of-duties-b1d6e07523bce2aadaf83ee6b61243b4.png)

1.  **Create the tag taxonomy.** Define the governed tag keys and their allowed values before anyone applies them or writes policies. For example, create a `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) or a `pii` tag with values like `ssn`, `email`, and `phone_number`. See [Standardize attributes and naming](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/best-practices#tag-standards) for recommendations on naming conventions and taxonomy design.
    
    *   Required permissions: Account admin, or a user with `CREATE` permission for tags at the account level.
2.  **Tag data assets.** A data steward, data creator, or AI classification system applies governed tags to Unity Catalog securable objects such as catalogs, schemas, tables, columns, models, and volumes. For example, tag columns that contain personally identifiable information with `pii : ssn`, or tag a model with `lifecycle : production`. Correct tagging is the essential first step for ABAC policies to apply.
    
    *   Required permissions: `ASSIGN` on the tag, and `APPLY TAG` on the object.

warning

Tagging is a security boundary. If a user can change tags on a data asset, they can change which policies apply to it. Organizations should control who can apply tags and audit tag changes.

3.  **Create a policy.** A governance admin creates a policy at a scope, such as a catalog or schema. The policy specifies who it applies to, what conditions it evaluates, and the action to apply, such as a row filter, a column mask, or a privilege grant.
    
    *   Required permissions: `MANAGE` permission or object ownership on the securable object where the policy is attached. For row filter and column mask policies, also `EXECUTE` privilege on the UDF.
4.  **Create data objects.** Data creators create securable objects such as tables, models, or volumes within the scopes to which they were granted access. New objects inherit tags from parent catalogs and schemas. Data creators also have `APPLY TAG` automatically on objects they create, so they can apply additional tags. Alternatively, they can rely on [automatic data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification) to handle tagging. If an organization relies on data creators to tag their own objects, it should establish clear tagging practices. Data creators do not need to configure any access controls if policies are set at higher levels, which Databricks recommends.
    
    *   Required permissions: `CREATE TABLE` or other relevant creation privileges on the parent object.
5.  **Access governed objects.** When a user attempts to access a securable object within a policy's scope, Unity Catalog evaluates applicable policies automatically. For row filter and column mask policies, the user sees filtered or masked data if the table or columns match the policy's conditions and the user is not exempt. For GRANT policies (Beta), the user gains the granted privilege if the conditions match and the user is in `TO` and not in `EXCEPT`.
    
    *   Required permissions: For row filter and column mask policies, users must be granted permissions on the table, such as `SELECT`, through a direct object grant. These policies filter records or mask columns for tables the user can already access. They do not grant permissions on their own. GRANT policies (Beta) grant the privilege themselves and union with any direct grants on the same securable.

## Benefits of ABAC[​](#benefits-of-abac "Direct link to benefits-of-abac")

*   **Reusable policies based on attributes:** A single policy can apply to multiple data objects that match the same attribute-based conditions, rather than being tied to one specific object.
    
*   **Automatic application to new objects:** When new data objects are created within scope and tagged with the relevant attributes, existing ABAC policies apply without additional configuration. Policies act like future grants, which means that access controls apply automatically as new data is created and tagged appropriately.
    
*   **Consistent enforcement within a scope:** Policies attached at the catalog or schema level are evaluated dynamically against matching data objects in that scope, which removes differences in how similar data is filtered or masked.
    
*   **Lower ongoing maintenance:** Changes can be made by updating policy logic or governed tags, rather than revisiting each individual object as is required with table-level row filters and column masks.
    
*   **Centralized governance:** Because policies can be defined once and applied across many matching data objects, governance teams can manage controls across larger parts of the data estate with fewer policy definitions.
    

## More information[​](#more-information "Direct link to more-information")

*   [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/)
*   [CREATE POLICY](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy)
*   [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/)
*   [Row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/)
*   [Audit log system table reference](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs)
*   [Requirements, quotas, and limitations for row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements)
