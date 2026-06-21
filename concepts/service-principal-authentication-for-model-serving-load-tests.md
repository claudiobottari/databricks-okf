---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa40f47f2eb161f4c6f72fd5841e30b4a7668a18fdb3d70b6b3f4679810fa1b4
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-for-model-serving-load-tests
    - SPAFMSLT
    - Service Principal Authentication for Model Serving
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Service Principal Authentication for Model Serving Load Tests
description: Setting up a Databricks service principal with Can Query permissions on the endpoint, storing its client ID and secret in a Databricks secret scope, and generating OAuth tokens for authenticating Locust load test traffic.
tags:
  - authentication
  - service-principal
  - oauth
timestamp: "2026-06-18T14:42:41.555Z"
---

# Service Principal Authentication for Model Serving Load Tests

**Service Principal Authentication for Model Serving Load Tests** refers to the process of using a Databricks service principal to generate OAuth tokens that authorize a Locust-based load test to query a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). This authentication method is required to interact with route-optimized endpoints during performance testing.

## Overview

When running a load test against a Databricks model serving endpoint using Locust, the test script must authenticate with the endpoint. To support automated, non-interactive testing, a service principal is used instead of a user identity. The service principal receives the appropriate permissions, and its credentials are stored securely in a [secret scope](/concepts/databricks-secret-scopes.md) so the Locust test can retrieve them and generate OAuth tokens at runtime. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Setup Steps

### 1. Create a Service Principal

Create a Databricks service principal in the workspace. This identity will be used by the load test to authenticate. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 2. Grant Query Permissions

Navigate to the model serving endpoint page, click **Permissions**, and assign the service principal the **Can Query** level permission. This ensures the principal has the right to invoke the endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 3. Create a Secret Scope

Create a Databricks secret scope to store the service principal’s credentials. Inside the scope, add two keys:

- `service_principal_client_id` – the client ID of the service principal.
- `service_principal_client_secret` – the client secret associated with the service principal.

The load test notebook reads these secrets to authenticate. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 4. Configure the Load Test Notebook

In the Locust load test notebook, configure the notebook variables to reference the secret scope and the keys created in the previous step. The test script (`fast-load-test.py`) uses these credentials to generate OAuth tokens and authenticate against the endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The model serving endpoint must be created with route optimization enabled (the Locust test is designed for route-optimized CPU endpoints). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- The service principal must have the `Can Query` permission on the endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- The secret scope must be created and populated before running the notebook. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Service Principal – A non-human identity used for automated workflows.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The endpoint that serves machine learning models for inference.
- OAuth Token – The token type used to authenticate requests to the endpoint.
- Locust – The open-source load testing framework used in the example notebook.
- [Secret Scope](/concepts/databricks-secret-scopes.md) – A secure store for sensitive credentials.
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) – General guidance on load testing model serving.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
