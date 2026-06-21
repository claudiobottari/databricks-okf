---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67a56fb324770d26458148833ecb20725657da87c2f17d0bf907b9c7f039242f
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-results-page
    - DCRP
    - Data Classification Results
    - Data Classification#View Classification Results|View classification results
    - Data Classification#view classification results
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Data Classification Results Page
description: The UI surface in Databricks Catalog Explorer where built-in and custom classifier detections are displayed and where custom classifiers are managed.
tags:
  - data-governance
  - unity-catalog
  - ui
timestamp: "2026-06-19T14:38:59.592Z"
---

# Data Classification Results Page

The **Data Classification Results Page** is the primary interface in Databricks Unity Catalog for viewing and managing the output of data classification scans. It displays detected sensitive data across all catalogs in the [Metastore](/concepts/metastore.md) and provides access to custom classifier management.

## Overview

The Data Classification Results Page shows the results of automated scans that identify sensitive data types across tables in Unity Catalog. From this page, users can view detected classifications, manage custom classifiers, and navigate to detailed classification information for specific columns and tables. ^[custom-classifiers-databricks-on-aws.md]

## Accessing Custom Classifier Management

From the Data Classification Results Page, users can access the custom classifier management interface by clicking the **Manage custom classifiers** button. This opens a side panel that lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]

![Manage custom classifiers button on the Data Classification results page.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-manage-button-27dea39992ed593d73cac1fbf16c8f27.png)

## Viewing Classification Results

To view custom classifier detections, users follow the same steps as for built-in classifications. The results page displays detections from both built-in and custom classifiers, allowing users to see all identified sensitive data in one unified view. ^[custom-classifiers-databricks-on-aws.md]

## Suspended Classifier Warnings

The Data Classification Results Page displays a warning when one or more custom classifiers are suspended. A suspended custom classifier produces no new detections. Common causes for suspension include:

- Example columns referencing tables that have been deleted or renamed
- Example columns that are not representative enough for stable detection
- The governed tag is no longer valid or the tag value is no longer valid

^[custom-classifiers-databricks-on-aws.md]

![Warning showing that one or more custom classifiers are suspended.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-suspended-warning-265378e7bb46e77fe26396a365144920.png)

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md) — User-defined classifiers that extend built-in detection capabilities
- [Data Classification in Unity Catalog](/concepts/data-classification-unity-catalog.md) — The overall data classification system
- [Governed Tags](/concepts/governed-tags.md) — Tags used by custom classifiers to mark detected sensitive data
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that hosts classification functionality
- System Catalog — Where classification metadata and custom classifier configuration are stored

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
