---
title: DELTA_VERSIONS_NOT_CONTIGUOUS error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-versions-not-contiguous-error-class
ingestedAt: "2026-06-18T08:07:47.303Z"
---

[SQLSTATE: KD00C](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

Versions (`<versionList>`) are not contiguous. A gap in the delta log between versions `<startVersion>` and `<endVersion>` was detected while trying to load version `<versionToLoad>`.

## AWS[​](#aws "Direct link to AWS")

This can happen when files have been manually removed from the Delta log, or due to S3 eventual consistency when a table is deleted and recreated at the same location. Please contact Databricks support to repair the table.

## AZURE[​](#azure "Direct link to AZURE")

This can happen when files have been manually removed from the Delta log. Please contact Databricks support to repair the table.

## GENERIC[​](#generic "Direct link to GENERIC")

This can happen when files have been manually removed from the Delta log.
