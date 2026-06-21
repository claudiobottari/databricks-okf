---
title: Hive metastore privileges and securable objects (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges
ingestedAt: "2026-06-18T08:03:48.791Z"
---

This article describes the privilege model for the legacy Databricks Hive metastore, which is built in to each Databricks workspace. It also describes how to grant, deny, and revoke privileges for objects in the built-in Hive metastore. Unity Catalog uses a different model for granting privileges. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).

## Requirements[​](#requirements "Direct link to Requirements")

*   An administrator must [enable and enforce table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#enable-table-acl-workspace) for the workspace.
*   The cluster must be enabled for [table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#table-access-control).

note

*   Data access control is _always enabled_ in Databricks SQL even if table access control is _not enabled_ for the workspace.
*   If table access control is enabled for the workspace and you have already specified ACLs (granted and denied privileges) in the workspace, those ACLs are respected in Databricks SQL.

Privileges on data objects managed by the Hive metastore can be granted by either a workspace admin or the owner of an object. You can manage privileges for Hive metastore objects by using SQL commands.

To manage privileges in SQL, you use [GRANT](https://docs.databricks.com/aws/en/sql/language-manual/security-grant), [REVOKE](https://docs.databricks.com/aws/en/sql/language-manual/security-revoke), [DENY](https://docs.databricks.com/aws/en/sql/language-manual/security-deny), [MSCK](https://docs.databricks.com/aws/en/sql/language-manual/security-msck), and [SHOW GRANTS](https://docs.databricks.com/aws/en/sql/language-manual/security-show-grant) statements in a notebook or the Databricks SQL query editor, using the syntax:

SQL

    GRANT privilege_type ON securable_object TO principal

Where:

*   `privilege_type` is a [Hive metastore privilege type](#privilege-types)
*   `securable_object` is a [securable object in the Hive metastore](#securable-objects)
*   `principal` is a user, service principal (represented by its applicationId value), or group. You must enclose users, service principals, and group names with [special characters](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-identifiers#delimited-identifiers) in backticks (`` ` ` ``). See [Principal](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-principal).

To grant a privilege to all users in your workspace, grant the privilege to the `users` group. For example:

SQL

    GRANT SELECT ON TABLE <schema-name>.<table-name> TO users

For more information about managing privileges for objects in the Hive metastore using SQL commands, see [Privileges and securable objects in the Hive metastore](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-privileges-hms).

You can also manage table access control in a fully automated setup using the [Databricks Terraform](https://docs.databricks.com/aws/en/dev-tools/terraform/) provider and [databricks\_sql\_permissions](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/sql_permissions#example-usage).

## Object ownership[​](#object-ownership "Direct link to Object ownership")

When table access control is enabled on a cluster or SQL warehouse, a user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users.

Groups may own objects, in which case all members of that group are considered owners.

Either the owner of an object or a workspace admin can transfer ownership of an object using the following command:

SQL

    ALTER <object> OWNER TO `<user-name>@<user-domain>.com`

note

When table access control is disabled on a cluster or SQL warehouse, owners are not registered when a schema, table, or view is created. A workspace admin must assign an owner to the object using the `ALTER <object> OWNER TO` command.

The securable objects are:

*   `CATALOG`: controls access to the entire data catalog.
    
    *   `SCHEMA`: controls access to a schema.
        *   `TABLE`: controls access to a managed or external table.
        *   `VIEW`: controls access to SQL views.
        *   `FUNCTION`: controls access to a named function.
*   `ANONYMOUS FUNCTION`: controls access to [anonymous or temporary functions](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-function).
    
    note
    
    `ANONYMOUS FUNCTION` objects are not supported in Databricks SQL.
    
*   `ANY FILE`: controls access to the underlying filesystem.
    
    warning
    
    Users granted access to `ANY FILE` can bypass the restrictions put on the catalog, schemas, tables, and views by reading from the filesystem directly.
    

note

Privileges on global and local temporary views are not supported. Local temporary views are visible only within the same session, and views created in the `global_temp` schema are visible to all users sharing a cluster or SQL warehouse. However, privileges on the underlying tables and views referenced by any temporary views are enforced.

*   `SELECT`: gives read access to an object.
*   `CREATE`: gives ability to create an object (for example, a table in a schema).
*   `MODIFY`: gives ability to add, delete, and modify data to or from an object.
*   `USAGE`: does not give any abilities, but is an additional requirement to perform any action on a schema object.
*   `READ_METADATA`: gives ability to view an object and its metadata.
*   `CREATE_NAMED_FUNCTION`: gives ability to create a named UDF in an existing catalog or schema.
*   `MODIFY_CLASSPATH`: gives ability to add files to the Spark class path.
*   `ALL PRIVILEGES`: gives all privileges (is translated into all the above privileges).

note

The `MODIFY_CLASSPATH` privilege is not supported in Databricks SQL.

### `USAGE` privilege[​](#usage-privilege "Direct link to usage-privilege")

To perform an action on a schema object in the Hive metastore, a user must have the `USAGE` privilege on that schema in addition to the privilege to perform that action. Any one of the following satisfies the `USAGE` requirement:

*   Be a workspace admin
*   Have the `USAGE` privilege on the schema or be in a group that has the `USAGE` privilege on the schema
*   Have the `USAGE` privilege on the `CATALOG` or be in a group that has the `USAGE` privilege
*   Be the owner of the schema or be in a group that owns the schema

Even the owner of an object inside a schema must have the `USAGE` privilege in order to use it.

## Privilege hierarchy[​](#privilege-hierarchy "Direct link to Privilege hierarchy")

When table access control is enabled on the workspace and on all clusters, SQL objects in Databricks are hierarchical and privileges are inherited downward. This means that granting or denying a privilege on the `CATALOG` automatically grants or denies the privilege to all schemas in the catalog. Similarly, privileges granted on a schema object are inherited by all objects in that schema. This pattern is true for all securable objects.

If you deny a user privileges on a table, the user can't see the table by attempting to list all tables in the schema. If you deny a user privileges on a schema, the user can't see that the schema exists by attempting to list all schemas in the catalog.

## Dynamic view functions[​](#dynamic-view-functions "Direct link to Dynamic view functions")

Databricks includes two user functions that allow you to express column- and row-level permissions dynamically in the body of a view definition that is managed by the Hive metastore.

*   [`current_user()`](https://docs.databricks.com/aws/en/sql/language-manual/functions/current_user): return the current user name.
*   `is_member()`: determine if the current user is a member of a specific Databricks [group](https://docs.databricks.com/aws/en/admin/users-groups/groups) at the workspace level.

The following example combines both functions to determine if a user has the appropriate group membership:

SQL

    -- Return: true if the user is a member and false if they are notSELECT  current_user as user,-- Check to see if the current user is a member of the "Managers" group.  is_member("Managers") as admin

### Column-level permissions[​](#column-level-permissions "Direct link to Column-level permissions")

You can use dynamic views to limit the columns a specific group or user can see. Consider the following example where only users who belong to the `auditors` group are able to see email addresses from the `sales_raw` table. At analysis time Spark replaces the `CASE` statement with either the literal `'REDACTED'` or the column `email`. This behavior allows for all the usual performance optimizations provided by Spark.

SQL

    -- Alias the field 'email' to itself (as 'email') to prevent the-- permission logic from showing up directly in the column name results.CREATE VIEW sales_redacted ASSELECT  user_id,  CASE WHEN    is_group_member('auditors') THEN email    ELSE 'REDACTED'  END AS email,  country,  product,  totalFROM sales_raw

### Row-level permissions[​](#row-level-permissions "Direct link to Row-level permissions")

Using dynamic views you can specify permissions down to the row or field level. Consider the following example, where only users who belong to the `managers` group are able to see transaction amounts (`total` column) greater than $1,000,000.00:

SQL

    CREATE VIEW sales_redacted ASSELECT  user_id,  country,  product,  totalFROM sales_rawWHERE  CASE    WHEN is_group_member('managers') THEN TRUE    ELSE total <= 1000000  END;

### Data masking[​](#data-masking "Direct link to Data masking")

As shown in the preceding examples, you can implement column-level masking to prevent users from seeing specific column data unless they are in the correct group. Because these views are standard Spark SQL, you can do more advanced types of masking with more complex SQL expressions. The following example lets all users perform analysis on email domains, but lets members of the `auditors` group see users' full email addresses.

SQL

    -- The regexp_extract function takes an email address such as-- user.x.lastname@example.com and extracts 'example', allowing-- analysts to query the domain nameCREATE VIEW sales_redacted ASSELECT  user_id,  region,  CASE    WHEN is_group_member('auditors') THEN email    ELSE regexp_extract(email, '^.*@(.*)$', 1)  END  FROM sales_raw
