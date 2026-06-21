---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02fbacdbf64a5fa09cfdc3849e559376ce5a62b180d801ff0f72f1d3313cf7a9
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oss-spark-iceberg-rest-catalog-configuration
    - OSIRCC
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: OSS Spark Iceberg REST Catalog Configuration
description: Configuration for open-source Apache Spark to connect to an Iceberg REST Catalog, requiring specific JARs (Iceberg Spark runtime and AWS bundle), SparkSession extensions, and OAuth2 authentication properties.
tags:
  - spark
  - iceberg
  - configuration
  - oss
timestamp: "2026-06-19T20:08:53.215Z"
---

# OSS Spark Iceberg REST Catalog Configuration

**OSS Spark Iceberg REST Catalog Configuration** refers to the process of configuring an open-source Apache Spark installation to connect to an [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) for reading data shared via [Delta Sharing](/concepts/delta-sharing.md) with Open ID Connect (OIDC) Federation. This setup enables OIDC federation data recipients to access OpenSharing shares created in Databricks using an Iceberg REST Catalog (IRC) client. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Prerequisites

Before configuring OSS Spark, ensure you have:

- An OIDC profile downloaded from the OIDC Profile Portal URL provided by the Databricks provider
- A Spark installation with Java 17 available
- The Iceberg Spark runtime and AWS bundle JARs (tested with versions 1.10.2)
- Your OAuth credentials (client ID, client secret, token URI, and scope) from the downloaded profile

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Configuration Steps

### 1. Obtain the Iceberg Profile from the OIDC Portal

1. Navigate to the OIDC profile portal URL that the Databricks provider shared with you.
2. Click **Download file** on the portal page.
3. In the downloaded file, replace `clientId`, `clientSecret`, and `scope` with your actual values.
4. Import the share profile file with your client code.

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### 2. Launch Spark Shell with Required Configuration

Run the `spark-shell` command with the following configuration. Replace the placeholder values before executing:

- `<spark-home>`: The path to your Spark installation.
- `<iceberg-jars-path>`: The path to your Iceberg JAR files.
- `<catalog-uri>`: The Iceberg REST Catalog endpoint from your downloaded profile file.
- `<share-name>`: The share name granted to you.
- `<oauth-token-uri>`: Your IdP's OAuth token endpoint.
- `<oauth-client-id>` and `<oauth-client-secret>`: Your OAuth credentials.
- `<oauth-scope>`: Your OAuth scope.
- `<spark-script>`: The path to the Scala script to run.

```bash
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 PATH=/usr/lib/jvm/java-17-openjdk-amd64/bin:$PATH <spark-home>/bin/spark-shell \
  --jars <iceberg-jars-path>/iceberg-spark-runtime-4.0_2.13-1.10.2.jar,<iceberg-jars-path>/iceberg-aws-bundle-1.10.2.jar \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
  --conf spark.sql.catalog.databricks=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.databricks.type=rest \
  --conf spark.sql.catalog.databricks.uri=<catalog-uri> \
  --conf spark.sql.catalog.databricks.warehouse=<share-name> \
  --conf spark.sql.catalog.databricks.rest.auth.type=oauth2 \
  --conf spark.sql.catalog.databricks.oauth2-server-uri=<oauth-token-uri> \
  --conf spark.sql.catalog.databricks.credential=<oauth-client-id>:<oauth-client-secret> \
  --conf spark.sql.catalog.databricks.scope=<oauth-scope> \
  --conf spark.sql.catalog.databricks.io-impl=org.apache.iceberg.aws.s3.S3FileIO \
  < <spark-script>
```

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Configuration Parameters Explained

| Parameter | Description |
|-----------|-------------|
| `spark.sql.extensions` | Enables Iceberg Spark session extensions |
| `spark.sql.catalog.databricks` | Catalog name; sets the SparkCatalog implementation |
| `spark.sql.catalog.databricks.type` | Must be `rest` for Iceberg REST Catalog |
| `spark.sql.catalog.databricks.uri` | The Iceberg REST Catalog endpoint |
| `spark.sql.catalog.databricks.warehouse` | The share name granted to the recipient |
| `spark.sql.catalog.databricks.rest.auth.type` | Set to `oauth2` for OIDC federation |
| `spark.sql.catalog.databricks.oauth2-server-uri` | Your IdP's OAuth token endpoint |
| `spark.sql.catalog.databricks.credential` | OAuth client ID and secret, colon-separated |
| `spark.sql.catalog.databricks.scope` | OAuth scope value |
| `spark.sql.catalog.databricks.io-impl` | Set to `org.apache.iceberg.aws.s3.S3FileIO` for S3-based data |

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Required JAR Files

The configuration requires two Iceberg JAR files:
- `iceberg-spark-runtime-4.0_2.13-1.10.2.jar` — The Iceberg Spark runtime
- `iceberg-aws-bundle-1.10.2.jar` — The AWS bundle for S3 file I/O

Both files must be included in the `--jars` parameter, separated by commas. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Alternative Authentication Methods

If you are using bearer tokens to manage authentication instead of OIDC federation, refer to the documentation on Creating a recipient object for non-Databricks users using bearer tokens. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) — The catalog interface that enables cross-platform data access
- Open ID Connect (OIDC) Federation — Authentication method for secure data sharing
- OSS Spark — Open-source Apache Spark distribution
- [OpenSharing](/concepts/opensharing.md) — Databricks' implementation of the Delta Sharing protocol
- Data Recipient Configuration — General setup for consuming shared data

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
