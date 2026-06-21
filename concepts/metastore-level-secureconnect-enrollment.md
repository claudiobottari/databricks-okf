---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3271f3f4456619854e7cf1c2cb5c22ed87afc28d0a78984678b443fb4cdcda1
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-level-secureconnect-enrollment
    - MSE
    - Metastore-level SecureConnect setting
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: Metastore-level SecureConnect enrollment
description: A metastore administrator can configure a metastore so that all new recipients automatically use SecureConnect, controlled via Catalog Explorer settings.
tags:
  - administration
  - delta-sharing
  - configuration
timestamp: "2026-06-19T23:04:56.670Z"
---

# Metastore-level [SecureConnect](/concepts/secureconnect.md) enrollment

**Metastore-level [SecureConnect](/concepts/secureconnect.md) enrollment** is a configuration that allows a [Metastore](/concepts/metastore.md) administrator to enable [SecureConnect](/concepts/secureconnect.md) by default for all new recipients created within a [Delta Sharing](/concepts/delta-sharing.md) provider’s [Metastore](/concepts/metastore.md). When enabled, any recipient added after the setting is turned on automatically uses [SecureConnect](/concepts/secureconnect.md) to access shared data, without requiring per-recipient firewall updates. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Overview

By default, [SecureConnect](/concepts/secureconnect.md) is disabled for both new and existing recipients. A [Metastore](/concepts/metastore.md) administrator can change this default at the [Metastore](/concepts/metastore.md) level so that newly created recipients are automatically enrolled in [SecureConnect](/concepts/secureconnect.md). This simplifies the provider’s workflow, because the provider no longer needs to manually toggle [SecureConnect](/concepts/secureconnect.md) for each new recipient. Existing recipients are not affected by the metastore-level change; they must be configured individually. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Procedure

To enable [SecureConnect](/concepts/secureconnect.md) for new recipients on a [Metastore](/concepts/metastore.md):

1. In your Databricks workspace, open **Catalog Explorer**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
   (Alternatively, click **Share > OpenSharing** in the upper-right corner.)
3. Click **Settings** in the upper-right corner.
4. Turn on **Enable [SecureConnect](/concepts/secureconnect.md) for new recipients**.
5. Click **Save**.

Once saved, any recipient created after this point will have [SecureConnect](/concepts/secureconnect.md) enabled by default. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Considerations

- The setting applies only to **new** recipients created after the change. Recipients that already exist must have [SecureConnect](/concepts/secureconnect.md) enabled individually by a recipient owner or a user with the `USE_RECIPIENT` privilege. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- [SecureConnect](/concepts/secureconnect.md) enrollment at the [Metastore](/concepts/metastore.md) level is part of a larger setup that includes configuring the storage firewall and, optionally, attaching a network connectivity configuration (NCC) for private connectivity. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- For providers using [SecureConnect](/concepts/secureconnect.md) with open recipients, IP access lists can further restrict which client IP addresses can reach the sharing endpoint and storage. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related concepts

- [SecureConnect](/concepts/secureconnect.md)
- [OpenSharing](/concepts/opensharing.md)
- [Metastore](/concepts/metastore.md)
- [Recipient](/concepts/data-recipient.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
