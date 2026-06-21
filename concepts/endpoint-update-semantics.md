---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1c0412a5bc84486429d8cb73a9a90de155f3f0d774b2be6aaec37337fbccba8
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - endpoint-update-semantics
    - EUS
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Update Semantics
description: Rules governing how model serving endpoints can be updated, including constraints on external_model presence and configuration change handling.
tags:
  - model-serving
  - databricks
  - configuration
timestamp: "2026-06-19T14:37:42.204Z"
---

```markdown
---
title: Endpoint Update Semantics
summary: Updates to model serving endpoints keep the old configuration serving traffic until the new one is ready, cannot overlap with another in-progress update, and can be cancelled from the UI. External model endpoints have additional restrictions.
sources:
  - create-foundation-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:22:19.308Z"
updatedAt: "2026-06-18T11:22:19.308Z"
tags:
  - model-serving
  - operations
  - reliability
aliases:
  - endpoint-update-semantics
  - EUS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Endpoint Update Semantics

**Endpoint Update Semantics** describe the behavior of configuration changes applied to a [[model serving endpoint]] after its initial creation. Understanding these semantics is important for maintaining availability and avoiding unintended downtime.

## What Can Be Updated

After enabling a model serving endpoint, you can set the compute configuration as desired. This includes workload size and compute configuration, which determine the resources allocated for serving the model. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Failure Behavior During an Update

Until the new configuration is ready, the old configuration keeps serving prediction traffic. If an update fails, the previous active configuration remains in effect as if the update never happened. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Update Concurrency

While an update is in progress, another update cannot be made. You can cancel an in-progress configuration update from the Serving UI by selecting **Cancel update** on the top right of the endpoint's details page. This functionality is available only in the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Restrictions for External Model Endpoints

Endpoints that serve an external model have additional update restrictions:

- When an `external_model` is present in the endpoint configuration, the served entities list can contain only one served entity object.
- Existing endpoints with an `external_model` cannot be updated to remove it.
- Endpoints created without an `external_model` cannot be updated to add one.

^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [[Foundation Model Serving Endpoints]]
- [[External Model Multi-Serving|External Models in Model Serving]]
- Create Foundation Model Serving Endpoints
- [[AI Gateway Inference Tables|AI Gateway-enabled inference tables]]

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
