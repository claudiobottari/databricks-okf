---
title: Performance considerations for row filter and column mask policies | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance
ingestedAt: "2026-06-18T08:03:29.911Z"
---

note

These considerations apply to row filter and column mask policies, which execute UDFs at query time. GRANT policies (Beta) are not subject to them. See [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).

Row filter and column mask policies introduce logic that runs at query time, so performance depends on how you design your policies. There's no single right approach for every workload. The best approach depends on your data volume, query patterns, how your users interact with protected tables, and your desired masking or filtering behavior. The following sections cover the most common performance considerations. Use them as a checklist when designing your policies, and [test with representative queries](#test-performance) before deploying to production.

## Performance overview[​](#performance-overview "Direct link to performance-overview")

## Reduce UDF complexity[​](#reduce-udf-complexity "Direct link to reduce-udf-complexity")

The UDF in an ABAC policy executes for every row (row filters) or every matching column value (column masks) during query execution. The complexity of the UDF directly affects query performance.

**Do:**

*   Keep UDFs simple. Favor basic `CASE` statements and simple boolean expressions.
*   Reference only target table columns in UDFs as much as possible. This enables [predicate pushdown](#predicate-pushdown).
*   If your UDF must reference external tables, keep any external reference small enough to broadcast. Ensure that referenced tables are optimized and partitioned to match the policy's access pattern. For example, partition a policy lookup table by username.
*   Avoid multi-level nesting and unnecessary function calls. Use built-in SQL functions as much as possible.

**Avoid:**

*   External API calls or lookups to other databases in UDFs. Network calls can introduce additional latency and timeouts.
*   Complex subqueries or joins against large tables. These prevent broadcast hash joins and force nested loop joins.
*   Heavy regex on large text fields. See [Regex on large text fields](#regex-masking).
*   Per-row metadata lookups, for example querying `information_schema`.

## Approach for targeting principals[​](#approach-for-targeting-principals "Direct link to approach-for-targeting-principals")

When you write an ABAC policy, you decide where to implement principal-based logic: in the policy's `TO`/`EXCEPT` clauses, or inside the UDF using identity functions like `current_user()` and `is_account_group_member()`.

In general, use the policy's `TO`/`EXCEPT` clauses to define which principals a policy applies to. This keeps the policy definition simpler and the UDF focused on data transformation, filtering, or masking. The `EXCEPT` clause eliminates the policy entirely for exempt users, which means no UDF execution for those users.

When the conditional logic is too complex for the policy's principal clauses, identity functions inside the UDF are a possible alternative. These functions are resolved once during query analysis, not per row. Multiple calls to identity functions like `is_account_group_member()` with different group arguments result in a single UC API call, so the performance impact is typically minimal.

The following UDF is efficient because it relies only on identity functions, which are resolved once during query analysis:

SQL

    CREATE OR REPLACE FUNCTION rowfilter()RETURNS BOOLEANRETURN  CASE    WHEN is_account_group_member('auditors') OR is_account_group_member('external-auditors') THEN true    WHEN is_account_group_member('low-privileged') THEN false    WHEN session_user() = 'admin@organization.com' THEN true    ELSE false  END;

In contrast, the following UDF is slower because it encodes privileges in a secondary table, which requires an additional table lookup:

SQL

    CREATE OR REPLACE FUNCTION rowfilter()RETURNS BOOLEANRETURN  CASE WHEN EXISTS(SELECT 1 FROM access_lease WHERE user = session_user()) THEN true  ELSE false END;

## Use deterministic, error-safe expressions[​](#use-deterministic-error-safe-expressions "Direct link to use-deterministic-error-safe-expressions")

Use deterministic expressions that cannot throw errors in policy UDFs and in queries against protected tables.

Non-deterministic functions (functions that return different results for the same input, such as `rand()` or `now()`) prevent the optimizer from caching results or applying constant folding. Both SQL and Python UDFs support the [`DETERMINISTIC`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-sql-function) keyword in the `CREATE FUNCTION` statement. For SQL UDFs, the optimizer derives determinism from the function body automatically, but you can also set it explicitly. For Python UDFs, the optimizer can't inspect the function body, so explicitly marking a Python UDF as deterministic is important to enable result caching for calls with identical arguments.

Some expressions throw errors if the inputs aren't valid, such as ANSI division on a zero denominator. When the SQL compiler detects this possibility, it can't push operations like filters down in the query plan. Doing so could trigger errors that reveal information about values before filtering or masking takes effect. Use error-safe alternatives like `try_divide` instead of `/`, `try_cast` instead of `CAST`, and `try_to_number` instead of `to_number`. These return `NULL` on failure instead of throwing, which lets the optimizer rearrange and fold expressions freely.

## Avoid Python UDFs[​](#avoid-python-udfs "Direct link to avoid-python-udfs")

Avoid Python UDFs in ABAC policies whenever possible. Python UDFs must be [wrapped in a SQL UDF](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply#wrapper-example) to be used in policies. They are also generally slower than SQL UDFs because the optimizer cannot inline or optimize them, and the Python function executes for every row in the target table.

If a Python UDF is unavoidable, see [Deterministic, error-safe expressions](#deterministic-expressions) for how to mark it as `DETERMINISTIC` to enable result caching.

## Keep lookup tables small[​](#keep-lookup-tables-small "Direct link to keep-lookup-tables-small")

A common pattern is to check access rights against a small lookup table (for example, a table that maps users to allowed priority levels). If the lookup table is significantly smaller than the target table, the optimizer converts the subquery into a broadcast hash join. The lookup table is copied to each executor and stored in memory as a hashmap, which enables fast filtering during the table scan. For a code example, see [Lookup tables in ABAC policy UDFs](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns#lookup-tables).

*   If the lookup table is large, the optimizer falls back to a shuffle join, which is slower.
*   If the lookup predicate is complex (not a simple equality check), broadcast join may also become ineligible.
*   Even with broadcast hash join, each row still incurs the cost of a hash table lookup during execution.

## Understand predicate pushdown on protected tables[​](#understand-predicate-pushdown-on-protected-tables "Direct link to understand-predicate-pushdown-on-protected-tables")

Predicate pushdown is a performance optimization where the engine pushes your filter conditions to the storage layer. This allows the engine to skip entire partitions of data that don't match your query, significantly reducing I/O and speeding up execution.

For tables protected by row filters and column masks, this optimization is more complex. This is the most common source of performance issues with protected tables, and the most difficult to address, because policy authors can't control what queries users run against protected tables.

### How the `SecureView` barrier affects predicate pushdown[​](#how-the-secureview-barrier-affects-predicate-pushdown "Direct link to how-the-secureview-barrier-affects-predicate-pushdown")

Both ABAC and [table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply) use a `SecureView` barrier to prevent predicates with side effects from being pushed across the policy boundary. This protects against side-channel data leakage, but it can also block partition pruning and liquid clustering optimizations, which can force full table scans. This applies even when the policy UDF resolves to a constant `true` (meaning no rows are actually filtered). The presence of a policy on a table introduces the `SecureView` barrier.

### Filters affected by the barrier[​](#filters-affected-by-the-barrier "Direct link to Filters affected by the barrier")

Generally, the optimizer can push only side-effect-free predicates through the `SecureView` barrier.

*   **Pushed down (fast)**: Simple equality comparisons (`WHERE col = 'value'`) and basic range comparisons (`WHERE col > 100`). These are free of side effects and do not risk leaking data.
*   **Blocked (slower)**: Predicates that call functions (`WHERE date_format(col, 'yyyy-MM-dd') = '1995-07-29'`) or introduce implicit type casts. These are kept above the `SecureView` barrier, meaning the engine must scan the table before applying the filter.

The following example shows the difference. Consider a table with a partition key on `o_orderdate` and a query that filters using `date_format`:

SQL

    EXPLAIN SELECT * FROM ordersWHERE date_format(o_orderdate, 'yyyy-MM-dd') = '1995-07-29'

Without a policy, the `date_format` predicate appears in `PartitionFilters` inside the `PhotonScan` node, which means partition pruning is active:

    +- PhotonScan parquet orders[...]   PartitionFilters: [isnotnull(o_orderdate),   (date_format(cast(o_orderdate as timestamp), yyyy-MM-dd, ...))]

With a policy (even one that always returns `true`), the `SecureView` barrier blocks the predicate. It moves to a `PhotonFilter` above the scan instead of staying in `PartitionFilters`, which results in a full table scan:

    +- PhotonFilter (date_format(cast(o_orderdate as timestamp),   yyyy-MM-dd, ...) = 1995-07-29)    +- PhotonSecureView orders        +- PhotonScan parquet orders[...]           PartitionFilters: [isnotnull(o_orderdate)]

A simpler predicate like `WHERE o_orderdate = '1995-07-29'` has no side effects and can still be pushed down even with the `SecureView` barrier in place:

    +- PhotonSecureView orders    +- PhotonScan parquet orders[...]       PartitionFilters: [isnotnull(o_orderdate),       (o_orderdate = 1995-07-29)]

Use simple equality predicates on protected tables when possible. For exempt users, use the `EXCEPT` clause in the policy to eliminate the `SecureView` barrier entirely, which restores full predicate pushdown.

## Reuse column masks where possible[​](#reuse-column-masks-where-possible "Direct link to reuse-column-masks-where-possible")

Applying many distinct column masks to a single table compounds the per-column cost. Mask only columns that contain truly sensitive data.

When multiple columns require the same transformation (for example, redacting to `NULL` or replacing with a fixed string), reuse the same masking function rather than creating a separate function per column.

Databricks recognizes policies that reference the same UDF with the same arguments as the same effective mask, so reusing functions avoids unnecessary overhead.

## Avoid regex masking on large text fields[​](#avoid-regex-masking-on-large-text-fields "Direct link to avoid-regex-masking-on-large-text-fields")

Using `regexp_replace` inside a column mask to redact elements within a serialized document (XML or JSON stored as a STRING column) is expensive. `regexp_replace` walks the full string for every row. The optimizer treats the STRING column as an opaque value and can't prune unused portions of the document. The engine reads and rewrites the entire payload even when the query only needs a few fields.

SQL

    -- Expensive: regex masking on serialized XMLCREATE FUNCTION mask_xml_pii(raw_xml STRING)RETURNS STRINGRETURN CASE  WHEN is_account_group_member('sensitive_data_viewers') THEN raw_xml  ELSE regexp_replace(raw_xml, '<SSN>[^<]*</SSN>', '<SSN>***</SSN>')END;

Instead, materialize the sensitive fields into typed columns in a separate table, then apply column masks to those scalar columns. The mask function then operates on a single small value per row rather than the entire serialized document.

SQL

    -- Source table stores raw XML as STRING-- Example XML: <person><SSN>123-45-6789</SSN><name>Alice</name><dob>1990-01-01</dob></person>-- Recommended: extract fields into a table, then mask scalar valuesCREATE TABLE person_data ASSELECT  id,  xpath_string(raw_xml, 'person/SSN') AS ssn,  xpath_string(raw_xml, 'person/name') AS name,  xpath_string(raw_xml, 'person/dob') AS date_of_birth,  raw_xmlFROM raw_records;-- Simple scalar mask, applied to each extracted columnCREATE FUNCTION redact(val STRING) RETURNS STRINGRETURN CASE  WHEN is_account_group_member('sensitive_data_viewers') THEN val  ELSE '***'END;

If you can store the data as a struct column instead of XML, use the VARIANT flexible masking pattern to redact individual fields within the struct. See [Mask struct columns with VARIANT](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns#struct-masking).

## Test UDF performance[​](#test-udf-performance "Direct link to test-udf-performance")

### Test at scale[​](#test-at-scale "Direct link to Test at scale")

Test UDF performance on at least 1 million rows before deploying to production. In addition to synthetic scale tests, run queries that represent the actual workload you expect on the protected table. Make incremental changes to your policy functions and measure the effect of each change rather than testing only the final version.

SQL

    WITH test_data AS (  SELECT    id,    your_mask_function(id) AS masked_id,    current_timestamp() AS ts  FROM (    SELECT CONCAT('ID', LPAD(CAST(id AS STRING), 6, '0')) AS id    FROM range(1000000)  ))SELECT  COUNT(*) AS rows_processed,  MAX(ts) - MIN(ts) AS total_durationFROM test_data;

Replace `your_mask_function` with the UDF you're testing. Compare results with and without the policy applied to isolate the policy's overhead.
