---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fbec479e155f52ede6daf96267f894cbaaaad3f01ca36d237496179fa368122
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-control-separation-for-pii-containing-tables
    - ACSFPT
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: Access Control Separation for PII-Containing Tables
description: A security pattern in Unity Catalog where raw tables containing unredacted PII have tightly restricted access (only pipeline service principals and administrators), while redacted tables are broadly available for analytics, dashboards, and observability.
tags:
  - data-governance
  - security
  - unity-catalog
  - compliance
timestamp: "2026-06-19T20:12:53.928Z"
---

Here is the wiki page for "Access Control Separation for PII-Containing Tables", written based solely on the provided source material.

---

# Access Control Separation for PII-Containing Tables

**Access Control Separation for PII-Containing Tables** is a data governance pattern that restricts access to raw, unredacted tables containing Personally Identifiable Information (PII) while granting broader access to a separate set of redacted tables. This approach helps organizations comply with data protection regulations and privacy standards by limiting who can view sensitive data.

## Pattern Overview

Sharing OpenTelemetry (OTel) trace data broadly for debugging or observability can create compliance and privacy risks when the data contains PII such as email addresses, phone numbers, and credit card numbers embedded in span attributes, log bodies, and resource metadata. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

A common solution involves incrementally reading new OTel spans from a raw source table, applying a redaction function to mask PII, and writing the results to a separate set of redacted tables. The raw tables retain the unredacted data for authorized users, while the redacted tables are safe for broader consumption. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Implementation on Databricks

On Databricks, this access control separation can be implemented using [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) and [AI Functions](/concepts/ai-functions.md). A pipeline incrementally reads new OTel spans from a raw source table, applies the `ai_mask` function to redact PII from span attributes, log bodies, and resource attributes, and writes the redacted results to a separate target schema. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Raw Data Retention

A configurable retention job handles cleanup of the raw data. The deployment configures auto time-to-live (TTL) on the raw OTel tables to automatically delete trace data older than a configurable number of days (default: 90). This helps organizations comply with General Data Protection Regulation (GDPR) and other data protection regulations that require personal data to be deleted after it is no longer needed for its original purpose. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Access Control

The raw OTel tables contain unredacted PII and should have restricted access. Grant access to the raw source schema only to pipeline service principals and administrators who need it for debugging or incident response. All routine analytics, dashboards, and observability workflows should query the redacted tables instead. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

For more information about Unity Catalog privileges, see Manage privileges in Unity Catalog.

## Related Concepts

- Data Governance – The overall framework for managing data availability, usability, and security.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks' data governance solution for managing permissions and access.
- [AI Functions](/concepts/ai-functions.md) – SQL functions for applying AI-driven operations like text masking.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – The pipeline framework used to orchestrate the redaction process.
- [Store OpenTelemetry Traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) – How OTel trace data is stored before redaction.
- ai_mask Function – The specific AI-backed function used for PII redaction.

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
