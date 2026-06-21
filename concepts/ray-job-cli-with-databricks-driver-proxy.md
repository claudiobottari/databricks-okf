---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 838b2ef27b1f918d1e47a4cb773fe2841a42fd0d674c4ff39515c42b8bf4949b
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-job-cli-with-databricks-driver-proxy
    - RJCWDDP
    - Databricks Driver Proxy
    - Databricks driver proxy
    - ray-job-cli-integration-via-databricks-driver-proxy
    - RJCIVDDP
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Job CLI with Databricks Driver Proxy
description: Connecting the Ray Job CLI to a Databricks-hosted Ray cluster through the driver proxy endpoint for external job submission
tags:
  - ray
  - databricks
  - cli
timestamp: "2026-06-19T17:57:58.439Z"
---

--- Existing page content (front matter) is kept as provided. Below is the updated body.

---

# Ray Job CLI with Databricks Driver Proxy

The **Ray Job CLI with Databricks Driver Proxy** describes how to submit Ray jobs to a [Ray cluster](/concepts/global-mode-ray-cluster.md) running on Databricks using the standard `ray job submit` command, with the connection routed through the Databricks driver proxy. This workflow is primarily intended for developers migrating from self-managed Ray solutions who already have infrastructure tooling built around the Ray CLI tools. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connection Command

Databricks does not support direct integration with the Ray Cluster CLI, but the Ray Job CLI can be connected through the driver proxy to the Ray cluster running on Databricks. The connection is established by providing a custom `--address` URL and authentication headers to the `ray job submit` command. The general form of the command is:

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Configuring the Address and Headers

The `--address` value must contain the Databricks workspace URL (beginning with `https://`) followed by `/driver-proxy/o/` and the remainder of the path. The path segment after `/driver-proxy/o/` is identical to the value shown in the Ray Dashboard proxy URL that appears after the Ray cluster is started. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

The `--headers` flag passes authentication credentials. The required cookie is `DATAPLANE_DOMAIN_SESSIONID`, and its value must be replaced with a valid session token for the workspace. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Usage Context

The Ray Job CLI is used for submitting jobs to a Ray cluster from external systems. However, it is **not required** for submitting jobs on Ray clusters on Databricks. Databricks recommends using its native tooling instead:

- Deploy the job using [Lakeflow Jobs](/concepts/lakeflow-jobs.md).
- Create a Ray cluster per application.
- Use Databricks Asset Bundles or Workflow Triggers to trigger the job.

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray cluster](/concepts/global-mode-ray-cluster.md) — The distributed compute environment created on Databricks.
- Ray Dashboard — The web UI for monitoring Ray clusters, whose proxy URL provides the address suffix.
- [Databricks driver proxy](/concepts/ray-job-cli-with-databricks-driver-proxy.md) — The mechanism that routes external traffic to services running within a Databricks cluster.
- Databricks Asset Bundles — Recommended tool for packaging and deploying production jobs.
- Workflow Triggers — Method for scheduling and triggering job runs.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Databricks job orchestration service.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
