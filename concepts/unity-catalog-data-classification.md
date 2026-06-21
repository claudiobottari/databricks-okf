---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5285d6a5479cdda58675b721aaefbe5a4d7a85a59f22d33f65e77bf0f0371dd
  pageDirectory: concepts
  sources:
    - secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-data-classification
    - UCDC
    - System tables for data classification
  citations:
    - file: secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
title: Unity Catalog Data Classification
description: A Databricks feature that scans tables in the background and automatically applies system governed tags (class.*) to detected sensitive columns such as PII, financial data, and contact information.
tags:
  - data-governance
  - unity-catalog
  - data-classification
timestamp: "2026-06-19T20:20:17.041Z"
---

# Unity Catalog Data Classification

**Unity Catalog Data Classification** is a governed data discovery feature on Databricks that automatically scans tables in a Unity Catalog schema, detects columns containing sensitive information (such as personally identifiable information – PII), and applies system-defined `class.*` governed tags to those columns. These tags can then be used with attribute‑based access control (ABAC) policies, such as column‑level masking, to restrict access to sensitive data. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## How It Works

Data Classification operates as a background scan on selected tables. When enabled on a catalog, it inspects the column values and metadata to identify patterns that match sensitive data types. For each detected match, the system applies a `class.*` governed tag to the column. The available tags include, but are not limited to:

- `class.name`
- `class.email_address`
- `class.us_ssn`
- `class.phone_number`
- `class.credit_card`
- `class.date_of_birth`

These tags are governed system tags; no custom tag creation is required for column‑level detection. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

Scans run in the background and populate results within 24 hours of enabling the feature. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Enabling Data Classification

To enable Data Classification for a catalog:

1. In Catalog Explorer, select the target catalog and go to the **Details** tab.
2. Next to **Data Classification**, click **Enable**.
3. Optionally choose which schemas to include in the scan.

After enabling, the system begins scanning tables in the selected schemas. The initial scan typically completes within 24 hours. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Viewing Classification Results

Once a scan completes, you can review the detected sensitive columns:

1. In Catalog Explorer, select the catalog and go to the **Details** tab.
2. Next to **Data Classification**, click **View results**.

The results page shows each detected column, the type of data it was classified as, and an option to **Exclude** incorrect detections. This feedback loop helps reduce false positives over time. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Enabling Automatic Tagging

Auto tagging is a separate step that, when enabled, automatically applies the `class.*` tags to both existing and future detections. You enable it from the same Data Classification results page. Tags are applied in the next background scan (within 24 hours). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

Once auto tagging is on, columns are automatically tagged as soon as Data Classification identifies them. This allows downstream governance policies – such as column‑level masks or access controls – to react immediately to new sensitive data. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Masking Sensitive Columns

Databricks provides the built‑in function `system.data_classification.mask_value` that returns a type‑aware safe placeholder for any column. This function can be used inside a [Column‑Level Masking](/concepts/abac-column-level-mask-unity-catalog.md) policy to obscure classified data. For example, it returns `0` for integers, `DATE '1970-01-01'` for dates, and a SHA‑256 hash for strings. No custom UDF is needed. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Using Data Classification in a Governance Workflow

A common pattern (as shown in the full tutorial) is to combine Data Classification with Control Tags and [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) to create a “secure by default” schema:

- Every new table inherits a `review_status = pending` control tag, causing all columns to be masked.
- Data Classification scans the table and applies `class.*` tags to sensitive columns.
- After a data steward reviews the classifications and flips the tag to `reviewed`, a second policy masks only the columns that carry `class.*` tags, while non‑sensitive columns become visible.

This approach ensures that unclassified data never leaks, and after review only genuinely sensitive columns remain protected. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance layer.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Policy engine that evaluates tags and attributes.
- [Column-Level Masking](/concepts/abac-column-level-mask-unity-catalog.md) – The mechanism to obscure column values at query time.
- [Governed Tags](/concepts/governed-tags.md) – System‑managed tags such as `class.*`.
- Secure new tables by default – Tutorial illustrating the end‑to‑end workflow.

## Sources

- secure-new-tables-by-default-with-control-tags-databricks-on-aws.md

# Citations

1. [secure-new-tables-by-default-with-control-tags-databricks-on-aws.md](/references/secure-new-tables-by-default-with-control-tags-databricks-on-aws-955564d7.md)
