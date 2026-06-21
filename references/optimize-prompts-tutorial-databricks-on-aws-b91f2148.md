---
title: Optimize prompts tutorial | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/prompt-optimization-quickstart
ingestedAt: "2026-06-18T08:18:27.958Z"
---

This tutorial example optimizes a simple prompt **classify this query** using MLflow Prompt Optimization using GEPA and GPT-OSS 20B for classification tasks.

## Install dependencies[​](#install-dependencies "Direct link to install-dependencies")

Python

    %pip install --upgrade mlflow databricks-sdk dspy openaidbutils.library.restartPython()

Ensure that you have access to the Databricks Foundation Model APIs to run this successfully.

Python

    import mlflowimport openaifrom mlflow.genai.optimize import GepaPromptOptimizerfrom mlflow.genai.scorers import Correctnessfrom databricks_openai import DatabricksOpenAI# Change the catalog and schema to your catalog and schemacatalog = ""schema = ""prompt_registry_name = "qa"prompt_location = f"{catalog}.{schema}.{prompt_registry_name}"openai_client = DatabricksOpenAI()# Register initial promptprompt = mlflow.genai.register_prompt(    name=prompt_location,    template="classify this: {{query}}",)# Define your prediction functiondef predict_fn(query: str) -> str:    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/1")    completion = openai_client.chat.completions.create(        model="databricks-gpt-oss-20b",        # load prompt template using PromptVersion.format()        messages=[{"role": "user", "content": prompt.format(question=query)}],    )    return completion.choices[0].message.content

## Test your function[​](#test-your-function "Direct link to test-your-function")

Observe how accurately the model can classify the input with a bare bones prompt. While accurate, it's not aligned to any task or use case you're looking for.

Python

    from IPython.display import Markdownoutput = predict_fn("The emergence of HIV as a chronic condition means that people living with HIV are required to take more responsibility for the self-management of their condition , including making physical , emotional and social adjustments.")Markdown(output[1]['text'])

## Optimize against data[​](#optimize-against-data "Direct link to optimize-against-data")

Provide data with expected responses and facts to help optimize the model behavior and output in a way that fits your use cases.

In this case, you want the model to output one word from a choice of five words. It should only output that word without any further explanation.

Python

    # Training data with inputs and expected outputsdataset = [    {        "inputs": {"query": "The emergence of HIV as a chronic condition means that people living with HIV are required to take more responsibility for the self-management of their condition , including making physical , emotional and social adjustments."},        "outputs": {"response": "BACKGROUND"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "This paper describes the design and evaluation of Positive Outlook , an online program aiming to enhance the self-management skills of gay men living with HIV ."},        "outputs": {"response": "BACKGROUND"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "This study is designed as a randomised controlled trial in which men living with HIV in Australia will be assigned to either an intervention group or usual care control group ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "The intervention group will participate in the online group program ` Positive Outlook ' ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "The program is based on self-efficacy theory and uses a self-management approach to enhance skills , confidence and abilities to manage the psychosocial issues associated with HIV in daily life ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "Participants will access the program for a minimum of 90 minutes per week over seven weeks ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    }]# Optimize the promptresult = mlflow.genai.optimize_prompts(    predict_fn=predict_fn,    train_data=dataset,    prompt_uris=[prompt.uri],    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),    scorers=[Correctness(model="databricks:/databricks-gpt-5")],)# Use the optimized promptoptimized_prompt = result.optimized_prompts[0]print(f"Optimized template: {optimized_prompt.template}")

## Review your prompt[​](#review-your-prompt "Direct link to review-your-prompt")

Open the link to your MLflow experiment and complete the following steps to have the prompts appear in your experiment:

1.  Ensure your experiment type is set to GenAI apps and agents
2.  Navigate to the prompt tab
3.  Click **select a schema** on the top right and enter the same schema you set above to see your prompt

## Load the new prompt and test again[​](#load-the-new-prompt-and-test-again "Direct link to load-the-new-prompt-and-test-again")

See what the prompt looks like and load it into your predict function to see how differently the model performs.

Python

    from IPython.display import Markdownprompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/34")Markdown(prompt.template)

Python

    from IPython.display import Markdowndef predict_fn(query: str) -> str:    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/34")    completion = openai_client.chat.completions.create(        model="databricks-gpt-oss-20b",        # load prompt template using PromptVersion.format()        messages=[{"role": "user", "content": prompt.format(query=query)}],    )    return completion.choices[0].message.contentoutput = predict_fn("The emergence of HIV as a chronic condition means that people living with HIV are required to take more responsibility for the self-management of their condition , including making physical , emotional and social adjustments.")Markdown(output[1]['text'])

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The following is a runnable notebook that optimizes prompts using MLflow GenAI Prompt Optimization with GEPA and demonstrates classification tasks with GPT-OSS 20B.

#### Prompt opitimization using GEPA and GPT-OSS 20B
