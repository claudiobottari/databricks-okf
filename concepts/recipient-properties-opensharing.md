---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e30e87da80cee497054b993377350985cfff2d17c5f30daad3c685e8c311fcf9
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-properties-opensharing
    - RP(
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Recipient Properties (OpenSharing)
description: Custom key-value metadata that can be attached to a recipient object in OpenSharing for organizing or annotating recipients.
tags:
  - delta-sharing
  - data-sharing
  - databricks
timestamp: "2026-06-18T11:23:05.350Z"
---

#Recipient Properties (OpenSharing)

**Recipient Properties** are optional key-value metadata that can be attached to an [OpenSharing](/concepts/opensharing.md) recipient object. They allow providers to store custom information — such as internal identifiers, contact details, or environment tags — alongside the recipient definition in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

When you create a data recipient for OpenSharing, you may optionally add custom properties to that recipient. Each property consists of a **Key** (name) and a **Value**. These properties are stored on the recipient object and can be viewed and modified later. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

Recipient properties are purely informational and do not affect authentication or sharing behavior. They are useful for record-keeping, automation scripts, or integration with external systems that consume the recipient list via the [Catalog API](https://docs.databricks.com/aws/en/api-catalog/) or CLI.

## Adding Recipient Properties

Recipient properties can be added during or after recipient creation using Catalog Explorer:

1. In your Databricks workspace, click **Catalog**.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click an existing recipient to open its **Overview** tab.
4. Click the edit icon (pencil) next to **Recipient properties**.
5. Add a property name (**Key**) and a **Value**.
6. Click **Save**.

Properties can also be managed programmatically via the Databricks Unity Catalog CLI or REST API. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Managing Recipient Properties

For detailed instructions on viewing, updating, and deleting recipient properties, see the dedicated [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) page. That page covers:

- Listing all properties on a recipient.
- Adding new properties.
- Editing or removing existing properties.
- Restricting recipient access with IP lists (which is a separate feature, not a property).

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) – The overall framework for sharing data.
- [Recipient (OpenSharing)](/concepts/data-recipient-opensharing.md) – The named object representing a data consumer.
- [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) – The primary guide for creating recipients.
- [Data shares (OpenSharing)](/concepts/databricks-opensharing.md) – The units of data that are granted to recipients.

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
