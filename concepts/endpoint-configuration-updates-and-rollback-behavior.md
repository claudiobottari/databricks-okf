---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f4d7c3f4f5d6a0226b621afd5682b6f5f182a95562a79950042e46196477786
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-configuration-updates-and-rollback-behavior
    - Rollback Behavior and Endpoint Configuration Updates
    - ECUARB
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
      start: 60
      end: 68
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
      start: 87
      end: 93
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
      start: 56
      end: 60
title: Endpoint Configuration Updates and Rollback Behavior
description: Process of modifying an existing endpoint's compute configuration; old configuration continues serving traffic until new config is ready, with cancel capability
tags:
  - operations
  - deployment
  - model-serving
timestamp: "2026-06-18T14:54:05.707Z"
---



# Endpoint Configuration Updates and Rollback Behavior

**Endpoint Configuration Updates and Rollback Behavior** describes how custom model serving endpoints in Databricks handle configuration changes, including rollback safety and error handling for update operations.

## Overview

When you update a custom model serving endpoint's configuration, the existing active configuration continues serving prediction traffic until the new configuration is ready. This ensures no service disruption during updates. The endpoint configuration update process has specific safeguards and limitations. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Update Process

### Safe Rollback

During an update, the old configuration remains active and continues serving traffic. The new configuration is deployed in parallel, and only after it is ready does traffic switch to the new configuration. If the update fails, the existing active configuration stays effective — as if the update never happened. ^[create-custom-model-serving-endpoints-databricks-on-aws.md:60-68]

### Update Constraints

While a configuration update is in progress, you cannot make another update. However, you can **cancel** an in-progress update using the Serving UI. To cancel an update, select **Cancel update** on the endpoint's details page. ^[create-custom-model-serving-endpoints-databricks-on-aws.md:87-93]

### Update Failure Handling

When a configuration update fails, the endpoint retains its previous working configuration. The failure does not affect the existing active state. To verify the update was applied successfully, review the [status of your endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#status). ^[create-custom-model-serving-endpoints-databricks-on-aws.md:56-60]

## Requirements for Updates

### Validation of Creator Identity

Configuration and served-entity updates re-validate the endpoint's recorded creator. The creator must:

1. Be a current member of the workspace
2. Hold the `workspace-access` entitlement
3. Have required Unity Catalog grants on each served entity

Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md:60-68]

### Best Practices

To avoid update failures:

- **Use a long-lived service principal** owned by your team as the endpoint creator
- **Do not use a personal user account** that might be deactivated or removed from the workspace
- The recorded creator **must remain a workspace member** for the lifetime of the endpoint

^[create-custom-model-serving-endpoints-databricks-on-aws.md:60-68]

## Rollback Behavior Summary

| Scenario | Behavior |
|----------|----------|
| Successful update | New configuration takes effect, old configuration replaced |
| Failed update | Existing active configuration stays effective |
| In-progress update | Another update not allowed; can cancel in UI |
| Creator validation failure | Update fails, existing configuration remains |

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — The type of endpoint being updated
- [Endpoint Creator Identity](/concepts/model-serving-endpoint-creator-identity.md) — The identity used for access control
- [Served Entity Grants](/concepts/served-entity-grants.md) — Permissions required for each model version
- [Model Serving Endpoint Status](/concepts/model-serving-endpoint-status.md) — How to check endpoint health after updates
- Endpoint Permissions — Managing access to endpoints

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

This page covers only the update and rollback behavior. For complete endpoint creation instructions, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
2. [create-custom-model-serving-endpoints-databricks-on-aws.md:60-68](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
3. [create-custom-model-serving-endpoints-databricks-on-aws.md:87-93](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
4. [create-custom-model-serving-endpoints-databricks-on-aws.md:56-60](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
