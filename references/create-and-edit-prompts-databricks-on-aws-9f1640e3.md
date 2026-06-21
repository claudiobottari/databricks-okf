---
title: Create and edit prompts | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/create-and-edit-prompts
ingestedAt: "2026-06-18T08:16:13.503Z"
---

This page shows you how to create new prompts and manage their versions in the MLflow Prompt Registry using the MLflow Python SDK. It includes instructions for using the MLflow Python SDK and the Databricks MLflow UI. All of the code on this page is included in the [example notebook](#example-notebook).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1.  Install MLflow and required packages
    
    Bash
    
        pip install --upgrade "mlflow[databricks]>=3.1.0" openai
    
2.  Create an MLflow experiment by following the [set up your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    
3.  Create or identify a Unity Catalog schema for storing prompts. You must have the `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges on the Unity Catalog schema.
    

note

A Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions is required in order to view or create prompts. If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), you have the required permissions on the Unity Catalog schema `main.default`.

## Step 1. Create a new prompt[​](#step-1-create-a-new-prompt "Direct link to Step 1. Create a new prompt")

You can create prompts in the Databricks MLflow UI, or programmatically using the MLflow Python SDK.

### Use the Databricks MLflow UI[​](#use-the-databricks-mlflow-ui "Direct link to Use the Databricks MLflow UI")

To create a prompt in the UI:

1.  Navigate to your MLflow experiment.
    
2.  Click the **Prompts** tab.
    
    ![MLflow experiments page showing Prompts tab.](https://docs.databricks.com/aws/en/assets/images/prompts-tab-63c6562246d66c015db8116a9df262f4.png)
    
3.  Click ![the new prompt button](data:image/png;base64,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). A dialog appears.
    
    ![New Prompt dialog.](https://docs.databricks.com/aws/en/assets/images/new-prompt-dialog-9052cd6d2745781e77f8781004f78eaf.png)
    
4.  If you haven't yet selected a schema for this experiment, the dialog includes a **Target schema** field. To choose a schema:
    
    1.  Next to the **Target schema** field, click **Choose** to open the schema picker.
    2.  In the picker, select the schema you want and click **Confirm**. You must have the following permissions on the schema: `CREATE FUNCTION`, `EXECUTE`, and `MANAGE`.
5.  In the **Name** field, type a name for the prompt. Prompt names can contain only letters, numbers, hyphens, underscores, and dots.
    
6.  For **Prompt type**, select one of the following:
    
    *   **Text**: A single text template. Use this for completion-style prompts.
    *   **Chat**: A list of role-based messages (for example, `system` and `user`). Use this for chat-style prompts that target conversational models.
7.  In the **Prompt** field, type your prompt content. Use `{{variable_name}}` syntax to define variables that you fill in at runtime.
    
8.  (Optional) In the **Commit message** field, type a short description of this version. Commit messages are stored with the prompt version and help you track changes across versions.
    
9.  Click **Create**.
    

The prompt appears in the UI:

![Registered Prompt in UI](https://docs.databricks.com/aws/en/assets/images/registered-prompt-52744d837b6e94662110af1cb866d244.png)

### Use the Python SDK[​](#use-the-python-sdk "Direct link to Use the Python SDK")

1.  Link your MLflow experiment to a default Prompt Registry location by setting an experiment tag using [`mlflow.set_experiment_tags`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment_tags). This lets SDKs and tools infer your Unity Catalog prompt schema automatically.
    
    Use the `mlflow.promptRegistryLocation` tag with the value `catalog.schema`:
    
    Python
    
        import mlflow# Link the current MLflow experiment to a UC schema for promptsmlflow.set_experiment_tags({    "mlflow.promptRegistryLocation": "main.default"})
    
2.  Create prompts using [`mlflow.genai.register_prompt()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt). Prompts use double-brace syntax (`{{variable}}`) for template variables.
    
    Python
    
        # Replace with a Unity Catalog schema where you have CREATE FUNCTION, EXECUTE, and MANAGE privilegesuc_schema = "main.default"# This table is created in the UC schema specified in the previous lineprompt_name = "summarization_prompt"# Define the prompt template with variablesinitial_template = """\ Summarize content you are provided with in {{num_sentences}} sentences.Content: {{content}}"""# Register a new promptprompt = mlflow.genai.register_prompt(    name=f"{uc_schema}.{prompt_name}",    template=initial_template,    # all following parameters are optional    commit_message="Initial version of summarization prompt",    tags={         "author": "data-science-team@company.com",         "use_case": "document_summarization",         "task": "summarization",         "language": "en",         "model_compatibility": "gpt-4"     } )print(f"Created prompt '{prompt.name}' (version {prompt.version})")
    

## Step 2: Use the prompt in your application[​](#step-2-use-the-prompt-in-your-application "Direct link to Step 2: Use the prompt in your application")

The following steps create a simple application that uses your prompt template using the Python SDK.

### Load the prompt from the registry[​](#load-the-prompt-from-the-registry "Direct link to Load the prompt from the registry")

Python

    # Load a specific version using URI syntaxprompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1")# Alternative syntax without URIprompt = mlflow.genai.load_prompt(name_or_uri=f"{uc_schema}.{prompt_name}", version="1")

### Use the prompt in your application[​](#use-the-prompt-in-your-application "Direct link to Use the prompt in your application")

1.  Initialize an OpenAI client to connect to either Databricks-hosted LLMs or LLMs hosted by OpenAI.
    
    *   Databricks-hosted LLMs
    *   OpenAI-hosted LLMs
    
    Use `databricks-openai` to get an OpenAI client that connects to Databricks-hosted LLMs. Select a model from the [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).
    
    Python
    
        import mlflowfrom databricks_openai import DatabricksOpenAI# Enable MLflow's autologging to instrument your application with Tracingmlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/docs-demo")# Create an OpenAI client that is connected to Databricks-hosted LLMsclient = DatabricksOpenAI()# Select an LLMmodel_name = "databricks-claude-sonnet-4"
    
2.  Define your application:
    
    Python
    
        # Use the trace decorator to capture the application's entry point@mlflow.tracedef my_app(content: str, num_sentences: int):    # Format with variables    formatted_prompt = prompt.format(        content=content,        num_sentences=num_sentences    )    response = client.chat.completions.create(        model=model_name,  # This example uses a Databricks hosted LLM. You can replace this with any AI Gateway or Model Serving endpoint, or with a valid OpenAI model like gpt-4o.        messages=[            {                "role": "system",                "content": "You are a helpful assistant.",            },            {                "role": "user",                "content": formatted_prompt,            },        ],    )    return response.choices[0].message.contentresult = my_app(content="This guide shows you how to integrate prompts from the MLflow Prompt Registry into your GenAI applications. You'll learn to load prompts, format them with dynamic data, and ensure complete lineage by linking prompt versions to your MLflow Models.", num_sentences=1)print(result)
    

## Step 3. Edit the prompt[​](#step-3-edit-the-prompt "Direct link to Step 3. Edit the prompt")

Prompt versions are immutable after you create them. To edit a prompt, you must create a new version. This Git-like versioning maintains complete history and enables rollbacks.

### Use the Databricks MLflow UI[​](#use-the-databricks-mlflow-ui-1 "Direct link to Use the Databricks MLflow UI")

To create a new version:

1.  On the **Prompts** tab, click ![New versions button.](data:image/png;base64,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) next to the prompt you want to edit.
    
    ![Edit existing prompt.](https://docs.databricks.com/aws/en/assets/images/create-new-version-11ca005916b089375bf4b74f3acb1f99.png)
    
2.  Type your prompt and click **Save**.
    

#### Compare prompt versions[​](#compare-prompt-versions "Direct link to Compare prompt versions")

To compare prompt versions:

1.  On the **Prompts** tab, click the name of the prompt.
    
    ![Prompt name in table.](https://docs.databricks.com/aws/en/assets/images/prompt-name-in-table-6a79e0fc120bd5b479ce45a31cd18459.png)
    
2.  At the upper left, click **Compare** and select the versions to compare.
    
    ![Compare prompts screen.](https://docs.databricks.com/aws/en/assets/images/prompt-versions-ui-51299e8c92f3fc8847ba83b701916424.png)
    

### Use the Python SDK[​](#use-the-python-sdk-1 "Direct link to Use the Python SDK")

Create a new version by calling [`mlflow.genai.register_prompt()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt) with an existing prompt name:

Python

    import mlflow# Define the improved templatenew_template = """\You are an expert summarizer. Condense the following content into exactly {{ num_sentences }} clear and informative sentences that capture the key points.Content: {{content}}Your summary should:- Contain exactly {{num_sentences}} sentences- Include only the most important information- Be written in a neutral, objective tone- Maintain the same level of formality as the original text"""# Register a new versionupdated_prompt = mlflow.genai.register_prompt(    name=f"{uc_schema}.{prompt_name}",    template=new_template,    commit_message="Added detailed instructions for better output quality",    tags={        "author": "data-science-team@company.com",        "improvement": "Added specific guidelines for summary quality"    })print(f"Created version {updated_prompt.version} of '{updated_prompt.name}'")

## Step 4. Use the new prompt[​](#step-4-use-the-new-prompt "Direct link to Step 4. Use the new prompt")

The following code shows how to use the prompt.

Python

    # Load a specific version using URI syntaxprompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/2")# Or load from specific versionprompt = mlflow.genai.load_prompt(name_or_uri=f"{uc_schema}.{prompt_name}", version="2")

## Step 5. Search and discover prompts[​](#step-5-search-and-discover-prompts "Direct link to Step 5. Search and discover prompts")

To find prompts in your Unity Catalog schema:

Python

    # REQUIRED format for Unity Catalog - specify catalog and schemaresults = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")# Using variables for your schemacatalog_name = uc_schema.split('.')[0]  # 'main'schema_name = uc_schema.split('.')[1]   # 'default'results = mlflow.genai.search_prompts(f"catalog = '{catalog_name}' AND schema = '{schema_name}'")# Limit resultsresults = mlflow.genai.search_prompts(    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",    max_results=50)

## Example notebook[​](#-example-notebook "Direct link to -example-notebook")

#### Create and edit prompts example notebook

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Evaluate prompt versions](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/evaluate-prompts) - Compare different prompt versions to identify the best performer.
*   [Track prompts with app versions](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/track-prompts-app-versions) - Link prompt versions to your application versions.
*   [Use prompts in deployed apps](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps) - Deploy prompts to production with aliases.
