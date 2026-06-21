---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de6f1cf9f8118eb45123697f7c982696738bbf4b1cb395b88fc885733cc5e834
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - http-vs-job-registry-webhooks
    - HVJRW
    - Job Registry Webhooks
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: HTTP vs Job Registry Webhooks
description: "Two types of webhooks based on trigger targets: HTTP endpoints (send HTTP requests to a URL) and job triggers (run a Databricks job in the same or different workspace)."
tags:
  - databricks
  - webhooks
  - jobs
  - http
timestamp: "2026-06-19T23:27:29.147Z"
---

# HTTP vs Job Registry Webhooks

The Databricks [Workspace Model Registry](/concepts/workspace-model-registry.md) supports two types of webhooks based on their trigger target: **HTTP registry webhooks** and **job registry webhooks**. Both listen for model registry events and automate downstream actions, but they differ in how they deliver the event, their payload structure, security model, and operational requirements. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Trigger Mechanism

**HTTP registry webhooks** send an HTTP POST request to a user‑specified URL when an event occurs. The URL can point to any HTTP endpoint, such as a Slack webhook or a CI/CD service. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

**Job registry webhooks** trigger a job run in a Databricks workspace by calling the `jobs/run-now` endpoint. The job can be in the same workspace as the webhook or in a different workspace; the target workspace is specified by an optional `workspace_url` field. If no `workspace_url` is provided, the job runs in the workspace where the webhook is created. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Payload Differences

HTTP webhooks send a JSON payload directly to the endpoint. The payload contains event‑specific fields such as `model_name`, `version`, `to_stage`, `comment`, or `tags`, as well as the shared `event`, `webhook_id`, `event_timestamp`, and a human‑readable `text` field. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

Job registry webhooks deliver the event payload as parameters to the triggered job. The exact format depends on the job’s task type:

- **Notebook and Python wheel jobs** receive a `notebook_params` dictionary with a single key `event_message` whose value is the webhook payload (a JSON string). ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Python, JAR, and Spark Submit jobs** receive the payload in `python_params`, `jar_params`, or `spark_submit_params` as a list containing the payload string. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **All other job types** receive no parameters. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- **Multi‑task jobs** populate all parameter fields (`notebook_params`, `python_named_params`, `jar_params`, `python_params`, `spark_submit_params`) to accommodate any task type within the job. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Security

Both webhook types support authentication, but the mechanisms differ.

For HTTP webhooks, if a shared secret is set, the outgoing request includes an `X-Databricks-Signature` header computed using the HMAC‑SHA‑256 algorithm over the payload and the secret. Recipients should verify the signature to confirm the request originated from Databricks. Additionally, a standard `Authorization` header can be specified in the `HttpUrlSpec`. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

For job registry webhooks, authentication to the target workspace is provided via a personal access token (or OAuth token) included in the `access_token` field of the `job_spec`. This token is used by the [MLflow](/concepts/mlflow.md) service to call `jobs/run-now`. Databricks recommends using tokens belonging to service principals for production workloads. The access token cannot be returned by Databricks users in the Model Registry API. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## IP Allowlisting for Job Webhooks

When a job registry webhook triggers a job in a different workspace that has IP allowlisting enabled, the region NAT IP of the workspace where the webhook is located must be allowlisted. If the webhook and the job are in the same workspace, no additional IP allowlisting is needed. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Audit Logging

When audit logging is enabled, the following information is recorded:

- For HTTP webhooks: the HTTP request sent to the URL, the URL itself, and the `enable_ssl_verification` setting are logged. ^[workspace-model-registry-webhooks-databricks-on-aws.md]
- For job registry webhooks: the `job_id` and `workspace_url` values are logged. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Shared Characteristics

Both webhook types share the same [Webhook Events|events](/concepts/registry-webhook-events.md) (e.g., `MODEL_VERSION_CREATED`, `TRANSITION_REQUEST_CREATED`) and the same two scopes: model‑specific (applies to one registered model) and registry‑wide (applies to all models in the workspace). Webhook creation, update, deletion, and testing follow the same REST API and Python client patterns; the only difference is whether an `http_url_spec` or a `job_spec` is provided. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Choosing Between Them

The choice depends on the desired action:

- Use **HTTP registry webhooks** when the downstream system exposes an HTTP endpoint (e.g., Slack, a CI/CD pipeline hook, or a custom microservice).
- Use **job registry webhooks** when the desired reaction is an automated Databricks job run (e.g., retraining, model validation, or deployment orchestration), especially when the job resides in a Databricks workspace.

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md)
- Webhook Events
- [MLflow](/concepts/mlflow.md)
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md)
- IP Access Lists
- [Audit Logging](/concepts/abac-policy-audit-logging.md)

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
