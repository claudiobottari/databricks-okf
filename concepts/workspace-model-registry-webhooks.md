---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5ea30e6d314b2810dbdd5722f5ee15eb5442b4941b0a0c3bfcb8e5da5ed6987
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-model-registry-webhooks
    - WMRW
    - Model Registry Webhooks
    - Webhooks for Workspace Model Registry
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Workspace Model Registry Webhooks
description: Event-driven notifications that trigger actions (HTTP calls or job runs) when MLflow Model Registry events occur in a Databricks workspace.
tags:
  - databricks
  - mlflow
  - webhooks
  - automation
timestamp: "2026-06-19T23:27:21.420Z"
---

# [Workspace Model Registry](/concepts/workspace-model-registry.md) Webhooks

**Workspace Model Registry webhooks** enable you to listen for [MLflow Model Registry](/concepts/mlflow-model-registry.md) events so your integrations can automatically trigger actions. Webhooks allow you to automate and integrate your machine learning pipeline with existing CI/CD tools and workflows — for example, triggering CI builds when a new model version is created or notifying team members through Slack each time a model transition to production is requested. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

Webhooks are available through the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) or the Python client `databricks-registry-webhooks` on PyPI. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Webhook Events

You can specify a webhook to trigger upon one or more of the following events:

- **MODEL_VERSION_CREATED**: A new model version was created.
- **MODEL_VERSION_TRANSITIONED_STAGE**: A model version's stage was changed.
- **TRANSITION_REQUEST_CREATED**: A user requested a model version's stage be transitioned.
- **COMMENT_CREATED**: A user wrote a comment on a registered model.
- **REGISTERED_MODEL_CREATED**: A new registered model was created. This event type can only be specified for a registry-wide webhook.
- **MODEL_VERSION_TAG_SET**: A user set a tag on the model version.
- **MODEL_VERSION_TRANSITIONED_TO_STAGING**: A model version was transitioned to staging.
- **MODEL_VERSION_TRANSITIONED_TO_PRODUCTION**: A model version was transitioned to production.
- **MODEL_VERSION_TRANSITIONED_TO_ARCHIVED**: A model version was archived.
- **TRANSITION_REQUEST_TO_STAGING_CREATED**: A user requested a model version be transitioned to staging.
- **TRANSITION_REQUEST_TO_PRODUCTION_CREATED**: A user requested a model version be transitioned to production.
- **TRANSITION_REQUEST_TO_ARCHIVED_CREATED**: A user requested a model version be archived.

^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Types of Webhooks

Webhooks are classified by their trigger target and by their scope.

### By Trigger Target

- **HTTP registry webhooks**: Send triggers to an HTTP endpoint. For example, the URL can point to Slack to post messages to a channel.
- **Job registry webhooks**: Trigger a job in a Databricks workspace. If IP allowlisting is enabled in the job's workspace, you must allowlist the workspace IPs of the model registry.

^[workspace-model-registry-webhooks-databricks-on-aws.md]

### By Scope

- **Model-specific webhooks**: The webhook applies to a specific registered model. You must have **CAN MANAGE** permissions on the registered model to create, modify, delete, or test model-specific webhooks.
- **Registry-wide webhooks**: The webhook is triggered by events on any registered model in the workspace, including the creation of a new registered model. To create a registry-wide webhook, omit the `model_name` field on creation. You must have **workspace admin** permissions to create, modify, delete, or test registry-wide webhooks.

^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Webhook Payload

Each event trigger includes minimal fields in the payload sent to the webhook endpoint. Sensitive information like artifact path location is excluded. Payloads are not encrypted, so recipients should validate the source using the shared secret. The `text` field facilitates Slack integration — to send a Slack message, provide a Slack webhook endpoint as the webhook URL. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Job Registry Webhook Payload

The payload for a job registry webhook depends on the type of job and is sent to the `jobs/run-now` endpoint in the target workspace. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

**Single-task jobs** have one of three payloads based on the task type:

