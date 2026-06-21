---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d82133fca475960d36aeebbd6dc1f12df3c2829c6b7c1914bd65c25f2aa34251
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-geo-data-processing
    - CDP
    - Cross‑Geo Data Processing
    - cross-geo-data-processing-for-foundation-model-apis
    - CDPFFMA
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Cross-Geo Data Processing
description: Databricks may process Foundation Model API request data outside the originating region/cloud provider; workspaces in non-EU/US regions must enable cross-Geo data processing to access certain models.
tags:
  - data-residency
  - compliance
  - foundation-model-apis
timestamp: "2026-06-19T18:53:54.905Z"
---

# Cross-Geo Data Processing

**Cross-Geo Data Processing** refers to the handling of data in a geographic region or cloud provider that differs from the one where the data originally resided. In the context of Databricks Foundation Model APIs, requests may be processed outside of the workspace’s home region as part of delivering model inference services. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Overview

When using Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md), the region and geography where API requests are processed depend on both the workspace region and the specific model being used. As part of providing these APIs, Databricks might process your data outside of the region and cloud provider where your data originated. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## When Cross-Geo Processing Is Required

Cross-Geo data processing must be explicitly enabled in the following scenario:

- If your workspace is located in a supported [Model Serving](/concepts/model-serving.md) region that is **not** a US or EU region, you must enable cross-Geo data processing to access certain models that are only available in US or EU regions (for example, OpenAI GPT-5.5, Anthropic Claude Opus 4.8, and others). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

Models listed as “EU and US models” in the Foundation Model APIs regional availability are only served from US or EU geographic areas. Workspaces outside those areas cannot use these models unless cross-Geo processing is turned on. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- Databricks Geos — Documentation of geographic regions where Databricks operates.
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) — Lists the geographic areas that process pay-per-token and provisioned throughput workloads.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that provides access to hosted language and embedding models.
- Data Residency — Regulatory requirement to keep data within specific geographic boundaries.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) — Security standards that may interact with data processing locations.

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
