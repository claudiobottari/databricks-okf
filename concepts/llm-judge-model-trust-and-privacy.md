---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b3700b9beaa7529715f99cea0b5e4de13d7edf92945aad9f5d8e1b5762bcca7
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-model-trust-and-privacy
    - Privacy and LLM Judge Model Trust
    - LJMTAP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: LLM Judge Model Trust and Privacy
description: Information about the models powering LLM judges, including Azure OpenAI hosting, regional data residency, opt-out of abuse monitoring, and the ability to disable partner-powered models.
tags:
  - security
  - privacy
  - llm-evaluation
  - databricks
timestamp: "2026-06-19T17:55:42.386Z"
---

# LLM Judge Model Trust and Privacy

**LLM Judge Model Trust and Privacy** refers to the data handling, regional hosting, and opt-out mechanisms that govern how [LLM Judges](/concepts/llm-judges.md) — the models used to evaluate GenAI agent outputs — process user prompts and responses. Databricks provides transparency about third-party services, regional hosting, and the ability to disable partner-powered models to address privacy concerns.

## Third-Party Services and Abuse Monitoring

LLM judges may use third-party services to evaluate GenAI applications, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of **Abuse Monitoring**, meaning no prompts or responses are stored with Azure OpenAI. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Regional Hosting

For workspaces in the European Union (EU), LLM judges use models hosted in the EU. All other regions use models hosted in the United States. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Partner-Powered AI Features

Disabling [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the LLM judge from calling partner-powered models. If partner-powered models are disabled, you can still use LLM judges by providing your own model (via the `model` argument in the judge definition, specifying `<provider>:/<model-name>`). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Usage Restrictions

LLM judges are intended to help customers evaluate their GenAI agents and applications. The outputs of LLM judges should **not** be used to train, improve, or fine-tune an LLM. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) – How to write pass/fail criteria for GenAI evaluation.
- [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) – Controls for partner model access.
- Azure OpenAI – Third-party service used by some LLM judges.
- Data residency – Regional hosting considerations for EU vs. US workspaces.
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – Building your own judges when partner models are disabled.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
