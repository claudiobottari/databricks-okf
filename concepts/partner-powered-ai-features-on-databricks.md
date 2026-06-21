---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1865fbf419269b2dc04746effd62c20ca2c9d94ded516c7239f74f091e175c11
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partner-powered-ai-features-on-databricks
    - PAFOD
    - Partner-Powered AI Features
    - Partner-powered AI Features
    - Partner-powered AI features
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Partner-powered AI Features on Databricks
description: A prerequisite for using Genie Code, requiring partner-powered AI features to be enabled at both account and workspace level, with supported region and geo availability requirements.
tags:
  - databricks
  - ai
  - compliance
  - geo
timestamp: "2026-06-19T10:43:51.862Z"
---

# Partner-powered AI Features on Databricks

**Partner-powered AI Features** on Databricks refer to platform capabilities—such as Genie Code for agent observability and evaluation—that rely on integration with external AI providers. These features must be explicitly enabled at both the account level and the workspace level before they can be used. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Enabling Partner-powered AI Features

To use any partner-powered AI feature within a Databricks workspace, an account administrator must first enable the feature for the account, and then a workspace administrator must enable it for the specific workspace. The exact steps for enabling this setting are described in the Databricks documentation on [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered). ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Dependencies

Partner-powered AI Features are a prerequisite for certain GenAI observability and evaluation tools. For example, Genie Code for agent observability and evaluation requires that partner-powered AI features be enabled for both the account and the workspace. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- Genie Code for agent observability and evaluation
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Databricks AI Platform
- Account Settings
- Workspace Settings

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
