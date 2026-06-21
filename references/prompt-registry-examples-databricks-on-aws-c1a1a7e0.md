---
title: Prompt Registry examples | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/examples
ingestedAt: "2026-06-18T08:16:16.981Z"
---

This page shows examples for the Prompt Registry operations.

## register\_prompt()[​](#register_prompt "Direct link to register_prompt")

**API reference:** [`mlflow.genai.register_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt)

Python

    prompt = mlflow.genai.register_prompt(    name="mycatalog.myschema.summarization",    template="""Summarize the following text in {{num_sentences}} sentences:Text: {{content}}Focus on: {{focus_areas}}""",    commit_message="Added focus areas parameter",    tags={        "tested_with": "gpt-4",        "avg_latency_ms": "1200",        "team": "content",        "project": "summarization-v2"    })

## load\_prompt()[​](#load_prompt "Direct link to load_prompt")

**API reference:** [`mlflow.genai.load_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.load_prompt)

The following code shows different ways to load a specific prompt version.

Python

    import mlflowfrom databricks.sdk import WorkspaceClientmodel = "databricks-claude-sonnet-4-5"llm = WorkspaceClient().serving_endpoints.get_open_ai_client()# Load specific version using URI formatmlflow.genai.load_prompt(name_or_uri="prompts:/docs.default.customer_support/1")# Load specific version using name + version parametermlflow.genai.load_prompt(  name_or_uri="docs.default.customer_support",  version=3,  # allow optional parameters to be missing when constructing the prompt  allow_missing=True,)# Use the promptprompt = mlflow.genai.load_prompt(name_or_uri="prompts:/docs.default.customer_support/1")formatted_prompt = prompt.format(question="How do I reset my password?")response = llm.chat.completions.create(    model=model,    messages=[{"role": "user", "content": formatted_prompt}],)print(f"\nResponse using version {prompt.version}:")print(response.choices[0].message.content)

## search\_prompts()[​](#search_prompts "Direct link to search_prompts")

**API Reference:** [`mlflow.genai.search_prompts`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.search_prompts)

### Unity Catalog Requirements[​](#unity-catalog-requirements "Direct link to unity-catalog-requirements")

**For Unity Catalog prompt registries, you must specify both catalog and schema:**

Python

    # REQUIRED format - list all prompts in a catalog.schemaresults = mlflow.genai.search_prompts("catalog = 'mycatalog' AND schema = 'myschema'")# This is the ONLY supported filter formatresults = mlflow.genai.search_prompts("catalog = 'rohit' AND schema = 'default'")

### Limitations[​](#limitations "Direct link to Limitations")

**The following filters are NOT supported in Unity Catalog:**

*   Name patterns: `name LIKE '%pattern%'`
*   Tag filtering: `tags.field = 'value'`
*   Exact name matching: `name = 'specific.name'`
*   Combined filters beyond catalog + schema

**To find specific prompts, use the returned list and filter programmatically:**

Python

    # Get all prompts in schemaall_prompts = mlflow.genai.search_prompts("catalog = 'mycatalog' AND schema = 'myschema'")# Filter programmaticallycustomer_prompts = [p for p in all_prompts if 'customer' in p.name.lower()]tagged_prompts = [p for p in all_prompts if p.tags.get('team') == 'support']

## set\_prompt\_alias()[​](#set_prompt_alias "Direct link to set_prompt_alias")

**API Reference:** [`mlflow.genai.set_prompt_alias`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.set_prompt_alias)

Python

    # Promote version 3 to productionmlflow.genai.set_prompt_alias(    name="mycatalog.myschema.chat_assistant",    alias="production",    version=3)# Set up staging for testingmlflow.genai.set_prompt_alias(    name="mycatalog.myschema.chat_assistant",    alias="staging",    version=4)

## delete\_prompt() and delete\_prompt\_version()[​](#delete_prompt-and-delete_prompt_version "Direct link to delete_prompt-and-delete_prompt_version")

### delete\_prompt\_version()[​](#delete_prompt_version "Direct link to delete_prompt_version()")

**API Reference:** [`MlflowClient.delete_prompt_version`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.delete_prompt_version)

Deletes a specific version of a prompt:

Python

    from mlflow import MlflowClientclient = MlflowClient()# Delete specific versions first (required for Unity Catalog)client.delete_prompt_version("mycatalog.myschema.chat_assistant", "1")client.delete_prompt_version("mycatalog.myschema.chat_assistant", "2")client.delete_prompt_version("mycatalog.myschema.chat_assistant", "3")# Then delete the entire promptclient.delete_prompt("mycatalog.myschema.chat_assistant")# For convenience with Unity Catalog, you can also search and delete all versions:search_response = client.search_prompt_versions("mycatalog.myschema.chat_assistant")for version in search_response.prompt_versions:    client.delete_prompt_version("mycatalog.myschema.chat_assistant", str(version.version))client.delete_prompt("mycatalog.myschema.chat_assistant")

### delete\_prompt()[​](#delete_prompt "Direct link to delete_prompt()")

After you delete the prompt version, you can delete the prompt.

important

*   For Unity Catalog registries, `delete_prompt()` fails if any versions still exist. All versions must be deleted first using `delete_prompt_version()`.
*   For other registry types, `delete_prompt()` works normally without version checking.

**API Reference:** [`MlflowClient.delete_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.delete_prompt)

Python

    from mlflow import MlflowClientclient = MlflowClient()# Delete specific versions first (required for Unity Catalog)client.delete_prompt_version("mycatalog.myschema.chat_assistant", "1")client.delete_prompt_version("mycatalog.myschema.chat_assistant", "2")client.delete_prompt_version("mycatalog.myschema.chat_assistant", "3")# Then delete the entire promptclient.delete_prompt("mycatalog.myschema.chat_assistant")# For convenience with Unity Catalog, you can also search and delete all versions:search_response = client.search_prompt_versions("mycatalog.myschema.chat_assistant")for version in search_response.prompt_versions:    client.delete_prompt_version("mycatalog.myschema.chat_assistant", str(version.version))client.delete_prompt("mycatalog.myschema.chat_assistant")
