---
title: Manually apply row filters and column masks | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply
ingestedAt: "2026-06-18T08:04:32.593Z"
---

This page provides guidance and examples for using row filters, column masks, and mapping tables to filter sensitive data in your tables. These features require Unity Catalog.

If you're looking for a centralized tag-based approach to filtering and masking, see [Attribute-based access control in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/). ABAC enables you to manage policies using governed tags and apply them consistently across many tables.

## Before you begin[​](#before-you-begin "Direct link to Before you begin")

To add row filters and column masks to tables, you must have:

*   A workspace that is enabled for Unity Catalog.
*   A SQL UDF that is registered in Unity Catalog. To use Python or Scala logic, first create a Python or Scala UDF, then create a SQL UDF that calls it. The SQL UDF is what you apply as the row filter or column mask. For an example, see [Column mask with Python UDF](#wrapper-example). For best practices and limitations of UDFs, see [Row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/).

You must also meet the following requirements:

*   To assign a function that adds row filters or column masks to a table, you must have the `EXECUTE` privilege on the function, `USE SCHEMA` on the schema, and `USE CATALOG` on the parent catalog.
*   If you are adding filters or masks when you create a _new_ table, you must have the `CREATE TABLE` privilege on the schema.
*   If you are adding filters or masks to an _existing_ table, you must be the table owner or have the `MANAGE` privilege on the table.

To access a table that has row filters or column masks, your compute resource must meet one of these requirements:

*   A SQL warehouse.
*   Standard access mode (formerly shared access mode) on Databricks Runtime 12.2 LTS or above.
*   Dedicated access mode (formerly single user access mode) on Databricks Runtime 15.4 LTS or above.

You cannot read row filters or column masks using dedicated compute on Databricks Runtime 15.3 or below.

To take advantage of the data filtering provided in Databricks Runtime 15.4 LTS and above, you must also verify that your workspace is enabled for serverless compute, because the data filtering functionality that supports row filters and column masks runs on serverless compute. You might be charged for serverless compute resources when you use compute configured as dedicated access mode to read tables that use row filters or column masks. Write operations to these tables are only supported on Databricks Runtime 16.3 and above, and must use supported patterns such as `MERGE INTO`. See [Fine-grained access control on dedicated compute](https://docs.databricks.com/aws/en/compute/single-user-fgac).

note

**Row filters and column masks are retained when replacing a table.**

If you run `REPLACE TABLE`, any existing row filter is retained regardless of schema changes. Column masks are also retained if the new table includes columns with the same names as those that had masks in the original table. In both cases, the policies are preserved even if they are not explicitly redefined. This prevents accidental loss of data access policies.

However, if a retained policy references a column that was removed or changed, subsequent queries might fail. To resolve this, update or drop the policy using `ALTER TABLE`.

## Apply a row filter[​](#apply-a-row-filter "Direct link to Apply a row filter")

To create a row filter, you write a function (UDF) to define the filter policy and then apply it to a table. Each table can have only one row filter. A row filter accepts zero or more input parameters where each input parameter binds to one column of the corresponding table.

important

UDF parameter types must match the data types of the table columns passed to them. If a column type differs from the UDF parameter type, such as a `STRING` column passed to an `INT` parameter, the column value is implicitly cast. With ANSI mode disabled, values that can't be cast are silently converted to `NULL`, which can cause the filter to produce incorrect results without raising an error. For details, see [Data type mismatch behavior](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/#type-mismatch).

You can apply a row filter using Catalog Explorer or SQL commands. The Catalog Explorer instructions assume that you have already created a function and registered it in Unity Catalog. The SQL instructions include examples of creating a row filter function and applying it to a table.

note

If you're using Lakeflow Spark Declarative Pipelines, you can use the Lakeflow Spark Declarative Pipelines Python API to create streaming tables or materialized views that use row filters and column masks. See [Publish tables with row filters and column masks](https://docs.databricks.com/aws/en/ldp/unity-catalog#row-filters-and-column-masks).

*   Catalog Explorer
*   SQL

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Browse or search for the table you want to filter.
3.  On the **Overview** tab, under **Row filter**, click **Add filter**.
4.  On the **Add row filter** dialog, select the catalog and schema that contain the filter function, then select the function.
5.  On the expanded dialog, view the function definition and select the table columns that match the columns included in the function statement.
6.  Click **Add**.

To remove the filter from the table, click **fx Row filter** and click **Remove**.

## Row filter examples[​](#row-filter-examples "Direct link to Row filter examples")

This example creates a SQL user-defined function that applies to members of the group `admin` in the region `US`.

When this sample function is applied to the `sales` table, members of the `admin` group can access all records in the table. If the function is called by a non-admin, the `RETURN_IF` condition fails and the `region='US'` expression is evaluated, filtering the table to only show records in the `US` region.

SQL

    CREATE FUNCTION us_filter(region STRING)RETURN IF(IS_ACCOUNT_GROUP_MEMBER('admin'), true, region='US');

Apply the function to a table as a row filter. Subsequent queries from the `sales` table then return a subset of rows.

SQL

    CREATE TABLE sales (region STRING, id INT);ALTER TABLE sales SET ROW FILTER us_filter ON (region);

Disable the row filter. Future user queries from the `sales` table then return all of the rows in the table.

SQL

    ALTER TABLE sales DROP ROW FILTER;

Create a table with the function applied as a row filter as part of the `CREATE TABLE` statement. Future queries from the `sales` table then each return a subset of rows.

SQL

    CREATE TABLE sales (region STRING, id INT)WITH ROW FILTER us_filter ON (region);

## Apply a column mask[​](#apply-a-column-mask "Direct link to Apply a column mask")

To apply a column mask, create a function (UDF) and apply it to a table column.

important

UDF parameter types must match the data types of the columns passed to them. If a column type differs from the UDF parameter type, the column value is implicitly cast. With ANSI mode disabled, values that can't be cast are silently converted to `NULL`, which can cause the mask to produce incorrect results without raising an error. For details, see [Data type mismatch behavior](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/#type-mismatch).

You can apply a column mask using Catalog Explorer or SQL commands. The Catalog Explorer instructions assume that you have already created a function and registered it in Unity Catalog. The SQL instructions include examples of creating a column mask function and applying it to a table column.

note

If you're using Lakeflow Spark Declarative Pipelines, you can use the Lakeflow Spark Declarative Pipelines Python API to create streaming tables or materialized views that use row filters and column masks. See [Publish tables with row filters and column masks](https://docs.databricks.com/aws/en/ldp/unity-catalog#row-filters-and-column-masks).

*   Catalog Explorer
*   SQL

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Browse or search for the table.
3.  On the **Overview** tab, find the row you want to apply the column mask to and click the ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAABWWlDQ1BJQ0MgUHJvZmlsZQAAKJFtkL1Lw1AUxU9rasUvHHQQOgREsFKlxIJdawcpOIRq/ZpM05iqafqaRtTVVWdnJ/8CpYqLbu6Ciojo5uKkZLEl3teqadX7uJwfl/Me9x3ALyiMGQKAgmlb6ekpcXFpWQy+oJ1OBwYRUNQyS8jyDFnwra3l3MDH9XqMv3X6GFp/Ni6jD68npaqeyvz1t1RnTiurpFXqUZVZNuAbIZa3bMZ5m7jfoqWI9znrDT7knG3wcd0zl04SXxH3qXklR3xHHMk2zfUmLhib6tcOfPtuzczMkvZShyAjAQmTiCOJecrmf2+s7k2iCIYdWFiDjjxsiHSb0TGgEadgQsU4IsQSotQxnvHv7LxZaQOIvwP+IW+2Qpmc7QEDYW82TH/p2QXOn5hiKT+J+hyhvDohNbirAgQOXPdtAQiGgdqt635UXLd2BLTdAxfOJ9PYYx56edxFAAAAOGVYSWZNTQAqAAAACAABh2kABAAAAAEAAAAaAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAASAAAAALlhkG8AAAD2SURBVDgRpZM9EoIwEEYDw0l0xgKuoR0tXkFrC1vxAvaewdbOc0DBjF5F86LLBIhA4Jsh//vY3WyCt5by1O3+UEX1UslqobJ0Y6wjT4bKL1dVVk9jJj0wL5BA4tXSeINnfGg0yIbkh50xjnVoZ+0hYYZmZaARCMfIi6jUAMTaoEcCIRxyIqEAkDE5CvpuzYYQTqFBhGLrpNcT/ZO/obUhGGMg181cIIydIBeEw/Yt2RAnaAqkA5oKaYDmQGrQXIgBkUDqgzqRimWjL7HstxVS3mgOBPvO9ft6AgTVT2S7P35Xfm27ThqbjklkP0LZz9K1qWKZj+k/LRuwBP9tGQAAAAAASUVORK5CYII=) **Mask** edit icon.
4.  On the **Add column mask** dialog, select the catalog and schema that contain the filter function, then select the function.
5.  On the expanded dialog, view the function definition. If the function includes any parameters in addition to the column being masked, select the table columns in which you want to cast those additional function parameters.
6.  Click **Add**.

To remove the column mask from the table, click **fx Column mask** in the table row and click **Remove**.

## Column mask examples[​](#column-mask-examples "Direct link to Column mask examples")

In this example, you create a user-defined function that masks the `ssn` column so that only users who are members of the `HumanResourceDept` group can view values in that column.

SQL

    CREATE FUNCTION ssn_mask(ssn STRING)  RETURN CASE WHEN is_account_group_member('HumanResourceDept') THEN ssn ELSE '***-**-****' END;

Apply the new function to a table as a column mask. You can add the column mask when you create the table or later.

SQL

    --Create the `users` table and apply the column mask in a single step:CREATE TABLE users (  name STRING,  ssn STRING MASK ssn_mask);

SQL

    --Create the `users` table and apply the column mask after:CREATE TABLE users  (name STRING, ssn STRING);ALTER TABLE users ALTER COLUMN ssn SET MASK ssn_mask;

Queries on that table now return masked `ssn` column values when the querying user is not a member of the `HumanResourceDept` group:

SQL

    SELECT * FROM users;  James  ***-**-****

To disable the column mask so that queries return the original values in the `ssn` column:

SQL

    ALTER TABLE users ALTER COLUMN ssn DROP MASK;

### Column mask with Python UDF[​](#column-mask-with-python-udf "Direct link to column-mask-with-python-udf")

To use Python or Scala logic in a column mask, you must create a Python or Scala UDF, and then wrap it in a SQL UDF. The SQL wrapper function is what you apply as the column mask.

This example creates a Python UDF to mask email addresses, then wraps it in a SQL UDF:

SQL

    -- Step 1: Create the Python UDF with masking logicCREATE OR REPLACE FUNCTION email_mask_python(email STRING)RETURNS STRINGLANGUAGE PYTHONAS $$import rereturn re.sub(r'^[^@]+', lambda m: '*' * len(m.group()), email)$$;-- Step 2: Create a SQL wrapper function that calls the Python UDFCREATE OR REPLACE FUNCTION email_mask_sql(email STRING)RETURN email_mask_python(email);

Then, apply the SQL wrapper as the column mask to your table:

SQL

    -- Create the `contacts` table and apply the SQL wrapper as the column maskCREATE TABLE contacts (  name STRING,  email STRING MASK email_mask_sql);

important

You must apply the SQL wrapper function (`email_mask_sql`) as the column mask, not the Python UDF directly. If you try to use the Python UDF (`email_mask_python`) directly as a column mask, you will receive a `[ROUTINE_NOT_FOUND]` error.

### Column mask with additional columns (`USING COLUMNS`)[​](#column-mask-with-additional-columns-using-columns "Direct link to column-mask-with-additional-columns-using-columns")

Use the `USING COLUMNS` clause when a masking function must reference static parameters or other columns in the table. `USING COLUMNS` enables conditional masking based on values beyond the column being masked.

The `USING COLUMNS` clause provides additional arguments to the masking function:

*   The first parameter of the masking function always maps to the masked column itself.
*   Supply additional parameters using `USING COLUMNS` with static values or column names from the same table.

The following example creates a column mask that redacts addresses differently based on the value in another column (`country`). The function takes an additional parameter that specifies the group. Only members of the resulting country-group pair can view addresses for that country.

SQL

    -- Create a masking function that accepts two parameters:-- 1. address (the masked column)-- 2. country (an additional column used for conditional logic)-- 3. group_suffix (group the user belongs to)CREATE FUNCTION mask_address_by_country(address STRING, country STRING, group_suffix STRING DEFAULT '_address_viewers')RETURN IF(  is_account_group_member(country || group_suffix),  address,  'REDACTED');-- Create a table and apply the mask using USING COLUMNS to pass the country columnCREATE TABLE customers (  name STRING,  address STRING MASK mask_address_by_country USING COLUMNS (country, '_address_viewers'),  country STRING);-- Insert sample dataINSERT INTO customers VALUES  ('Alice', '123 Main St, New York', 'US'),  ('Bob', '456 High St, London', 'UK'),  ('Charlie', '789 Rue de Rivoli, Paris', 'FR');

Query results depend on group membership. If the user is a member of `US_address_viewers`, they can see US addresses but not others:

SQL

    -- As a member of 'US_address_viewers' groupSELECT * FROM customers;  Alice    | 123 Main St, New York | US  Bob      | REDACTED              | UK  Charlie  | REDACTED              | FR

You can also apply the mask to an existing table:

SQL

    -- Apply mask to existing columnALTER TABLE customers  ALTER COLUMN address  SET MASK mask_address_by_country USING COLUMNS (country, '_address_viewers');

### Column mask for nested `STRUCT` fields[​](#column-mask-for-nested-struct-fields "Direct link to column-mask-for-nested-struct-fields")

You can apply column masks to nested `STRUCT` columns to selectively mask specific fields within the structure while preserving other fields. This is useful when a `STRUCT` contains both public and sensitive data, and you want to apply different access controls to individual fields based on user attributes.

To mask nested fields, create a masking function that reconstructs the STRUCT using `named_struct()`, replacing sensitive field values conditionally while keeping other fields intact.

This example creates a masking function for a STRUCT column that contains both a public `value` field and a sensitive `secret` field. The masking function uses `is_account_group_member()` to determine whether to show the full data or mask the sensitive field.

SQL

    -- Create a masking function for nested STRUCT fieldsCREATE FUNCTION mask_nested_field(data STRUCT<value: STRING, secret: STRING>)RETURN IF(  is_account_group_member('privileged_users'),  data,  named_struct('value', data.value, 'secret', 'REDACTED'));

Apply the masking function when creating a table with a STRUCT column:

SQL

    -- Create a table with a masked STRUCT columnCREATE TABLE sensitive_data (  id INT,  nested_column STRUCT<value: STRING, secret: STRING>    MASK mask_nested_field);-- Insert sample dataINSERT INTO sensitive_data VALUES  (1, named_struct('value', 'public_info', 'secret', 'private_info')),  (2, named_struct('value', 'general_data', 'secret', 'confidential_data'));

Query the table to test the masking. Results vary based on group membership. If the user isn't a member of `privileged_users`, the secret is redacted:

SQL

    -- As a non-member of 'privileged_users'SELECT * FROM sensitive_data;  1  {"value":"public_info","secret":"REDACTED"}  2  {"value":"general_data","secret":"REDACTED"}

You can also apply the mask to an existing table:

SQL

    -- Apply mask to existing STRUCT columnALTER TABLE sensitive_data  ALTER COLUMN nested_column  SET MASK mask_nested_field;

important

The masking function should return a value with the same STRUCT type as the masked column. This helps avoid confusing schema mismatches that can occur during `INSERT`, `MERGE`, and `UPDATE` operations. In this example, the function returns `STRUCT<value: STRING, secret: STRING>` to match the column type.

## Use mapping tables to create an access-control list[​](#use-mapping-tables-to-create-an-access-control-list "Direct link to Use mapping tables to create an access-control list")

To achieve row-level security, consider defining a mapping table (or access-control list). A comprehensive mapping table encodes which data rows in the original table are accessible to certain users or groups. Mapping tables are useful because they offer simple integration with your fact tables through direct joins.

This methodology addresses many use cases that include custom requirements. Examples include:

*   Imposing restrictions based on the logged-in user while accommodating different rules for specific user groups.
*   Creating intricate hierarchies, such as organizational structures, that require diverse sets of rules.
*   Replicating complex security models from external source systems.

By adopting mapping tables, you can accomplish these challenging scenarios and ensure robust row-level and column-level security implementations.

## Mapping table examples[​](#mapping-table-examples "Direct link to Mapping table examples")

Use a mapping table to check if the current user is in a list:

Create a new mapping table:

SQL

    DROP TABLE IF EXISTS valid_users;CREATE TABLE valid_users(username string);INSERT INTO valid_usersVALUES  ('fred@databricks.com'),  ('barney@databricks.com');

Create a new filter:

note

All filters run with definer's rights except for functions that check user context (for example, the `SESSION_USER` and `IS_ACCOUNT_GROUP_MEMBER` functions) which run as the invoker.

In this example, the function checks whether the current user is in the `valid_users` table. If the user is found, the function returns true.

SQL

    DROP FUNCTION IF EXISTS row_filter;CREATE FUNCTION row_filter()  RETURN EXISTS(    SELECT 1 FROM valid_users v    WHERE v.username = SESSION_USER());

The example below applies the row filter during table creation. You can also add the filter later using an `ALTER TABLE` statement. When applying the filter to unspecified columns, use the `ON ()` syntax. For a specific column, use `ON (column);`. For more details, see [Parameters](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-row-filter#parameters).

SQL

    DROP TABLE IF EXISTS data_table;CREATE TABLE data_table  (x INT, y INT, z INT)  WITH ROW FILTER row_filter ON ();INSERT INTO data_table VALUES  (1, 2, 3),  (4, 5, 6),  (7, 8, 9);

Select data from the table. This should only return data if the user is in the `valid_users` table.

SQL

    SELECT * FROM data_table;

Create a mapping table comprising accounts that should always have access to view all the rows in the table, regardless of the column values:

SQL

    CREATE TABLE valid_accounts(account string);INSERT INTO valid_accountsVALUES  ('admin'),  ('cstaff');

Now, create a SQL UDF that returns `true` if the values of all columns in the row are less than five or if the invoking user is a member of the above mapping table.

SQL

    CREATE FUNCTION row_filter_small_values (x INT, y INT, z INT)  RETURN (x < 5 AND y < 5 AND z < 5)  OR EXISTS(    SELECT 1 FROM valid_accounts v    WHERE IS_ACCOUNT_GROUP_MEMBER(v.account));

Finally, apply the SQL UDF to the table as a row filter:

SQL

    ALTER TABLE data_table SET ROW FILTER row_filter_small_values ON (x, y, z);
