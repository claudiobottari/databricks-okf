---
title: Optimize multiple prompts together | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/multi-prompt-optimization
ingestedAt: "2026-06-18T08:18:25.560Z"
---

In complex agent systems, you might have chained multiple prompts together. You can provide all these prompts together for GEPA to consider and optimize each prompt.

## Install dependencies[​](#install-dependencies "Direct link to Install dependencies")

Python

    %pip install --upgrade mlflow databricks-sdk dspy openaidbutils.library.restartPython()

## Set up two basic functions with basic prompts[​](#set-up-two-basic-functions-with-basic-prompts "Direct link to set-up-two-basic-functions-with-basic-prompts")

Python

    import mlflowfrom mlflow.genai.scorers import Correctnessfrom databricks_openai import DatabricksOpenAIfrom mlflow.genai.optimize import GepaPromptOptimizeropenai_client = DatabricksOpenAI()catalog = ""schema = ""plan_prompt_name = f"{catalog}.{schema}.plan"answer_prompt_name = f"{catalog}.{schema}.answer"# Register multiple promptsplan_prompt = mlflow.genai.register_prompt(    name=plan_prompt_name,    template="Make a plan to classify {{query}}.",)answer_prompt = mlflow.genai.register_prompt(    name=answer_prompt_name,    template="classify {{query}} following the plan: {{plan}}",)def predict_fn(query: str) -> str:    plan_prompt = mlflow.genai.load_prompt(f"prompts:/{plan_prompt_name}/1")    completion = openai_client.chat.completions.create(        model="databricks-gpt-5",  # strong model        messages=[{"role": "user", "content": plan_prompt.format(query=query)}],    )    plan = completion.choices[0].message.content    answer_prompt = mlflow.genai.load_prompt(f"prompts:/{answer_prompt_name}/1")    completion = openai_client.chat.completions.create(        model="databricks-gpt-5-nano",  # cost efficient model        messages=[            {                "role": "user",                "content": answer_prompt.format(query=query, plan=plan),            }        ],    )    return completion.choices[0].message.content

## Test the models as is[​](#test-the-models-as-is "Direct link to test-the-models-as-is")

Python

    from IPython.display import Markdownoutput = predict_fn("The emergence of HIV as a chronic condition means that people living with HIV are required to take more responsibility for the self-management of their condition , including making physical , emotional and social adjustments .")Markdown(output)

Python

    dataset = [    {        "inputs": {"query": "The emergence of HIV as a chronic condition means that people living with HIV are required to take more responsibility for the self-management of their condition , including making physical , emotional and social adjustments ."},        "outputs": {"response": "BACKGROUND"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "This paper describes the design and evaluation of Positive Outlook , an online program aiming to enhance the self-management skills of gay men living with HIV ."},        "outputs": {"response": "BACKGROUND"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "This study is designed as a randomised controlled trial in which men living with HIV in Australia will be assigned to either an intervention group or usual care control group ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "The intervention group will participate in the online group program ` Positive Outlook ' ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "The program is based on self-efficacy theory and uses a self-management approach to enhance skills , confidence and abilities to manage the psychosocial issues associated with HIV in daily life ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    },    {        "inputs": {"query": "Participants will access the program for a minimum of 90 minutes per week over seven weeks ."},        "outputs": {"response": "METHODS"},        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}    }]# Optimize bothresult = mlflow.genai.optimize_prompts(    predict_fn=predict_fn,    train_data=dataset,    prompt_uris=[plan_prompt.uri, answer_prompt.uri],    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gemini-2-5-pro"),    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],)# Access optimized promptsoptimized_plan = result.optimized_prompts[0]optimized_answer = result.optimized_prompts[1]

## Load the new prompt and test again[​](#load-the-new-prompt-and-test-again "Direct link to load-the-new-prompt-and-test-again")

See what the prompt looks like and load it into your predict function to see how differently the model performs.

Python

    plan_prompt = mlflow.genai.load_prompt(f"prompts:/{plan_prompt_name}/4")Markdown(plan_prompt.template)

Python

    answer_prompt = mlflow.genai.load_prompt(f"prompts:/{answer_prompt_name}/4")Markdown(answer_prompt.template)

Python

    from IPython.display import Markdowndef predict_fn(query: str) -> str:    plan_prompt = mlflow.genai.load_prompt(f"prompts:/{plan_prompt_name}/4")    completion = openai_client.chat.completions.create(        model="databricks-gpt-5",  # strong model        messages=[{"role": "user", "content": plan_prompt.format(query=query)}],    )    plan = completion.choices[0].message.content    answer_prompt = mlflow.genai.load_prompt(f"prompts:/{answer_prompt_name}/4")    completion = openai_client.chat.completions.create(        model="databricks-gpt-5-nano",  # cost efficient model        messages=[            {                "role": "user",                "content": answer_prompt.format(query=query, plan=plan),            }        ],    )    return completion.choices[0].message.contentoutput = predict_fn("Participants will access the program for a minimum of 90 minutes per week over seven weeks")Markdown(output)

#### Prompt opitimization using GEPA and GPT-OSS 20B
