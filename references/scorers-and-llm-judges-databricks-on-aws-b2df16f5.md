---
title: Scorers and LLM judges | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers
ingestedAt: "2026-06-18T08:15:07.508Z"
---

Scorers are a key component of the MLflow GenAI evaluation framework. They provide a unified interface to define evaluation criteria for your models, agents, and applications. Like their name suggests, scorers score how well your application did based on the evaluation criteria. This could be a pass/fail, true/false, numerical value, or a categorical value.

You can use the same scorer for [evaluation in development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) and [monitoring in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to keep evaluation consistent throughout the application lifecycle.

Choose the right type of scorer depending on how much customization and control you need. Each approach builds on the previous one, adding more complexity and control.

Start with [built-in judges](#built-in-judges) for quick evaluation. As your needs evolve, build [custom LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) for domain-specific criteria and create [custom code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) for deterministic business logic.

The following screenshot shows the results from the built-in LLM judge `Safety` and a custom scorer `exact_match`:

![Example metrics from scorers](https://docs.databricks.com/aws/en/assets/images/basic-scorer-example-ui-417a4c80eb9d51ec5e12ceffdbaf352d.png)

## How scorers work[​](#how-scorers-work "Direct link to How scorers work")

A scorer receives a [Trace](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) from either `evaluate()` or the monitoring service. It then does the following:

1.  Parses the `trace` to extract specific fields and data that are used to assess quality
2.  Runs the scorer to perform the quality assessment based on the extracted fields and data
3.  Returns the quality assessment as [`Feedback`](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations) to attach to the `trace`

![Evaluation traces](https://docs.databricks.com/aws/en/assets/images/predefined-traces-1f3af862ed541693147768142e8977c2.png)

![Evaluation UI](https://docs.databricks.com/aws/en/assets/images/predefined-ui-0a79f2dcfbe85f1bab37782e4f5f3e35.png)

## LLMs as judges[​](#llms-as-judges "Direct link to LLMs as judges")

LLM judges are a type of MLflow `Scorer` that uses Large Language Models for quality assessment.

Think of a judge as an AI assistant specialized in quality assessment. It can evaluate your app's inputs, outputs, and even explore the entire execution trace to make assessments based on criteria you define. For example, a judge can understand that `give me healthy food options` and `food to keep me fit` are similar queries.

note

Judges are a type of scorer that use LLMs for evaluation. Use them directly with `mlflow.genai.evaluate()` or wrap them in [custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) for advanced scoring logic.

### Built-in LLM judges[​](#built-in-llm-judges "Direct link to built-in-llm-judges")

MLflow provides research-validated built-in judges for common quality dimensions like relevance, safety, groundedness, and correctness. For the complete list and detailed guidance on each judge, see [Built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/).

### Multi-turn judges[​](#multi-turn-judges "Direct link to multi-turn-judges")

For conversational AI systems, MLflow also provides built-in judges that evaluate entire conversations rather than individual turns. See [Multi-turn judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/#multi-turn-judges).

### Custom LLM judges[​](#custom-llm-judges "Direct link to Custom LLM judges")

In addition to built-in judges, you can create your own judges using custom prompts and instructions.

Use custom LLM judges when you need to define specialized evaluation tasks, need more control over grades or scores (not just pass/fail), or need to validate that your agent made appropriate decisions and performed operations correctly for your specific use case. Use [judge alignment](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) to train custom LLM judges to match human evaluation standards through systematic feedback.

See [Custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/).

### Select the LLM that powers the judge[​](#select-the-llm-that-powers-the-judge "Direct link to Select the LLM that powers the judge")

By default, each judge uses a [Databricks-hosted LLM](#llm-judge-trust) designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument in the judge definition. Specify the model in the format `<provider>:/<model-name>`. For example:

Python

    from mlflow.genai.scorers import CorrectnessCorrectness(model="databricks:/databricks-gpt-5-mini")

## Information about the models powering LLM judges[​](#information-about-the-models-powering-llm-judges "Direct link to information-about-the-models-powering-llm-judges")

*   LLM judges might use third-party services to evaluate your GenAI applications, including Azure OpenAI operated by Microsoft.
*   For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI.
*   For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US.
*   Disabling [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered) prevents the LLM judge from calling partner-powered models. You can still use LLM judges by providing your own model.
*   LLM judges are intended to help customers evaluate their GenAI agents/applications, and LLM judge outputs should not be used to train, improve, or fine-tune an LLM.

### Judge accuracy[​](#judge-accuracy "Direct link to Judge accuracy")

Databricks continuously improves judge quality through:

*   **Research validation** against human expert judgment
*   **Metrics tracking**: Cohen's Kappa, accuracy, F1 score
*   **Diverse testing** on academic and real-world datasets

## Code-based scorers[​](#code-based-scorers "Direct link to Code-based scorers")

Custom code-based scorers offer the ultimate flexibility to define precisely how your GenAI application's quality is measured. You can define evaluation metrics tailored to your specific business use case, whether based on simple heuristics, advanced logic, or programmatic evaluations.

Use custom scorers for the following scenarios:

1.  Defining a custom heuristic or code-based evaluation metric.
2.  Customizing how the data from your app's trace is mapped to built-in LLM judges.
3.  Using your own LLM (rather than a Databricks-hosted LLM judge) for evaluation.
4.  Any other use cases where you need more flexibility and control than provided by custom LLM judges.

See [Code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers).
