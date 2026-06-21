---
title: DELETE FROM | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-delete-from
ingestedAt: "2026-06-18T08:18:47.481Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [SQL language reference](https://docs.databricks.com/aws/en/sql/language-manual/)
*   DML statements
*   DELETE FROM

Last updated on **Mar 16, 2026**

**Applies to:** ![check marked yes](data:image/png;base64,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) Databricks SQL ![check marked yes](data:image/png;base64,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) Databricks Runtime

Deletes the rows that match a predicate. When no predicate is provided, deletes all rows.

This statement is only supported for Delta Lake tables.

### Syntax[​](#syntax "Direct link to Syntax")

    [ common_table_expression ]    DELETE FROM table_name [table_alias] [WHERE predicate]

### Parameters[​](#parameters "Direct link to Parameters")

*   **[common table expression](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-cte)**
    
    Common table expressions (CTE) are one or more named queries which can be reused multiple times within the main query block to avoid repeated computations or to improve readability of complex, nested queries.
    
*   [table\_name](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name)
    
    Identifies an existing table. The name must not include a [temporal specification](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name).
    
    `table_name` must not be a foreign table.
    
*   [table\_alias](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-alias)
    
    Define an alias for the table. The alias must not include a column list.
    
*   **[WHERE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-where)**
    
    Filter rows by predicate.
    
    The `WHERE` predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. The following types of subqueries are not supported:
    
    *   Nested subqueries, that is, an subquery inside another subquery
    *   `NOT IN` subquery inside an `OR`, for example, `a = 3 OR b NOT IN (SELECT c from t)`
    
    In most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`. We recommend using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow.
    

### Examples[​](#examples "Direct link to Examples")

SQL

    > DELETE FROM events WHERE date < '2017-01-01'> DELETE FROM all_events   WHERE session_time < (SELECT min(session_time) FROM good_events)> DELETE FROM orders AS t1   WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid)> DELETE FROM events   WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01')

*   [common table expression](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-cte)
*   [COPY](https://docs.databricks.com/aws/en/sql/language-manual/delta-copy-into)
*   [INSERT](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into)
*   [MERGE](https://docs.databricks.com/aws/en/sql/language-manual/delta-merge-into)
*   [PARTITION](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-partition#partition)
*   [query](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-query)
*   [UPDATE](https://docs.databricks.com/aws/en/sql/language-manual/delta-update)
