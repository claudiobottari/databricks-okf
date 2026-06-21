---
title: Model serving observability with Genie Code | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-genie-code
ingestedAt: "2026-06-18T08:12:10.518Z"
---

This article describes how Genie Code can help you diagnose issues, analyze performance, and get guidance for your model serving endpoints.

## Requirements[​](#requirements "Direct link to Requirements")

To use Genie Code for model serving observability, your workspace needs the following:

*   Partner-powered AI features enabled for both the account and workspace. See [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered).
*   Your workspace must be in a supported region. Genie Code is a [Designated Service](https://docs.databricks.com/aws/en/resources/designated-services) that uses Geos to manage data residency. See [Geo availability of Genie Code features](https://docs.databricks.com/aws/en/genie-code/#geo-availability).

note

Genie Code currently only supports custom model serving endpoints.

## What can Genie Code help with?[​](#what-can-genie-code-help-with "Direct link to what-can-genie-code-help-with")

When you use Genie Code on a model serving endpoint page, it becomes an observability companion for model serving. It can analyze endpoint health, diagnose deployment failures, investigate latency issues, and provide best practice guidance — all from the Genie Code pane.

![Genie Code pane on an endpoint page](https://docs.databricks.com/aws/en/assets/images/genie-code-endpoint-pane-e0f2ff6e295a4d520753a2a76ba51ff1.png)

Genie Code is a read-only advisor in this mode. It can inspect your endpoints and provide recommendations, but it can't modify configurations or deployments. It has clear, step-by-step instructions and links to documentation so you can make changes yourself.

## Get started[​](#get-started "Direct link to Get started")

To get started:

1.  Go to a model serving endpoint page.
2.  Click ![Sparkle genie code icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTAgOC43NUwwIDguMDA1ODZDMC4wMDAyMDA1NjUgNy4wMzYyMSAwLjc4NjIxNCA2LjI1MDIgMS43NTU4NiA2LjI1TDIuODU2NDUgNi4yNUMzLjIyODIzIDYuMjUgMy41NjgxMSA2LjQ2MDQzIDMuNzM0MzggNi43OTI5N0w0LjMyOTEgNy45ODE0NUM1LjAyNDMyIDkuMzcxOCA2LjQ0NTUxIDEwLjI1IDggMTAuMjVDOS41NTQ0OSAxMC4yNSAxMC45NzU3IDkuMzcxOCAxMS42NzA5IDcuOTgxNDVMMTIuMjY1NiA2Ljc5Mjk3TDEyLjMzNSA2LjY3MzgzQzEyLjUxNjUgNi40MTA3MiAxMi44MTgyIDYuMjUgMTMuMTQzNiA2LjI1TDE2IDYuMjVWNy43NUwxMy40NjM5IDcuNzVMMTMuMDEyNyA4LjY1MjM0QzEyLjA2MzQgMTAuNTUwOSAxMC4xMjI2IDExLjc1IDggMTEuNzVDNS44NzczNSAxMS43NSAzLjkzNjYxIDEwLjU1MDkgMi45ODczIDguNjUyMzRMMi41MzYxMyA3Ljc1SDEuNzU1ODZDMS42MTQ2NCA3Ljc1MDIgMS41MDAyIDcuODY0NjQgMS41IDguMDA1ODZWOC43NUMxLjUgOS4wMjYxNCAxLjcyMzg2IDkuMjUgMiA5LjI1VjEwLjc1QzAuODk1NDMgMTAuNzUgMCA5Ljg1NDU3IDAgOC43NVogTTEwLjUgMTIuNzVWMTQuMjVMNS41IDE0LjI1VjEyLjc1TDEwLjUgMTIuNzVaIE04IDEuNzVDOC4zNjQ1MiAxLjc1IDguNjc2NjUgMi4wMTIwMiA4LjczOTI2IDIuMzcxMDlMOC45NjU4MiAzLjY3MzgzQzkuMDIwMDYgMy45ODU3MyA5LjI2NDI3IDQuMjI5OTQgOS41NzYxNyA0LjI4NDE4TDEwLjg3ODkgNC41MTA3NEMxMS4yMzggNC41NzMzNSAxMS41IDQuODg1NDggMTEuNSA1LjI1QzExLjUgNS42MTQ1MiAxMS4yMzggNS45MjY2NSAxMC44Nzg5IDUuOTg5MjZMOS41NzYxNyA2LjIxNTgyQzkuMjY0MjcgNi4yNzAwNiA5LjAyMDA2IDYuNTE0MjcgOC45NjU4MiA2LjgyNjE3TDguNzM5MjYgOC4xMjg5MUM4LjY3NjY1IDguNDg3OTggOC4zNjQ1MiA4Ljc1IDggOC43NUM3LjYzNTQ4IDguNzUgNy4zMjMzNSA4LjQ4Nzk4IDcuMjYwNzQgOC4xMjg5MUw3LjAzNDE4IDYuODI2MTdDNi45Nzk5NCA2LjUxNDI3IDYuNzM1NzMgNi4yNzAwNiA2LjQyMzgzIDYuMjE1ODJMNS4xMjEwOSA1Ljk4OTI2QzQuNzYyMDIgNS45MjY2NSA0LjUgNS42MTQ1MiA0LjUgNS4yNUM0LjUgNC44ODU0OCA0Ljc2MjAyIDQuNTczMzUgNS4xMjEwOSA0LjUxMDc0TDYuNDIzODMgNC4yODQxOEM2LjczNTczIDQuMjI5OTQgNi45Nzk5NCAzLjk4NTczIDcuMDM0MTggMy42NzM4M0w3LjI2MDc0IDIuMzcxMDlMNy4yOTU5IDIuMjQxMjFDNy40MDI1MyAxLjk1MDU3IDcuNjgxMSAxLjc1IDggMS43NVoiIGZpbGw9InVybCgjc3BhcmtsZV9nZW5pZV9jb2RlX2dyYWRpZW50KSIvPgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJzcGFya2xlX2dlbmllX2NvZGVfZ3JhZGllbnQiIHgxPSIxNS4zMDQ4IiB5MT0iMC4zMjI5OTMiIHgyPSIwLjI0ODU2MiIgeTI9IjE1LjM3OTIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agb2Zmc2V0PSIwLjIzNSIgc3RvcC1jb2xvcj0iIzQyOTlFMCIvPgo8c3RvcCBvZmZzZXQ9IjAuNDciIHN0b3AtY29sb3I9IiNDQTQyRTAiLz4KPHN0b3Agb2Zmc2V0PSIwLjc2IiBzdG9wLWNvbG9yPSIjRkY1RjQ2Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjwvZGVmcz4KPC9zdmc+Cg==) to open the Genie Code pane.
3.  In the lower-right corner, select **Agent**. This toggles on Genie Code's Agent mode.
4.  Enter a prompt describing what you need help with. For example, "Check the health of this endpoint" or "Why is my latency so high?"

## Capabilities[​](#capabilities "Direct link to Capabilities")

### Health checks and diagnostics[​](#health-checks-and-diagnostics "Direct link to Health checks and diagnostics")

Genie Code can analyze your endpoint's status and configuration to identify potential issues:

*   Check endpoint health and deployment states.
*   Review configuration against best practices.
*   Assess scaling and resource utilization.

### Troubleshooting and analysis[​](#troubleshooting-and-analysis "Direct link to Troubleshooting and analysis")

Genie Code can help resolve issues with your endpoints:

*   Diagnose deployment failures using build logs, events, and endpoint state.
*   Investigate high latency or timeout issues using metrics, events, and inference table data.
*   Analyze error patterns from service logs and inference tables.
*   Identify misconfigurations or resource constraints.
*   Compare current and pending configurations with risk assessment.

### Guidance and best practices[​](#guidance-and-best-practices "Direct link to Guidance and best practices")

Genie Code has recommendations based on your endpoint's configuration:

*   Recommend optimal scaling configurations for production and development workloads.
*   Explain endpoint states and transitions.
*   Guide you on monitoring and observability setup.
*   Search Databricks documentation and provide links to relevant articles.

## Use cases[​](#use-cases "Direct link to Use cases")

Try these prompts to get started:

*   Health checks:
    *   "Check the health of this endpoint."
    *   "Is my endpoint configured correctly?"
    *   "Review my endpoint's scaling configuration."
*   Deployment failures:
    *   "/diagnose" or "Why did my deployment fail?"
    *   "Help me fix deployment errors."
    *   "My endpoint is stuck in a pending state."
*   Latency debugging:
    *   "Why is my latency so high?"
    *   "Analyze the latency spike from this morning."
    *   "Show me the performance metrics for the last 24 hours."
*   Configuration review:
    *   "What changed in my pending configuration?"
    *   "Is my concurrency setting appropriate for production?"
    *   "Show me my inference table configuration."
*   Request history:
    *   "Show me recent requests to this endpoint."
    *   "What errors are my users hitting?"
    *   "Analyze error patterns from the last week."

## Additional information[​](#additional-information "Direct link to Additional information")

*   [Genie Code](https://docs.databricks.com/aws/en/genie-code/)
*   [Use Genie Code](https://docs.databricks.com/aws/en/genie-code/use-genie-code)
*   [Monitor model quality and endpoint health](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints)
*   [Debugging guide for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug)
*   [Optimize Model Serving endpoints for production](https://docs.databricks.com/aws/en/machine-learning/model-serving/production-optimization)
