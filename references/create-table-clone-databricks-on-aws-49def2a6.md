---
title: CREATE TABLE CLONE | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-clone
ingestedAt: "2026-06-18T08:18:40.730Z"
---

**Applies to:** ![check marked yes](data:image/png;base64,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) Databricks SQL ![check marked yes](data:image/png;base64,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) Databricks Runtime

Clones a source Delta, managed Apache Iceberg, or Apache Parquet table to a target location at a specific version. Cloning can be either deep or shallow: deep clones copy the data, while shallow clones reference the source data without copying it.

*   **Delta**, **Parquet**, and **Foreign Iceberg** tables support both deep and shallow cloning.
*   Managed **Iceberg** tables support only deep cloning, and you can't change the table format during cloning.

For more information, see [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/clone-parquet).

In Databricks SQL and Databricks Runtime 13.3 LTS and above, you can use shallow clone with Unity Catalog managed tables. In Databricks Runtime 12.2 LTS and below, there is no support for shallow clones in Unity Catalog. See [Shallow clone for Unity Catalog tables](https://docs.databricks.com/aws/en/tables/operations/clone-unity-catalog).

important

There are important differences between shallow and deep clones that can determine how best to use them. See [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone).

note

Streaming tables and materialized views are not supported as source or target tables for `CLONE`. See [Limitations](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-streaming-table#st-limitations) and [Limitations](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-materialized-view#mv-limitations).

## Syntax[​](#syntax "Direct link to Syntax")

    CREATE TABLE [IF NOT EXISTS] table_name   [SHALLOW | DEEP] CLONE source_table_name [TBLPROPERTIES clause] [LOCATION path]

    [CREATE OR] REPLACE TABLE table_name   [SHALLOW | DEEP] CLONE source_table_name [TBLPROPERTIES clause] [LOCATION path]

## Parameters[​](#parameters "Direct link to Parameters")

*   **IF NOT EXISTS**
    
    If specified, the statement is ignored if `table_name` already exists.
    
*   **\[CREATE OR\] REPLACE**
    
    If `CREATE OR` is specified the table is replaced if it exists and newly created if it does not. Without `CREATE OR` the `table_name` must exist.
    
*   **[table\_name](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name)**
    
    The name of the table to be created. The name must not include a [temporal specification or options specification](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name). If the name is not qualified the table is created in the current schema. `table_name` must not exist already unless `REPLACE` or `IF NOT EXISTS` has been specified.
    
*   **SHALLOW CLONE** or **DEEP CLONE**
    
    If you specify `SHALLOW CLONE` Databricks will make a copy of the source table's definition, but refer to the source table's files. When you specify `DEEP CLONE` (default) Databricks will make a complete, independent copy of the source table.
    
    Managed Iceberg tables only support deep cloning, not shallow cloning.
    
*   **[source\_table\_name](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name)**
    
    The name of the table to be cloned. The name may include a [temporal specification or options specification](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name).
    
*   **[TBLPROPERTIES](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-tblproperties#tblproperties)**
    
    Optionally sets one or more user-defined properties.
    
*   **LOCATION path**
    
    Optionally creates an external table, with the provided location as the path where the data is stored. If `table_name` itself is a path instead of a table identifier, the operation will fail. `path` must be a STRING literal.
    

## Examples[​](#examples "Direct link to Examples")

Deep clone and shallow clone a Delta Lake table:

SQL

    -- Deep clone: copies data and metadataCREATE TABLE target_catalog.target_schema.target_tableDEEP CLONE source_catalog.source_schema.source_table;-- Shallow clone: copies metadata only, references source data filesCREATE TABLE target_catalog.target_schema.target_tableSHALLOW CLONE source_catalog.source_schema.source_table;

Deep clone a managed Iceberg table (only deep cloning is supported):

SQL

    CREATE TABLE target_catalog.target_schema.target_tableDEEP CLONE source_catalog.source_schema.source_table;

For more Delta Lake clone examples, including data archiving and ML workflows, see [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone). For more managed Iceberg clone examples, see [Clone a managed Iceberg table](https://docs.databricks.com/aws/en/iceberg/clone).
