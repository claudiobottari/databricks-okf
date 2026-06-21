---
title: Tracing Claude Code | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/claude-code
ingestedAt: "2026-06-18T08:17:00.893Z"
---

    import asyncioimport pandas as pdfrom claude_agent_sdk import ClaudeSDKClientimport mlflow.anthropicfrom mlflow.genai import evaluate, scorerfrom mlflow.genai.judges import make_judgemlflow.anthropic.autolog()async def run_agent(query: str) -> str:   """Run Claude Agent SDK and return response"""   async with ClaudeSDKClient() as client:      await client.query(query)      response_text = ""      async for message in client.receive_response():            response_text += str(message) + "\n\n"      return response_textdef predict_fn(query: str) -> str:   """Synchronous wrapper for evaluation"""   return asyncio.run(run_agent(query))relevance = make_judge(   name="relevance",   instructions=(      "Evaluate if the response in {{ outputs }} is relevant to "      "the question in {{ inputs }}. Return either 'pass' or 'fail'."   ),   model="openai:/gpt-4o",)# Create evaluation dataseteval_data = pd.DataFrame(   [      {"inputs": {"query": "What is machine learning?"}},      {"inputs": {"query": "Explain neural networks"}},   ])# Run evaluation with automatic tracingmlflow.set_experiment("claude_evaluation")evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
