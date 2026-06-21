---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ead339d9123435b9c765becbcb0f1363bed7259f5dec1ede3e7d5504fb107c56
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - redirect-url-destination
    - RUD
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Redirect URL Destination
description: A special destination type that redirects users to an external access request system, disabling the in-product request form and all other destinations for that object.
tags:
  - unity-catalog
  - access-control
  - integration
timestamp: "2026-06-19T19:22:55.200Z"
---

# Redirect URL Destination

A **Redirect URL Destination** is a type of access request destination in [Unity Catalog](/concepts/unity-catalog.md) that redirects users to an external URL when they request access to a securable object, instead of showing the in-product access request form. Only one redirect URL can be configured per object, and when a URL is set, no other destination types (such as email, Slack, or webhook) can be added for that object.^[manage-access-requests-databricks-on-aws.md]

## Overview

When administrators configure a redirect URL on a Unity Catalog securable object, users who attempt to request access to that object are taken directly to the specified external URL. This is useful when an organization wants to route access requests to its own external access request system rather than using Databricks' built-in request flow.^[manage-access-requests-databricks-on-aws.md]

The redirect URL destination is available alongside other destination types, including email addresses, Slack channels, Microsoft Teams channels, and webhook endpoints. However, a redirect URL is mutually exclusive with all other destination types — if a URL is set, no other destinations can be configured for that object.^[manage-access-requests-databricks-on-aws.md]

## Configuration Requirements

To configure a redirect URL destination on an object, you must either be the object owner, have the `MANAGE` privilege on the object, or be a [metastore admin](/concepts/metastore-admin-role.md). You can configure destinations using [Catalog Explorer](/concepts/catalog-explorer.md), the REST API, or Terraform.^[manage-access-requests-databricks-on-aws.md]

### Configuring in Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. Select a securable object.
3. Click the kebab menu and select **Manage access request destinations**.
4. Select the redirect URL option and enter the desired URL.
5. Click **Update**.

When a redirect URL is selected, no other destination types can be added.^[manage-access-requests-databricks-on-aws.md]

## Inheritance Behavior

Redirect URL destinations, like other access request destinations, follow [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) inheritance rules. When you configure a redirect URL at higher levels of the hierarchy (such as a catalog), it applies to all child objects that don't already have their own destination configured. If a child object has its own destination configured, inheritance is overridden for that specific object.^[manage-access-requests-databricks-on-aws.md]

## Behavior Differences from Other Destinations

When a redirect URL is configured, users do not see the in-product access request form. Instead, they are redirected to the configured URL. This contrasts with other destination types (email, Slack, webhook) where the in-product request form is displayed, and the request is sent to the configured destinations for approval. With a redirect URL, the entire access request process is handled externally.^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) — Overview of all destination types for access requests
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI surface for configuring access request destinations
- [Metastore Admin](/concepts/metastore-admin-role.md) — Role with privileges to configure access request destinations
- [Default Email Destinations](/concepts/default-email-destinations.md) — Alternative configuration for delivering access requests
- Webhook Destination — Another destination type that sends access requests as JSON payloads

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
