---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d8baae49930add9908f5c780a1ee4bfb1be105bde8268e6bd42aa4d5ba6cb93
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-session-user-management
    - LSUM
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Session User Management
description: The policies, permissions model, and API methods for assigning and managing domain expert reviewers for labeling sessions, including SCIM integration and workspace access.
tags:
  - mlflow
  - user-management
  - permissions
  - labeling
timestamp: "2026-06-19T17:59:15.443Z"
---

# Labeling Session User Management

**Labeling Session User Management** encompasses the processes for assigning, adding, and replacing users who act as domain expert reviewers within a [labeling session](/concepts/labeling-sessions.md). Proper user management ensures that the right experts have access to review traces and provide feedback on GenAI applications via the MLflow Review App. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

A labeling session can have one or more assigned users. These users are domain experts who review the traces in the session and provide labels using the [MLflow Review App](/concepts/mlflow-review-app.md). Users can be assigned at session creation time via the UI or the API, and the list of assigned users can be modified after the session exists. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## User Access Requirements

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they already have workspace access. However, granting a user permission to a labeling session also grants them access to the labeling session’s MLflow experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Users without workspace access:** An account admin must use account-level SCIM provisioning to sync users and groups from the identity provider to the Databricks account. Alternatively, users can be registered manually. See User and Group Management.
- **Users with existing workspace access:** No additional configuration is required. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When users are assigned to a labeling session, the system automatically grants the necessary `WRITE` permissions on the [MLflow Experiment](/concepts/mlflow-experiment.md) containing the labeling session. This allows assigned users to view and interact with the experiment data. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Users to Existing Sessions

To add users to an existing labeling session, use the `set_assigned_users()` API method. You must pass the current list of assigned users plus the new users to avoid overwriting existing assignments. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling

# Find existing session by name
all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "customer_review_session":
        session = s
        break
if session:
    # Add more users to the session
    new_users = ["expert2@company.com", "expert3@company.com"]
    session.set_assigned_users(session.assigned_users + new_users)
    print(f"Session now has users: {session.assigned_users}")
else:
    print("Session not found")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Replacing Assigned Users

To completely replace the set of assigned users, call `set_assigned_users()` with the new list. This overwrites any previous list. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
# Replace all assigned users
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
print("Updated assigned users list")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Distribute labeling work evenly** across multiple experts to avoid fatigue and ensure balanced feedback. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Assign users based on domain expertise** and availability. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Remember that users must have access to the Databricks workspace** – if they do not, use SCIM provisioning to grant access first. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- For programmatic access to sessions, store the `session.mlflow_run_id` instead of relying on session names (which may not be unique). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md)
- [MLflow Review App](/concepts/mlflow-review-app.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md)
- User and Group Management
- [Create and Manage Labeling Schemas](/concepts/labeling-schemas.md)

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
