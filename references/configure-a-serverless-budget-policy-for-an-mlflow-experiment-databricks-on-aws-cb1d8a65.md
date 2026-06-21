---
title: Configure a serverless budget policy for an MLflow experiment | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/serverless-budget-policy
ingestedAt: "2026-06-18T08:15:30.120Z"
---

Set a [serverless budget policy](https://docs.databricks.com/aws/en/admin/usage/budget-policies) on an MLflow experiment to control which policy MLflow uses for serverless workloads it runs against the experiment. Affected workloads include [scheduled scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring), [synthetic evaluation set generation](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/synthesize-evaluation-set), and [agent evaluation](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app).

By default, these workloads use the workspace's default serverless budget policy. If your workspace disables the default policy (for example, when each user and service principal must select a dedicated policy), MLflow cannot pick a fallback and registering a scorer or running an evaluation fails with the following error:

Text

    403 Client Error: ForbiddenPERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.

Set the policy on the experiment to unblock these workflows. MLflow then uses that policy for every serverless workload it creates for the experiment.

## Requirements[​](#requirements "Direct link to Requirements")

*   Permission to use the budget policy you want to set. Users and service principals can only assign a policy that they are entitled to use.

## Set the budget policy in the UI[​](#set-the-budget-policy-in-the-ui "Direct link to Set the budget policy in the UI")

1.  Open the MLflow experiment.
2.  In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow uses this policy for serverless workloads it creates on behalf of the experiment.

## Set the budget policy with the API[​](#set-the-budget-policy-with-the-api "Direct link to Set the budget policy with the API")

Use [`mlflow.set_experiment_tag()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment_tag) to set the `mlflow.workload_creation_policy_id` tag on the experiment:

Python

    import mlflowmlflow.set_experiment_tag(    experiment_id="<your-experiment-id>",    key="mlflow.workload_creation_policy_id",    value="<your-policy-id>",)

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy.

To find the ID of a budget policy, see [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Monitor GenAI apps in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring)
*   [Manage production scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/manage-production-scorers)
*   [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies)
