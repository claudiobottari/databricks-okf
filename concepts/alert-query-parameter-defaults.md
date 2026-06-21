---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d8248907b25269cd07212f03d7a75cbe74cf1a391f66bb8152af941b49f3fb5
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-query-parameter-defaults
    - AQPD
  citations:
    - file: profile-alerts-databricks-on-aws.md
title: Alert Query Parameter Defaults
description: The behavior where profile alerts use default parameter values when the underlying query includes parameters, requiring confirmation that defaults reflect alert intent.
tags:
  - databricks
  - sql
  - alerting
  - queries
timestamp: "2026-06-19T19:58:18.194Z"
---

# Alert Query Parameter Defaults

**Alert Query Parameter Defaults** are the predefined parameter values that a [Databricks SQL Alert](/concepts/databricks-sql-alerts.md) uses when evaluating a [Profile Alert](/concepts/profile-alerts.md) query. This concept is critical for ensuring that alerts built on [Profile Metrics Table](/concepts/profile-metrics-table.md) or [Drift Metrics Table](/concepts/drift-metrics-table.md) queries behave as intended, because the alert always evaluates the query using the parameter values that were saved as defaults at the time the alert was created. ^[profile-alerts-databricks-on-aws.md]

---

## How Defaults Affect Alert Behavior

When a user creates a [Databricks SQL Alert](/concepts/databricks-sql-alerts.md) from a query that contains parameters (e.g., date range filters, table references, or threshold values), the alert-system stores those parameters' **default values** alongside the alert definition. Every time the alert runs its scheduled evaluation or is triggered manually, it substitutes the default values—not the values the creator had in mind when they last edited the query, and not a live "current" value. ^[profile-alerts-databricks-on-aws.md]

This behavior means that if the default values no longer reflect the original intent of the alert (for example, if the parameter was intended to be "last 7 days" but the default was saved as "last 30 days"), the alert may produce unexpected results or fail to trigger when it should. To avoid this, **you should confirm that the default values reflect the intent of the alert** before finalizing the alert creation. ^[profile-alerts-databricks-on-aws.md]

---

## Where Parameter Defaults Are Defined

Parameter defaults are set at the **query** level, inside the SQL editor that builds the query used by the alert. Each parameter in the query has a field for a default value. When the query is saved and then used as the basis for a [Databricks SQL Alert](/concepts/databricks-sql-alerts.md), the alert inherits those defaults. If you later change a parameter's default in the query (without re‑saving the alert), the existing alert continues to use the old default until you explicitly update the alert or recreate it. ^[profile-alerts-databricks-on-aws.md]

---

## Common Pitfall: Drift Metrics Time Windows

A common scenario where parameter defaults matter is in [Drift Metrics Table](/concepts/drift-metrics-table.md) queries that filter on a `window_end_time` or similar time‑based column. If the default for such a parameter is a static date (e.g. `'2024-01-01'`), the alert will always compare against that fixed date, ignoring the dynamic "30‑day lookback" or "last refresh" semantics that the user may have intended. The [30-Day Lookback Window](/concepts/30-day-lookback-window.md) limitation of profile metrics tables compounds this: the first window may be partial, but the alert's parameter default will still be the saved static value. ^[profile-alerts-databricks-on-aws.md]

---

## Best Practices for Setting Defaults

| Practice | Reason |
|---|---|
| **Use dynamic defaults** (e.g. `CURRENT_DATE - 30`) | Makes the alert respond to the most recent data without manual updates. |
| **Test the query with the default** | Run the query in the SQL editor as-is to see what the alert will evaluate. |
| **Review defaults when cloning** | When duplicating an alert, check that the cloned alert's parameter defaults match the new context. |
| **Document the intent** | Add a comment in the query or the alert description explaining what the default represents. |

^[profile-alerts-databricks-on-aws.md]

---

## Related Concepts

- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – The alert system that evaluates queries on a schedule
- [Profile Alerts](/concepts/profile-alerts.md) – Alerts specifically built on profile metrics tables
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics per column, time window, and slice
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics measuring distribution changes over time
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – A time‑boundary constraint that can affect the first window's completeness
- Query Parameters in Databricks SQL – General mechanism for parameterizing SQL queries

---

## Sources

- profile-alerts-databricks-on-aws.md

# Citations

1. [profile-alerts-databricks-on-aws.md](/references/profile-alerts-databricks-on-aws-08d2e777.md)
