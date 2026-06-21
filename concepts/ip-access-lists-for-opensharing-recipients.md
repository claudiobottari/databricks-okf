---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94a3ae0f132c32a299b3681fad67a978c6eda61e67e7cfa75daf5168097e5bff
  pageDirectory: concepts
  sources:
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ip-access-lists-for-opensharing-recipients
    - IALFOR
    - IP Access Lists for Open Sharing
    - IP Access Lists for OpenSharing
    - IP access lists for OpenSharing
    - IP ACLs for OpenSharing
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
title: IP Access Lists for OpenSharing Recipients
description: A security feature that allows providers to restrict Databricks-to-Open sharing recipients to a defined set of IP addresses, limiting network-level access to shared data.
tags:
  - delta-sharing
  - security
  - networking
  - databricks
timestamp: "2026-06-19T19:23:52.523Z"
---

# IP Access Lists for OpenSharing Recipients

**IP Access Lists for OpenSharing Recipients** is a security feature for Databricks-to-Open sharing that allows data providers to restrict recipient access to a limited set of IP addresses. This enables providers to enforce network-level access controls on who can consume shared data, even after sharing credentials have been issued. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Overview

IP access lists are an optional security measure for [OpenSharing](/concepts/opensharing.md) recipients that use Databricks-to-Open sharing. When an IP access list is assigned to a recipient, only requests originating from the specified IP addresses are permitted to access the shared data. This adds a layer of access control beyond the bearer token or [OIDC federation](/concepts/oidc-federation-policy.md) authentication mechanism. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

The feature is available for [recipient objects](/concepts/recipient-object-delta-sharing.md) created with authentication types `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`, collectively known as Databricks-to-Open sharing recipients. It is not applicable to Databricks-to-Databricks sharing recipients. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Interacting with IP Access Lists

IP access lists can be viewed and managed through the recipient details screen. When describing a recipient, the details include whether IP access lists are assigned, alongside other metadata such as [token lifetime](/concepts/recipient-token-lifetime.md), activation link, and authentication type. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

For the complete instructions on creating and managing IP access lists for recipients, refer to the dedicated documentation on [Restrict OpenSharing recipient access using IP access lists](https://docs.databricks.com/aws/en/delta-sharing/access-list). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol for sharing data with non-Databricks users
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — Sharing data with recipients outside the Databricks ecosystem
- Bearer token authentication — A token-based authentication method for OpenSharing recipients
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — Open ID Connect-based authentication for recipients
- [Recipient objects](/concepts/recipient-object-delta-sharing.md) — Named objects representing identities with whom data is shared
- [Recipient Properties](/concepts/recipient-properties.md) — Customizable metadata attached to recipient objects
- Data sharing access control — Broader permission management for Delta Sharing

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
