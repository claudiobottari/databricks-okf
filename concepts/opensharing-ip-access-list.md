---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fabdac73aaf9619d5abf64d20a085501851cacc9f26e8e4c8da526c40859f434
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-ip-access-list
    - OIAL
    - Restrict OpenSharing recipient access using IP access lists
    - Workspace IP Access Lists
  citations:
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: OpenSharing IP Access List
description: An IP-based allow list that data providers can assign to recipients using the Databricks-to-Open sharing protocol to restrict access to shared data from specific IP addresses or CIDR ranges.
tags:
  - delta-sharing
  - security
  - access-control
timestamp: "2026-06-19T20:14:30.324Z"
---

# OpenSharing IP Access List

The **OpenSharing IP Access List** is a security feature that allows data providers using the [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md) to restrict a recipient to a specific set of IP addresses when they access shared data. This list is independent of Workspace IP access lists and supports only allow lists (deny lists are not supported). ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## What the IP Access List Affects

The IP access list controls access to the following endpoints and operations related to the recipient:

- OpenSharing OSS Protocol REST API calls
- OpenSharing activation URL access
- OpenSharing credential file download

When the provider has [SecureConnect](/concepts/secureconnect.md) enabled, the IP access list also enforces access to shared data storage. Without SecureConnect, storage URLs remain reachable from any client IP, regardless of the IP access list. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Limitations

Each recipient supports a maximum of 100 IP/CIDR values, where one CIDR range counts as a single value. Only IPv4 addresses are supported. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Assigning an IP Access List to a Recipient

A data provider can assign an IP access list when creating a new recipient or to an existing recipient using [Catalog Explorer](/concepts/catalog-explorer.md) or the Databricks Unity Catalog CLI.

**Permissions required**:
- To assign when creating a recipient: `CREATE RECIPIENT` privilege.
- To assign to an existing recipient: recipient object owner (or [Metastore](/concepts/metastore.md) admin for viewing).

Steps in Catalog Explorer:
1. Click **Catalog** and select **OpenSharing** from the gear icon or **Share > OpenSharing**.
2. On the **Shared by me** tab, click **Recipients** and select the target recipient.
3. On the **IP access list** tab, click **Add IP address/CIDRs** for each IP address (in single IP format, e.g., `8.8.8.8`) or range (in CIDR format, e.g., `8.8.8.4/10`).

^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Removing an IP Access List

To remove an IP access list, use the same navigation path and click the trash can icon next to the IP address you want to delete. If all IP addresses are removed, the recipient can access the shared data from any location.

**Permissions required**: Recipient object owner. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Viewing a Recipient's IP Access List

The IP access list can be viewed via Catalog Explorer, the Databricks Unity Catalog CLI, or the `DESCRIBE RECIPIENT` SQL command in a notebook or Databricks SQL query.

**Permissions required**: [Metastore](/concepts/metastore.md) admin, a user with the `USE RECIPIENT` privilege, or the recipient object owner.

In Catalog Explorer, navigate to the recipient and open the **IP access list** tab to see allowed addresses. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Audit Logging

The following operations trigger audit log entries related to IP access lists:

- Recipient management operations: create, update
- Denial of access to any OpenSharing OSS Protocol REST API call
- Denial of access to the OpenSharing activation URL (Databricks-to-Open sharing only)
- Denial of access to the OpenSharing credential file download (Databricks-to-Open sharing only)

For more information on enabling and reading audit logs, see Audit and monitor data sharing. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md)
- [SecureConnect](/concepts/secureconnect.md)
- Workspace IP access lists
- [Recipient (Delta Sharing)](/concepts/recipient-delta-sharing.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Audit logging](/concepts/abac-policy-audit-logging.md)

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
