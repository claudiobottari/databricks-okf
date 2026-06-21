---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b4523f873476914971bf54e89913e08a974c1e53632493012b361d0b3379efd
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - registry-webhook-events
    - RWE
    - Webhook Events|events
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Registry Webhook Events
description: The set of MLflow Model Registry events that can trigger webhooks, including model version creation, stage transitions, transition requests, comments, tags, and registered model creation.
tags:
  - mlflow
  - events
  - webhooks
timestamp: "2026-06-19T23:27:21.008Z"
---

# Registry Webhook Events

**Registry Webhook Events** are predefined trigger conditions in the [Workspace Model Registry](/concepts/workspace-model-registry.md) that enable integrations to automatically respond to changes in registered models and model versions. Webhooks listen for these events to automate machine learning pipelines, integrate with CI/CD tools, trigger notifications, or initiate workflows in response to model registry activity. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Available Event Types

Webhooks can be configured to trigger on one or more of the following events: ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Model Version Events

- **MODEL_VERSION_CREATED**: A new model version was created for the associated model.
- **MODEL_VERSION_TAG_SET**: A user set a tag on the model version.
- **MODEL_VERSION_TRANSITIONED_STAGE**: A model version's stage was changed.
- **MODEL_VERSION_TRANSITIONED_TO_STAGING**: A model version was transitioned to staging.
- **MODEL_VERSION_TRANSITIONED_TO_PRODUCTION**: A model version was transitioned to production.
- **MODEL_VERSION_TRANSITIONED_TO_ARCHIVED**: A model version was archived.

### Transition Request Events

- **TRANSITION_REQUEST_CREATED**: A user requested a model version's stage be transitioned.
- **TRANSITION_REQUEST_TO_STAGING_CREATED**: A user requested a model version be transitioned to staging.
- **TRANSITION_REQUEST_TO_PRODUCTION_CREATED**: A user requested a model version be transitioned to production.
- **TRANSITION_REQUEST_TO_ARCHIVED_CREATED**: A user requested a model version be archived.

### Registered Model Events

- **REGISTERED_MODEL_CREATED**: A new registered model was created. This event type can only be specified for a registry-wide webhook, created by omitting a model name in the create request.
- **COMMENT_CREATED**: A user wrote a comment on a registered model.

## Event Payload Structure

Each webhook trigger includes a JSON payload with event-specific fields. The payload contains minimal information; sensitive details such as artifact path location are excluded. Users with appropriate ACLs can use the [MLflow Model Registry](/concepts/mlflow-model-registry.md) client or REST APIs to query for additional information. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Common Payload Fields

All event payloads include: ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- `event`: The type of event that occurred.
- `webhook_id`: The unique identifier of the webhook.
- `event_timestamp`: The Unix timestamp of when the event occurred.
- `model_name`: The name of the registered model.
- `version`: The version number of the model version involved.
- `text`: A human-readable message describing the event, designed to facilitate Slack integration.

### Event-Specific Fields

Different events include additional fields: ^[workspace-model-registry-webhooks-databricks-on-aws.md]

- **MODEL_VERSION_TRANSITIONED_STAGE**: Includes `to_stage` and `from_stage` fields indicating the stage transition.
- **MODEL_VERSION_TAG_SET**: Includes a `tags` array containing key-value pairs of the tags that were set.
- **COMMENT_CREATED**: Includes a `comment` field with the raw text content of the comment.

## Example Payloads

### MODEL_VERSION_TRANSITIONED_STAGE

```json
{
  "event": "MODEL_VERSION_TRANSITIONED_STAGE",
  "webhook_id": "c5596721253c4b429368cf6f4341b88a",
  "event_timestamp": 1589859029343,
  "model_name": "Airline_Delay_SparkML",
  "version": "8",
  "to_stage": "Production",
  "from_stage": "None",
  "text": "Registered model 'someModel' version 8 transitioned from None to Production."
}
```
^[workspace-model-registry-webhooks-databricks-on-aws.md]

### MODEL_VERSION_TAG_SET

```json
{
  "event": "MODEL_VERSION_TAG_SET",
  "webhook_id": "8d7fc634e624474f9bbfde960fdf354c",
  "event_timestamp": 1589859029343,
  "model_name": "Airline_Delay_SparkML",
  "version": "8",
  "tags": [{"key":"key1","value":"value1"},{"key":"key2","value":"value2"}],
  "text": "example@example.com set version tag(s) 'key1' => 'value1', 'key2' => 'value2' for registered model 'someModel' version 8."
}
```
^[workspace-model-registry-webhooks-databricks-on-aws.md]

### COMMENT_CREATED

```json
{
  "event": "COMMENT_CREATED",
  "webhook_id": "8d7fc634e624474f9bbfde960fdf354c",
  "event_timestamp": 1589859029343,
  "model_name": "Airline_Delay_SparkML",
  "version": "8",
  "comment": "Raw text content of the comment",
  "text": "A user commented on registered model 'someModel' version 8."
}
```
^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Webhook Types and Scope

Events are delivered through two types of webhooks: ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **HTTP registry webhooks**: Send event payloads to an HTTP endpoint.
- **Job registry webhooks**: Trigger a job in a Databricks workspace.

Webhooks also have two scope types with different access control requirements: ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Model-specific webhooks**: Apply to a specific registered model. Requires CAN MANAGE permissions on the registered model.
- **Registry-wide webhooks**: Triggered by events on any registered model in the workspace, including new model creation. Requires workspace admin permissions.

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md)
- Model Versioning
- [Model Stage Transitions](/concepts/model-versioning-and-stage-transitions.md)
- Job Triggers

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
