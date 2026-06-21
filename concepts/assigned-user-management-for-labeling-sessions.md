---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be71d8c29866ab17bfbf8df072012177c80524a7d2b4b497a70fbfcae595965f
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assigned-user-management-for-labeling-sessions
    - AUMFLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Assigned User Management for Labeling Sessions
description: The process of adding, replacing, and configuring permissions for domain expert reviewers in labeling sessions, including automatic WRITE permission grants on the underlying MLflow Experiment.
tags:
  - mlflow
  - human-feedback
  - permissions
  - user-management
timestamp: "2026-06-19T09:33:30.410Z"
---

# Assigned User Management for Labeling Sessions

**Assigned User Management for Labeling Sessions** refers to the process of designating domain experts who will review MLflow traces and provide assessments (labels) within a [Labeling Session](/concepts/labeling-session.md). Properly managing assigned users ensures that the right reviewers have access to the session and that their feedback is collected systematically.

## Overview

Each labeling session must have at least one assigned user. Users are identified by their email address and granted access to the session’s MLflow experiment and the Review App. Assignment can be done at session creation or modified later using the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Assigning Users During Session Creation

When creating a labeling session via the API, the `assigned_users` parameter accepts a list of email addresses for the domain experts who will provide labels. At least one user is required. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session = labeling.create_labeling_session(
    name="customer_service_review_jan_2024",
    assigned_users=["alice@company.com", "bob@company.com"],
    label_schemas=[schemas.EXPECTED_FACTS]
)
```

The same parameter is used when creating sessions that use custom label schemas or when connecting to a deployed agent. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

In the UI, after creating a session, the session owner can click **Share** in the session details view, enter reviewer email addresses, and save. Reviewers are then notified and given access to the Review App. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Users to Existing Sessions

To add users to an existing session, use the `set_assigned_users()` method on the session object. This method replaces the entire list of assigned users, so you must combine the existing list with new users. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
# Find the session by name
session = next(s for s in labeling.get_labeling_sessions()
               if s.name == "customer_review_session")

# Append new users to the existing list
new_users = ["expert2@company.com", "expert3@company.com"]
session.set_assigned_users(session.assigned_users + new_users)
```

After the call, `session.assigned_users` reflects the updated list. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Replacing Assigned Users

To completely replace the set of reviewers — for example, when a session needs a new reviewer lead — call `set_assigned_users()` with a list containing only the desired users. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

This overwrites any previous assignment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## User Access Requirements and Permissions

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they have workspace access. However, granting a user permission to a labeling session gives them access to the labeling session’s MLflow experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Users without workspace access**: An account admin must use account-level SCIM provisioning to sync users and groups from the identity provider to the Databricks account. Alternatively, admins can manually register users. See User and group management (SCIM). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Users with existing workspace access**: No additional configuration is required. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When users are assigned, the system automatically grants necessary `WRITE` permissions on the MLflow experiment that contains the labeling session. This gives assigned users the ability to view and interact with the experiment data. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Distribute work evenly**: Assign users based on domain expertise and availability to avoid overloading any single reviewer. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Store run IDs for reference**: Use `session.mlflow_run_id` when adding or replacing users programmatically, rather than relying on session names (which may not be unique). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Keep sessions focused**: Aim for 25–100 traces per session to prevent reviewer fatigue. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Ensure users have workspace access**: Although users without workspace access can be assigned, they must be provisioned via SCIM and granted permissions. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Session](/concepts/labeling-session.md) – The container for traces and feedback
- [Labeling Schemas](/concepts/labeling-schemas.md) – The questions and format for feedback collection
- [Review App](/concepts/mlflow-review-app.md) – The UI where assigned users provide assessments
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs, including labeling sessions
- SCIM Provisioning – How to sync users from an identity provider to Databricks

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
