---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1978886bea0a5746193df10e16dbfe48a5fb76ee9eebe4bf86bc92d257496a6d
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-commands
    - ARCC
    - AI Runtime CLI Command Reference
    - AI Runtime CLI command reference
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: AI Runtime CLI Commands
description: The set of CLI commands (air run, air logs, air list runs, air cancel) used to submit, monitor, and manage training jobs.
tags:
  - cli
  - commands
  - databricks
timestamp: "2026-06-18T10:43:35.397Z"
---

# AI Runtime CLI Commands

The **AI Runtime CLI (`air`)** provides several subcommands for submitting, monitoring, and managing machine‑learning workloads. This page documents every subcommand, its flags, and common usage patterns.  
The same information is always available from the CLI itself via `air --help` or `air <command> --help`. The CLI help reflects the exact version installed and is the source of truth if it differs from this documentation. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Subcommand reference

| Command | Purpose |
|---|---|
| `air run` | Submit a workload defined by a YAML configuration file. |
| `air get run` | Show metadata, status, and configuration for a specific run. |
| `air list runs` | List recent runs. |
| `air logs` | Stream or download logs for a run. |
| `air cancel` | Cancel a running workload. |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

### `air run`

Submit a workload defined by a YAML file.

**Flags**

| Flag | Purpose |
|---|---|
| `--file` | Path to the YAML configuration file (required). |
| `--watch` | Stream logs until the run completes. |
| `--dry-run` | Validate the configuration without submitting. |
| `--override` | Override YAML fields from the command line (repeatable). |
| `--idempotency-key` | A unique key that makes the submission safely retryable. If the same key has been used before, the existing run is returned instead of creating a new one. |
| `--email` | Send an email notification when the run completes. |
| `-p`, `--profile` | Use a specific Databricks CLI authentication profile. |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

**Examples**

```bash
# Basic submission
air run --file train.yaml

# Watch logs until completion
air run --file train.yaml --watch

# Override compute resources
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120

# Validate configuration only
air run --file train.yaml --dry-run

# Safely retryable submission
air run --file train.yaml --idempotency-key my-unique-key
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md, ai-runtime-cli-examples-databricks-on-aws.md]

---

### `air get run`

Display metadata, status, and configuration for a specific run.

**Usage**

```bash
air get run <run-id>
```

The output includes clickable links to the run’s MLflow experiment and [MLflow Run](/concepts/mlflow-run.md) in the workspace UI. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

### `air list runs`

List recent runs.

**Flags**

| Flag | Purpose |
|---|---|
| `--limit` | Maximum number of runs to return. |
| `--active` | Show only running workloads. |

**Usage**

```bash
air list runs --limit 10
air list runs --active
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

### `air logs`

Stream or download logs for a run.

**Flags**

| Flag | Purpose |
|---|---|
| `--node` | Target a specific node (default: node 0). |
| `--download-to` | Write logs to a local directory instead of streaming. |

**Usage**

```bash
# Stream logs from node 0
air logs <run-id>

# Stream logs from a specific node
air logs <run-id> --node 2

# Download logs to a local directory
air logs <run-id> --download-to ./logs/
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

### `air cancel`

Cancel a running workload.

**Usage**

```bash
air cancel <run-id>
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## Inline help for YAML configuration

The CLI can show interactive help for the YAML configuration fields without submitting a run:

```bash
air -h config               # Full YAML config reference
air -h config.compute       # Per-field help for the compute section
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## Global flags

The following flags apply to every subcommand. They are described in detail on the [AI Runtime CLI global flags](/concepts/ai-runtime-cli-global-flags.md) page.

| Flag | Purpose |
|---|---|
| `--version` | Print the installed CLI version. |
| `-p`, `--profile` | Use the named Databricks CLI authentication profile. |
| `-h`, `--help` | Show help. When followed by a config path (e.g., `-h config`), show YAML field help. |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## See also

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Overview of the tool
- [AI Runtime CLI global flags](/concepts/ai-runtime-cli-global-flags.md) — Detailed documentation of shared flags
- AI Runtime CLI quickstart — Step‑by‑step guide to submitting your first run
- Workload YAML reference — Full specification of the YAML configuration format

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md
- ai-runtime-cli-examples-databricks-on-aws.md
- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
2. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
