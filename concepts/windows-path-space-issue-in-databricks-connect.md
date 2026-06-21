---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1fbf22d7dcd60e2c649e963db7ca426a46f80c90ffcf58fd61d2b29415fb902d
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - windows-path-space-issue-in-databricks-connect
    - WPSIIDC
  citations:
    - file: troubleshooting-databricks-connect-for-python-databricks-on-aws.md
title: Windows Path Space Issue in Databricks Connect
description: On Windows, Databricks Connect fails with a filename syntax error if installed into a directory path containing spaces; workarounds include using a space-free path or the short name form.
tags:
  - databricks-connect
  - windows
  - troubleshooting
timestamp: "2026-06-19T23:14:45.571Z"
---

# Windows Path Space Issue in [Databricks Connect](/concepts/databricks-connect.md)

The **Windows Path Space Issue in Databricks Connect** is a common installation error that occurs when [Databricks Connect](/concepts/databricks-connect.md) is installed into a directory whose full path contains a space (for example, `C:\Program Files\...`). The error prevents [Databricks Connect](/concepts/databricks-connect.md) from running properly on Windows. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Error Message

When the issue occurs, the user sees the following error message:

```
The filename, directory name, or volume label syntax is incorrect.
```

^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Cause

[Databricks Connect](/concepts/databricks-connect.md) is installed into a directory path that contains a space. On Windows, tools such as `spark-shell` and other Spark-related binaries may fail when the installation path includes spaces because the command-line parsing does not correctly handle the quoted path. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Workarounds

Two workarounds are available:

1. **Install [Databricks Connect](/concepts/databricks-connect.md) into a directory path that contains no spaces.**  
   For example, choose a path like `C:\DatabricksConnect\` instead of `C:\Program Files\DatabricksConnect\`.

2. **Configure the system `PATH` using the short name (8.3) form of the directory.**  
   On Windows, folders with spaces have a short name alias (e.g., `C:\PROGRA~1\`). Set the `PATH` environment variable to use this short form rather than the long name with spaces. See [StackOverflow: How do I specify C:\Program Files without a space in it for programs that can't](https://stackoverflow.com/questions/892555/how-do-i-specify-c-program-files-without-a-space-in-it-for-programs-that-cant) for details. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The tool that this issue affects.
- Conflicting or Missing PATH Entry for Binaries — Another path-related troubleshooting topic for [Databricks Connect](/concepts/databricks-connect.md).
- Python Version Mismatch — Another common [Databricks Connect](/concepts/databricks-connect.md) issue on Windows.
- Databricks Connect Installation — Installation instructions that should account for path spaces.

## Sources

- troubleshooting-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-python-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-python-databricks-on-aws-bb4d5efd.md)
