---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29adace46ff081beeb5c80d76ba4af701a40783fd0ac134a78ec628a81d81a38
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - webhook-payload-structure
    - WPS
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Webhook Payload Structure
description: The JSON payload sent to webhook endpoints, which includes event type, webhook ID, timestamp, model name, version, and event-specific fields. Sensitive info like artifact paths are excluded.
tags:
  - databricks
  - webhooks
  - payload
  - json
timestamp: "2026-06-19T23:27:44.581Z"
---

# Webhook Payload Structure

**Webhook Payload Structure** describes the format and content of the data sent when a [Workspace Model Registry](/concepts/workspace-model-registry.md) event triggers a webhook. Each event trigger includes a minimal set of fields in the payload for the outgoing request to the webhook endpoint. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## General Characteristics

Payloads have several important characteristics:

- **Sensitive information is excluded**: Artifact path locations and other sensitive data are not included in the payload. Users and principals with appropriate ACLs can use client or REST APIs to query the Model Registry for this information. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Payloads are not encrypted**: The payload content is sent without encryption. Recipients should validate that Databricks is the source using the HMAC with SHA-256 algorithm signature included in the request header. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Slack integration support**: The `text` field in the payload is designed to facilitate Slack integration. To send a Slack message, provide a Slack webhook endpoint as the webhook URL. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Common Fields

All webhook payloads share a set of common fields, though the exact fields depend on the event type. Common fields include:

- `event`: The type of event that triggered the webhook (e.g., `MODEL_VERSION_TRANSITIONED_STAGE`).
- `webhook_id`: A unique identifier for the webhook.
- `event_timestamp`: The timestamp of the event in milliseconds since epoch.
- `model_name`: The name of the registered model involved in the event.
- `version`: The version number of the model involved in the event.
- `text`: A human-readable description of the event, suitable for Slack messages.

^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Model-Specific Fields

Depending on the event type, additional fields may be included:

- **Stage transition events** (e.g., `MODEL_VERSION_TRANSITIONED_STAGE`): Include `to_stage` and `from_stage` fields indicating the stage change. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Tag set events** (e.g., `MODEL_VERSION_TAG_SET`): Include a `tags` array containing objects with `key` and `value` fields. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Comment events** (e.g., `COMMENT_CREATED`): Include a `comment` field containing the raw text content of the comment. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Job Registry Webhook Payload

For webhooks with job triggers, the payload is sent to the `jobs/run-now` endpoint in the target workspace. The format depends on the job type: ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Single-Task Jobs

- **Notebook and Python wheel jobs**: Receive a JSON payload with a parameter dictionary containing an `event_message` field. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Python, JAR, and Spark Submit jobs**: Receive a JSON payload with a parameter list containing the webhook payload as a string. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **All other jobs**: Receive a JSON payload with no parameters. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Multi-Task Jobs

Multi-task jobs receive a JSON payload with all parameter fields populated to accommodate different task types: `notebook_params`, `python_named_params`, `jar_params`, `python_params`, and `spark_submit_params`. Each field contains the webhook payload in the appropriate format for that task type. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Example Payloads

### MODEL_VERSION_TRANSITIONED_STAGE

The payload for a stage transition event includes `to_stage` and `from_stage` fields:

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

The payload for a tag set event includes a `tags` array:

```json
{
  "event": "MODEL_VERSION_TAG_SET",
  "webhook_id": "8d7fc634e624474f9bbfde960fdf354c",
  "event_timestamp": 1589859029343,
  "model_name": "Airline_Delay_SparkML",
  "version": "8",
  "tags": [
    {"key": "key1", "value": "value1"},
    {"key": "key2", "value": "value2"}
  ],
  "text": "example@example.com set version tag(s) 'key1' => 'value1', 'key2' => 'value2' for registered model 'someModel' version 8."
}
```

^[workspace-model-registry-webhooks-databricks-on-aws.md]

### COMMENT_CREATED

The payload for a comment event includes a `comment` field:

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

## Security: Payload Verification

When a shared secret is configured, Databricks includes an `X-Databricks-Signature` header computed from the payload using the HMAC with SHA-256 algorithm. Recipients should verify the payload source by: ^[workspace-model-registry-webhooks-databricks-on-aws.md]

1. Extracting the `X-Databricks-Signature` from the request header.
2. Computing an HMAC-SHA256 hash of the request body using the shared secret.
3. Comparing the computed hash with the value in the header.

If the values do not match, the request should not be trusted. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry Webhooks](/concepts/workspace-model-registry-webhooks.md) — Overview of webhook types, events, and management.
- HMAC with SHA-256 algorithm — The algorithm used for payload signing.
- [Model Version Stage Transitions](/concepts/model-versioning-and-stage-transitions.md) — Events related to stage changes.
- Model Version Tags — Metadata associated with model versions.
- Slack Integration — Using webhooks to send Slack notifications.

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
