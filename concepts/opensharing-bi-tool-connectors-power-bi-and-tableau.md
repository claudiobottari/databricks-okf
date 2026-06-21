---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f1d55342fed7b04a55e0cacaa69928b5d7dbda21b5c79f1939614c772f4fd52
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-bi-tool-connectors-power-bi-and-tableau
    - Tableau) and OpenSharing BI Tool Connectors (Power BI
    - OBTC(BAT
    - Tableau OpenSharing Connector
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing BI Tool Connectors (Power BI and Tableau)
description: Specialized connectors for Power BI Desktop and Tableau that allow users to discover, analyze, and visualize OpenSharing datasets through a graphical interface using credential files.
tags:
  - power-bi
  - tableau
  - visualization
  - data-sharing
timestamp: "2026-06-19T20:11:04.975Z"
---

# OpenSharing BI Tool Connectors (Power BI and Tableau)

The **OpenSharing BI Tool Connectors** for **Power BI** and **Tableau** enable business intelligence users to discover, analyze, and visualize datasets shared via the OpenSharing open protocol using bearer tokens. These connectors allow direct read access to shared data without requiring a Databricks workspace, using only a credential file provided by the data provider. The connectors support near-real-time access to the latest data, but loaded datasets must fit into the local machine's memory. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Power BI Connector

### Requirements
- Power BI Desktop version 2.99.621.0 or later.
- Access to the credential file (`config.share`) shared by the data provider. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Connection Steps
1. Open the credential file in a text editor to retrieve the endpoint URL and the bearer token.
2. Open Power BI Desktop.
3. On the **Get Data** menu, search for **OpenSharing**.
4. Select the **OpenSharing** connector and click **Connect**.
5. Enter the endpoint URL (from the credential file) into the **OpenSharing Server URL** field.
6. (Optional) Under **Advanced Options**, set a **Row Limit** to control the maximum number of rows imported (default is 1 million rows).
7. Click **OK**.
8. For authentication, choose **Bearer Token** and paste the token from the credential file.
9. Click **Connect**. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Limitations
- All loaded data must fit into the memory of the machine running Power BI Desktop. The row limit setting (under Advanced Options) manages the import size. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Tableau Connector

### Requirements
- Tableau Desktop or Tableau Server version 2024.1 or later.
- Access to the credential file shared by the data provider. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Connection Steps
1. Go to [Tableau Exchange](https://exchange.tableau.com/products/1019), download the **OpenSharing Connector**, and place it in the appropriate desktop connectors folder.
2. Open Tableau Desktop.
3. On the **Connectors** page, search for **OpenSharing by Databricks**.
4. Select **Upload Share file** and choose the credential file provided by the data provider.
5. Click **Get Data**.
6. In the Data Explorer, select the table you want to query.
7. (Optional) Add SQL filters or set a row limit.
8. Click **Get Table Data**. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Limitations
- All loaded data must fit into the memory of the machine running Tableau Desktop. The row limit setting controls import volume.
- **All columns are returned as type `String`**, regardless of the original data types.
- SQL filters work only if the OpenSharing server supports the [`predicateHint`](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#request-body) feature.
- Deletion vectors and column mapping are **not supported** by the Tableau connector. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The open protocol used for data sharing.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying standard that powers OpenSharing.
- Credential File – The file containing endpoint and token information provided by the data provider.
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) – The authentication method used by the connectors.
- Power BI – Microsoft’s business analytics tool.
- Tableau – Salesforce’s data visualization platform.
- [Data Profiling](/concepts/data-profiling.md) – Techniques for understanding shared data quality.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Storage optimization feature not supported in the Tableau connector.

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
