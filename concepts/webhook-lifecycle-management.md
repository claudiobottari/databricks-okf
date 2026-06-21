---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c391ad800a2b508883450738c771ee73d6698e92ebeae1182846e9af3e570a3a
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - webhook-lifecycle-management
    - WLM
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Webhook Lifecycle Management
description: "Management operations for webhooks: create (in TEST_MODE or ACTIVE), test with mock events, update (status and properties), list, and delete via REST API or Python client."
tags:
  - databricks
  - webhooks
  - api
  - lifecycle
timestamp: "2026-06-19T23:27:55.407Z"
---

# Webhook Lifecycle Management

**Webhook Lifecycle Management** refers to the process of creating, testing, updating, and deleting webhooks that listen for [Workspace Model Registry](/concepts/workspace-model-registry.md) events on Databricks. Proper lifecycle management ensures that integrations with CI/CD tools, notification systems, and automated workflows remain reliable and secure throughout the webhook's operational lifetime. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Lifecycle Stages

### 1. Creation

A webhook is created by specifying the model name (for model-specific webhooks) or omitting it (for registry-wide webhooks), along with the events to trigger on and the target specification. The target can be either an HTTP endpoint (`http_url_spec`) or a Databricks job (`job_spec`). ^[workspace-model-registry-webhooks-databricks-on-aws.md]

When creating a webhook, you can set its initial status to `TEST_MODE` to validate the configuration before enabling it for real events. A description and optional shared secret for HMAC signature verification can also be provided. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

Webhooks can be created using the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md), the Python client library `databricks-registry-webhooks`, or the Databricks Terraform provider with the `databricks_mlflow_webhook` resource. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### 2. Testing

Webhooks created in `TEST_MODE` can be tested by sending a mock event to the specified endpoint. The test endpoint returns the HTTP status code and body received from the target URL, allowing you to verify that the integration works correctly without triggering on real events. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### 3. Activation

To enable a webhook for real events, its status is updated to `ACTIVE`. The update operation can also modify any other properties of the webhook, such as the event list, target URL, or description. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### 4. Deactivation and Deletion

A webhook can be disabled by setting its status to `DISABLED`, which prevents it from triggering on events while preserving its configuration. Alternatively, a webhook can be permanently deleted, removing it entirely from the system. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Webhook Types

### By Target

- **HTTP registry webhooks**: Send triggers to an HTTP endpoint, such as a Slack webhook URL for posting notifications to a channel. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Job registry webhooks**: Trigger a job run in a Databricks workspace, either in the same workspace or a different workspace specified by `workspace_url`. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### By Scope

- **Model-specific webhooks**: Apply to a single registered model. Requires CAN MANAGE permissions on that model. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Registry-wide webhooks**: Trigger on events from any registered model in the workspace, including new model creation. Requires workspace admin permissions. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Security Considerations

### Signature Verification

Databricks includes an `X-Databricks-Signature` header in HTTP webhook requests, computed from the payload and the shared secret using HMAC with SHA-256. Recipients should verify this signature to confirm that Databricks is the source of the request, especially when SSL certificate validation is disabled. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Authorization Headers

An optional Authorization header can be specified in the `HttpUrlSpec` of the webhook, allowing clients to verify the source of the HTTP request by checking the bearer token or authorization credentials. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### IP Allowlisting for Job Webhooks

When a job registry webhook triggers a job in a different workspace that has IP allowlisting enabled, the region NAT IP of the webhook's workspace must be allowlisted to accept incoming requests. If the webhook and job are in the same workspace, no additional IP allowlisting is needed. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Audit Logging

When audit logging is enabled, the following webhook lifecycle events are recorded:

- Create webhook
- Update webhook
- List webhook
- Delete webhook
- Test webhook
- Webhook trigger

For HTTP webhooks, the trigger audit log includes the URL and `enable_ssl_verification` values. For job webhooks, the `job_id` and `workspace_url` are logged. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The system that manages registered models and their versions.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for [MLflow](/concepts/mlflow.md) runs and evaluations.
- CI/CD Integration — Automated pipelines that webhooks can trigger.
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The API used to manage webhooks programmatically.
- Databricks Terraform Provider — Infrastructure-as-code tool for managing webhooks.

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
