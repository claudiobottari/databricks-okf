---
title: Common patterns for row filtering and column masking | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns
ingestedAt: "2026-06-18T08:03:19.156Z"
---

This page describes common patterns for implementing ABAC row filter and column mask policies.

*   For overall concepts, see [Core concepts for attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts).
*   For policy syntax, see [Create and manage row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies).
*   For GRANT policies (Beta), see [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).

## Cast-compatible masking functions[​](#cast-compatible-masking-functions "Direct link to cast-compatible-masking-functions")

Databricks automatically casts the masking function output to match the target column's data type. See [Automatic type casting for column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation#type-casting).

The following patterns help you design cast-compatible masking functions.

### Return a castable type[​](#return-a-castable-type "Direct link to Return a castable type")

When masking a column, return the same data type or a type that is castable to it. Check the data types of the columns your policy targets and verify that every branch of the function returns a compatible value.

SQL

    -- Succeeds: Masks a DOUBLE column, returns DOUBLE in every branchCREATE FUNCTION mask_salary(salary DOUBLE, user_role STRING)RETURNS DOUBLERETURN CASE  WHEN user_role IN ('admin', 'hr') THEN salary  WHEN user_role = 'manager' THEN ROUND(salary / 1000) * 1000  ELSE 0.0END;-- Fails: 'CONFIDENTIAL' cannot be cast to a DOUBLE column typeCREATE FUNCTION mask_salary_as_text(salary DOUBLE, user_role STRING)RETURNS STRINGRETURN CASE  WHEN user_role IN ('admin', 'hr') THEN CAST(salary AS STRING)  ELSE 'CONFIDENTIAL'END;

### Avoid numeric overflow[​](#avoid-numeric-overflow "Direct link to Avoid numeric overflow")

When a mask function accepts and returns a wider numeric type than the target column, the result is automatically cast back to the column's type. If the returned value exceeds the range of the narrower type, the cast overflows and the query fails at runtime.

SQL

    -- The target column is TINYINT (max 127). The input is upcast to BIGINT-- for the function. Adding 1000 produces a BIGINT result that overflows-- when cast back to TINYINT.CREATE FUNCTION mask_score(score BIGINT)RETURNS BIGINTRETURN score + 1000;

### Use VARIANT for multiple column types[​](#use-variant-for-multiple-column-types "Direct link to Use VARIANT for multiple column types")

