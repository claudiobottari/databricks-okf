---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 765e0305bd713989252fc2dd6ca154abd3eb4ca021025da3ed6d9e57e5dc6c3e
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-windows-path-space-restriction
    - DCWPSR
  citations:
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Windows path space restriction
description: Databricks Connect fails on Windows when installed into a directory path containing spaces; workarounds include using short name forms or space-free paths.
tags:
  - databricks
  - windows
  - installation
timestamp: "2026-06-19T23:15:16.561Z"
---

Here is the wiki page for "[Databricks Connect](/concepts/databricks-connect.md) Windows path space restriction".

---

## [Databricks Connect](/concepts/databricks-connect.md) Windows Path Space Restriction

The **Databricks Connect Windows path space restriction** is a known issue that occurs when [Databricks Connect](/concepts/databricks-connect.md) for Scala is installed or executed from a directory path containing spaces on a Windows operating system. This restriction prevents [Databricks Connect](/concepts/databricks-connect.md) from functioning correctly and produces a specific error message. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Error Message

When this restriction is encountered, users see the following error:

```
The filename, directory name, or volume label syntax is incorrect.
```

^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Cause

[Databricks Connect](/concepts/databricks-connect.md) was installed into a directory with a space in the path. This is a known compatibility issue with the way [Databricks Connect](/concepts/databricks-connect.md) resolves file paths on Windows. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Solutions

There are two workarounds for this restriction: ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

1. **Install into a path without spaces**: Reinstall [Databricks Connect](/concepts/databricks-connect.md) into a directory path that contains no spaces. For example, use `C:\Users\username\databricks-connect` instead of `C:\Program Files\databricks-connect`. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

2. **Use the short name form**: Configure your path using the Windows short name (8.3 filename) form. For example, replace a path like `C:\Program Files` with its short form `C:\PROGRA~1`. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting IDEs and applications to Databricks clusters
- Troubleshooting Databricks Connect — General guidance for resolving connection issues
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The Scala-specific client for [Databricks Connect](/concepts/databricks-connect.md)
- Environment variables for Databricks Connect — Common configuration variables that may also be affected by path issues

### Sources

- troubleshooting-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
