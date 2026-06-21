---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4696e2fd50967c2b37124c7f8584b1a7ef3ea6380b94a2702b1a5dd69de61d40
  pageDirectory: concepts
  sources:
    - install-the-ai-runtime-cli-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-authentication-via-databricks-cli-profiles
    - ARCAVDCP
  citations:
    - file: install-the-ai-runtime-cli-databricks-on-aws.md
title: AI Runtime CLI Authentication via Databricks CLI Profiles
description: The air CLI reuses Databricks CLI authentication profiles, which can be passed via the -p flag or the DATABRICKS_CONFIG_PROFILE environment variable.
tags:
  - authentication
  - databricks
  - cli
timestamp: "2026-06-19T19:10:36.462Z"
---

# AI Runtime CLI Authentication via Databricks CLI Profiles

**AI Runtime CLI Authentication via Databricks CLI Profiles** refers to the method by which the `air` CLI authenticates against a Databricks workspace by reusing authentication profiles configured through the Databricks CLI. This approach centralizes credential management and avoids duplicating authentication configuration across tools.

## Overview

The AI Runtime CLI (`air`) does not manage authentication independently. Instead, it relies entirely on Databricks CLI authentication profiles stored in `~/.databrickscfg`. This means users configure their workspace credentials once with the Databricks CLI, and then the AI Runtime CLI automatically inherits those credentials for all `air` commands. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Requirements

- Python 3.10 or newer
- A Databricks workspace with [AI Runtime](/concepts/ai-runtime.md) enabled
- The Databricks CLI installed, which manages authentication profiles in `~/.databrickscfg`

^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Creating a Profile

To create a new authentication profile, log in to your workspace using the Databricks CLI and name the profile when prompted:

```bash
databricks auth login --host https://<your-workspace>.cloud.databricks.com
```

This command stores the profile in `~/.databrickscfg`, which the AI Runtime CLI then reads for authentication. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Specifying a Profile

When running any `air` command, pass the profile name using the `-p` flag:

```bash
air list runs -p my-workspace
```

This explicitly tells the AI Runtime CLI which workspace to authenticate against. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Setting a Default Profile

To avoid passing `-p` with every command, set the `DATABRICKS_CONFIG_PROFILE` environment variable in your shell:

```bash
export DATABRICKS_CONFIG_PROFILE=my-workspace
```

After setting this variable, the AI Runtime CLI uses the specified profile by default for all commands that do not explicitly pass `-p`. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Authentication Options

For all available authentication methods and configuration options, see the Databricks CLI Authentication documentation. The AI Runtime CLI supports the same authentication mechanisms that the Databricks CLI supports, including OAuth tokens, personal access tokens, and Azure AD tokens (on Azure). ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool for managing training workloads
- Databricks CLI — The parent CLI that manages authentication profiles
- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment required for AI Runtime CLI functionality
- ~/.databrickscfg — The configuration file storing authentication profiles
- AI Runtime CLI Quickstart — Getting started guide for the AI Runtime CLI
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — Configuration reference for `train.yaml` files

## Sources

- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. [install-the-ai-runtime-cli-databricks-on-aws.md](/references/install-the-ai-runtime-cli-databricks-on-aws-22b6c9fd.md)
