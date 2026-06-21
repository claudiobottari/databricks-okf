---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26bd49368fe79351beec7c8765e87ea667986b9ce4aa68c8109b616d7e79e400
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-for-endpoint-testing
    - SPAFET
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Service Principal Authentication for Endpoint Testing
description: Using Databricks service principals with OAuth tokens, secret scopes, and Can Query permissions to authenticate load tests against model serving endpoints.
tags:
  - authentication
  - databricks
  - security
  - oauth
timestamp: "2026-06-19T14:23:14.939Z"
---

# Service Principal Authentication for Endpoint Testing

**Service Principal Authentication for Endpoint Testing** refers to the process of using a Databricks Service Principal to authenticate load test clients against [Model Serving endpoints](/concepts/model-serving-endpoint.md). This approach is required when running automated load tests—such as those using the [Locust framework](/concepts/locust-load-testing-framework.md)—against route-optimized endpoints, because the test tooling must programmatically generate OAuth tokens with permission to query the endpoint.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

When performing load testing on a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md), the test client (e.g., Locust) needs to authenticate with each request. Rather than using a user's personal credentials—which are unsuitable for automated, high-volume scenarios—a service principal provides a secure, non-interactive identity that can be granted fine-grained permissions and rotated independently of any individual user.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Setup Steps

### 1. Create a Databricks Service Principal

Create a service principal in your Databricks workspace following the standard administrative workflow.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 2. Grant Endpoint Permissions

Navigate to the Model Serving endpoint page, open the **Permissions** tab, and grant the service principal **Can Query** level permissions. This authorization allows the service principal to invoke the endpoint during load tests.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 3. Create a Secret Scope

Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md) that will store the service principal's credentials securely. The secrets within this scope are referenced by the load test notebook at runtime.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 4. Store Credentials as Secrets

Store two values in the secret scope:

| Secret Key | Value |
|------------|-------|
| `service_principal_client_id` | The client ID (Application ID) of the Databricks service principal |
| `service_principal_client_secret` | The client secret generated for the service principal |

These secrets are used by the load test framework to generate OAuth tokens for each request against the endpoint.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## How Authentication Works in the Load Test

The Locust load test notebook reads the service principal credentials from the Databricks secret scope at startup. It then uses those credentials to obtain OAuth tokens, which are attached as authentication headers to every HTTP request sent to the model serving endpoint during the test. This ensures that all concurrent client connections are properly authenticated.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints being tested
- [Locust Framework](/concepts/locust-load-testing-framework.md) — The open-source load testing tool used
- OAuth Token Generation — The authentication mechanism used for programmatic access
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md) — A type of endpoint that requires service principal authentication for load testing
- [Endpoint Concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md) — The number of concurrent requests an endpoint can handle, which load tests measure
- Service Principal Permissions — How to grant and manage access for service principals

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
