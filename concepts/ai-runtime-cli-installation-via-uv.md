---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcce1cdcc7904c3d718c1eef5c8e7e0bb7d585fc5e98df2c624a248707d5708b
  pageDirectory: concepts
  sources:
    - install-the-ai-runtime-cli-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-installation-via-uv
    - ARCIVU
    - AI Runtime (air) CLI Installation
    - AI Runtime CLI installation
    - AI Runtime CLI Installation and Authentication
  citations:
    - file: install-the-ai-runtime-cli-databricks-on-aws.md
title: AI Runtime CLI Installation via uv
description: The recommended method to install the air CLI is using the uv Python package manager, which isolates the tool in its own environment.
tags:
  - installation
  - python
  - cli
timestamp: "2026-06-19T19:10:14.857Z"
---

# AI Runtime CLI Installation via uv

The **AI Runtime CLI** (`air`) is a command-line tool for managing workloads on Databricks AI Runtime. Databricks recommends installing the CLI using `uv`, a fast Python package and project manager, as this method isolates the CLI in its own environment and avoids conflicts with other Python installations used for training code. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

The AI Runtime CLI is currently in **Beta**. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Requirements

Before installing the AI Runtime CLI, you must have:

- **Python 3.10 or newer** installed on your system. ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- A **Databricks workspace with AI Runtime enabled**. See the [AI Runtime](/concepts/ai-runtime.md) requirements documentation for details. ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- The **Databricks CLI** installed and configured, because the AI Runtime CLI reuses Databricks CLI authentication profiles stored in `~/.databrickscfg`. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Install the CLI

To install the AI Runtime CLI with `uv`, run the following command in a terminal:

```bash
uv tool install --force databricks-air --python 3.12
```

^[install-the-ai-runtime-cli-databricks-on-aws.md]

- `uv tool install` creates an isolated environment for the `air` binary and adds it to your `PATH`, so it does not interfere with the Python interpreter used for training code. ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- The `--force` flag ensures the tool is installed even if a previous version exists. ^[install-the-ai-runtime-cli-databricks-on-aws.md]
- Specifying `--python 3.12` is recommended but optional. If omitted, `uv` uses the latest available Python version that satisfies the package's constraints. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

If you do not already have `uv` installed, install it first with the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

^[install-the-ai-runtime-cli-databricks-on-aws.md]

After installation, verify that the CLI is available by running:

```bash
air --help
```

^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Authenticate

The AI Runtime CLI reuses authentication profiles from the Databricks CLI. To set up authentication:

1. Log in to your Databricks workspace and name the profile when prompted:
   ```bash
   databricks auth login --host https://<your-workspace>.cloud.databricks.com
   ```
   ^[install-the-ai-runtime-cli-databricks-on-aws.md]

2. Pass the profile name to any `air` command using the `-p` flag:
   ```bash
   air list runs -p my-workspace
   ```
   ^[install-the-ai-runtime-cli-databricks-on-aws.md]

Alternatively, set the `DATABRICKS_CONFIG_PROFILE` environment variable in your shell to make a profile the default:
   ```bash
   export DATABRICKS_CONFIG_PROFILE=my-workspace
   ```
   ^[install-the-ai-runtime-cli-databricks-on-aws.md]

For all supported authentication options, see the documentation on Databricks CLI authentication. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Next Steps

After installing and authenticating, you can define workloads in a `train.yaml` configuration file with inline dependencies. Start with the AI Runtime CLI quickstart and refer to the Workload YAML reference as you build out your configuration. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md)
- uv
- Databricks CLI
- [AI Runtime](/concepts/ai-runtime.md)
- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md)
- Authentication for the Databricks CLI

## Sources

- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. [install-the-ai-runtime-cli-databricks-on-aws.md](/references/install-the-ai-runtime-cli-databricks-on-aws-22b6c9fd.md)
