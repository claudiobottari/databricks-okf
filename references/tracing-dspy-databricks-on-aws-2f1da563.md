---
title: Tracing DSPy | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/dspy
ingestedAt: "2026-06-18T08:17:09.490Z"
---

![DSPy Tracing using autolog](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/dspy-tracing.gif)

[DSPy](https://dspy.ai/) is an open-source framework for building modular AI systems and offers algorithms for optimizing their prompts and weights.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides automatic tracing capability for DSPy. You can enable tracing for DSPy by calling the [`mlflow.dspy.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.dspy.html#mlflow.dspy.autolog) function, and nested traces are automatically logged to the active MLflow Experiment upon invocation of DSPy modules.

Python

    import mlflowmlflow.dspy.autolog()

note

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.dspy.autolog()` to enable automatic tracing for this integration.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with DSPy, you need to install MLflow and the `dspy-ai` library.

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras and `dspy-ai`:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" dspy-ai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is highly recommended for the best tracing experience with DSPy.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

**API Keys**: Ensure your LLM provider API keys are configured. For production environments, use [AI Gateway or Databricks secrets](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/#secure-api-key-management) instead of hardcoded values for secure API key management.

Bash

    export OPENAI_API_KEY="your-openai-api-key"# Add other provider keys as needed

### Example Usage[​](#example-usage "Direct link to Example Usage")

Python

    import dspyimport mlflowimport os# Ensure your OPENAI_API_KEY (or other LLM provider keys) is set in your environment# os.environ["OPENAI_API_KEY"] = "your-openai-api-key" # Uncomment and set if not globally configured# Enabling tracing for DSPymlflow.dspy.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/dspy-tracing-demo")# Define a simple ChainOfThought model and run itlm = dspy.LM("openai/gpt-4o-mini")dspy.configure(lm=lm)# Define a simple summarizer model and run itclass SummarizeSignature(dspy.Signature):    """Given a passage, generate a summary."""    passage: str = dspy.InputField(desc="a passage to summarize")    summary: str = dspy.OutputField(desc="a one-line summary of the passage")class Summarize(dspy.Module):    def __init__(self):        self.summarize = dspy.ChainOfThought(SummarizeSignature)    def forward(self, passage: str):        return self.summarize(passage=passage)summarizer = Summarize()summarizer(    passage=(        "MLflow Tracing is a feature that enhances LLM observability in your Generative AI (GenAI) applications "        "by capturing detailed information about the execution of your application's services. Tracing provides "        "a way to record the inputs, outputs, and metadata associated with each intermediate step of a request, "        "enabling you to easily pinpoint the source of bugs and unexpected behaviors."    ))

### Tracing during Evaluation[​](#tracing-during-evaluation "Direct link to Tracing during Evaluation")

Evaluating DSPy models is an important step in the development of AI systems. MLflow Tracing can help you track the performance of your programs after the evaluation, by providing detailed information about the execution of your programs for each input.

When MLflow auto-tracing is enabled for DSPy, traces will be automatically generated when you execute DSPy's [built-in evaluation suites](https://dspy.ai/learn/evaluation/overview/). The following example demonstrates how to run evaluation and review traces in MLflow:

Python

    import dspyfrom dspy.evaluate.metrics import answer_exact_matchimport mlflowimport os# Ensure your OPENAI_API_KEY (or other LLM provider keys) is set in your environment# os.environ["OPENAI_API_KEY"] = "your-openai-api-key" # Uncomment and set if not globally configured# Enabling tracing for DSPy evaluationmlflow.dspy.autolog(log_traces_from_eval=True)# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/dspy-eval-demo")# Define a simple evaluation seteval_set = [    dspy.Example(        question="How many 'r's are in the word 'strawberry'?", answer="3"    ).with_inputs("question"),    dspy.Example(        question="How many 'a's are in the word 'banana'?", answer="3"    ).with_inputs("question"),    dspy.Example(        question="How many 'e's are in the word 'elephant'?", answer="2"    ).with_inputs("question"),]# Define a programclass Counter(dspy.Signature):    question: str = dspy.InputField()    answer: str = dspy.OutputField(        desc="Should only contain a single number as an answer"    )cot = dspy.ChainOfThought(Counter)# Evaluate the programswith mlflow.start_run(run_name="CoT Evaluation"):    evaluator = dspy.evaluate.Evaluate(        devset=eval_set,        return_all_scores=True,        return_outputs=True,        show_progress=True,    )    aggregated_score, outputs, all_scores = evaluator(cot, metric=answer_exact_match)    # Log the aggregated score    mlflow.log_metric("exact_match", aggregated_score)    # Log the detailed evaluation results as a table    mlflow.log_table(        {            "question": [example.question for example in eval_set],            "answer": [example.answer for example in eval_set],            "output": outputs,            "exact_match": all_scores,        },        artifact_file="eval_results.json",    )

If you open the MLflow UI and go to the "CoT Evaluation" run, you will see the evaluation result, and the list of traces generated during the evaluation on the `Traces` tab.

note

You can disable tracing for these steps by calling the [`mlflow.dspy.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.dspy.html#mlflow.dspy.autolog) function with the `log_traces_from_eval` parameters set to `False`.

### Tracing during Compilation (Optimization)[​](#tracing-during-compilation-optimization "Direct link to Tracing during Compilation (Optimization)")

[Compilation (optimization)](https://dspy.ai/learn/optimization/overview/) is the core concept of DSPy. Through compilation, DSPy automatically optimizes the prompts and weights of your DSPy program to achieve the best performance.

By default, MLflow does **NOT** generate traces during complication, because complication can trigger hundreds or thousands of invocations of DSPy modules. To enable tracing for compilation, you can call the [`mlflow.dspy.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.dspy.html#mlflow.dspy.autolog) function with the `log_traces_from_compile` parameter set to `True`.

Python

    import dspyimport mlflowimport os# Ensure your OPENAI_API_KEY (or other LLM provider keys) is set in your environment# os.environ["OPENAI_API_KEY"] = "your-openai-api-key" # Uncomment and set if not globally configured# Enable auto-tracing for compilationmlflow.dspy.autolog(log_traces_from_compile=True)# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/dspy-compile-demo")# Optimize the DSPy program as usualtp = dspy.MIPROv2(metric=metric, auto="medium", num_threads=24)optimized = tp.compile(cot, trainset=trainset, ...)

### Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for LlamaIndex can be disabled globally by calling `mlflow.llama_index.autolog(disable=True)` or `mlflow.autolog(disable=True)`.
