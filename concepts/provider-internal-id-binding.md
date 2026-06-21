---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38c393bdaaab7f1df9258867c8c165802f153ecab97c7edc3cde8f2b42790118
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-internal-id-binding
    - PIIB
    - PII
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: Provider Internal ID Binding
description: Catalogs bind to a provider's internal ID (not its name), so recreating a provider with the same name after deletion breaks the catalog's connection to shared data.
tags:
  - delta-sharing
  - unity-catalog
  - databricks
  - architecture
timestamp: "2026-06-19T19:27:14.138Z"
---

# Provider Internal ID Binding

**Provider Internal ID Binding** is a property of [Unity Catalog](/concepts/unity-catalog.md) securable objects used in [OpenSharing](/concepts/opensharing.md) on Databricks. When a recipient's [Metastore](/concepts/metastore.md) creates a catalog to access data shared by an external provider, that catalog is bound to the provider's *internal immutable identifier*, not to the provider's user‑facing name. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Implications for Provider Management

Because catalogs bind to the internal ID, renaming a provider object does not break access to the shared data — the ID remains unchanged. However, dropping a provider object and recreating it with the same name *will* break the catalog's connection to the shared data, because the new object receives a different internal ID. For this reason, the documentation explicitly warns: "Don't drop and recreate the provider to apply a new credential. Catalogs bind to the provider's internal ID, not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data." ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Credential Rotation and the Internal ID

The internal ID binding is especially important when rotating credentials for open recipients (providers with authentication type `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`). The correct procedure is to use the REST API `PATCH` endpoint to update the provider's `recipient_profile_str` field in place. This preserves the provider's internal ID and ensures that existing catalogs continue to function. Using `DROP PROVIDER` followed by `CREATE PROVIDER` would assign a new ID and break catalog access. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Identifying the Internal ID

The internal ID of a provider object is returned in API responses, for example in the `id` field of a successful provider update response:

```json
{
  "id": "abcd2a5b-c18e-46eb-ae11-3056cfe99bef"
}
```

This ID is distinct from the provider's `name` and is used by the system to maintain the binding between the provider object and the catalogs that consume its shares. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- Provider – The securable object that represents a data sharing organization.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages provider objects and their bindings.
- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol that uses provider objects and internal IDs.
- [Catalog](/concepts/unity-catalog.md) – A Unity Catalog securable that can be bound to a provider's shared data.
- [Credential Rotation](/concepts/provider-credential-rotation.md) – The process of updating a provider's authentication token.

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
