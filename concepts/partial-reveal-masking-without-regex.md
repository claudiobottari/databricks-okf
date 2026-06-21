---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2aa6c537eeb5f0bc2bab1088efc5792d8203ab3796ef25eb3cc1eff85f58fcf9
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partial-reveal-masking-without-regex
    - PRMWR
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Partial reveal masking without regex
description: Revealing parts of sensitive values using string operations like RIGHT and CONCAT instead of expensive regex-based masking, improving performance on large text fields.
tags:
  - abac
  - column-masking
  - performance
  - string-operations
timestamp: "2026-06-19T14:18:15.420Z"
---

---
title: Partial reveal masking without regex
summary: Revealing part of a sensitive value using string operations (e.g., RIGHT, CONCAT) instead of regex-based masking to avoid expensive scans on large text fields.
sources:
  - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:40:14.050Z"
updatedAt: "2026-06-18T14:40:14.050Z"
tags:
  - abac
  - column-masking
  - performance
  - unity-catalog
aliases:
  - partial-reveal-masking-without-regex
  - PRMWR
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Partial Reveal Masking Without Regex

**Partial reveal masking without regex** refers to a technique for data masking that reveals only part of a sensitive value using string functions rather than regular expressions. This approach avoids the performance costs associated with regex-based masking on large text fields.

## Overview

When masking sensitive data like social security numbers, phone numbers, or credit card numbers, it is often desirable to reveal only the last few characters while hiding the rest. The recommended approach for this pattern uses simple string operations such as `CONCAT()` and `RIGHT()` instead of regular expressions. This is because regex-based masking scans the entire value for every row, which is expensive on large text fields. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example Implementation

The following SQL function demonstrates how to implement partial reveal masking without regex. The function accepts the sensitive value and a parameter controlling how many characters to reveal at the end:

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
DETERMINISTIC
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

This function:
- Takes an SSN (or any string) as input
- Accepts a `show_last` parameter to control how many trailing characters to reveal
- Uses `CONCAT()` to join a masked prefix with the revealed portion
- Uses `RIGHT()` to extract the specified number of characters from the end of the string

## Benefits

Using string operations instead of regex provides several advantages:

- **Better performance**: String functions like `RIGHT()` and `CONCAT()` process only the relevant portion of the value rather than scanning the entire string for pattern matching
- **Deterministic behavior**: Marking the function as `DETERMINISTIC` allows the query engine to optimize execution, as it indicates the function always returns the same result for the same input
- **Simplicity**: The logic is straightforward and easy to maintain compared to complex regex patterns

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — The policy framework that uses UDFs for dynamic data masking
- Deterministic Functions in ABAC — Best practices for marking functions as DETERMINISTIC for performance optimization
- [Regex Masking Performance](/concepts/regex-masking-performance-on-large-text-fields.md) — Understanding the performance implications of regex-based masking
- [Consistent Hashing for Pseudonymization](/concepts/consistent-hashing-for-deterministic-pseudonymization.md) — An alternative masking technique using hashing

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
