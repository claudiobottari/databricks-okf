---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e80382de04896f9610bed21cde4d4f62fada25da3357c8f4b1cd29ef05c22f62
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-certification-and-deprecation-signals
    - Deprecation Signals and Data Certification
    - DCADS
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Data Certification and Deprecation Signals
description: System tags that mark data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use) to provide inline trust signals.
tags:
  - data-governance
  - trust-signals
  - certification
  - deprecation
timestamp: "2026-06-18T11:27:45.146Z"
---

# Data Certification and Deprecation Signals

**Data Certification and Deprecation Signals** are system tags that administrators apply to data assets in Unity Catalog to indicate their quality and lifecycle status. These signals help users quickly identify trusted, production-ready data and avoid outdated or unreliable assets during discovery.

## Overview

Data Certification and Deprecation Signals form part of the metadata layer that shapes [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md). By applying consistent tags, administrators make it easier for users across the organization to find, understand, and trust data assets. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How the Signals Work

Administrators use system tags to mark a data asset as either *certified* (trusted, meeting quality standards) or *deprecated* (outdated, unsuitable for new use). These tags appear inline in the workspace and influence how the asset surfaces in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

- **Certified** – Indicates that the asset has been reviewed and approved. Assets with this tag are promoted in search and clearly labeled, helping users choose reliable sources.
- **Deprecated** – Signals that the asset should no longer be used for new work. Assets with this tag are de-emphasized in search and visually flagged to discourage accidental consumption.

Both signals are implemented through system tags, which are predefined tags provided by Databricks. The act of applying and removing these tags is governed by the same permission model as other tag operations.

## Effect on Discovery

The quality of admin-side metadata directly determines how useful the discovery experience is for users. When certification and deprecation signals are consistently applied, users can filter and search for data assets with confidence, knowing that certified assets are trustworthy and deprecated assets are flagged. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Usage

To apply these signals, see the detailed procedure in [Flag certified and deprecated data](/concepts/certified-and-deprecated-data-flags.md). The process involves setting the appropriate system tag on the target catalog object (table, view, model, etc.). Users with the necessary privileges can manage these tags through Catalog Explorer or the Unity Catalog API.

## Related Concepts

- [Flag certified and deprecated data](/concepts/certified-and-deprecated-data-flags.md) – Step-by-step instructions for applying certification/deprecation tags
- [Governed Tags](/concepts/governed-tags.md) – Controlled tag vocabularies for organizing data by topic, team, or domain
- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) – The overall framework for enabling users to find and trust data
- [System Tags](/concepts/system-tags.md) – Predefined tags offered by Databricks, including those used for certification and deprecation
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that hosts these signals
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) – Tag operations (including certification/deprecation) are logged for compliance

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
