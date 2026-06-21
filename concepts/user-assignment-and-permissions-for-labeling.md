---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 45f61638983ebf5b9079dd01acc299b1ede0101d2457652582fc961a1fff3aff
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-assignment-and-permissions-for-labeling
    - Permissions for Labeling and User Assignment
    - UAAPFL
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: User Assignment and Permissions for Labeling
description: The process of assigning domain experts to labeling sessions, including automatic WRITE permission grants on the underlying MLflow experiment and identity provisioning for external users.
tags:
  - permissions
  - users
  - mlflow
  - labeling
timestamp: "2026-06-19T14:34:00.461Z"
---

# User Assignment and Permissions for Labeling

**User Assignment and Permissions for Labeling** refers to the process of designating domain experts (reviewers) to participate in [Labeling Sessions](/concepts/labeling-sessions.md) and managing their access rights to the underlying [MLflow experiments](/concepts/mlflow-experiment.md) and tracing data within the Databricks [MLflow Review App](/concepts/mlflow-review-app.md).

## Overview

When a labeling session is created, the creator defines a list of **assigned users** — typically domain experts who will review agent traces and provide structured labels. These users can be added, removed, or replaced throughout the lifetime of the session using the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The system automatically manages permissions to ensure that assigned users can view and interact with the relevant experiment data. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## User Access Requirements

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they already have workspace access. However, assigning a user to a session grants them access to the labeling session’s MLflow experiment. Therefore, proper identity management is important. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Users without workspace access**: An account admin must use account-level SCIM provisioning to sync users and groups from the identity provider to the Databricks account. Alternatively, users can be manually registered. See User and Group Management.
- **Users with existing workspace access**: No additional configuration is required. They can be assigned directly to labeling sessions. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Permission Setup

When a user is assigned to a labeling session, the system automatically grants **WRITE** permissions on the MLflow Experiment that contains the labeling session. This allows the assigned user to view and interact with the experiment data, including traces and labels. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

This automatic permission grant simplifies onboarding but also means that session creators should be mindful of which experiment the session lives under, as access may be broadened to users who otherwise would not see that experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Assigning Users to Sessions

### Creating a Session with Assigned Users

When creating a labeling session via the UI or API, the `assigned_users` parameter accepts a list of email addresses of the reviewers. Example using the API:

```python
import mlflow.genai.labeling as labeling

session = labeling.create_labeling_session(
    name="customer_service_review_jan_2024",
    assigned_users=["alice@company.com", "bob@company.com"],
    ...
)
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Adding Users to an Existing Session

To add more users after the session has been created, use the `set_assigned_users()` method. Pass the current list of assigned users concatenated with the new ones:

```python
new_users = ["expert2@company.com", "expert3@company.com"]
session.set_assigned_users(session.assigned_users + new_users)
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Replacing All Assigned Users

To replace the entire list of assigned users, pass only the new list to `set_assigned_users()`:

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Assign users based on domain expertise and availability.** Ensure that the reviewers have the knowledge needed to evaluate the agent’s behavior. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Distribute labeling work evenly across multiple experts** to avoid single-reviewer bias and prevent reviewer fatigue. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Remember that assigned users must have access to the Databricks workspace** (either through SCIM provisioning or existing access) before they can participate. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Store the `session.mlflow_run_id`** when creating a session, as session names may not be unique. Use the run ID for programmatic access rather than relying on names. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Review App](/concepts/mlflow-review-app.md)
- SCIM Provisioning
- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md)

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
