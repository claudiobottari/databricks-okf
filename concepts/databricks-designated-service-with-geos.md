---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3238de824eb490d77610ed26f5834da8dde9de3750a9c7292e40d2b150daf56
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-designated-service-with-geos
    - DDSWG
    - Databricks Designated Service
    - Databricks Designated Services
    - Designated Services
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Databricks Designated Service with Geos
description: Foundation Model APIs is a Databricks Designated Service that uses Databricks Geos to manage data residency when processing customer content.
tags:
  - data-residency
  - compliance
  - security
  - databricks
timestamp: "2026-06-18T11:38:31.025Z"
---

# Databricks Designated Service with Geos

**Databricks Designated Service with Geos** refers to a classification of Databricks services that are processed within specific geographic boundaries (Databricks Geos) to help customers manage data residency requirements. When a service is identified as a Databricks Designated Service, its processing of customer content occurs within the designated geographic region, providing control over where data is stored and processed. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Databricks Designated Services are a set of service offerings that adhere to the Databricks Geos framework, which defines geographic boundaries for data processing. This designation helps customers comply with data residency regulations by ensuring that customer content processed by the service remains within the specified geographic region. ^[databricks-foundation-model-apis-databricks-on-aws.md]

The key characteristic of a Databricks Designated Service is that it uses Databricks Geos to manage data residency when processing customer content. This is particularly important for organizations that operate in jurisdictions with strict data localization requirements. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Examples of Designated Services

### Foundation Model APIs

One example of a Databricks Designated Service is the [Foundation Model APIs](/concepts/foundation-model-apis.md), which allow users to access and query state-of-the-art open models from a serving endpoint. The Foundation Model APIs are explicitly classified as a Databricks Designated Service, meaning they use Databricks Geos to manage data residency when processing customer content. ^[databricks-foundation-model-apis-databricks-on-aws.md]

Foundation Model APIs are provided in three modes:

- **Pay-per-token**: Recommended for getting started with Foundation Model APIs, though not designed for high-throughput applications.
- **Provisioned throughput**: Recommended for production workloads requiring high throughput, performance guarantees, and additional security requirements (available with compliance certifications like HIPAA).
- **AI Functions optimized models**: Recommended for batch inference workloads.

## How Databricks Geos Work with Designated Services

When a service is designated, Databricks processes customer content only within the geographic boundaries defined by Databricks Geos. This ensures that data does not leave the approved region during processing. The specific geographic boundaries depend on the customer's workspace location and the service configuration. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- Databricks Geos — The geographic boundaries used for data residency management
- Data Residency — Regulatory requirements for keeping data within specific geographic locations
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — A Databricks Designated Service for accessing LLMs
- [Model Serving](/concepts/model-serving.md) — The broader service that Foundation Model APIs build upon
- Compliance Certifications — Including HIPAA availability for provisioned throughput endpoints
- AWS Regions — Supported regions for Databricks Designated Services

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
