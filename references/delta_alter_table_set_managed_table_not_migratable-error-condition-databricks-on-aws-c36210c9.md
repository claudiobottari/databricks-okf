---
title: DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-alter-table-set-managed-table-not-migratable-error-class
ingestedAt: "2026-06-18T08:07:01.191Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Error messages](https://docs.databricks.com/aws/en/error-messages/)
*   [Error classes in Databricks](https://docs.databricks.com/aws/en/error-messages/error-classes)
*   DELTA\_ALTER\_TABLE\_SET\_MANAGED\_TABLE\_NOT\_MIGRATABLE error condition

Last updated on **Jan 19, 2026**

[SQLSTATE: 55019](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-55-object-not-in-prerequisite-state)

`ALTER TABLE <table> SET MANAGED` is unable to migrate the given table. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support.

## METADATA\_CLEANUP\_ERROR[​](#metadata_cleanup_error "Direct link to METADATA_CLEANUP_ERROR")

Unable to create checkpoint or clean up old metadata files before migrating the table.

\== Error ==

`<error>`
