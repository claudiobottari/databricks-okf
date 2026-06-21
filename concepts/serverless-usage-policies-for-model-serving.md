---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 176d28dfb3a81ffe081d9a5f7ac492bbb8e4ac810b1d6c53a031431a98a07bb1
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-usage-policies-for-model-serving
    - SUPFMS
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Serverless Usage Policies for Model Serving
description: Custom tagging mechanism for attributing serverless usage costs to specific projects or teams via budget policies attached to endpoints.
tags:
  - model-serving
  - cost-management
  - billing
  - databricks
timestamp: "2026-06-19T19:26:15.075Z"
---

Here is the wiki page for "Serverless Usage Policies for Model Serving".

---

## Serverless Usage Policies for Model Serving

**Serverless Usage Policies for Model Serving** allow organizations to apply custom tags to serverless usage for granular billing attribution on Databricks. When a workspace uses serverless usage policies to attribute costs, you can attach a policy to a [Model Serving](/concepts/model-serving.md) endpoint to control how the endpoint's consumption is tracked and billed. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Assigning a Policy During Endpoint Creation

During model serving endpoint creation, you can select a serverless usage policy from the **Usage policy** menu in the Serving UI. If you have been assigned a serverless usage policy, all endpoints that you create are automatically assigned that policy — even if you do not explicitly select a policy from the menu. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Editing a Policy on an Existing Endpoint

If you have `CAN MANAGE` permissions on an existing endpoint, you can edit or add a serverless usage policy from the **Endpoint details** page in the Serving UI. ^[manage-model-serving-endpoints-databricks-on-aws.md]

> **Important:** Existing endpoints are not automatically tagged with your assigned serverless usage policy. You must manually update each existing endpoint if you want to attach a policy to it. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Related Concepts

- Attribute Usage with Serverless Usage Policies — The underlying mechanism for tagging serverless consumption.
- [Budget Policies](/concepts/serverless-budget-policy.md) — The administrative controls for managing serverless spending.
- Model Serving Endpoint Permissions — The `CAN MANAGE` permission required to edit policies on existing endpoints.
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — The type of endpoint that can be stopped and configured with a usage policy.

### Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
