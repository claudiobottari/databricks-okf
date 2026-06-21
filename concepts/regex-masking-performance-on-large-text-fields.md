---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33c44d29f04466221605c325e6abd0a65206229caf293e09b8ed35b9d9c30329
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regex-masking-performance-on-large-text-fields
    - RMPOLTF
    - Regex Masking Performance
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Regex masking performance on large text fields
description: Using regexp_replace inside column masks on serialized documents (XML/JSON stored as STRING) is expensive because it walks the full string per row; the recommended alternative is to materialize sensitive fields as typed scalar columns and mask those individually.
tags:
  - performance
  - regex-masking
  - column-masks
  - data-modeling
timestamp: "2026-06-19T19:54:45.915Z"
---

# Regex masking performance on large text fields

Using `regexp_replace` inside a column mask to redact elements within a serialized document (such as XML or JSON stored as a `STRING` column) is expensive. `regexp_replace` walks the full string for every row, and the optimizer treats the `STRING` column as an opaque value—it cannot prune unused portions of the document. As a result, the engine reads and rewrites the entire payload even when the query only needs a few fields. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Recommended alternative

Instead of applying a regex mask on a large text column, materialize the sensitive fields into typed columns in a separate table, then apply column masks to those scalar columns. The mask function then operates on a single small value per row rather than the entire serialized document. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

The following example shows an expensive approach and the recommended alternative.

### Expensive: regex masking on a raw XML column

```sql
CREATE FUNCTION mask_xml_pii(raw_xml STRING)
  RETURNS STRING
  RETURN
    CASE
      WHEN is_account_group_member('sensitive_data_viewers') THEN raw_xml
      ELSE regexp_replace(raw_xml, '<SSN>[^<]*</SSN>', '<SSN>***</SSN>')
    END;
```

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Recommended: extract fields and mask scalar values

```sql
-- Source table stores raw XML as STRING
-- Example XML: <person><SSN>123-45-6789</SSN><name>Alice</name><dob>1990-01-01</dob></person>

-- Extract fields into a table, then mask scalar values
CREATE TABLE person_data AS
SELECT
  id,
  xpath_string(raw_xml, 'person/SSN') AS ssn,
  xpath_string(raw_xml, 'person/name') AS name,
  xpath_string(raw_xml, 'person/dob') AS date_of_birth,
  raw_xml
FROM raw_records;

-- Simple scalar mask, applied to each extracted column
CREATE FUNCTION redact(val STRING)
  RETURNS STRING
  RETURN
    CASE
      WHEN is_account_group_member('sensitive_data_viewers') THEN val
      ELSE '***'
    END;
```

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Additional options

If you can store the data as a struct column instead of XML, use the VARIANT flexible masking pattern to redact individual fields within the struct. This avoids the overhead of full-string processing. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related concepts

- [Column mask](/concepts/column-mask-policies.md) – General mechanism for applying transformations at query time.
- [Row filter](/concepts/row-filter-policies.md) – Filtering logic that also executes a UDF per row.
- UDF performance considerations – Guidelines for keeping policy UDFs efficient.
- Predicate pushdown – Optimization that can be blocked by the `SecureView` barrier on protected tables.
- SecureView barrier – Security boundary that may prevent partition pruning and other optimizations.
- Deterministic UDFs – Marking UDFs as deterministic enables result caching.

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
