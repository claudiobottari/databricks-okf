---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34c2751c840f28fe233b0e4570115382117fdb9248caf0f911822acb09432cce
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-global-flags
    - ARCGF
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: AI Runtime CLI global flags
description: Cross-cutting flags available to all air CLI commands, including --version, --profile (-p), and --help (-h).
tags:
  - cli
  - configuration
  - databricks
timestamp: "2026-06-19T22:01:36.914Z"
---

Here is the wiki page for "AI Runtime CLI global flags", written based solely on the provided source material.

---

## AI Runtime CLI global flags

The **AI Runtime CLI** (Beta) provides several global flags that apply to every `air` subcommand. These flags control output, authentication, and help display.

| Flag | Purpose |
|------|---------|
| `--version` | Print the installed CLI version. |
| `-p`, `--profile` | Use the named Databricks CLI authentication profile instead of the default. |
| `-h`, `--help` | Show help. When followed by a config path (e.g., `air -h config.compute`), show YAML field help. |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

The `--version` flag outputs the exact version of the `air` CLI installed. The `--profile` (short form `-p`) flag lets you select a non-default Databricks CLI authentication profile, useful when you manage multiple workspaces or service principals. The `--help` (short form `-h`) flag displays contextual help: basic usage for the top-level command, command-specific flags when placed after a subcommand, and YAML configuration field help when followed by a config path (e.g., `air -h config.compute`). ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

The CLI help output reflects the exact version you have installed, so it is the source of truth if it differs from the documentation. The same information is always available from the CLI itself:

```bash
air --help              # All commands
air <command> --help    # Flags for a specific command
air -h config           # YAML config reference
air -h config.compute   # Per-field help for a YAML section
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related concepts

- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) – complete list of subcommands.
- AI Runtime CLI quickstart – getting started with the CLI.
- Workload YAML reference – detailed configuration schema.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
