---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d1e4d6e45d9536b277f1f1c46b9f64d86a459b4b14d0bbdbad235cf2f3fc7f9
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-specific-vs-registry-wide-webhooks
    - MVRW
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Model-Specific vs Registry-Wide Webhooks
description: "Two scope-based webhook types: model-specific (applies to a single registered model, requires CAN MANAGE permission) and registry-wide (triggered by events on any model, requires workspace admin permissions)."
tags:
  - databricks
  - permissions
  - webhooks
  - scope
timestamp: "2026-06-19T23:27:35.851Z"
---

# Model-Specific vs Registry-Wide Webhooks

**Model-Specific vs Registry-Wide Webhooks** describes the two scope-based classifications of webhooks in the [Workspace Model Registry](/concepts/workspace-model-registry.md) on Databricks. These webhooks listen for registry events and automatically trigger actions, enabling integration with CI/CD tools and workflows. The distinction between model-specific and registry-wide webhooks determines which events trigger the webhook and what permissions are required to manage them. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Model-Specific Webhooks

A **model-specific webhook** applies only to a specific registered model in the [Workspace Model Registry](/concepts/workspace-model-registry.md). It is created by specifying a `model_name` in the creation request. This type of webhook is suitable when you want to automate actions for a particular model, such as triggering a CI build when a new version of that specific model is created or sending a Slack notification when a transition to production is requested for that model. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Permissions

To create, modify, delete, or test a model-specific webhook, you must have **CAN MANAGE** permissions on the registered model. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Example Use Cases

- Trigger a CI build when a new version of a specific model is created.
- Notify a team via Slack when a transition request is made for a particular model.
- Run automated validation jobs when a model version enters the staging stage.

## Registry-Wide Webhooks

A **registry-wide webhook** applies to events on any registered model in the workspace, including the creation of new registered models. To create a registry-wide webhook, omit the `model_name` field in the creation request. This type of webhook is useful for global monitoring and governance, such as logging all model version transitions across the workspace or enforcing compliance checks on every new model registration. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Permissions

To create, modify, delete, or test a registry-wide webhook, you must have **workspace admin** permissions. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Special Event Type

The `REGISTERED_MODEL_CREATED` event type can only be specified for registry-wide webhooks, as it is triggered when any new registered model is created in the workspace. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Example Use Cases

- Monitor all model version transitions across the workspace for audit purposes.
- Send notifications for any comment created on any registered model.
- Trigger a compliance validation workflow whenever a new model is registered.
- Log all transition requests for governance and reporting.

## Comparison Table

| Feature | Model-Specific Webhook | Registry-Wide Webhook |
|---|---|---|
| Scope | Single registered model | All registered models in the workspace |
| Required Permission | CAN MANAGE on the model | Workspace admin |
| Creation | Specify `model_name` | Omit `model_name` |
| `REGISTERED_MODEL_CREATED` event | Not supported | Supported |
| Typical Use | Per-model automation | Workspace-wide governance |

## Webhook Trigger Types

Both model-specific and registry-wide webhooks can be configured with two types of trigger targets:

- **HTTP registry webhooks**: Send triggers to an HTTP endpoint, such as Slack.
- **Job registry webhooks**: Trigger a job in a Databricks workspace, either in the same workspace or a different workspace. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Managing Webhooks

Webhooks are managed through the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) or the Python client `databricks-registry-webhooks` on PyPI. You can create, update, delete, list, and test webhooks programmatically. Webhooks can also be created using the Databricks Terraform provider. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The central model management system.
- [MLflow](/concepts/mlflow.md) — The open-source platform underlying the Model Registry.
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The API for managing webhooks programmatically.
- Databricks Terraform provider — Infrastructure-as-code tool for managing webhooks.
- CI/CD Integration — Using webhooks to automate ML pipelines.
- [Audit Logging](/concepts/abac-policy-audit-logging.md) — Tracking webhook-related events for security and compliance.

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