See [VARIANT-based masking functions for multiple column types](#variant-masking).

### Test cast compatibility[​](#test-cast-compatibility "Direct link to Test cast compatibility")

Test masking functions with different data patterns.

SQL

    SELECT CAST(mask_salary(salary, 'admin') AS DOUBLE) FROM employees;SELECT CAST(mask_salary(salary, 'manager') AS DOUBLE) FROM employees;SELECT CAST(mask_salary(salary, 'viewer') AS DOUBLE) FROM employees;

## VARIANT-based masking functions for multiple column types[​](#variant-based-masking-functions-for-multiple-column-types "Direct link to variant-based-masking-functions-for-multiple-column-types")

When you need to mask columns of different data types (for example, `INT`, `DOUBLE`, `DECIMAL(10,2)`, `DECIMAL(15,5)`, and so on), you can write a single masking UDF that accepts and returns a `VARIANT` type. Databricks automatically casts the column mask function output to match the target column's data type following ANSI SQL standards.

This approach reduces the number of UDFs and policies needed. Instead of writing separate masking functions for each column type, one function handles all types.

### Mask multiple numeric types with a single function[​](#mask-multiple-numeric-types-with-a-single-function "Direct link to Mask multiple numeric types with a single function")

Rather than creating a separate mask function for each numeric precision, you can use `VARIANT` to handle them all with a single function:

SQL

    CREATE FUNCTION mask_numeric(val VARIANT)RETURNS VARIANTDETERMINISTICRETURN 0::VARIANT;

This function returns `0` as a `VARIANT`, which Databricks automatically casts to the target column's type. A single ABAC policy using this function can mask `INT`, `DOUBLE`, and `DECIMAL` columns without requiring separate functions for each precision.

If you prefer to preserve the type explicitly within the function, you can branch on the type and return an appropriate masked value for each using [`schema_of_variant()`](https://docs.databricks.com/aws/en/semi-structured/variant#return-the-schema-of-a-variant):

SQL

    -- Use VARIANT to accommodate different data typesCREATE FUNCTION flexible_mask(data VARIANT)RETURNS VARIANTRETURN CASE  WHEN schema_of_variant(data) = 'INT' THEN 0::VARIANT  WHEN schema_of_variant(data) = 'DATE' THEN DATE'1970-01-01'::VARIANT  WHEN schema_of_variant(data) = 'DOUBLE' THEN 0.00::VARIANT  ELSE NULL::VARIANTEND;

### Mask struct columns with VARIANT[​](#mask-struct-columns-with-variant "Direct link to mask-struct-columns-with-variant")

For Databricks Runtime 18.1 and above, you can also mask struct columns by casting them to `VARIANT` within an ABAC policy. Branch on the struct's shape to selectively redact fields:

note

Casting structs to `VARIANT` for masking is supported only within ABAC column mask policies.

The following example uses `schema_of_variant()` to identify two different struct shapes and redact sensitive fields in each:

SQL

    CREATE FUNCTION flexible_mask(data VARIANT)RETURNS VARIANTRETURN CASEWHEN schema_of_variant(data) = 'OBJECT<age: BIGINT, email: STRING>' THEN  to_variant_object(named_struct('age', data:age, 'email', 'redacted'))WHEN schema_of_variant(data) = 'OBJECT<id: BIGINT, ssn: STRING>' THEN  to_variant_object(named_struct('id', data:id, 'ssn', 'xxx-xx-xxxx'))ELSE NULL::VARIANTEND;

## Prevent access until sensitive columns are tagged[​](#prevent-access-until-sensitive-columns-are-tagged "Direct link to prevent-access-until-sensitive-columns-are-tagged")

A common governance pattern is to control access based on whether data has been classified. You can implement this with a default restrictive tag and policies that enforce different levels of protection depending on the classification status.

1.  Apply a tag like `classification : unverified` to all new objects by default, through automation or through tag inheritance by applying the tag at the catalog or schema level, so that any new tables added to the catalog or schema automatically inherit the tag.
2.  Create a row filter policy that blocks access to tables tagged `classification : unverified`.
3.  Create a column mask policy that masks sensitive columns on tables where the `classification : unverified` tag is no longer present.
4.  When a data steward completes classification, they update the tag. The blocking policy no longer matches, and the masking policy takes effect.

SQL

    -- Block access to unverified tables for all non-admin usersCREATE FUNCTION catalog.schema.block_all() RETURNS BOOLEAN  RETURN FALSE;CREATE POLICY block_unverifiedON CATALOG my_catalogROW FILTER catalog.schema.block_allTO `account users` EXCEPT `data_admins`FOR TABLESWHEN has_tag_value('classification', 'unverified');

To protect sensitive data after it has been classified, define a column mask policy that takes effect when the `classification : unverified` tag is no longer present:

SQL

    CREATE FUNCTION catalog.schema.mask_pii(val STRING)RETURNS STRINGRETURN '***';CREATE POLICY mask_reviewed_piiON CATALOG my_catalogCOLUMN MASK catalog.schema.mask_piiTO `account users`EXCEPT `data_admins`FOR TABLESWHEN NOT has_tag_value('classification', 'unverified')MATCH COLUMNS (has_tag_value('pii', 'name') OR has_tag_value('pii', 'address')) AS mON COLUMN m;

## Partial reveal without regex[​](#partial-reveal-without-regex "Direct link to partial-reveal-without-regex")

Reveal part of a sensitive value using string operations instead of regex. Regex-based masking scans the entire value for every row, which is expensive on large text fields (see [Avoid regex masking on large text fields](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#regex-masking)).

SQL

    CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRINGDETERMINISTIC  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));

## Consistent hashing (deterministic pseudonymization)[​](#consistent-hashing-deterministic-pseudonymization "Direct link to consistent-hashing-deterministic-pseudonymization")

Consistent hashing (also called deterministic pseudonymization) replaces sensitive data with a hashed value that is the same across multiple tables. Marking a function as `DETERMINISTIC` tells the engine that the function always returns the same result for the same input, which helps it optimize the query. See [Use deterministic, error-safe expressions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#deterministic-expressions).

The following function consistently hashes a string value, and uses a `version` parameter to support key rotation. Increment the `version` number through the policy's `USING COLUMNS` clause to generate new hashes without breaking historical data that used the previous version. The function concatenates the original value with the version number before hashing, so the same input with the same version always produces the same hash.

SQL

    CREATE FUNCTION pseudonymize(val STRING, version INT) RETURNS STRINGDETERMINISTIC  RETURN SHA2(CONCAT(val, CAST(version AS STRING)), 256);

## Row filtering with column-only predicates[​](#row-filtering-with-column-only-predicates "Direct link to row-filtering-with-column-only-predicates")

Filter rows using simple boolean logic that references only table columns. Column-only predicates enable predicate pushdown, which allows the engine to skip irrelevant data during scans (see [Understand predicate pushdown on protected tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#predicate-pushdown)).

SQL

    CREATE FUNCTION filter_by_region(region STRING, allowed STRING)RETURNS BOOLEANDETERMINISTIC  RETURN array_contains(split(allowed, ','), lower(region));

Use with a policy that passes the allowed regions as a constant:

SQL

    CREATE POLICY regional_accessON CATALOG analyticsROW FILTER filter_by_regionTO 'emea_team'FOR TABLESMATCH COLUMNS has_tag('region') AS rgnUSING COLUMNS (rgn, 'emea,apac');

When a table has multiple columns representing related attributes (for example, `ship_to_country` and `bill_to_country`), you can match them with separate tag conditions and pass both to a single UDF. This avoids creating separate policies for each column. A policy can include up to three column expressions in the `MATCH COLUMNS` clause (see [Policy quotas](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements#policy-quotas)).

SQL

    CREATE FUNCTION filter_by_countries(ship_country STRING, bill_country STRING, allowed STRING)RETURNS BOOLEANDETERMINISTIC  RETURN array_contains(split(allowed, ','), lower(ship_country))      OR array_contains(split(allowed, ','), lower(bill_country));CREATE POLICY regional_ordersON SCHEMA prod.ordersROW FILTER filter_by_countriesTO analystsFOR TABLESWHEN has_tag_value('sensitivity', 'high')MATCH COLUMNS  has_tag('ship_country') AS ship,  has_tag('bill_country') AS billUSING COLUMNS (ship, bill, 'us,ca,mx');

An analyst sees only orders where either the shipping or billing country is in their allowed list.

## Lookup tables in ABAC policy UDFs[​](#lookup-tables-in-abac-policy-udfs "Direct link to lookup-tables-in-abac-policy-udfs")

When access rules vary per user and cannot be expressed through the policy's `TO`/`EXCEPT` clauses alone, you can check access rights against a small lookup table. Use `TO`/`EXCEPT` when possible, as it is the preferred approach for targeting principals (see [Approach for targeting principals](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#targeting-principals)). Keep the lookup table small so the optimizer converts the subquery into a broadcast hash join (see [Keep lookup tables small](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#lookup-tables)).

SQL

    CREATE TABLE access_rules (  principal VARCHAR(255),  priority VARCHAR(64));INSERT INTO access_rules VALUES  ('alice@company.com', '1-URGENT'),  ('alice@company.com', '2-HIGH'),  ('bob@company.com', '1-URGENT');CREATE FUNCTION priority_allowed(o_priority STRING) RETURNS BOOLEANRETURN EXISTS (  SELECT 1 FROM access_rules  WHERE principal = session_user() AND priority = o_priority);CREATE POLICY priority_filterON CATALOG operationsROW FILTER priority_allowedTO `account users`FOR TABLESMATCH COLUMNS has_tag('priority') AS priUSING COLUMNS (pri);
