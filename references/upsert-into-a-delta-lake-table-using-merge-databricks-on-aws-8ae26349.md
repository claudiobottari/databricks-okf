---
title: Upsert into a Delta Lake table using merge | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta/merge
ingestedAt: "2026-06-18T08:05:04.078Z"
---

You can upsert data from a source table, view, or DataFrame into a target Delta Lake table by using the `MERGE` SQL operation. Delta Lake supports inserts, updates, and deletes in `MERGE`, and it supports extended syntax beyond the SQL standards to facilitate advanced use cases.

Suppose you have a source table named `people10mupdates` or a source path at `/tmp/delta/people-10m-updates` that contains new data for a target table named `people10m` or a target path at `/tmp/delta/people-10m`. Some of these new records may already be present in the target data. To merge the new data, you want to update rows where the person's `id` is already present and insert the new rows where no matching `id` is present. You can run the following query:

*   SQL
*   Python
*   Scala

SQL

    MERGE INTO people10mUSING people10mupdatesON people10m.id = people10mupdates.idWHEN MATCHED THEN  UPDATE SET    id = people10mupdates.id,    firstName = people10mupdates.firstName,    middleName = people10mupdates.middleName,    lastName = people10mupdates.lastName,    gender = people10mupdates.gender,    birthDate = people10mupdates.birthDate,    ssn = people10mupdates.ssn,    salary = people10mupdates.salaryWHEN NOT MATCHED  THEN INSERT (    id,    firstName,    middleName,    lastName,    gender,    birthDate,    ssn,    salary  )  VALUES (    people10mupdates.id,    people10mupdates.firstName,    people10mupdates.middleName,    people10mupdates.lastName,    people10mupdates.gender,    people10mupdates.birthDate,    people10mupdates.ssn,    people10mupdates.salary  )

important

Only a single row from the source table can match a given row in the target table. In Databricks Runtime 16.0 and above, `MERGE` evaluates conditions specified in the `WHEN MATCHED` and `ON` clauses to determine duplicate matches. In Databricks Runtime 15.4 LTS and below, `MERGE` operations only consider conditions specified in the `ON` clause.

