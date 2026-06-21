---
title: Prompt Registry | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/
ingestedAt: "2026-06-18T08:16:09.832Z"
---

## Overview[​](#overview "Direct link to Overview")

The MLflow Prompt Registry is a centralized repository for managing prompt templates across their lifecycle. It enables teams to:

*   **Version and track prompts** with Git-like versioning, commit messages, and rollback capabilities
*   **Deploy safely with aliases** using mutable references (e.g., "production", "staging") for A/B testing and gradual rollouts
*   **Collaborate without code changes** by allowing non-engineers to modify prompts through the UI
*   **Integrate with any framework** including LangChain, LlamaIndex, and other GenAI frameworks
*   **Maintain governance** through Unity Catalog integration for access control and audit trails
*   **Track lineage** by linking prompts to experiments and evaluation results

The Prompt Registry follows a Git-like model:

*   **Prompts**: Named entities in Unity Catalog
*   **Versions**: Immutable snapshots with auto-incrementing numbers
*   **Aliases**: Mutable pointers to specific versions
*   **Tags**: Version-specific key-value pairs

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1.  Install MLflow with Unity Catalog support:
    
    Bash
    
        pip install --upgrade "mlflow[databricks]>=3.1.0"
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
3.  Make sure you have access to a Unity Catalog schema with the `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions to view or create prompts in the prompt registry.

## Quick start[​](#quick-start "Direct link to quick-start")

The following code shows the essential workflow for using the Prompt Registry. Notice the double-brace syntax for template variables:

Python

    import mlflowfrom databricks.sdk import WorkspaceClientmodel = "databricks-claude-sonnet-4-5"llm = WorkspaceClient().serving_endpoints.get_open_ai_client()# Register a prompt templateprompt = mlflow.genai.register_prompt(    name="docs.default.customer_support",    template="You are a helpful assistant. Answer this question: {{question}}",    commit_message="Initial customer support prompt")print(f"Created version {prompt.version}")  # "Created version 1"# Set a production aliasmlflow.genai.set_prompt_alias(    name="docs.default.customer_support",    alias="production",    version=1)# Load and use the prompt in your applicationprompt = mlflow.genai.load_prompt(name_or_uri="prompts:/docs.default.customer_support@production")formatted_prompt = prompt.format(question="How do I reset my password?")response = llm.chat.completions.create(    model=model,    messages=[{"role": "user", "content": formatted_prompt}],)print(response.choices[0].message.content)

## SDK overview[​](#sdk-overview "Direct link to sdk-overview")

The following table summarizes the six main functions that Prompt Registry provides. For examples, see [Prompt Registry examples](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/examples).

## Prompt template formats[​](#prompt-template-formats "Direct link to Prompt template formats")

Prompt templates can be stored in two formats: simple prompts or conversations. For both, prompt strings can be templatized using the double-brace syntax `"Hello {{name}}"`.

The following example shows both simple and conversation-style prompts, using the double-brace format for template variables:

Python

    # Simple promptsimple_prompt = mlflow.genai.register_prompt(    name="mycatalog.myschema.greeting",    template="Hello {{name}}, how can I help you today?",    commit_message="Simple greeting")# Conversation or chat-style promptcomplex_prompt = mlflow.genai.register_prompt(    name="mycatalog.myschema.analysis",    template=[        {"role": "system", "content": "You are a helpful {{style}} assistant."},        {"role": "user", "content": "{{question}}"},    ],    commit_message="Multi-variable analysis template")# Use the promptrendered = complex_prompt.format(    style="edgy",    question="What is a good costume for a rainy Halloween?")

### Single-brace format compatibility[​](#single-brace-format-compatibility "Direct link to Single-brace format compatibility")

LangChain, LlamaIndex, and some other libraries support single-brace syntax (Python f-string syntax) for prompt templates: `"Hello {name}"`. For compatibility, MLflow supports converting prompts to single-brace format:

*   LangChain
*   LlamaIndex

Python

    from langchain_core.prompts import ChatPromptTemplate# Load from registrymlflow_prompt = mlflow.genai.load_prompt("prompts:/mycatalog.myschema.chat@production")# Convert to LangChain formatlangchain_template = mlflow_prompt.to_single_brace_format()chat_prompt = ChatPromptTemplate.from_template(langchain_template)# Use in chainchain = chat_prompt | llm | output_parser

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Create and edit prompts](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/create-and-edit-prompts) - Get started with your first prompt
*   [Use prompts in deployed apps](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps) - Deploy prompts to production with aliases
*   [Evaluate prompts](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/evaluate-prompts) - Compare prompt versions systematically
