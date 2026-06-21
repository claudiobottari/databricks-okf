---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67f4d255b48b170fd1a913b07774ccbf338627b4de39e0d6fe792ca8adbcf2a5
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-networking-and-security-limitations
    - Security Limitations and Model Serving Networking
    - MSNASL
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Model Serving Networking and Security Limitations
description: Security restrictions for Model Serving endpoints including access control, PrivateLink support, outbound network policies, and security patching policies.
tags:
  - model-serving
  - networking
  - security
  - databricks
timestamp: "2026-06-19T19:43:49.507Z"
---

# Model Serving Networking and Security Limitations

**Model Serving Networking and Security Limitations** describes the network-level constraints, security patching behavior, and compliance requirements that apply to [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints for custom models and AI Agent deployments. These limits are in addition to the resource and payload limits that apply to the same endpoint types. ^[model-serving-limits-and-regions-databricks-on-aws.md]

---

## Ingress and Access Control

Model Serving endpoints are protected by access control and respect all networking-related ingress rules that are configured on the workspace. This includes IP allowlists and PrivateLink connections that restrict which networks or users can reach the endpoint. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## PrivateLink to External Endpoints

By default, Model Serving does not support PrivateLink to external endpoints (that is, endpoints that are not hosted inside the Databricks workspace VPC). Support for this functionality is evaluated and implemented on a per-region basis. Customers who require this capability should contact their Databricks account team for the latest availability information. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Security Patches for Model Images

Model Serving does **not** provide security patches to existing model images after they are deployed. This policy exists because updating a running container image could destabilize production deployments. Instead, security patches are included **only in new model images** that are created when a new model version is registered and deployed. To receive the latest patches, users must create a new endpoint or update an existing endpoint to serve a newer model version. ^[model-serving-limits-and-regions-databricks-on-aws.md]

If a compliance security profile standard is in effect (see below), Databricks attempts to automatically rebuild outdated containers on the customer’s behalf. If that automated rebuild fails, an event log message is generated with guidance on how to bring the endpoint back into compliance, such as re-logging the model. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Outbound Network Access (Egress Control)

You can restrict outbound network access from Model Serving endpoints by configuring network policies for serverless egress control. This allows administrators to control which external destinations the serving container can reach. For details, see the documentation on [Manage network policies for serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies). ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Compliance Security Profile Standards

When a compliance security profile standard (such as HIPAA, PCI DSS, or UK Cyber Essentials Plus) is enabled, served containers must be built in the most recent 30 days. Databricks automatically rebuilds outdated containers to satisfy this requirement. If the automated rebuild job fails, the system logs an event message such as:

> “Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com.”

This compliance requirement applies to **CPU and GPU workloads** for custom models, AI agents, and external models. For [Foundation Model APIs](/concepts/foundation-model-apis.md) workloads (provisioned throughput, pay-per-token, and batch inference using AI Functions and Databricks-hosted models), the same 30-day container freshness rule applies. ^[model-serving-limits-and-regions-databricks-on-aws.md]

> **Note:** Some Foundation Model workloads that require [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) for provisioned throughput are not UK Cyber Essentials Plus compliant. Contact your Databricks account team for details. ^[model-serving-limits-and-regions-databricks-on-aws.md]

---

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The compute infrastructure that serves models.
- IP Allowlists – Ingress rules that restrict client IP addresses.
- PrivateLink – AWS PrivateLink for private connectivity to Databricks workspaces.
- Network Policies for Serverless Egress Control – Mechanisms to restrict outbound traffic.
- Access Control for Serving Endpoints – Permissions and authentication for endpoint usage.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) – Databricks security frameworks for regulated workloads.
- Foundation Model APIs Rate Limits and Quotas – Separate limits for foundation model endpoints.
- [Cross Geography Routing](/concepts/cross-geography-routing-for-global-endpoints.md) – A feature affecting compliance for certain foundation model deployments.

## Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
