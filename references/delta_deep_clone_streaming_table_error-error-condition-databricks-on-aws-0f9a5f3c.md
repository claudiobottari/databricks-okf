---
title: DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-deep-clone-streaming-table-error-error-class
ingestedAt: "2026-06-18T08:07:17.366Z"
---

[SQLSTATE: 0A000](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

Deep clone of streaming table failed:

## LOCATION\_NOT\_SUPPORTED[​](#location_not_supported "Direct link to LOCATION_NOT_SUPPORTED")

Specifying a `LOCATION` is not supported. The cloned streaming table uses managed storage.

## OLD\_ARCHITECTURE\_NOT\_SUPPORTED[​](#old_architecture_not_supported "Direct link to OLD_ARCHITECTURE_NOT_SUPPORTED")

Only streaming tables using the default publishing mode are supported.

## REQUIRES\_WITH\_HISTORY[​](#requires_with_history "Direct link to REQUIRES_WITH_HISTORY")

`WITH HISTORY` is required. Use `CREATE TABLE` ... DEEP `CLONE` `...` `WITH HISTORY`.

## SCHEDULED\_TABLE\_NOT\_SUPPORTED[​](#scheduled_table_not_supported "Direct link to SCHEDULED_TABLE_NOT_SUPPORTED")

Scheduled streaming tables are not supported for deep clone.

## TIME\_TRAVEL\_NOT\_SUPPORTED[​](#time_travel_not_supported "Direct link to TIME_TRAVEL_NOT_SUPPORTED")

Time travel is not supported for streaming table deep clone.
