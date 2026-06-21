---
title: Evaluate and compare prompt versions | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/evaluate-prompts
ingestedAt: "2026-06-18T08:16:15.412Z"
---

This guide shows you how to systematically evaluate different prompt versions to identify the most effective ones for your agents and GenAI applications. You'll learn to create prompt versions, build evaluation datasets with expected facts, and use MLflow's evaluation framework to compare performance.

All of the code on this page is included in the [example notebook](#example-notebook).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

This guide requires:

*   MLflow 3.1.0 or higher.
*   OpenAI API access or Databricks Model Serving.
*   Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges.

note

If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), you have the required permissions on the Unity Catalog schema `workspace.default`.

## Best practices[​](#best-practices "Direct link to Best practices")

1.  **Start simple**: Begin with basic prompts and iteratively improve based on evaluation results.
2.  **Use consistent datasets**: Evaluate all versions against the same data for fair comparison.
3.  **Track everything**: Log prompt versions, evaluation results, and deployment decisions.
4.  **Test edge cases**: Include challenging examples in your evaluation dataset.
5.  **Monitor production**: Continue evaluating prompts after deployment to catch degradation.
6.  **Document changes**: Use meaningful commit messages to track why changes were made.

## Step 1: Configure your environment[​](#step-1-configure-your-environment "Direct link to Step 1: Configure your environment")

note

