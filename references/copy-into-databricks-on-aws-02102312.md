---
title: COPY INTO | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-copy-into
ingestedAt: "2026-06-18T08:18:43.797Z"
---

**Applies to:** ![check marked yes](data:image/png;base64,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) Databricks SQL ![check marked yes](data:image/png;base64,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) Databricks Runtime

Loads data from a file location into a Delta table. This is a retryable and idempotent operation — Files in the source location that have already been loaded are skipped. This is true even if the files have been modified since they were loaded. For examples, see [Common data loading patterns using `COPY INTO`](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/examples).

## Syntax[​](#syntax "Direct link to Syntax")

SQL

    COPY INTO target_table [ BY POSITION | ( col_name [ , <col_name> ... ] ) ]  FROM { source_clause |         ( SELECT expression_list FROM source_clause ) }  FILEFORMAT = data_source  [ VALIDATE [ ALL | num_rows ROWS ] ]  [ FILES = ( file_name [, ...] ) | PATTERN = glob_pattern ]  [ FORMAT_OPTIONS ( { data_source_reader_option = value } [, ...] ) ]  [ COPY_OPTIONS ( { copy_option = value } [, ...] ) ]source_clause  source [ WITH ( [ CREDENTIAL { credential_name |                                 (temporary_credential_options) } ]                  [ ENCRYPTION (encryption_options) ] ) ]

## Parameters[​](#parameters "Direct link to Parameters")

*   **`target_table`**
    
    Identifies an existing Delta table. The [target\_table](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name) must not include a [temporal specification or options specification](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name).
    
    If the table name is provided in the form of a location, such as: `` delta.`/path/to/table` `` , Unity Catalog can govern access to the locations that are being written to. You can write to an external location by:
    
    *   Defining the location as an external location and having `WRITE FILES` permissions on that external location.
    *   Having `WRITE FILES` permissions on a named storage credential that provide authorization to write to a location using: ``COPY INTO delta.`/some/location` WITH (CREDENTIAL <named-credential>)``
    
    See [Connect to cloud object storage using Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/) for more details.
    
*   **`BY POSITION` | ( col\_name \[ , <col\_name> … \] )**
    
    Matches source columns to target table columns by ordinal position. Type casting of the matched columns is done automatically.
    
    This parameter is only supported for headerless CSV file format. You must specify `FILEFORMAT = CSV`. `FORMAT_OPTIONS` must also be set to `("headers" = "false")` (`FORMAT_OPTIONS ("headers" = "false")` is the default).
    
    Syntax option 1: `BY POSITION`
    
    *   Matches source columns to target table columns by ordinal position automatically.
        *   The default name matching is not used for matching.
        *   `IDENTITY` columns and `GENERATED` columns of the target table are ignored when matching the source columns.
        *   If the number of source columns doesn't equal the filtered target table columns, `COPY INTO` raises an error.
    
    Syntax option 2: `( col_name [ , <col_name> ... ] )`
    
    *   Matches source columns to the specified target table columns by relative ordinal position using a target table column name list in parentheses, separated by comma.
        *   The original table column order and column names are not used for matching.
        *   `IDENTITY` columns and `GENERATED` columns cannot be specified in the column name list, otherwise `COPY INTO` raises an error.
        *   The specified columns cannot be duplicated.
        *   When the number of source columns doesn't equal the specified table columns, `COPY INTO` raises an error.
        *   For the columns that are not specified in the column name list, `COPY INTO` assigns default values, if any, and assigns `NULL` otherwise. If any column is not nullable, `COPY INTO` raises an error.
