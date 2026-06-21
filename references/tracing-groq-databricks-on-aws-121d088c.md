---
title: Tracing Groq | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/groq
ingestedAt: "2026-06-18T08:17:13.474Z"
---

![Groq tracing using autolog](https://docs.databricks.com/aws/en/assets/images/groq-tracing-c479723e95472339d07b0dd94b38854b.png)

MLflow Tracing provides automatic tracing capability when using Groq. When Groq auto-tracing is enabled by calling the [`mlflow.groq.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.groq.html#mlflow.groq.autolog) function, usage of the Groq SDK will automatically record generated traces during interactive development.

note

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.groq.autolog()` to enable automatic tracing for this integration.

Note that only synchronous calls are supported, and that asynchronous API and streaming methods are not traced.

### Example Usage[​](#example-usage "Direct link to Example Usage")

Python

    import groqimport mlflow# Turn on auto tracing for Groq by calling mlflow.groq.autolog()mlflow.groq.autolog()# Set up MLflow tracking on Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/groq-demo")client = groq.Groq()# Use the create method to create new messagemessage = client.chat.completions.create(    model="llama-3.3-70b-versatile",    messages=[        {            "role": "user",            "content": "Explain the importance of low latency LLMs.",        }    ],)print(message.choices[0].message.content)

## Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for Groq can be disabled globally by calling `mlflow.groq.autolog(disable=True)` or `mlflow.autolog(disable=True)`.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Understand tracing concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) - Learn how MLflow captures and organizes trace data
*   [Debug and observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use the Trace UI to analyze your Groq application's behavior
*   [Evaluate your app's quality](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Set up quality assessment for your Groq-powered application
