---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dfc4e312e2b1c42dcf0896e39e87eb0f55be5c1640e80c4de961775c6997a3e
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-databricks-to-open-protocol
    - O(P
    - OpenSharing Databricks-to-Open Sharing Protocol
    - OpenSharing Databricks-to-Open sharing protocol
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
    - file: |-
        read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md}

        ## Limitations

        - **Power BI connector**: Data must fit in memory; a row limit (default 1 M) can be set.
        - **Tableau connector**: All columns are returned as `String`; deletion vectors and column mapping are unsupported; SQL filters require server-side `predicateHint` support.
        - **Python connector**: CDF queries on tables with column mapping are not supported; CDF queries using `use_delta_format=True` fail if the schema changed during the queried version range.
        - **Streaming tables**: Only the current snapshot can be read; history
    - file: CDF
    - file: |-
        and Structured Streaming sources are not supported.
        - **Materialized views**: Only the current snapshot can be read; Structured Streaming sources are not supported.
        - **Iceberg client**: Namespaces with more than 100 shared views return only the first 100; metadata does not auto-refresh (requires manual or scheduled refresh).
        - **Spark client for structured streaming**: `Trigger.availableNow` is not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing (Databricks-to-Open) Protocol
description: An open sharing protocol that uses bearer tokens and credential files to provide secure read-only access to shared data, with providers managing credential expiration and rotation.
tags:
  - delta-sharing
  - data-sharing
  - protocol
timestamp: "2026-06-19T20:10:40.099Z"
---

# OpenSharing (Databricks-to-Open) Protocol

The **OpenSharing (Databricks-to-Open) Protocol** is an open sharing model that enables secure, near-real-time read access to data sets shared by a provider. Recipients use a credential file and bearer tokens to connect to the shared data without the ability to modify the source. The protocol supports a variety of clients, including Databricks, Apache Spark, pandas, Power BI, Tableau, and [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)-compatible tools. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Overview

In the Databricks-to-Open sharing model, a data provider shares tables or volumes by issuing a credential file to a member of the recipient team. The recipient distributes that file securely to authorized users, who can then read the shared data as long as the credential remains valid and the provider continues to share. Access lasts until the credential expires or is revoked by the provider. Data updates are available in near real time. Recipients can read and copy the data but cannot modify the source. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

The provider controls the storage bucket, credential scope, expiration, and read vs. read/write capabilities. When mounting an open share in a Secure Egress Gateway (SEG) workspace, the provider's bucket is automatically allowlisted for outbound access; recipients should verify the provider before mounting. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Authentication and Credentials

Authentication for the OpenSharing protocol uses **bearer tokens** contained in a credential file (often named `config.share`). The credential file also contains the endpoint URL for the sharing server. This file is downloaded by the recipient from an activation link provided by the data provider. For workspaces with [Unity Catalog](/concepts/unity-catalog.md), recipients can import the credential file directly via the Catalog Explorer UI, which creates a provider object and eliminates the need to handle the raw file for subsequent access. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

For non–Unity Catalog workspaces, or for external clients, the credential file must be stored in an accessible location (absolute path) and used explicitly in connection commands. The bearer token and endpoint are extracted from the file to configure clients like Spark, pandas, Power BI, or Iceberg. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Reading Shared Data

### Using Databricks with Unity Catalog

1. **Import the provider**: In Catalog Explorer, navigate to **OpenSharing** → **Shared with me** → **Install share**. Upload the credential file and assign a provider name.
2. **Create catalogs**: From the share row, click **Create catalog** to materialise the shared assets as Unity Catalog catalogs.
3. **Grant access**: Use Unity Catalog access controls to grant permissions to team members.
4. **Query**: Read shared tables using standard Unity Catalog SQL syntax, just like any other registered object. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

If the credential is rotated, the provider object can be updated without recreating the catalog (see Rotate credentials for open recipients). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Apache Spark (without Unity Catalog)

Install the `delta-sharing` Python and Spark connectors, then use the credential file path to list shares and load tables. The protocol supports reading table snapshots, change data feed (CDF), and structured streaming. For tables with deletion vectors or column mapping, the `responseFormat` option must be set to `delta` (requires `delta-sharing-spark` 3.1+). See Delta Sharing connectors for detailed syntax. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using pandas

Install the `delta-sharing` Python connector. Use `delta_sharing.load_as_pandas()` with the profile path and table identifier (`<profile-path>#<share>.<schema>.<table>`). CDF queries are also supported via `load_table_changes_as_pandas()`. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Power BI

From Power BI Desktop (version 2.99.621.0+), select the **OpenSharing** connector, enter the server URL and bearer token from the credential file. Optionally set a row limit. The loaded data must fit in memory. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Tableau

From Tableau Desktop or Server (2024.1+), download the OpenSharing Connector from Tableau Exchange, upload the credential file, and select the desired table. All columns are returned as `String` type. Deletion vectors and column mapping are not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Iceberg Clients

External Iceberg clients (e.g., Snowflake, Trino, Flink, Spark) can read shared assets via the [Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md). The credential file provides the `icebergEndpoint` URL and bearer token. Configure a catalog integration with the share name, then create a database linked to the catalog to query tables. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md}

## Limitations

- **Power BI connector**: Data must fit in memory; a row limit (default 1 M) can be set.
- **Tableau connector**: All columns are returned as `String`; deletion vectors and column mapping are unsupported; SQL filters require server-side `predicateHint` support.
- **Python connector**: CDF queries on tables with column mapping are not supported; CDF queries using `use_delta_format=True` fail if the schema changed during the queried version range.
- **Streaming tables**: Only the current snapshot can be read; history, CDF, and Structured Streaming sources are not supported.
- **Materialized views**: Only the current snapshot can be read; Structured Streaming sources are not supported.
- **Iceberg client**: Namespaces with more than 100 shared views return only the first 100; metadata does not auto-refresh (requires manual or scheduled refresh).
- **Spark client for structured streaming**: `Trigger.availableNow` is not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Requesting a New Credential

If the credential activation URL or downloaded file is lost, corrupted, or expired, contact the data provider. For Unity Catalog recipients, apply the new credential via the Databricks REST API (see Rotate credentials for open recipients). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open standard on which OpenSharing is built.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ [Metastore](/concepts/metastore.md) that simplifies provider import and access control.
- [Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md) – API used by external Iceberg clients to read shared data.
- Bearer token authentication – Security mechanism used in this protocol.
- [Credential file](/concepts/credential-file-opensharing.md) – The `config.share` file containing endpoint and token.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Spark feature supported for reading shared Delta tables.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – Mechanism for reading incremental changes from shared tables.

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
2. read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md}

## Limitations

- **Power BI connector**: Data must fit in memory; a row limit (default 1 M) can be set.
- **Tableau connector**: All columns are returned as `String`; deletion vectors and column mapping are unsupported; SQL filters require server-side `predicateHint` support.
- **Python connector**: CDF queries on tables with column mapping are not supported; CDF queries using `use_delta_format=True` fail if the schema changed during the queried version range.
- **Streaming tables**: Only the current snapshot can be read; history
3. CDF
4. and Structured Streaming sources are not supported.
- **Materialized views**: Only the current snapshot can be read; Structured Streaming sources are not supported.
- **Iceberg client**: Namespaces with more than 100 shared views return only the first 100; metadata does not auto-refresh (requires manual or scheduled refresh).
- **Spark client for structured streaming**: `Trigger.availableNow` is not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
