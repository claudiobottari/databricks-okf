---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 660d22d49698022485e344ce59c43864ebdded3358c6aab0bdead39f2ff69a3b
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-session-user-management-and-permissions
    - Permissions and Labeling Session User Management
    - LSUMAP
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Session User Management and Permissions
description: Process for assigning users to labeling sessions, including automatic WRITE permission grants on the MLflow experiment, SCIM provisioning for non-workspace users, and APIs for adding or replacing assigned users.
tags:
  - mlflow
  - permissions
  - user-management
  - labeling
timestamp: "2026-06-18T11:19:12.110Z"
---

# Labeling Session User Management and Permissions

**Labeling Session User Management and Permissions** encompasses the processes, requirements, and best practices for assigning domain experts to [Labeling Sessions](/concepts/labeling-sessions.md) and managing their access to [MLflow Review App](/concepts/mlflow-review-app.md) in Databricks.

## User Access Requirements

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they already have workspace access. However, granting a user permission to a labeling session also gives them access to the labeling session's [MLflow Experiment](/concepts/mlflow-experiment.md). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Workspace Access Configuration

For users who do not have access to the workspace, an account admin must use account-level SCIM provisioning to sync users and groups automatically from your identity provider to your Databricks account. Alternatively, you can manually register these users and groups to give them access when you set up identities in Databricks. For users who already have access to the workspace that contains the review app, no additional configuration is required. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Automatic Permissions Granting

When you assign users to a labeling session, the system automatically grants the necessary `WRITE` permissions on the MLflow Experiment containing the labeling session. This gives assigned users access to view and interact with the experiment data. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Assigned Users

### Adding Users to Existing Sessions

To add users to an existing session, use the `set_assigned_users()` API method. Retrieve the current user list and append new users to it: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

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
```

### Replacing All Assigned Users

To completely replace the set of users assigned to a session, pass a new list to `set_assigned_users()`: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling

# Find session by name
all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "session_name":
        session = s
        break

if session:
    # Replace all assigned users
    session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
    print("Updated assigned users list")
```

### Sharing Sessions via the UI

To share a labeling session with reviewers through the MLflow UI: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

1. Open the experiment and click **Labeling sessions** in the sidebar.
2. Click the session name in the list.
3. Click **Share** at the upper right.
4. Enter an email address for each reviewer and click **Save**.

Reviewers are notified and given access to the Review App.

## Viewing Reviewer Feedback

To view reviewer feedback for a session in the UI: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

1. Click the session name in the list.
2. Click the request to see the notification showing the trace and reviewer assessments.
3. Click **Assessments** at the upper right to display reviewers' input.

## Best Practices

### Session Organization

- Store the `session.mlflow_run_id` when creating a session, as session names may not be unique. Use the run ID for programmatic access instead of relying on session names. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Use clear, descriptive, date-stamped names, such as `customer_service_review_march_2024`. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### User Management

- Assign users based on domain expertise and availability. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Distribute labeling work evenly across multiple experts to avoid reviewer fatigue. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Ensure that assigned users have access to the Databricks workspace; set up account-level SCIM provisioning for users who do not. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Containers for traces and labels that drive feedback collection
- [Labeling Schemas](/concepts/labeling-schemas.md) — Question formats that define what feedback is collected
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that labeling sessions are logged to
- [[MLflow Trace|MLflow Traces]] — The execution records that are reviewed and labeled in sessions
- [Human Feedback for GenAI](/concepts/human-feedback-collection-for-judge-alignment.md) — The broader workflow for incorporating human assessments

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
