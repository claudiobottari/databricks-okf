---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35f3421c9e0dc9bd46e32d870afc3d49837db6ddd492d667967102d5e0dc5944
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-geos-and-data-residency
    - Data Residency and Databricks Geos
    - DGADR
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Databricks Geos and Data Residency
description: Databricks' framework for managing data residency when processing customer content, applicable to Foundation Model APIs as a Designated Service.
tags:
  - data-residency
  - compliance
  - security
timestamp: "2026-06-19T18:13:02.375Z"
---

# Databricks Geos and Data Residency

**Databricks Geos** is a data residency feature used by certain Databricks services to control where customer content is processed and stored. It ensures that data remains within specific geographic boundaries as required by compliance or regulatory policies. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Usage

The Foundation Model APIs on Databricks are classified as a [Databricks Designated Service](/concepts/databricks-designated-service-with-geos.md) – a service that processes customer content using pre-defined geographic boundaries. As a designated service, Foundation Model APIs rely on **Databricks Geos** to manage data residency. This means that when you query a foundation model through the APIs, the content is processed and stored only within the geographic region configured for your workspace, helping meet data sovereignty requirements. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- Data Residency – The practice of keeping data within specific geographic or legal boundaries.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The Databricks service that uses Databricks Geos for data residency management.
- Databricks Designated Services – Services that are subject to geo‑based data residency controls.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
