---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91e756650369d0d824dcc9ea93a3e493e6db130b5b7d60d65946d58bda1388cd
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-credential-rotation
    - PCR
    - Credential Rotation
    - Credential rotation
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: Provider Credential Rotation
description: The process of rotating bearer tokens or credentials for OpenSharing providers using Databricks REST API PATCH request, without dropping and recreating the provider object.
tags:
  - delta-sharing
  - security
  - credentials
  - databricks
timestamp: "2026-06-19T19:26:45.604Z"
---

# Provider Credential Rotation

**Provider Credential Rotation** is the process of updating authentication credentials stored in a Unity Catalog provider object when a data provider using the OpenSharing Databricks‑to‑Open sharing protocol rotates its bearer token and issues a new credential file. This procedure ensures that the recipient’s workspace continues to have access to shared data without interruption.

## Overview

In OpenSharing on Databricks, a provider object in the recipient’s Unity Catalog [Metastore](/concepts/metastore.md) stores the credentials needed to connect to a data provider. When the provider rotates its credentials—typically a bearer token—the recipient must update the stored credential in the provider object. Credential rotation applies only to provider objects with authentication type `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`. Databricks‑to‑Databricks providers (`DATABRICKS`) rotate automatically and require no recipient action. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

> **Important:** Recipients who access data without a provider object—for example, by using the `delta-sharing` Python or Spark connector directly—must apply the new credential file in their connector configuration instead. See Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens|Read data shared using OpenSharing. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## When to Use Provider Credential Rotation

A data provider may send a new credential file as part of a routine security rotation or after a security incident. When you receive such a file, you must update the provider object. **Do not drop and recreate the provider** to apply a new credential: Catalog bind to the provider’s internal ID, not its name. Recreating the provider with the same name breaks the catalog’s connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

The Databricks Unity Catalog CLI, Catalog Explorer, and the `ALTER PROVIDER` SQL command do not support updating credentials. Instead, you must use the Databricks REST API. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Procedure

### Prerequisites

- You must be the owner of the provider object or a [Metastore](/concepts/metastore.md) admin.
- You have the new credential file from the provider. The file contains the bearer token and endpoint URL.

### Step 1: Update the Credential

Send a `PATCH` request to the provider endpoint with the full contents of the new credential file in the `recipient_profile_str` field. The following Python example can be run from a notebook on the recipient workspace:

```python
import json
import requests

new_profile = {
    "shareCredentialsVersion": 1,
    "bearerToken": "<new-bearer-token>",
    "endpoint": "https://<provider-workspace>.cloud.databricks.com/api/2.0/delta-sharing/metastores/<metastore-id>",
}

token = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .apiToken()
    .get()
)
workspace_url = spark.conf.get("spark.databricks.workspaceUrl")

response = requests.patch(
    f"https://{workspace_url}/api/2.1/unity-catalog/providers/<provider-name>",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    },
    json={"recipient_profile_str": json.dumps(new_profile)},
)
print(response.status_code)
print(response.json())
```

A successful rotation returns HTTP 200 and the provider’s updated metadata, including the new endpoint and timestamps. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

For the full API specification, see the [Update a provider REST API](https://docs.databricks.com/api/workspace/providers/update) documentation.

### Step 2: Verify the Rotation

Confirm that the catalog, schemas, and tables are still accessible. The catalog name should remain the same as before rotation. You can check this using Catalog Explorer or by running a `SHOW CATALOGS` SQL command. Previous error banners (e.g., authentication failures) should be gone, and the provider’s shares should be listed again. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The protocol for sharing data between Databricks workspaces and non‑Databricks systems.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that manages metadata and access.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol for secure data sharing.
- Provider Object – A securable object in Unity Catalog representing a data provider.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) – A sharing method that does not require manual credential rotation.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – A sharing method that uses bearer tokens and may require credential rotation.

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