See the [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api) for Scala and Python syntax details. For SQL syntax details, see [`MERGE INTO`](https://docs.databricks.com/aws/en/sql/language-manual/delta-merge-into)

## Modify all unmatched rows using merge[​](#modify-all-unmatched-rows-using-merge "Direct link to modify-all-unmatched-rows-using-merge")

In Databricks SQL and Databricks Runtime 12.2 LTS and above, you can use the `WHEN NOT MATCHED BY SOURCE` clause to `UPDATE` or `DELETE` records in the target table that do not have corresponding records in the source table. Databricks recommends adding an optional conditional clause to avoid fully rewriting the target table.

The following code example shows the basic syntax of using this for deletes, overwriting the target table with the contents of the source table and deleting unmatched records in the target table. For a more scalable pattern for tables where source updates and deletes are time-bound, see [Incrementally sync Delta Lake table with source](#incremental-sync).

*   Python
*   Scala
*   SQL

Python

    (targetDF  .merge(sourceDF, "source.key = target.key")  .whenMatchedUpdateAll()  .whenNotMatchedInsertAll()  .whenNotMatchedBySourceDelete()  .execute())

The following example adds conditions to the `WHEN NOT MATCHED BY SOURCE` clause and specifies values to update in unmatched target rows.

*   Python
*   Scala
*   SQL

Python

    (targetDF  .merge(sourceDF, "source.key = target.key")  .whenMatchedUpdate(    set = {"target.lastSeen": "source.timestamp"}  )  .whenNotMatchedInsert(    values = {      "target.key": "source.key",      "target.lastSeen": "source.timestamp",      "target.status": "'active'"    }  )  .whenNotMatchedBySourceUpdate(    condition="target.lastSeen >= (current_date() - INTERVAL '5' DAY)",    set = {"target.status": "'inactive'"}  )  .execute())

## Merge operation semantics[​](#merge-operation-semantics "Direct link to Merge operation semantics")

The following is a detailed description of the `merge` programmatic operation semantics.

*   There can be any number of `whenMatched` and `whenNotMatched` clauses.
    
*   `whenMatched` clauses are executed when a source row matches a target table row based on the match condition. These clauses have the following semantics.
    
    *   `whenMatched` clauses can have at most one `update` and one `delete` action. The `update` action in `merge` only updates the specified columns (similar to the `update` [operation](https://docs.databricks.com/aws/en/delta/tutorial#update)) of the matched target row. The `delete` action deletes the matched row.
        
    *   Each `whenMatched` clause can have an optional condition. If this clause condition exists, the `update` or `delete` action is executed for any matching source-target row pair only when the clause condition is true.
        
    *   If there are multiple `whenMatched` clauses, then they are evaluated in the order they are specified. All `whenMatched` clauses, except the last one, must have conditions.
        
    *   If none of the `whenMatched` conditions evaluate to true for a source and target row pair that matches the merge condition, then the target row is left unchanged.
        
    *   To update all the columns of the target Delta Lake table with the corresponding columns of the source dataset, use `whenMatched(...).updateAll()`. This is equivalent to:
        
        Scala
        
            whenMatched(...).updateExpr(Map("col1" -> "source.col1", "col2" -> "source.col2", ...))
        
        for all the columns of the target Delta Lake table. Therefore, this action assumes that the source table has the same columns as those in the target table, otherwise the query throws an analysis error.
        
*   `whenNotMatched` clauses are executed when a source row does not match any target row based on the match condition. These clauses have the following semantics.
    
    *   `whenNotMatched` clauses can have only the `insert` action. The new row is generated based on the specified column and corresponding expressions. You do not need to specify all the columns in the target table. For unspecified target columns, `NULL` is inserted.
        
    *   Each `whenNotMatched` clause can have an optional condition. If the clause condition is present, a source row is inserted only if that condition is true for that row. Otherwise, the source column is ignored.
        
    *   If there are multiple `whenNotMatched` clauses, then they are evaluated in the order they are specified. All `whenNotMatched` clauses, except the last one, must have conditions.
        
    *   To insert all the columns of the target Delta Lake table with the corresponding columns of the source dataset, use `whenNotMatched(...).insertAll()`. This is equivalent to:
        
        Scala
        
            whenNotMatched(...).insertExpr(Map("col1" -> "source.col1", "col2" -> "source.col2", ...))
        
        for all the columns of the target Delta Lake table. Therefore, this action assumes that the source table has the same columns as those in the target table, otherwise the query throws an analysis error.
        
*   `whenNotMatchedBySource` clauses are executed when a target row does not match any source row based on the merge condition. These clauses have the following semantics.
    
    *   `whenNotMatchedBySource` clauses can specify `delete` and `update` actions.
    *   Each `whenNotMatchedBySource` clause can have an optional condition. If the clause condition is present, a target row is modified only if that condition is true for that row. Otherwise, the target row is left unchanged.
    *   If there are multiple `whenNotMatchedBySource` clauses, then they are evaluated in the order they are specified. All `whenNotMatchedBySource` clauses, except the last one, must have conditions.
    *   By definition, `whenNotMatchedBySource` clauses do not have a source row to pull column values from, and so source columns can't be referenced. For each column to be modified, you can either specify a literal or perform an action on the target column, such as `SET target.deleted_count = target.deleted_count + 1`.

important

*   A `merge` operation can fail if multiple rows of the source dataset match and the merge attempts to update the same rows of the target Delta Lake table. According to the SQL semantics of merge, such an update operation is ambiguous as it is unclear which source row should be used to update the matched target row. You can preprocess the source table to eliminate the possibility of multiple matches.
*   You can apply a SQL `MERGE` operation on a SQL VIEW only if the view has been defined as `CREATE VIEW viewName AS SELECT * FROM deltaTable`.

## Data deduplication when writing into Delta Lake tables[​](#data-deduplication-when-writing-into-delta-lake-tables "Direct link to data-deduplication-when-writing-into-delta-lake-tables")

A common ETL use case is to collect logs into Delta Lake table by appending them to a table. However, often the sources can generate duplicate log records and downstream deduplication steps are needed to take care of them. With `merge`, you can avoid inserting the duplicate records.

*   SQL
*   Python
*   Scala
*   Java

SQL

    MERGE INTO logsUSING newDedupedLogsON logs.uniqueId = newDedupedLogs.uniqueIdWHEN NOT MATCHED  THEN INSERT *

note

The dataset containing the new logs needs to be deduplicated within itself. By the SQL semantics of merge, it matches and deduplicates the new data with the existing data in the table, but if there is duplicate data within the new dataset, it is inserted. Hence, deduplicate the new data before merging into the table.

If you know that you may get duplicate records only for a few days, you can optimize your query further by partitioning the table by date, and then specifying the date range of the target table to match on.

*   SQL
*   Python
*   Scala
*   Java

SQL

    MERGE INTO logsUSING newDedupedLogsON logs.uniqueId = newDedupedLogs.uniqueId AND logs.date > current_date() - INTERVAL 7 DAYSWHEN NOT MATCHED AND newDedupedLogs.date > current_date() - INTERVAL 7 DAYS  THEN INSERT *

This is more efficient than the previous command as it looks for duplicates only in the last 7 days of logs, not the entire table. Furthermore, you can use this insert-only merge with Structured Streaming to perform continuous deduplication of the logs.

*   In a streaming query, you can use merge operation in `foreachBatch` to continuously write any streaming data to a Delta Lake table with deduplication. See the following [streaming example](https://docs.databricks.com/aws/en/structured-streaming/delta-lake#merge-in-streaming) for more information on `foreachBatch`.
*   In another streaming query, you can continuously read deduplicated data from this Delta Lake table. This is possible because an insert-only merge only appends new data to the Delta Lake table.

## Slowly changing data (SCD) and change data capture (CDC) with Delta Lake[​](#slowly-changing-data-scd-and-change-data-capture-cdc-with-delta-lake "Direct link to slowly-changing-data-scd-and-change-data-capture-cdc-with-delta-lake")

Lakeflow Spark Declarative Pipelines has native support for tracking and applying SCD Type 1 and Type 2. Use `AUTO CDC ... INTO` with Lakeflow Spark Declarative Pipelines to ensure that out of order records are handled correctly when processing CDC feeds. See [The AUTO CDC APIs: Simplify change data capture with pipelines](https://docs.databricks.com/aws/en/ldp/cdc).

## Incrementally sync Delta Lake table with source[​](#incrementally-sync-delta-lake-table-with-source "Direct link to incrementally-sync-delta-lake-table-with-source")

In Databricks SQL and Databricks Runtime 12.2 LTS and above, you can use `WHEN NOT MATCHED BY SOURCE` to create arbitrary conditions to atomically delete and replace a portion of a table. This can be especially useful when you have a source table where records may change or be deleted for several days after initial data entry, but eventually settle to a final state.

The following query shows using this pattern to select 5 days of records from the source, update matching records in the target, insert new records from the source to the target, and delete all unmatched records from the past 5 days in the target.

SQL

    MERGE INTO target AS tUSING (SELECT * FROM source WHERE created_at >= (current_date() - INTERVAL '5' DAY)) AS sON t.key = s.keyWHEN MATCHED THEN UPDATE SET *WHEN NOT MATCHED THEN INSERT *WHEN NOT MATCHED BY SOURCE AND created_at >= (current_date() - INTERVAL '5' DAY) THEN DELETE

By providing the same boolean filter on the source and target tables, you are able to dynamically propagate changes from your source to target tables, including deletes.

note

While this pattern can be used without any conditional clauses, this would lead to fully rewriting the target table which can be expensive.
