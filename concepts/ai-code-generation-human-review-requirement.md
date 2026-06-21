---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e69e2b68805c6d9452a1791c11e079664433a55bc6d84db30ce1adf335aca7c
  pageDirectory: concepts
  sources:
    - openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-code-generation-human-review-requirement
    - ACGHRR
  citations:
    - file: openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
title: AI Code Generation Human Review Requirement
description: A safety requirement that all AI-generated code must undergo human review before production use, with additional restrictions for external users.
tags:
  - AI-code-generation
  - software-safety
  - human-in-the-loop
timestamp: "2026-06-19T19:50:09.906Z"
---

# AI Code Generation Human Review Requirement

The **AI Code Generation Human Review Requirement** is a mitigation requirement that applies when using OpenAI models on Databricks for applications involving code generation or transformation scenarios. Under this requirement, all code produced by an AI model must be reviewed by a human before it is used in production. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Scope

This requirement is part of the larger set of OpenAI high‑risk use case mitigation requirements. It specifically targets any application that leverages OpenAI models to generate or transform code, such as code completion, refactoring, script generation, or automated programming assistance. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Requirement Details

When using OpenAI for code generation or transformation, you must:

1. **Conduct human review** of any code before it is used in production. A human must verify the correctness, security, and appropriateness of the generated code.
2. **Limit user‑based risk** by either:
   - Restricting code generation to internal users only, or
   - Implementing client‑side monitoring to detect and prevent misuse.

^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Rationale

AI‑generated code may contain subtle bugs, security vulnerabilities, or logic errors that automated checks alone cannot reliably catch. Human review helps ensure that the code meets organizational standards and does not introduce risks into production systems. Restricting access to internal users or monitoring client‑side usage further reduces the attack surface and allows for faster detection of anomalous behavior. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Related Concepts

- AI Safety and Governance – Broader principles for responsible AI deployment.
- Code Review Workflow – Processes for reviewing code changes in CI/CD pipelines.
- OpenAI High Risk Use Case Mitigation – The full set of mitigation requirements for OpenAI models on Databricks.
- [Production Monitoring](/concepts/production-monitoring.md) – Techniques for monitoring model outputs and usage patterns.
- Model Governance on Databricks – Policies and tools for managing AI models.

## Sources

- openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md

# Citations

1. [openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md](/references/openai-high-risk-use-case-mitigation-requirements-databricks-on-aws-1a6b8630.md)
