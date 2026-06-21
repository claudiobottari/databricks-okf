---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae4105416e2f0dabab7f22f261c46a3bfabbd53fdd251b783f82efe1a5b86c98
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - sqlstate-0akdc
    - SQLSTATE 0A
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: SQLSTATE 0AKDC
description: The SQLSTATE code associated with the DELTA_CLONE_INCOMPATIBLE_SOURCE error, categorized under class 0A (Feature Not Supported).
tags:
  - databricks
  - sqlstate
  - error-handling
timestamp: "2026-06-19T18:22:31.636Z"
---

# SQLSTATE 0AKDC

**SQLSTATE 0AKDC** is a custom SQL state code used in Databricks to indicate that a requested operation is not supported because it relies on a feature that is not available. It belongs to the SQLSTATE class `0A` (Feature Not Supported) and is assigned to multiple [Delta Clone](/concepts/delta-clone.md) error conditions. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md, delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md, delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Classes Using SQLSTATE 0AKDC

Three error classes in Databricks use this SQL state code:

- DELTA_CLONE_INCOMPATIBLE_SOURCE – Raised when the clone source has a valid format but uses an unsupported feature with Delta. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE – Raised when attempting to clone a table with history from an unsupported source. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET – Raised

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
2. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
3. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
