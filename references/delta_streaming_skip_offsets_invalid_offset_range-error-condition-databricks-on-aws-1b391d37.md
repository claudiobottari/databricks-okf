---
title: DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-streaming-skip-offsets-invalid-offset-range-error-class
ingestedAt: "2026-06-18T08:07:33.416Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Error messages](https://docs.databricks.com/aws/en/error-messages/)
*   [Error classes in Databricks](https://docs.databricks.com/aws/en/error-messages/error-classes)
*   DELTA\_STREAMING\_SKIP\_OFFSETS\_INVALID\_OFFSET\_RANGE error condition

Last updated on **Jan 19, 2026**

[SQLSTATE: 42616](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

Invalid skip offset range for Delta source range=\[`<startOffset>, <endOffset>`). Fix this offset range and try again.

## EVENT\_TIME\_PRESENT[​](#event_time_present "Direct link to EVENT_TIME_PRESENT")

Offsets cannot have event time (eventTimeMillis must be empty).

## INITIAL\_SNAPSHOT[​](#initial_snapshot "Direct link to INITIAL_SNAPSHOT")

Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).

## INVALID\_INDEX[​](#invalid_index "Direct link to INVALID_INDEX")

Offset index must be `BASE_INDEX (<baseIndex>)`.
