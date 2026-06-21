---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e534f9f0615a75a596c2e0727c673096fa9ea4ab3944b25f6ff28356a3e55520
  pageDirectory: concepts
  sources:
    - openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-input-safety-restrictions-for-ai-models
    - IISRFAM
  citations:
    - file: openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
title: Image Input Safety Restrictions for AI Models
description: A mitigation requirement that image inputs to AI models must be restricted to low risk and topical images to prevent misuse.
tags:
  - AI-safety
  - multimodal-models
  - content-filtering
timestamp: "2026-06-19T19:50:16.471Z"
---

# Image Input Safety Restrictions for AI Models

**Image Input Safety Restrictions for AI Models** refers to the mandatory safeguards that must be in place when AI models—particularly those from OpenAI deployed on Databricks—accept image inputs. Under the OpenAI high‑risk use case mitigation framework, applications that process images are classified as high risk and require explicit restrictions to prevent misuse. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Specific Requirement

The primary mitigation for applications enabling image inputs is that **such inputs are restricted to low‑risk and topical images**. This means the model must only receive images that pose minimal safety or security risk and that are directly relevant to the application’s intended domain. Unrestricted or out‑of‑scope image uploads are not permitted. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Context

This requirement is part of a broader set of mitigation obligations that end users must implement when using OpenAI models on Databricks. Other high‑risk use cases—such as chat applications, code generation, and user‑facing applications—carry their own mitigations. The image input restriction ensures that models are not exposed to content that could lead to harmful, biased, or otherwise inappropriate outputs. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Related Concepts

- [High‑risk use case](/concepts/openai-high-risk-use-case-mitigation-framework.md) – A classification that triggers additional safety measures.
- OpenAI models on Databricks – The platform context for these restrictions.
- [Input validation](/concepts/inputoutput-based-evaluation.md) – General techniques for filtering user‑supplied content.
- Model safety – Broader practices for responsible AI deployment.
- Applications enabling image inputs – The specific use case addressed by this restriction.

## Sources

- openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md

# Citations

1. [openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md](/references/openai-high-risk-use-case-mitigation-requirements-databricks-on-aws-1a6b8630.md)
