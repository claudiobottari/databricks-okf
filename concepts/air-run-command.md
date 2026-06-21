---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 268307260734cbf291063e8baabfcb8b6c446333fcf4d2f90f0baa403406e95e
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-command
    - ARC
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: air run command
description: The primary CLI command used to submit AI training workloads, with support for YAML config files, field overrides, dry-run validation, idempotency keys, and log watching.
tags:
  - databricks
  - cli
  - command-reference
timestamp: "2026-06-19T22:03:23.093Z"
---

```markdown
---
title: air run command
summary: Submits a workload defined by a YAML file to Databricks AI Runtime, supporting flags for file path, watch mode, dry-run, overrides, idempotency keys, email notifications, and authentication profiles.
sources:
  - ai-runtime-cli-command-reference-databricks-on-aws.md
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:42:10.309Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - cli
  - command
  - workload-submission
aliases:
  - air-run-command
  - ARC
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# air run command

The `air run` command submits a workload defined by a YAML configuration file to the [[AI Runtime Environments|AI Runtime (Preview)|AI Runtime]] platform. It is a core subcommand of the [[AI Runtime CLI|AI Runtime CLI (Beta)]]. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Syntax

```bash
air run [flags]
```

## Flags

| Flag               | Purpose                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--file`           | Path to the YAML configuration file that defines the workload.                                                                                              |
| `--watch`          | Stream logs to the terminal in real time after submission and wait for completion.                                                                          |
| `--dry-run`        | Validate the configuration without actually submitting the workload.                                                                                        |
| `--override`       | Override specific YAML configuration fields from the command line (e.g., `--override compute.num_accelerators=32`). Multiple overrides can be space-separated. |
| `--idempotency-key`| Provide a unique key to make the submission safely retryable. If the same key has been used before, the existing run is returned instead of creating a new one.|
| `--email`          | Email address to notify when the run completes.                                                                                                             |
| `-p`, `--profile`  | Use a named Databricks CLI authentication profile instead of the default.                                                                               |

^[ai-runtime-cli-command-reference-databricks-on-aws.md, ai-runtime-cli-quickstart-databricks-on-aws.md]

## Description

The `air run` command reads a [[train.yaml Workload Configuration|YAML workload configuration]] that defines the experiment name, compute requirements (e.g., number of accelerators, accelerator type), optional environment dependencies, and the command to execute. After submission, the CLI uploads any local code configured in the `code_source` section, submits the job to AI Runtime, and prints a run ID. That run ID is used to inspect the workload with other CLI commands. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The submission creates a run inside the [[MLflow experiment]] named in the `experiment_name` field of the YAML configuration. The run captures metrics, parameters, artifacts, and logs, all viewable in the workspace [[MLflow|MLflow UI]]. Logs are also accessible outside MLflow via `air logs`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

When `--watch` is supplied, the CLI streams logs from node 0 to the terminal until the workload finishes. For distributed workloads, logs from other nodes can be retrieved later with `air logs --node`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The `--dry-run` flag validates the YAML configuration without executing the workload, which helps catch configuration errors early. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The `--idempotency-key` flag makes the submission idempotent: if the same key is reused, the CLI returns the existing run rather than launching a duplicate. This is useful for retry-safe pipelines. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Examples

**Submit a workload and watch the logs**:
```bash
air run --file train.yaml --watch
```

**Validate the configuration without submitting**:
```bash
air run --file train.yaml --dry-run
```

**Override YAML fields from the command line**:
```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

**Idempotent submission**:
```bash
air run --file train.yaml --idempotency-key my-unique-key
```

---

## Global Flags

The `air run` command also accepts the following global flags from the AI Runtime CLI:

| Flag        | Purpose                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `--version` | Print the installed CLI version.                                                                                                             |
| `-h`, `--help` | Show help for the command. When followed by a config path (e.g., `air -h config.compute`), show per-field YAML help.                       |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Commands

- `air get run` – Show metadata, status, and configuration for a specific run.
- `air list runs` – List recent runs (`--limit`, `--active`).
- `air logs` – Stream or download logs for a run (supports `--node`, `--download-to`).
- `air cancel` – Cancel a running workload.

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## See Also

- [[AI Runtime CLI Commands|AI Runtime CLI command reference]] — Full list of available `air` subcommands.
- AI Runtime CLI quickstart — Step-by-step guide to submitting a first workload.
- Workload YAML reference — Detailed documentation for the YAML configuration fields.
- Track runs with MLflow and the Jobs run page — Monitoring and tracking submitted runs.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md
- ai-runtime-cli-quickstart-databricks-on-aws.md
```

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
2. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
