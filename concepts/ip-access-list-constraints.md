---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6108ed1bd041772629b31a26ebba486c23433ed34ca577f23df6cfa058f5f7f
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ip-access-list-constraints
    - IALC
  citations:
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: IP Access List Constraints
description: "Technical limitations of recipient IP access lists: maximum 100 IP/CIDR values per recipient, only IPv4 addresses supported, only allow lists (no deny lists) available."
tags:
  - delta-sharing
  - networking
  - limitations
timestamp: "2026-06-19T20:14:54.051Z"
---

# IP Access List Constraints

**IP Access List Constraints** refer to the rules and limitations that apply when a data provider uses IP access lists to restrict recipient access to shared data under the [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md). These lists are independent of Workspace IP access lists and are used to control which client IP addresses a recipient may use when accessing shared data. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Supported List Types

Only **allow lists** are supported. IP access lists for OpenSharing recipients cannot be used as deny lists. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Quantity and Format Constraints

Each recipient supports a maximum of **100 IP/CIDR values**, where a single CIDR notation (for example, `8.8.8.4/10`) counts as one value toward that limit. Only **IPv4 addresses** are supported. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

If all IP addresses are removed from a recipient’s access list, the recipient can access shared data from any IP address. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Affected Operations

The IP access list enforces access on the following operations:

- OpenSharing OSS Protocol REST API calls
- OpenSharing activation URL access (Databricks-to-Open sharing only)
- OpenSharing credential file download (Databricks-to-Open sharing only)

When a request originates from an IP address not on the allow list, the system denies access and records an audit log entry. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Interaction with SecureConnect

When the provider has [SecureConnect](/concepts/secureconnect.md) enabled, the IP access list also enforces access to the shared data storage itself. Without SecureConnect, storage URLs remain reachable from any client IP regardless of the IP access list. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [SecureConnect](/concepts/secureconnect.md)
- [Recipient](/concepts/data-recipient.md)
- Workspace IP access lists

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
