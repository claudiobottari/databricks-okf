---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64013c10c977d4256c9eaea51a60cc164aeddf125f1dc6bda8523fbbeef2da46
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-email-destinations
    - DED
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Default Email Destinations
description: A metastore-wide setting that routes access requests to the object owner's email when no explicit destination is configured.
tags:
  - unity-catalog
  - access-control
  - email
timestamp: "2026-06-19T19:22:19.295Z"
---

# Default Email Destinations

**Default Email Destinations** is an administrative setting in Databricks that automatically delivers access requests to the appropriate object owner's email address when no explicit destination has been configured for a Unity Catalog securable object. This feature ensures that users can always submit access requests, even for objects that lack manually configured destinations.

## Overview

When enabled, default email destinations provide a safety net for the [Access Request Destinations](/concepts/access-request-destinations.md) system. If a user attempts to request access to a Unity Catalog object that has no configured destination, the request is automatically routed to the object owner's email address rather than being blocked. This ensures that access requests are delivered even when administrators have not explicitly configured destinations for individual objects. ^[manage-access-requests-databricks-on-aws.md]

Databricks recommends enabling default email destinations as the fastest way to start receiving and responding to access requests across an entire [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[manage-access-requests-databricks-on-aws.md]

## How It Works

When default email destinations are enabled, the routing behavior depends on the type of object being requested: ^[manage-access-requests-databricks-on-aws.md]

- **Catalog objects** (tables, views, schemas, etc.): Access requests are sent to the **catalog owner's** email address.
- **Objects outside a catalog** (external locations, storage credentials, etc.): Access requests are sent to the **object owner's** email address.

## Enabling Default Email Destinations

To enable default email destinations, a user must have both **metastore admin** and **workspace admin** privileges. ^[manage-access-requests-databricks-on-aws.md]

1. In the upper-right corner of your workspace, click your profile photo and select **Settings**.
2. Click **Notifications**.
3. Turn on **Enable default email destinations for access requests in UC**.

^[manage-access-requests-databricks-on-aws.md]

## Relationship to Explicit Destinations

Default email destinations do not override explicitly configured destinations. If an object already has one or more destinations configured (such as email addresses, Slack channels, Microsoft Teams channels, webhook endpoints, or a redirect URL), the default email destination does not apply. The request is sent only to the explicitly configured destinations. ^[manage-access-requests-databricks-on-aws.md]

If multiple destinations are configured, the request is sent to all of them. If no destination is configured and default email destinations are disabled, users cannot request access to the object. ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) — The broader system for routing access requests in Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that implements access request functionality
- Catalog Owner — The principal who receives default email notifications for catalog objects
- [Metastore Admin](/concepts/metastore-admin-role.md) — A role required to enable default email destinations
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) — Another role required to enable default email destinations

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
