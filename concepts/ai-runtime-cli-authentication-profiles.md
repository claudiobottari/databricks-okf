---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5757fe605b347a29cde1b856157de120f0dfe5d988921ef25173fa48dd23fdbe
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-authentication-profiles
    - ARCAP
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: AI Runtime CLI authentication profiles
description: The air CLI uses Databricks authentication profiles via the -p/--profile flag, allowing users to select a named credential profile instead of the default.
tags:
  - authentication
  - cli
timestamp: "2026-06-18T14:21:24.244Z"
---

# AI Runtime CLI Authentication Profiles

**AI Runtime CLI authentication profiles** allow users to select a specific Databricks CLI authentication profile when submitting workloads with the `air` CLI, rather than relying on the default profile. This enables switching between different workspaces, service principals, or user identities without modifying the default configuration.

## Overview

The `air` CLI supports a `-p` (or `--profile`) global flag that specifies which named authentication profile to use for a command. When this flag is omitted, the CLI uses the default profile configured for the Databricks CLI. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Usage

The `-p` flag is available on the `air run` command, which submits a workload defined by a YAML file. The profile determines the Databricks workspace and credentials used for the submission. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

```bash
air run --file workload.yaml -p my-production-profile
```

## Supported Commands

The `-p` flag is listed as a supported option for the `air run` command. Other commands such as `air get run`, `air list runs`, `air logs`, and `air cancel` may also accept the flag as a global option, though the source material explicitly documents it for `air run`. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for AI Runtime
- [Databricks CLI authentication profiles](/concepts/databricks-authentication-type.md) — The underlying credential configuration mechanism
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Full list of CLI commands and flags
- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) — The YAML file format for defining AI Runtime workloads

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
