---
title: Install the AI Runtime CLI | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation
ingestedAt: "2026-06-18T08:08:13.116Z"
---

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page describes how to install the `air` CLI and configure authentication against a Databricks workspace.

## Requirements[​](#requirements "Direct link to Requirements")

*   Python 3.10 or newer.
*   A Databricks workspace with AI Runtime enabled. See [Requirements](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/#requirements).
*   The [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install), which manages authentication profiles in `~/.databrickscfg`.

## Install the CLI[​](#install-the-cli "Direct link to Install the CLI")

Databricks recommends installing the CLI with [uv](https://docs.astral.sh/uv/):

Bash

    uv tool install --force databricks-air --python 3.12

`uv tool install` puts `air` in its own isolated environment and exposes it on your `PATH`, so it doesn't conflict with the Python interpreter you use for your training code.

`--python 3.12` is recommended but optional. If you do not specify the Python version, `uv` uses the latest available version that satisfies the the package's Python constraint.

If you don't already have `uv`, install it first:

Bash

    curl -LsSf https://astral.sh/uv/install.sh | sh

Verify the installation:

## Authenticate[​](#authenticate "Direct link to Authenticate")

The AI Runtime CLI reuses Databricks CLI authentication profiles. Log in to your workspace and name the profile when prompted:

Bash

    databricks auth login --host https://<your-workspace>.cloud.databricks.com

Pass the profile name to any `air` command with `-p`. For example:

Bash

    air list runs -p my-workspace

Alternatively, set `DATABRICKS_CONFIG_PROFILE` in your shell to make a profile the default:

Bash

    export DATABRICKS_CONFIG_PROFILE=my-workspace

For all authentication options, see [Authentication for the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/authentication).

## Next steps[​](#next-steps "Direct link to Next steps")

After installing, define workloads in a `train.yaml` config with inline dependencies. Start with the quickstart, then use the YAML reference as you build out your config:

*   [AI Runtime CLI quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
