---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18ca4ef7558ff6fe961546f9c8904ba15338e6897267cffbe3be2d3b27f3ded7
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assigned-user-management-for-labeling
    - AUMFL
    - assigned-user-management-for-labeling-sessions
    - AUMFLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Assigned User Management for Labeling
description: The process of adding, replacing, and managing domain experts assigned to labeling sessions, including automatic WRITE permission grants on the MLflow experiment.
tags:
  - mlflow
  - permissions
  - user-management
  - labeling
timestamp: "2026-06-18T14:51:33.207Z"
---

# Assigned User Management for Labeling

**Assigned User Management for Labeling** refers to the process of designating domain experts to review traces and provide feedback within [Labeling Sessions](/concepts/labeling-sessions.md). Managing the list of assigned users is a core part of setting up and maintaining a labeling workflow, as these users are the ones who produce the human-generated assessments (labels) that drive evaluation and improvement of GenAI applications.

## User Access Requirements

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they already have access to the workspace. However, because granting a user permission to a labeling session also gives them access to the labeling session’s MLflow experiment, access management must be handled carefully.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Users who already have workspace access** need no additional configuration; they can be assigned directly.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Users without workspace access** must first be provisioned. An account admin uses account-level SCIM provisioning to sync users and groups automatically from your identity provider, or manually registers them. See User and group management on Databricks for details.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When you assign users to a labeling session, the system automatically grants the necessary `WRITE` permissions on the MLflow Experiment that contains the labeling session. This enables assigned users to view and interact with the experiment data.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Users to Existing Sessions

To add users to an existing labeling session, use the `set_assigned_users()` method on the session object. The method takes a list of user email addresses and replaces the current list. To add new users while retaining existing ones, combine the current list with the new users, as shown in the following example:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session.set_assigned_users(session.assigned_users + new_users)
```

After this call, the session’s `assigned_users` attribute reflects the updated list.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Replacing All Assigned Users

To completely replace the set of assigned users (e.g., when handing off the session to a new review team), call `set_assigned_users()` with only the new list:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

This removes any previous assignees and sets the session to the specified users.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Retrieving Assigned Users

The current list of assigned users is available via the `session.assigned_users` attribute, which returns a list of email addresses. This can be used to verify assignments or to programmatically manage user lists.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Assign users based on domain expertise and availability.** The quality of labels depends on matching reviewers with the right subject-matter knowledge.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Distribute labeling work evenly** across multiple experts to avoid overburdening a single reviewer and to get diverse perspectives.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Remember that users must have access to the Databricks workspace.** Even if they are provisioned via SCIM, they must be able to log in and use the Review App.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – The container for traces and assigned-user reviews.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit that holds labeling session runs and data.
- SCIM Provisioning – Mechanism to sync users from an identity provider to Databricks.
- [Labeling Schemas](/concepts/labeling-schemas.md) – The questions and format used to collect feedback.
- [MLflow Review App](/concepts/mlflow-review-app.md) – The UI where assigned users provide labels.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