*   **`source`**
    
    The file location to load the data from. Files in this location must have the format specified in `FILEFORMAT`. The location is provided in the form of a URI.
    
    Access to the source location can be provided through:
    
    *   **`credential_name`**
        
        Optional name of the credential used to access or write to the storage location. You use this credential only if the file location is not included in an [external location](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-external-locations). See [credential\_name](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#credential-name).
        
    *   Inline temporary credentials.
        
    
    *   Defining the source location as an external location and having `READ FILES` permissions on the external location through Unity Catalog.
    *   Using a named storage credential with `READ FILES` permissions that provide authorization to read from a location through Unity Catalog.
    
    You don't need to provide inline or named credentials if the path is already defined as an external location that you have permissions to use. See [Overview of external locations](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#external-locations) for more details.
    
    note
    
    If the source file path is a root path, please add a slash (`/`) at the end of the file path, for example, `s3://my-bucket/`.
    
    Accepted credential options are:
    
    *   `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and `AWS_SESSION_TOKEN` for AWS S3
    *   `AZURE_SAS_TOKEN` for ADLS and Azure Blob Storage
    
    Accepted encryption options are:
    
    *   `TYPE = 'AWS_SSE_C'`, and `MASTER_KEY` for AWS S3

See [Load data using COPY INTO with temporary credentials](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/temporary-credentials).

*   **`SELECT expression_list`**
    
    Selects the specified columns or expressions from the source data before copying into the Delta table. The expressions can be anything you use with `SELECT` statements, including window operations. You can use aggregation expressions only for global aggregates–you cannot `GROUP BY` on columns with this syntax.
    
*   **`FILEFORMAT = data_source`**
    
    The format of the source files to load. One of `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, `BINARYFILE`.
    
*   **`VALIDATE`**
    
    **Applies to:** ![check marked yes](data:image/png;base64,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) Databricks SQL ![check marked yes](data:image/png;base64,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) Databricks Runtime 10.4 LTS and above
    
    The data that is to be loaded into a table is validated but not written to the table. These validations include:
    
    *   Whether the data can be parsed.
    *   Whether the schema matches that of the table or if the schema needs to be evolved.
    *   Whether all nullability and check constraints are met.
    
    The default is to validate all of the data that is to be loaded. You can provide a number of rows to be validated with the `ROWS` keyword, such as `VALIDATE 15 ROWS`. The `COPY INTO` statement returns a preview of the data of 50 rows or less when a number of less than 50 is used with the `ROWS` keyword).
    
*   **`FILES`**
    
    A list of file names to load, with a limit of 1000 files. Cannot be specified with `PATTERN`.
    
*   **`PATTERN`**
    
    A glob pattern that identifies the files to load from the source directory. Cannot be specified with `FILES`.
    
*   **`FORMAT_OPTIONS`**
    
    Options to be passed to the Apache Spark data source reader for the specified format. See [Format options](#format-options) for each file format.
    
*   **`COPY_OPTIONS`**
    
    Options to control the operation of the `COPY INTO` command.
    
    *   `force`: boolean, default `false`. If set to `true`, idempotency is disabled and files are loaded regardless of whether they've been loaded before.
    *   `mergeSchema`: boolean, default `false`. If set to `true`, the schema can be evolved according to the incoming data.

## Invoke `COPY INTO` concurrently[​](#invoke-copy-into-concurrently "Direct link to invoke-copy-into-concurrently")

`COPY INTO` supports concurrent invocations against the same table. As long as `COPY INTO` is invoked concurrently on **distinct** sets of input files, each invocation should eventually succeed, otherwise you get a transaction conflict. `COPY INTO` should not be invoked concurrently to improve performance; a single `COPY INTO` command with multiple files typically performs better than running concurrent `COPY INTO` commands with a single file each. `COPY INTO` can be called concurrently when:

*   Multiple data producers don't have an easy way to coordinate and cannot make a single invocation.
*   When a very large directory can be ingested sub-directory by sub-directory. When ingesting directories with a very large number of files, Databricks recommends using [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/) when possible.

To learn how to access metadata for file-based data sources, see [File metadata column](https://docs.databricks.com/aws/en/ingestion/file-metadata-column).

## Format options[​](#format-options "Direct link to format-options")

For options specific to each file format (JSON, CSV, XML, Parquet, Avro, text, ORC, and binary), see [DataFrameReader options](https://docs.databricks.com/aws/en/spark/api-options#batch-read-options).

## Related articles[​](#related-articles "Direct link to Related articles")

*   [Credentials](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-external-locations)
*   [DELETE](https://docs.databricks.com/aws/en/sql/language-manual/delta-delete-from)
*   [INSERT](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into)
*   [MERGE](https://docs.databricks.com/aws/en/sql/language-manual/delta-merge-into)
*   [PARTITION](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-partition#partition)
*   [query](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-query)
*   [UPDATE](https://docs.databricks.com/aws/en/sql/language-manual/delta-update)
*   [Get started using COPY INTO to load data](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/)
