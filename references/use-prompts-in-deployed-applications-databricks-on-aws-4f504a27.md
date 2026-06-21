---
title: Use prompts in deployed applications | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps
ingestedAt: "2026-06-18T08:16:20.777Z"
---

This guide shows you how to use prompts from the MLflow Prompt Registry in your production GenAI applications.

When deploying GenAI applications, configure them to load prompts from the MLflow Prompt Registry using aliases rather than hard-coded versions. This approach enables dynamic updates without redeployment.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1.  Install MLflow and required packages
    
    Bash
    
        pip install --upgrade "mlflow[databricks]>=3.1.0"
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    
3.  Verify you have access to a Unity Catalog schema with the `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions to use the prompt registry.
    

note

A Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions is required to view or create prompts. If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), you have the required permissions on the Unity Catalog schema `workspace.default`.

## Step 1. Create a new prompt[​](#step-1-create-a-new-prompt "Direct link to Step 1. Create a new prompt")

You can create prompts programmatically using the Python SDK.

Create prompts programmatically with [`mlflow.genai.register_prompt()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt). Prompts use double-brace syntax (`{{variable}}`) for template variables.

Python

    import mlflow# Replace with a Unity Catalog schema where you have CREATE FUNCTION permissionuc_schema = "workspace.default"# This table will be created in the above UC schemaprompt_name = "summarization_prompt"# Define the prompt template with variablesinitial_template = """\Summarize content you are provided with in {{num_sentences}} sentences.Content: {{content}}"""# Register a new promptprompt = mlflow.genai.register_prompt(    name=f"{uc_schema}.{prompt_name}",    template=initial_template,    # all parameters below are optional    commit_message="Initial version of summarization prompt",    tags={        "author": "data-science-team@company.com",        "use_case": "document_summarization",        "task": "summarization",        "language": "en",        "model_compatibility": "gpt-4"    })print(f"Created prompt '{prompt.name}' (version {prompt.version})")

## Step 2. Add an alias to the prompt version[​](#step-2-add-an-alias-to-the-prompt-version "Direct link to Step 2. Add an alias to the prompt version")

Aliases allow you to assign a static string tag to a specific prompt version, making it easier to reference prompts in production applications. Instead of hardcoding version numbers, you can use meaningful aliases like `production`, `staging`, or `development`. When you must update your production prompt, reassign the `production` alias to point to a newer version without changing or redeploying your application code.

Python

    import mlflowmlflow.genai.set_prompt_alias(    name=f"{uc_schema}.{prompt_name}",    alias="production",    version=1)

## Step 3. Reference the prompt in your app[​](#step-3-reference-the-prompt-in-your-app "Direct link to Step 3. Reference the prompt in your app")

After you register your prompt and assign an alias, you can reference it in your deployed applications using the prompt URI format. The recommended approach is to use environment variables to make your application flexible and avoid hardcoding prompt references.

The prompt URI format is: `prompts:/{catalog}.{schema}.{prompt_name}@{alias}`

Using the prompt we registered in Step 1, the URI would be:

*   `prompts://workspace.default.summarization_prompt@production`

The MLflow client caches the prompt template, so the prompt registry doesn't introduce latency to your agent. For details, see [Prompt Caching](https://mlflow.org/docs/latest/genai/prompt-registry/#prompt-caching).

Here's how to reference the prompt in your application:

Python

    import mlflowimport osfrom typing import Optionalmlflow.set_tracking_uri("databricks")mlflow.set_registry_uri("databricks-uc")class ProductionApp:    def __init__(self):        # Use environment variable for flexibility        self.prompt_alias = os.getenv("PROMPT_ALIAS", "production")        self.prompt_name = os.getenv("PROMPT_URI", "workspace.default.summarization_prompt")    def get_prompt(self) -> str:        """Load prompt from registry using alias."""        uri = f"prompts:/{self.prompt_name}@{self.prompt_alias}"        prompt = mlflow.genai.load_prompt(uri)        return prompt    # Rest of your application's code# Example usageapp = ProductionApp()prompt = app.get_prompt()print(f"Loaded prompt: {prompt}")

## Version management workflows[​](#version-management-workflows "Direct link to Version management workflows")

Aliases enable you to iterate on prompts during development and promote them through environments without changing application code.

### Development workflow[​](#development-workflow "Direct link to Development workflow")

Use a development alias to test prompt changes before promoting to production:

Python

    from datetime import datetimeimport mlflowdef develop_prompt(base_name: str, changes: str):    """Iterate on prompts during development."""    # Register new version    new_version = mlflow.genai.register_prompt(        name=base_name,        template=changes,        commit_message=f"Dev iteration: {datetime.now()}"    )    # Update dev alias    mlflow.genai.set_prompt_alias(        name=base_name,        alias="dev",        version=new_version.version    )    return new_version

### Promotion workflow[​](#promotion-workflow "Direct link to Promotion workflow")

Promote prompts between environments by reassigning aliases:

Python

    import mlflowdef promote_prompt(name: str, from_env: str, to_env: str):    """Promote prompt from one environment to another."""    # Get current version in source environment    source = mlflow.genai.load_prompt(f"prompts:/{name}@{from_env}")    # Point target environment to same version    mlflow.genai.set_prompt_alias(        name=name,        alias=to_env,        version=source.version    )    print(f"Promoted {name} v{source.version} from {from_env} to {to_env}")

## Alias strategies[​](#alias-strategies "Direct link to Alias strategies")

Design your alias strategy based on your team's deployment patterns. The following examples demonstrate common approaches:

Python

    import mlflow# Standard environment aliasesENVIRONMENT_ALIASES = ["dev", "staging", "production"]# Feature branch aliasesdef create_feature_alias(prompt_name: str, feature: str, version: int):    """Create alias for feature development."""    mlflow.genai.set_prompt_alias(        name=prompt_name,        alias=f"feature-{feature}",        version=version    )# Regional aliasesREGIONAL_ALIASES = {    "us": "production-us",    "eu": "production-eu",    "asia": "production-asia"}# Rollback-ready aliasesdef safe_production_update(name: str, new_version: int):    """Update production with rollback capability."""    try:        # Save current production        current = mlflow.genai.load_prompt(f"prompts:/{name}@production")        mlflow.genai.set_prompt_alias(name, "production-previous", current.version)    except:        pass  # No current production    # Update production    mlflow.genai.set_prompt_alias(name, "production", new_version)

## Use the prompt registry with a deployed agent using Custom Agents[​](#use-the-prompt-registry-with-a-deployed-agent-using-custom-agents "Direct link to use-the-prompt-registry-with-a-deployed-agent-using-custom-agents")

To access the prompt registry from an agent deployed using Custom Agents, you must use manual authentication and override security environment variables to configure the Databricks Client to connect to the registry.

important

Overriding these security environment variables disables automatic passthrough for other resources your agent depends on.

For more information, see [Manual authentication for AI agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/agent-authentication-model-serving#manual-authentication).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Run scorers in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Monitor the quality of your deployed prompts
*   [Evaluate prompts](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/evaluate-prompts) - Test new prompt versions before promoting to production

*   [Evaluate prompts](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/evaluate-prompts)
*   [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)
