---
title: DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-uniform-refresh-not-supported-error-class
ingestedAt: "2026-06-18T08:07:44.170Z"
---

[SQLSTATE: 0AKDC](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

`REFRESH` identifier `SYNC UNIFORM` is not supported for reason:

## COLUMN\_MASK[​](#column_mask "Direct link to COLUMN_MASK")

Column mask is not supported by `REFRESH` identifier `SYNC UNIFORM`.

## COMPATIBILITY\_NOT\_ENABLED[​](#compatibility_not_enabled "Direct link to COMPATIBILITY_NOT_ENABLED")

`REFRESH` identifier `SYNC UNIFORM` requires compatibility to be included in delta.universalFormat.enabledFormats.

## ROW\_LEVEL\_SECURITY[​](#row_level_security "Direct link to ROW_LEVEL_SECURITY")

Row level security is not supported by `REFRESH` identifier `SYNC UNIFORM`.

## UNSUPPORTED\_READER\_FEATURES[​](#unsupported_reader_features "Direct link to UNSUPPORTED_READER_FEATURES")

The reader table feature(s) `<readerFeatures>` are not supported by `REFRESH` identifier `SYNC UNIFORM`.

## UNSUPPORTED\_TYPE[​](#unsupported_type "Direct link to UNSUPPORTED_TYPE")

`<sourceType>` is not supported by `REFRESH` identifier `SYNC UNIFORM`.

## WRONG\_TYPE[​](#wrong_type "Direct link to WRONG_TYPE")

`REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`.