- **Notebook and Python wheel jobs**: A JSON payload with a parameter dictionary containing an `event_message` field.
- **Python, JAR, and Spark Submit jobs**: A JSON payload with a parameter list.
- **All other jobs**: A JSON payload with no parameters.

**Multi-task jobs** have a JSON payload with all parameters populated to account for different task types, including `notebook_params`, `python_named_params`, `jar_params`, `python_params`, and `spark_submit_params`. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Example Payloads

For a `MODEL_VERSION_TRANSITIONED_STAGE` event, the payload includes fields such as `event`, `webhook_id`, `event_timestamp`, `model_name`, `version`, `to_stage`, `from_stage`, and a human-readable `text` field. For a `MODEL_VERSION_TAG_SET` event, the payload includes a `tags` array. For a `COMMENT_CREATED` event, the payload includes the `comment` text. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Security

Databricks includes the `X-Databricks-Signature` in the header, computed from the payload and the shared secret key associated with the webhook using the HMAC with SHA-256 algorithm. You can also include a standard `Authorization` header in the outgoing request by specifying one in the `HttpUrlSpec` of the webhook. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Client Verification

If a shared secret is set, the payload recipient should verify the source of the HTTP request by using the shared secret to HMAC-encode the payload and comparing the encoded value with the `X-Databricks-Signature` from the header. This is particularly important if SSL certificate validation is disabled (`enable_ssl_verification` set to `false`). ^[workspace-model-registry-webhooks-databricks-on-aws.md]

By default, `enable_ssl_verification` is `true`. For self-signed certificates, this field must be `false`, and the destination server must disable certificate validation. Databricks recommends that you perform secret validation with the HMAC-encoded portion of the payload. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### IP Allowlisting for Job Registry Webhooks

To use a webhook that triggers job runs in a different workspace that has IP allowlisting enabled, you must allowlist the region NAT IP where the webhook is located. If the webhook and the job are in the same workspace, you do not need to add any IPs to your allowlist. Contact your accounts team to identify the IPs you need to allowlist. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Audit Logging

If audit logging is enabled for your workspace, the following events are included in the audit logs: create webhook, update webhook, list webhook, delete webhook, test webhook, and webhook trigger. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

For webhooks with HTTP endpoints, the HTTP request sent to the URL, along with the URL and `enable_ssl_verification` values, are logged. For webhooks with job triggers, the `job_id` and `workspace_url` values are logged. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Lifecycle Management

Webhooks support the following lifecycle operations through the REST API or Python client:

- **Create**: Create a webhook with an HTTP endpoint or job trigger, specifying events, status, and optional description.
- **Test**: For webhooks in `TEST_MODE`, send a mock event to verify connectivity. The test endpoint returns the received status code and body from the specified URL.
- **Update**: Change webhook properties, including status (to `ACTIVE` or `DISABLED`).
- **Delete**: Permanently remove a webhook.
- **List**: Retrieve all webhooks for a model or registry-wide.

^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Creating an HTTP Registry Webhook

When an HTTPS endpoint is ready to receive the webhook event request, you can create a webhook using the Databricks REST API or the `RegistryWebhooksClient` Python client. The `http_url_spec` requires the `url` field and optionally accepts `secret` and `authorization` fields. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Creating a Job Registry Webhook

The workflow for managing job registry webhooks is similar to HTTP registry webhooks, with the only difference being the `job_spec` field that replaces the `http_url_spec` field. The `job_spec` requires a `job_id` and optionally accepts a `workspace_url` (for triggering jobs in a different workspace) and an `access_token`. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

As a security best practice, Databricks recommends using OAuth tokens for authentication. If using personal access tokens, Databricks recommends using tokens belonging to service principals instead of workspace users. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

You can also create both HTTP and job registry webhooks with the Databricks Terraform provider and the `databricks_mlflow_webhook` resource. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md)
- Model lifecycle management
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md)
- Service principals
- OAuth tokens
- Databricks Terraform provider
- [Audit logging](/concepts/abac-policy-audit-logging.md)

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
