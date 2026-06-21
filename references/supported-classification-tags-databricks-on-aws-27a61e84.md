---
title: Supported classification tags | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification-tags
ingestedAt: "2026-06-18T08:04:02.137Z"
---

Data Classification detects sensitive data and assigns [system tags](https://docs.databricks.com/aws/en/admin/governed-tags/#system-governed-tags) to matching columns. For a mapping of tags to compliance frameworks, see [Compliance framework reference](#compliance-reference). For a full list of tags organized by **global tags** (which apply across all cloud regions) and **regional tags** (which detect data specific to certain countries or regions), see [Global tags](#global-tags) and [Regional tags](#regional-tags).

## Compliance framework reference[​](#compliance-framework-reference "Direct link to compliance-framework-reference")

The following tables show which tags are relevant to common regulatory frameworks. A tag may appear in more than one framework.

*   PII
*   PCI DSS
*   GDPR
*   HIPAA
*   GLBA
*   DPDPA
*   PIPEDA

These tags detect personally identifiable information (PII) — data that can be used to identify an individual, either directly or in combination with other data.

Global tags detect sensitive data regardless of geographic origin.

Regional tags detect sensitive data specific to certain countries or regions. With the exception of United States tags, which are available in all regions, regional tags are available in Databricks workspaces deployed in the corresponding region only.

*   United States
*   United Kingdom
*   Germany
*   Australia
*   Brazil
*   India
*   Canada

These tags are available in Databricks workspaces deployed in **all regions**.
