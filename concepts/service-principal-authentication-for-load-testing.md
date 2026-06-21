---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8555e8057563609ad1db1a50cd9b6a6c5bd4c414f212f8953f4fe245bfc853ca
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-for-load-testing
    - SPAFLT
    - Service principal setup for load testing
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Service Principal Authentication for Load Testing
description: Setting up a Databricks Service Principal with OAuth token generation and secret-scoped credentials to authenticate load test clients against route-optimized model serving endpoints.
tags:
  - authentication
  - security
  - model-serving
timestamp: "2026-06-19T09:22:21.356Z"
---

```markdown
---
title: Service Principal Authentication for Load Testing
summary: Setup process for creating a Databricks Service Principal with Can Query permissions and storing OAuth credentials in Databricks secrets for load test authentication
sources:
  - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:07:34.936Z"
updatedAt: "2026-06-18T11:07:34.936Z"
tags:
  - databricks
  - authentication
  - security
aliases:
  - service-principal-authentication-for-load-testing
  - SPAFLT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Service Principal Authentication for Load Testing

**Service principal authentication for load testing** refers to the use of a Databricks service principal and OAuth tokens to authenticate requests to a [[Custom Model Serving Endpoint Support|custom model serving endpoint]] during performance tests. This approach is required when using the Locust load-testing framework against route-optimized endpoints, because Locust must generate OAuth tokens with permission to query the endpoint.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Setup Steps

The following steps are performed outside the load-test notebook, typically by an administrator or developer:

1. **Create a Databricks service principal** – Follow the workspace administration instructions to add a service principal.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
2. **Grant endpoint permissions** – In the Model Serving endpoint UI, navigate to **Permissions** and assign the service principal the **Can Query** privilege.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
3. **Create a secret scope** – Use the Databricks secrets API or CLI to create a secret scope that will store the service principal credentials.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
4. **Store credentials as secrets** – Within the secret scope, store two keys:
   - `service_principal_client_id` – the client ID of the service principal.
   - `service_principal_client_secret` – the client secret of the service principal.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## How It Works

The load-test notebook (based on the Locust framework) reads the service principal credentials from Databricks Secrets and uses them to obtain OAuth tokens. These tokens are then attached to each HTTP request sent to the serving endpoint. The supporting script `fast-load-test.py` validates the authentication token and reads the payload from `input.json` before the test begins.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Because the endpoint is route-optimized, the load test must generate tokens that are scoped to the endpoint’s permission model. Using a service principal ensures that the test identity is distinct from any individual user, which is a best practice for automated testing.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Locust and Authentication

Locust is an open-source load-testing framework used in the example notebook. It relies on CPU resources to generate traffic and automatically detects the number of CPU cores to maximize throughput. The Locust test uses the `--processes -1` flag to enable multi-core utilization. Authentication is handled transparently via the service principal OAuth token, and Locust does not need to manage user sessions.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- Use a dedicated service principal rather than a personal user account to avoid credential expiry tied to an individual and to separate test permissions from production access.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- Store the client ID and client secret in a [[Databricks Secret Scopes|secret scope]] with restricted access; avoid hard-coding them in notebooks or scripts.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- Grant only the minimum permissions needed (`Can Query` on the endpoint) to the service principal.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Service Principal – A Databricks identity used for automated workflows.
- [[Model Serving Endpoint]] – The endpoint that serves custom models and is the target of the load test.
- OAuth – The token-based authentication protocol used to authorize requests to the endpoint.
- Databricks Secrets – Secure storage for credentials like client IDs and secrets.
- Locust – The open-source load-testing framework used in the example notebook.
- [[Route optimization for serving endpoints]] – An endpoint configuration that requires OAuth token authentication.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
