---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 729f72224cf9839f32d835db579cf35afd811b7c845bd4bbb53c04d781bf2175
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version-compatibility-for-databricks-connect
    - VCFDC
    - Version Support Matrix for Databricks Connect
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Version Compatibility for Databricks Connect
description: Specific version requirements for Databricks Connect including supported Databricks Runtime versions (7.3 LTS to 12.2 LTS), Python minor version matching, and exact package version alignment.
tags:
  - databricks
  - versioning
  - compatibility
  - prerequisites
timestamp: "2026-06-18T11:33:47.346Z"
---

# Version Compatibility for Databricks Connect

**Databricks Connect** allows you to connect popular IDEs, notebook servers, and custom applications to a Databricks cluster, running Spark jobs remotely instead of locally. Correct version compatibility between the client library and the cluster is essential for reliable operation. This page documents the supported Databricks Runtime versions, Python version matching, client package version requirements, and Java requirements. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported Databricks Runtime Versions

Databricks Connect supports only the following Databricks Runtime (DBR) versions:

- Databricks Runtime 12.2 LTS ML, Databricks Runtime 12.2 LTS
- Databricks Runtime 11.3 LTS ML, Databricks Runtime 11.3 LTS
- Databricks Runtime 10.4 LTS ML, Databricks Runtime 10.4 LTS
- Databricks Runtime 9.1 LTS ML, Databricks Runtime 9.1 LTS
- Databricks Runtime 7.3 LTS

These versions cover the legacy Databricks Connect client for DBR 12.2 LTS and below. Newer DBR versions (13.x and above) require a different client setup. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Python Version Requirements

You must install Python 3 on your development machine. The **minor version** of your client Python installation must match the minor Python version installed on your Databricks cluster. For example, if your cluster runs Python 3.9, your local Python must also be 3.9. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The following table shows the Python version shipped with each supported Databricks Runtime:

| Databricks Runtime | Client Python Version |
|-------------------|-----------------------|
| Databricks Runtime 12.2 LTS (ML) | Python 3.10 |
| Databricks Runtime 11.3 LTS (ML) | Python 3.9 |
| Databricks Runtime 10.4 LTS (ML) | Python 3.8 |
| Databricks Runtime 9.1 LTS (ML) | Python 3.7 |
| Databricks Runtime 7.3 LTS | Python 3.7 |

Databricks strongly recommends using a Python virtual environment (such as `venv` or Conda) to manage the correct Python version and avoid conflicts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Databricks Connect Client Package Version

The major and minor version of the `databricks-connect` package must always match the Databricks Runtime version of the cluster. For a cluster running DBR 12.2 LTS, you must install `databricks-connect==12.2.*`. Databricks recommends using the most recent patch release within that series by specifying the `*` wildcard: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
pip3 install --upgrade "databricks-connect==12.2.*"
```

Replace `12.2` with the corresponding version for your cluster (e.g., `11.3`, `10.4`, `9.1`, or `7.3`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Java Runtime Environment

The client requires Java 8 (OpenJDK 8 JRE). It does **not** support Java 11 or later. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Best Practices

- **Always use a Python virtual environment** to isolate the correct Python version and the `databricks-connect` package from other Python projects.
- **Uninstall PySpark before installing Databricks Connect.** The two packages conflict and can cause “stream corrupted” or “class not found” errors. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Verify connectivity** after configuration by running `databricks-connect test`. This checks the Java version, Python version, and cluster connection. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Match the patch version** within the same major.minor series. Using an older patch may miss bug fixes; using a newer patch within the same series is safe.

## Limitations

Databricks Connect for DBR 12.2 LTS and below does **not** support:

- [Unity Catalog](/concepts/unity-catalog.md) (not available with this client version)
- Structured Streaming
- Native Scala, Python, and R APIs for Delta table operations (SQL API is supported)
- `COPY INTO` SQL command
- Global temporary views
- Koalas / `pyspark.pandas`
- Process isolation enabled clusters (`spark.databricks.pyspark.enableProcessIsolation=true`)
- Table access control clusters

For the full list of limitations, see the Databricks Connect documentation. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview and setup guide
- Databricks Runtime — Understanding cluster runtime versions
- Python virtual environment — Recommended isolation for Python dependencies
- JRE — Java Runtime Environment requirements
- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) — Authentication method for client connection
- SparkSession — The entry point for using Databricks Connect

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
