---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3028ac789fed60ceb21e3e56fab73e0f8f06051703011082232282b4e04886cc
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-for-ml-endpoint-load-tests
    - SPAFMELT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Service Principal Authentication for ML Endpoint Load Tests
description: Setting up a Databricks service principal with Can Query permissions and OAuth tokens stored in Databricks secrets to authenticate Locust load tests against model serving endpoints.
tags:
  - authentication
  - service-principal
  - oauth
  - load-testing
timestamp: "2026-06-19T17:50:26.308Z"
---

# Service Principal Authentication for ML Endpoint Load Tests

**Service Principal Authentication for ML Endpoint Load Tests** refers to the process of using a Databricks service principal to authenticate and authorize load testing tools — such as Locust — against a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). This approach enables automated, programmatic access to endpoints during performance testing without relying on individual user credentials.

## Overview

When running load tests against Databricks Model Serving endpoints, the testing framework must authenticate to the endpoint to send requests. Using a service principal provides a secure, non-interactive authentication method suitable for automated load testing workflows. The service principal must have appropriate permissions on the endpoint and be configured to generate OAuth tokens for API access. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Prerequisites

Before configuring service principal authentication for load tests, the following components must be in place:

- A Databricks service principal created in the workspace
- A Model Serving endpoint with route optimization enabled
- A Databricks secret scope to store credentials securely

## Setup Steps

### 1. Create a Service Principal

Create a Databricks service principal following the standard workspace administration procedures. The service principal will act as the identity used by the load testing framework to authenticate against the endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 2. Grant Endpoint Permissions

Navigate to the Model Serving endpoint page in the Databricks workspace. Click **Permissions** and grant the service principal **Can Query** level permissions. This permission level allows the service principal to send inference requests to the endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 3. Create a Secret Scope

Create a Databricks secret scope to securely store the service principal credentials. The secret scope will contain two keys:

- `service_principal_client_id` — The client ID of the Databricks service principal
- `service_principal_client_secret` — The client secret for the Databricks service principal

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 4. Store Credentials in Secrets

Place the service principal's client ID and client secret into the Databricks secret scope. The load testing notebook will retrieve these values at runtime to generate OAuth tokens for endpoint authentication. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Authentication Flow

The load testing framework (such as Locust) uses the stored service principal credentials to generate OAuth tokens. These tokens are then included in requests sent to the route-optimized endpoint, enabling the load test to interact with the endpoint programmatically. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The target endpoint being load tested
- [Locust Load Testing Framework](/concepts/locust-load-testing-framework.md) — The open-source tool used for running load tests
- [OAuth token authentication](/concepts/oidc-vs-bearer-token-authentication.md) — The authentication mechanism used by service principals
- [Databricks secrets](/concepts/databricks-secret-scopes.md) — Secure storage for credentials
- Route optimization — Endpoint configuration that affects load test behavior
- Endpoint concurrency — The number of concurrent requests an endpoint can handle

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
