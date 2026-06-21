---
title: DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-table-changes-view-unsupported-error-class
ingestedAt: "2026-06-18T08:07:35.317Z"
---

[SQLSTATE: 0AKDC](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

table\_changes on view '`<viewName>`' is not supported.

## MULTIPLE\_RELATIONS[​](#multiple_relations "Direct link to MULTIPLE_RELATIONS")

The view references more than one relation.

## NON\_DETERMINISTIC\_EXPRESSIONS[​](#non_deterministic_expressions "Direct link to NON_DETERMINISTIC_EXPRESSIONS")

The view contains non-deterministic expressions.

## NOT\_DELTA\_TABLE[​](#not_delta_table "Direct link to NOT_DELTA_TABLE")

The view does not reference a Delta table.

## NOT\_SHARED\_VIEW[​](#not_shared_view "Direct link to NOT_SHARED_VIEW")

The view is not a OpenSharing view.

## SUBQUERY[​](#subquery "Direct link to SUBQUERY")

The view contains a subquery.

## UNSUPPORTED\_OPERATOR[​](#unsupported_operator "Direct link to UNSUPPORTED_OPERATOR")

The view contains an operator that is not allowed.
