---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b90bff70a2c192e74ea5e6918cc6fa911b79f96f401d99cc6b08ab6843c3acaa
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - job-registry-webhook-payload-by-job-type
    - JRWPBJT
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Job Registry Webhook Payload by Job Type
description: "Different payload formats for job-triggering webhooks based on job type: notebook/Python wheel jobs get a params dict, Python/JAR/Spark submit jobs get a params list, multi-task jobs get all parameter types populated."
tags:
  - databricks
  - webhooks
  - jobs
  - payload
timestamp: "2026-06-19T23:27:46.242Z"
---

# Job Registry Webhook Payload by Job Type

When a job registry webhook is triggered by a [Workspace Model Registry](/concepts/workspace-model-registry.md) event, the payload sent to the `jobs/run-now` endpoint in the target workspace depends on the type of job being triggered. The payload structure varies between single-task and Multi-task Jobs|multi-task jobs, and within single-task jobs, further differences exist based on the task type. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Single-Task Jobs

Single-task jobs have three distinct payload formats based on the task type of the job being triggered. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

### Notebook and Python Wheel Jobs

For single-task jobs that run notebooks or Python wheels, the payload is a JSON object containing a `job_id` field and a `notebook_params` dictionary. The `notebook_params` dictionary contains a single field, `event_message`, whose value is the webhook payload. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

```json
{
  "job_id": 1234567890,
  "notebook_params": {
    "event_message": "<Webhook Payload>"
  }
}
```

### Python, JAR, and Spark Submit Jobs

For single-task jobs that run Python scripts, JAR files, or Spark Submit tasks, the payload is a JSON object containing a `job_id` field and a `python_params` list. The list contains a single string element which is the webhook payload. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

```json
{
  "job_id": 1234567890,
  "python_params": ["<Webhook Payload>"]
}
```

### All Other Single-Task Jobs

For all other single-task job types not covered above, the payload contains only the `job_id` field with no parameters. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

```json
{
  "job_id": 1234567890
}
```

## Multi-Task Jobs

For multi-task jobs, the payload includes all possible parameter fields to accommodate different task types within the job. The payload contains a `job_id` field and all five parameter fields: `notebook_params`, `python_named_params`, `jar_params`, `python_params`, and `spark_submit_params`. This ensures that the webhook payload is available regardless of which task type is executed within the multi-task job. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

```json
{
  "job_id": 1234567890,
  "notebook_params": {
    "event_message": "<Webhook Payload>"
  },
  "python_named_params": {
    "event_message": "<Webhook Payload>"
  },
  "jar_params": ["<Webhook Payload>"],
  "python_params": ["<Webhook Payload>"],
  "spark_submit_params": ["<Webhook Payload>"]
}
```

## Summary Table

| Job Type | Payload Structure | Parameter Field(s) |
|---|---|---|
| Single-task: Notebook | `notebook_params` with `event_message` | Dictionary |
| Single-task: Python wheel | `notebook_params` with `event_message` | Dictionary |
| Single-task: Python script | `python_params` as list | List (string) |
| Single-task: JAR | `python_params` as list | List (string) |
| Single-task: Spark Submit | `python_params` as list | List (string) |
| Single-task: Other types | No parameters | None |
| Multi-task | All fields populated | All of the above |

## Related Concepts

- [Workspace Model Registry Webhooks](/concepts/workspace-model-registry-webhooks.md) — Overview of webhook functionality and event types
- [Job Registry Webhooks](/concepts/http-vs-job-registry-webhooks.md) — Creating and managing job-triggered webhooks
- HTTP Registry Webhook Payload — Payload format for HTTP endpoint webhooks
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The model registry system that generates webhook events
- [Webhook Security](/concepts/webhook-security-and-verification.md) — HMAC signature verification and IP allowlisting

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
