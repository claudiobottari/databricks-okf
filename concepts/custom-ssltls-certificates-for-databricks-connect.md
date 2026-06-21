---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8ca676cee1d3e9f93e8d8d85fde080a8758c5fbf0dc7bc123d0901d6b87f544
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-ssltls-certificates-for-databricks-connect
    - CSCFDC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
      start: 52
      end: 54
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
      start: 56
      end: 58
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
      start: 60
      end: 61
title: Custom SSL/TLS Certificates for Databricks Connect
description: Configuring custom SSL/TLS certificates in Databricks Connect via the GRPC_DEFAULT_SSL_ROOTS_FILE_PATH environment variable
tags:
  - databricks
  - security
  - certificates
timestamp: "2026-06-19T13:55:08.331Z"
---

---
title: Custom SSL/TLS Certificates for Databricks Connect
summary: Configuring custom SSL/TLS certificates for Databricks Connect by setting the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable when the cluster uses a custom certificate.
sources:
  - advanced-usage-of-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:20:49.414Z"
updatedAt: "2026-06-18T14:20:49.414Z"
tags:
  - databricks-connect
  - security
  - ssl-tls
  - certificates
aliases:
  - custom-ssltls-certificates-for-databricks-connect
  - CSCFDC
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Custom SSL/TLS Certificates for Databricks Connect

When connecting to a Databricks cluster that uses a custom SSL/TLS certificate to resolve the workspace fully qualified domain name (FQDN), you must configure your local development machine to trust that certificate by setting the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to the full path of the certificate bundle installed on the cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md:52-54]

## Configuration

Set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` to the absolute path of the CA certificate bundle that contains the custom certificate, typically the same path used on the cluster (e.g., `/etc/ssl/certs/ca-bundle.crt`). ^[advanced-usage-of-databricks-connect-databricks-on-aws.md:52-54]

### Python Example

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md:56-58]

For instructions on setting environment variables in other operating systems or shells, refer to your operating system’s documentation. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md:60-61]

## Prerequisites

- A Databricks cluster configured with a custom SSL/TLS certificate for its FQDN.
- Local access to the certificate bundle file path that matches the cluster’s configuration.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects local code to Databricks clusters
- gRPC — The underlying protocol used for Spark Connect communication
- SSL/TLS — The encryption layer for secure connections
- [Spark Connect](/concepts/spark-connect.md) — The protocol enabling remote Spark session connectivity

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md:52-54](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
2. [advanced-usage-of-databricks-connect-databricks-on-aws.md:56-58](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
3. [advanced-usage-of-databricks-connect-databricks-on-aws.md:60-61](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
