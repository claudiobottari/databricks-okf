---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 662b089a72584a681e069be67a79b812c690361f90899ca94179e7ca5a9b2ad4
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-level-secureconnect-toggle
    - RST
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: Recipient-level SecureConnect toggle
description: Recipient owners and users with the USE_RECIPIENT privilege can toggle SecureConnect on or off for individual recipients, disabled by default unless the metastore setting is enabled.
tags:
  - administration
  - delta-sharing
  - permissions
timestamp: "2026-06-19T23:04:45.926Z"
---

# Recipient-level [SecureConnect](/concepts/secureconnect.md) toggle

The **Recipient-level [SecureConnect](/concepts/secureconnect.md) toggle** is a per-recipient setting in Databricks [OpenSharing](/concepts/opensharing.md) that enables or disables [SecureConnect](/concepts/secureconnect.md) for a given [Data Recipient](/concepts/data-recipient.md). When [SecureConnect](/concepts/secureconnect.md) is enabled on a recipient, Databricks routes the recipient's requests through a managed proxy, allowing the provider to share data from cloud storage behind a firewall or private endpoint without having to allowlist each recipient's network individually. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Who can configure the toggle

The toggle is controlled by the **recipient owner** or by any user who has been granted the `USE_RECIPIENT` privilege on the recipient. These users can turn [SecureConnect](/concepts/secureconnect.md) on or off for each recipient at any time. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Default behavior

By default, [SecureConnect](/concepts/secureconnect.md) is **disabled** on a recipient. However, if the provider's [Metastore](/concepts/metastore.md) has been configured to "Enable [SecureConnect](/concepts/secureconnect.md) for new recipients" (see [Metastore-level SecureConnect setting](/concepts/metastore-level-secureconnect-enrollment.md)), any recipient created *after* that setting is turned on will have [SecureConnect](/concepts/secureconnect.md) enabled automatically. Recipients that existed before the [Metastore](/concepts/metastore.md) setting was enabled remain unaffected; they must be configured individually. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## How to configure the toggle (UI)

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared by me** tab, click the **Recipients** tab.
4. Locate the desired recipient and turn the **SecureConnect** toggle on or off.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Relationship with the [Metastore](/concepts/metastore.md) setting

The metastore-level setting (configured under **OpenSharing > Settings**) controls whether *new* recipients automatically have [SecureConnect](/concepts/secureconnect.md) enabled. The recipient-level toggle overrides this for existing recipients and allows per-recipient fine-tuning. A provider can therefore:
- Enable [SecureConnect](/concepts/secureconnect.md) by default for all new recipients via the [Metastore](/concepts/metastore.md) setting.
- Manually enable or disable [SecureConnect](/concepts/secureconnect.md) for existing recipients using the recipient-level toggle.
- Maintain a mix of SecureConnect-enabled and SecureConnect-disabled recipients if some recipients do not require it.

## Impact on billing and access

When [SecureConnect](/concepts/secureconnect.md) is enabled for a recipient, the provider is billed for data transfer through the proxy. Usage is attributed per recipient via the `recipient_id` field in the billing system table. Additionally, for open (non-Databricks) recipients, IP ACLs can be used to restrict which client IP addresses are allowed to reach [SecureConnect](/concepts/secureconnect.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Limitations

- The toggle applies only to recipients created under a SecureConnect-enabled [Metastore](/concepts/metastore.md).
- [SecureConnect](/concepts/secureconnect.md) is not available on AWS GovCloud.
- The toggle does not affect recipients using OIDC sharing (not currently supported with [SecureConnect](/concepts/secureconnect.md)) or cloud token optimization (not available for [SecureConnect](/concepts/secureconnect.md)). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related concepts

- [SecureConnect](/concepts/secureconnect.md)
- [OpenSharing](/concepts/opensharing.md)
- [Metastore-level SecureConnect setting](/concepts/metastore-level-secureconnect-enrollment.md)
- [Recipient management](/concepts/recipient-lifecycle-management.md)
- [IP ACLs for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md)
- [Data transfer billing for SecureConnect](/concepts/opensharing-secureconnect.md)

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