You need `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges on both the catalog and schema to create prompts and evaluation datasets.

First, set up your Unity Catalog schema and install required packages:

Python

    # Install required packages%pip install --upgrade "mlflow[databricks]>=3.1.0" openaidbutils.library.restartPython()# Configure your Unity Catalog schemaimport mlflowimport pandas as pdfrom openai import OpenAIimport uuidCATALOG = "main"        # Replace with your catalog nameSCHEMA = "default"      # Replace with your schema name# Create unique names for the prompt and datasetSUFFIX = uuid.uuid4().hex[:8]  # Short unique suffixPROMPT_NAME = f"{CATALOG}.{SCHEMA}.summary_prompt_{SUFFIX}"EVAL_DATASET_NAME = f"{CATALOG}.{SCHEMA}.summary_eval_{SUFFIX}"print(f"Prompt name: {PROMPT_NAME}")print(f"Evaluation dataset: {EVAL_DATASET_NAME}")# Set up OpenAI clientclient = OpenAI()

## Step 2: Create prompt versions[​](#step-2-create-prompt-versions "Direct link to Step 2: Create prompt versions")

Register different prompt versions representing different approaches to your task:

Python

    # Version 1: Basic promptprompt_v1 = mlflow.genai.register_prompt(    name=PROMPT_NAME,    template="Summarize this text: {{content}}",    commit_message="v1: Basic summarization prompt")print(f"Created prompt version {prompt_v1.version}")# Version 2: Improved with comprehensive guidelinesprompt_v2 = mlflow.genai.register_prompt(    name=PROMPT_NAME,    template="""You are an expert summarizer. Create a summary of the following content in *exactly* 2 sentences (no more, no less - be very careful about the number of sentences).Guidelines:- Include ALL core facts and key findings- Use clear, concise language- Maintain factual accuracy- Cover all main points mentioned- Write for a general audience- Use exactly 2 sentencesContent: {{content}}Summary:""",    commit_message="v2: Added comprehensive fact coverage with 2-sentence requirement")print(f"Created prompt version {prompt_v2.version}")

## Step 3: Create evaluation dataset[​](#step-3-create-evaluation-dataset "Direct link to Step 3: Create evaluation dataset")

Build a dataset with expected facts that should appear in good summaries:

Python

    # Create evaluation dataseteval_dataset = mlflow.genai.datasets.create_dataset(    uc_table_name=EVAL_DATASET_NAME)# Add summarization examples with expected factsevaluation_examples = [    {        "inputs": {            "content": """Remote work has fundamentally changed how teams collaborate and communicate. Companies have adopted new digital tools for video conferencing, project management, and file sharing. While productivity has remained stable or increased in many cases, challenges include maintaining company culture, ensuring work-life balance, and managing distributed teams across time zones. The shift has also accelerated digital transformation initiatives and changed hiring practices, with many companies now recruiting talent globally rather than locally."""        },        "expectations": {            "expected_facts": [                "remote work changed collaboration",                "digital tools adoption",                "productivity remained stable",                "challenges with company culture",                "work-life balance issues",                "global talent recruitment"            ]        }    },    {        "inputs": {            "content": """Electric vehicles are gaining mainstream adoption as battery technology improves and charging infrastructure expands. Major automakers have committed to electrification with new models launching regularly. Government incentives and environmental regulations are driving consumer interest. However, challenges remain including higher upfront costs, limited charging stations in rural areas, and concerns about battery life and replacement costs. The market is expected to grow significantly over the next decade."""        },        "expectations": {            "expected_facts": [                "electric vehicles gaining adoption",                "battery technology improving",                "charging infrastructure expanding",                "government incentives",                "higher upfront costs",                "limited rural charging",                "market growth expected"            ]        }    },    {        "inputs": {            "content": """Artificial intelligence is transforming healthcare through diagnostic imaging, drug discovery, and personalized treatment plans. Machine learning algorithms can now detect diseases earlier and more accurately than traditional methods. AI-powered robots assist in surgery and patient care. However, concerns exist about data privacy, algorithm bias, and the need for regulatory oversight. Healthcare providers must balance innovation with patient safety and ethical considerations."""        },        "expectations": {            "expected_facts": [                "AI transforming healthcare",                "diagnostic imaging improvements",                "drug discovery acceleration",                "personalized treatment",                "earlier disease detection",                "data privacy concerns",                "algorithm bias issues",                "regulatory oversight needed"            ]        }    }]eval_dataset = eval_dataset.merge_records(evaluation_examples)print(f"Added {len(evaluation_examples)} summarization examples to evaluation dataset")

## Step 4: Create evaluation functions and custom metrics[​](#step-4-create-evaluation-functions-and-custom-metrics "Direct link to Step 4: Create evaluation functions and custom metrics")

Define functions that use your prompt versions and create custom evaluation metrics:

Python

    def create_summary_function(prompt_name: str, version: int):    """Create a summarization function for a specific prompt version."""    @mlflow.trace    def summarize_content(content: str) -> dict:        # Load the prompt version        prompt = mlflow.genai.load_prompt(            name_or_uri=f"prompts:/{prompt_name}/{version}"        )        # Format and call the LLM        formatted_prompt = prompt.format(content=content)        response = client.chat.completions.create(            model="gpt-4o-mini",            messages=[{"role": "user", "content": formatted_prompt}],            temperature=0.1        )        return {"summary": response.choices[0].message.content}    return summarize_content

### Create a judge with a custom prompt[​](#create-a-judge-with-a-custom-prompt "Direct link to Create a judge with a custom prompt")

Create a [judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) with a custom prompt to evaluate specific criteria using [`make_judge`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.make_judge):

Python

    from typing import Literalfrom mlflow.genai import make_judge# Create a custom judge using make_judgesentence_count_judge = make_judge(    name="sentence_count_compliance",    instructions="""Evaluate if this summary follows the 2-sentence requirement.Summary: {{ outputs }}Count the sentences carefully and determine if the summary has exactly 2 sentences.""",    feedback_value_type=Literal["correct", "incorrect"],)

## Step 5: Run comparative evaluation[​](#step-5-run-comparative-evaluation "Direct link to Step 5: Run comparative evaluation")

Evaluate each prompt version using both built-in and custom scorers:

Python

    from mlflow.genai.scorers import Correctness# Define scorersscorers = [    Correctness(),  # Checks expected facts    sentence_count_judge,  # Custom sentence count judge]# Evaluate each versionresults = {}for version in [1, 2]:    print(f"\nEvaluating version {version}...")    with mlflow.start_run(run_name=f"summary_v{version}_eval"):        mlflow.log_param("prompt_version", version)        # Run evaluation        eval_results = mlflow.genai.evaluate(            predict_fn=create_summary_function(PROMPT_NAME, version),            data=eval_dataset,            scorers=scorers,        )        results[f"v{version}"] = eval_results        print(f"  Correctness score: {eval_results.metrics.get('correctness/mean', 0):.2f}")        print(f"  Sentence compliance: {eval_results.metrics.get('sentence_count_compliance/mean', 0):.2f}")

## Step 6: Compare results and select best version[​](#step-6-compare-results-and-select-best-version "Direct link to Step 6: Compare results and select best version")

Analyze the results to identify the best performing prompt:

Python

    # Compare versions across all metricsprint("=== Version Comparison ===")for version, result in results.items():    correctness_score = result.metrics.get('correctness/mean', 0)    compliance_score = result.metrics.get('sentence_count_compliance/mean', 0)    print(f"{version}:")    print(f"  Correctness: {correctness_score:.2f}")    print(f"  Sentence compliance: {compliance_score:.2f}")    print()# Calculate composite scoresprint("=== Composite Scores ===")composite_scores = {}for version, result in results.items():    correctness = result.metrics.get('correctness/mean', 0)    compliance = result.metrics.get('sentence_count_compliance/mean', 0)    # Weight correctness more heavily (70%) than compliance (30%)    composite = 0.7 * correctness + 0.3 * compliance    composite_scores[version] = composite    print(f"{version}: {composite:.2f}")# Find best versionbest_version = max(composite_scores.items(), key=lambda x: x[1])print(f"\nBest performing version: {best_version[0]} (score: {best_version[1]:.2f})")# Show why this version is bestbest_results = results[best_version[0]]print(f"\nWhy {best_version[0]} is best:")print(f"- Captures {best_results.metrics.get('correctness/mean', 0):.0%} of expected facts")print(f"- Follows sentence requirements {best_results.metrics.get('sentence_count_compliance/mean', 0):.0%} of the time")

After identifying the best performing prompt version through evaluation, you're ready to deploy it. To learn how to use aliases for production deployment, see [Use prompts in deployed apps](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps).

## Example notebook[​](#-example-notebook "Direct link to -example-notebook")

For a complete working example, see the following notebook.

#### Evaluating a GenAI app quickstart notebook

*   [Evaluation Harness](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) - Deep dive into `mlflow.genai.evaluate()`
*   [Predefined scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Available scorers for prompt evaluation
*   [Custom prompt judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Create sophisticated evaluation metrics

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Track prompts with app versions](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/track-prompts-app-versions) - Link evaluated prompt versions to your application versions
*   [Use prompts in deployed apps](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps) - Deploy your best-performing prompts with aliases
*   [Create custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Build domain-specific evaluation metrics
