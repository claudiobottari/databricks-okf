---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a487e2a9020785d6a856f221a6c46af7e03f1eea9e759a3adb16681561cb2c8
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partial-reveal-without-regex
    - PRWR
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Partial reveal without regex
description: A performance-optimized pattern for revealing part of a sensitive value (e.g. last digits of an SSN) using simple string functions like RIGHT and CONCAT instead of expensive regex-based masking on large text fields.
tags:
  - data-governance
  - column-masking
  - performance
  - abac
timestamp: "2026-06-19T17:47:20.519Z"
---

# Partial reveal without regex

**Partial reveal without regex** is a column masking pattern that reveals only a portion of a sensitive value using simple string operations instead of regular expressions. This approach is preferred over regex-based masking for performance reasons, particularly when dealing with large text fields. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Performance benefits

Regex-based masking scans the entire value for every row, which can be expensive on large text fields. By using string operations instead, the mask function avoids the overhead of regex compilation and pattern matching, resulting in faster query execution. For more information on performance implications, see ABAC Performance Considerations. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Implementation

The pattern uses SQL string functions — specifically `CONCAT` and `RIGHT` — to construct a partially obscured value while revealing a configurable number of characters from the end of the string. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Example: Social Security Number masking

The following function masks a Social Security Number (SSN) by replacing the first eight characters with asterisks, then appending the last N digits as specified by the `show_last` parameter: ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
DETERMINISTIC
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));
```

Marking the function as `DETERMINISTIC` tells the engine that the function always returns the same result for the same input, which helps it optimize the query. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Usage with column mask policies

The function can be used in an ABAC column mask policy. The `show_last` parameter can be passed as a constant through the policy definition, allowing different policies to reveal different amounts of the sensitive value without creating separate functions: ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
-- Reveal last 4 digits for general users
CREATE POLICY mask_ssn_last4
ON SCHEMA hr.employees
COLUMN MASK mask_ssn
TO `analysts`
FOR TABLES
WHEN has_tag_value('sensitivity', 'high')
MATCH COLUMNS has_tag('ssn') AS s
USING COLUMNS (s, 4);

-- Reveal last 2 digits for less privileged users
CREATE POLICY mask_ssn_last2
ON SCHEMA hr.employees
COLUMN MASK mask_ssn
TO `interns`
FOR TABLES
WHEN has_tag_value('sensitivity', 'high')
MATCH COLUMNS has_tag('ssn') AS s
USING COLUMNS (s, 2);
```

## When to use

This pattern is appropriate when:

- You need to reveal a fixed number of characters from the beginning or end of a value.
- The sensitive data is consistently formatted (e.g., all values have the same length).
- Performance is a concern on large text columns.

For more complex partial reveal requirements (such as revealing different portions based on value length or content), consider whether regex is truly necessary or whether a combination of string functions can achieve the same result.

## Related concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) — ABAC policies that mask sensitive columns
- ABAC Performance Considerations — Performance implications of ABAC policy design
- Common patterns for row filtering and column masking — Additional ABAC policy patterns
- [Consistent hashing (deterministic pseudonymization)](/concepts/consistent-hashing-deterministic-pseudonymization.md) — Alternative approach for masking sensitive data

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
