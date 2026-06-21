---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48fdad2944d3fe59ef423d68795581fa33887041ce5e3b40d29b4f8e5d6768a8
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-region-availability
    - MSRA
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Model Serving Region Availability
description: Regional limitations for Databricks Model Serving, including control plane dependencies and per-region feature availability for custom models, AI agents, and Foundation Model APIs.
tags:
  - model-serving
  - regions
  - availability
  - databricks
timestamp: "2026-06-19T19:44:03.824Z"
---

## Model Serving Region Availability

**Model Serving Region Availability** refers to the set of AWS regions where [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints can be deployed and are fully supported. The availability of specific endpoint types (custom models, AI agents, Foundation Model APIs) and associated compliance features may vary by region.

### Determining Region Support

A workspace can use Model Serving only if its deployment region supports the service **and** the workspace’s Control Plane is located in a supported region. If the workspace is in a region that supports Model Serving but the control plane is in an unsupported region, the service is not available. Attempting to use Model Serving in such a workspace results in an error message stating that the workspace is not supported.^[model-serving-limits-and-regions-databricks-on-aws.md]

### Where to Find Supported Regions

Detailed, feature-level regional availability for Model Serving is documented on the **Model serving features availability** page. That page lists which specific features (e.g., GPU serving, provisioned throughput, external models) are available in each region.^[model-serving-limits-and-regions-databricks-on-aws.md]

For [Foundation Model APIs](/concepts/foundation-model-apis.md) region availability (pay-per-token, provisioned throughput, batch inference), see the **Foundation models hosted on Databricks** page.^[model-serving-limits-and-regions-databricks-on-aws.md]

### Unsupported Regions

If you require an endpoint in a region that is not currently supported, contact your Databricks account team to discuss options.^[model-serving-limits-and-regions-databricks-on-aws.md]

### Compliance Security Profile Region Tables

The source article contains tables that list region availability and supported compliance standards for:

- **CPU and GPU workloads** (including external models) – see the table under the heading “Compliance security profile standards: CPU and GPU workloads”.
- **Foundation Model APIs workloads** (provisioned throughput, pay-per-token, batch inference) – see the table under “Compliance security profile standards: Foundation Model APIs workloads”.

These tables are not reproduced here; refer to the original documentation for the exact region-to-standard mappings.^[model-serving-limits-and-regions-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- Control Plane
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- Serverless Endpoints
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [External Models](/concepts/external-models.md)

### Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
