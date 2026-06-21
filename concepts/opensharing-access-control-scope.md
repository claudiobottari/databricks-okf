---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c60de306f0b23bf15de0ae8f0e7ecc0fcb26d92fff8d40a23cfefe8c31157a2d
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-access-control-scope
    - OACS
  citations:
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: OpenSharing Access Control Scope
description: "The three specific endpoints affected by IP access lists: OpenSharing OSS Protocol REST API access, OpenSharing activation URL access, and OpenSharing credential file download."
tags:
  - delta-sharing
  - access-control
  - api
timestamp: "2026-06-19T20:14:50.985Z"
---

# OpenSharing Access Control Scope

**OpenSharing Access Control Scope** refers to the specific operations and endpoints that are restricted when a data provider assigns an IP Access List (allow list) to a recipient using the [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md). The IP access list is independent of workspace-level IP access lists and only supports allow‑list entries. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Scope of IP Access List Enforcement

When assigned to a recipient, the IP access list controls access to the following OpenSharing endpoints and operations:

- **OpenSharing OSS Protocol REST API** – All API calls made by the recipient against the shared data catalog must originate from an allowed IP address.
- **OpenSharing activation URL** – The recipient’s browser or client must be on an allowed IP to complete the activation flow (applies to Databricks‑to‑Open sharing only).
- **OpenSharing credential file download** – Downloading the credential file (used by open‑source Delta Sharing clients) is restricted to allowed IPs.

^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Effect of SecureConnect on Storage Access

When the provider has [SecureConnect](/concepts/secureconnect.md) enabled, the IP access list **also** enforces access to the shared data storage back‑end (e.g., cloud object storage). Without SecureConnect, storage URLs remain reachable from any client IP, regardless of the IP access list. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Limitations

- Only **allow lists** are supported (deny lists are not available).
- Maximum of **100 IP/CIDR values** per recipient (a single CIDR block counts as one value).
- Supports **IPv4 addresses only**.
- The list is managed independently of [Workspace IP Access Lists](/concepts/opensharing-ip-access-list.md).

^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Management Operations

The following recipient management operations trigger audit log events related to IP access lists:

- Create and update recipient
- Denial of access to OpenSharing OSS Protocol REST API calls
- Denial of access to OpenSharing activation URL (Databricks‑to‑Open sharing only)
- Denial of access to OpenSharing credential file download (Databricks‑to‑Open sharing only)

^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for data sharing.
- [Open Sharing Protocol](/concepts/opensharing-protocol.md) – The variation that uses open‑source Delta Sharing clients.
- IP Access List – The mechanism for restricting access by source IP.
- [SecureConnect](/concepts/secureconnect.md) – A security feature that extends IP‑based enforcement to storage URLs.
- [Recipient](/concepts/data-recipient.md) – The consumer entity in a Delta Sharing relationship.
- [OpenSharing Activation URL](/concepts/opensharing-recipient-activation-link.md) – The URL used to activate a recipient’s access.
- [OpenSharing Credential File](/concepts/opensharing-credential-file.md) – A file containing credentials for open‑source clients.

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
