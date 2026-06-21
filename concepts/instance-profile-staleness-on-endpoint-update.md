---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d16f6077c66f820ff7aa4376e4c84669705868645f3efd6b35350c275a06168b
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-staleness-on-endpoint-update
    - IPSOEU
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile Staleness on Endpoint Update
description: When an instance profile's IAM role is edited or deleted in Databricks Settings, running serving endpoints continue using the old role until the endpoint is explicitly updated.
tags:
  - aws
  - model-serving
  - operational-concerns
timestamp: "2026-06-19T21:58:08.545Z"
---

# Instance Profile Staleness on Endpoint Update

**Instance Profile Staleness on Endpoint Update** refers to a behavior where a model serving endpoint continues to use the previously associated instance profile's IAM role, even after that profile has been edited or deleted from the Databricks UI, until certain conditions trigger an update.

## Overview

When an instance profile is attached to a model serving endpoint, the endpoint uses the AWS Identity and Access Management (IAM) role from that profile to access AWS resources. However, changes made to the instance profile outside of the endpoint's configuration do not take effect immediately. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Staleness Scenarios

### Editing an Instance Profile via the Databricks UI

If a customer modifies the IAM role associated with an instance profile through the **Settings** page of the Databricks UI, any model serving endpoints currently running with that instance profile will continue to use the **old** IAM role until the endpoint is explicitly updated. The endpoint does not automatically detect the change and refresh its credentials. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Deleting an Instance Profile via the Databricks UI

If a customer deletes an instance profile from the **Settings** page of the Databricks UI, and that profile is currently in use by one or more running endpoints, those running endpoints are **not** impacted. The endpoint retains its existing configuration and continues to function. The stale reference does not cause an error or interruption in service. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Root Cause

The [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint stores a snapshot of the instance profile's ARN at the time of configuration. Subsequent modifications to the instance profile in the central Databricks settings are not propagated back to the endpoint. Because of this, the endpoint's configuration is decoupled from the instance profile's state in the Databricks UI. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Resolution

To pick up changes to an instance profile, the endpoint must be explicitly updated. Use the `PUT /api/2.0/serving-endpoints/{name}/config` API with the updated `instance_profile_arn` field in the `served_entities` block to refresh the endpoint's configuration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile – The IAM role wrapper used to grant AWS resource access.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The serverless endpoint that hosts and serves models.
- STS Temporary Security Credentials – The mechanism used by the endpoint to authenticate data access; these credentials cannot bypass network restrictions.
- [Serving UI](/concepts/serving-ui.md) – The Databricks interface for creating and managing serving endpoints.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
