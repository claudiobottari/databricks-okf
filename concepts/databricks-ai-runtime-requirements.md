---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 174bd048665fdcec4cf6cf59547f384d1d901d2f708f4281992d782b8a91d862
  pageDirectory: concepts
  sources:
    - install-the-ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-requirements
    - DARR
    - Databricks Runtime Requirements
  citations:
    - file: install-the-ai-runtime-cli-databricks-on-aws.md
title: Databricks AI Runtime Requirements
description: Prerequisites for using AI Runtime, including a Databricks workspace with AI Runtime enabled and Python 3.10+.
tags:
  - databricks
  - requirements
  - machine-learning
timestamp: "2026-06-19T19:10:23.969Z"
---

# Databricks AI Runtime Requirements

The **Databricks AI Runtime** enables machine learning workflows on Databricks. To use the AI Runtime, a Databricks workspace must have the AI Runtime feature enabled. The specific workspace-level prerequisites are documented separately (see the AI Runtime documentation’s Requirements section). ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## AI Runtime CLI Requirements

To install and use the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`), the following additional requirements apply:

- **Python 3.10 or newer.** ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- A Databricks workspace with AI Runtime enabled. ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- The Databricks CLI, which manages authentication profiles stored in `~/.databrickscfg`. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

The CLI relies on existing Databricks CLI authentication profiles; if you do not already have a profile for your workspace, you must log in first (e.g., `databricks auth login --host <workspace-url>`). ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Command-line tool for managing AI Runtime workloads.
- Databricks CLI – Core CLI for workspace authentication and management.
- [Python](/concepts/python-wheel-task.md) – Required runtime for the AI Runtime CLI.

## Sources

- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. [install-the-ai-runtime-cli-databricks-on-aws.md](/references/install-the-ai-runtime-cli-databricks-on-aws-22b6c9fd.md)
