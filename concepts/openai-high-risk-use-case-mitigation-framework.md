---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 215f11549c2bd324423f3353b3ff9250aea9a8a729e050de432490ec993579c2
  pageDirectory: concepts
  sources:
    - openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-high-risk-use-case-mitigation-framework
    - OHRUCMF
    - OpenAI High Risk Use Case Mitigation
    - High‑risk use case
  citations:
    - file: openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
title: OpenAI High Risk Use Case Mitigation Framework
description: A structured set of mitigation requirements that end users must implement when deploying OpenAI models for high-risk use cases on Databricks.
tags:
  - AI-governance
  - risk-management
  - OpenAI
  - Databricks
timestamp: "2026-06-19T19:50:04.227Z"
---

# OpenAI High Risk Use Case Mitigation Framework

The **OpenAI High Risk Use Case Mitigation Framework** defines the set of mandatory requirements that end users must implement when using OpenAI models on Databricks for designated high‑risk use cases. Databricks requires these mitigations to ensure responsible and secure deployment; the responsibility for implementing them lies with the user. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Mitigation Requirements

The framework categorises high‑risk use cases into four types and prescribes a specific mitigation for each:

| High‑risk use case | Description | Mitigation |
|-------------------|-------------|------------|
| **Applications involving chat or conversations** | Applications that enable users to interact with a conversational agent | Verify that the application is **grounded or topical** – users must not have unrestricted access to query the model with general inputs that generate unrestricted outputs. |
| **Applications accessible to users outside your organisation** | Any application where end users are external to the organisation | Authenticate or monitor such users through at least one of the following: two‑factor or multi‑factor authentication; logging of individual end‑user IDs for visibility and remediation; or logging of individual IP addresses for visibility and remediation. |
| **Applications involving code generation or transformation scenarios** | Applications that generate or transform code | **Conduct human review** of any code before it is used in production, and limit user‑based risk by either restricting code generation to internal users or implementing client‑side monitoring for misuse. |
| **Applications enabling image inputs** | Applications that accept images as input | Ensure that image inputs are restricted to **low‑risk and topical** images only. |

^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## User Responsibility

The framework does not rely on platform‑enforced controls; it places the onus on the end user to implement the listed mitigations in their own infrastructure and application logic. Failure to meet these requirements may affect compliance with Databricks’ terms of service for OpenAI model use. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Related Concepts

- OpenAI Model Serving on Databricks – How OpenAI models are deployed and served.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – General model serving infrastructure.
- Responsible AI – Broader principles for safe AI deployment.
- Human-in-the-loop – Human review pattern referenced for code generation scenarios.
- Authentication and Monitoring – User authentication and logging mechanisms.

## Sources

- openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md

# Citations

1. [openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md](/references/openai-high-risk-use-case-mitigation-requirements-databricks-on-aws-1a6b8630.md)
