---
title: Manage production scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/manage-production-scorers
ingestedAt: "2026-06-18T08:15:26.733Z"
---

After you [set up production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring), you can manage your scorers throughout their lifecycle. This page covers how to list, update, stop, restart, and delete scorers.

For the full API parameter reference, see [Scorer lifecycle management API reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring).

## Scorer lifecycle[​](#scorer-lifecycle "Direct link to Scorer lifecycle")

Scorer lifecycles are centered around MLflow experiments. Scorers are _immutable_ — each lifecycle operation returns a new scorer instance rather than modifying the original.

### Lifecycle example[​](#lifecycle-example "Direct link to Lifecycle example")

The following example demonstrates a scorer moving through all lifecycle states:

Python

    from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig, delete_scorer# Register → Start → Update → Stop → Deletesafety_judge = Safety().register(name="safety_check")safety_judge = safety_judge.start(    sampling_config=ScorerSamplingConfig(sample_rate=1.0),)safety_judge = safety_judge.update(    sampling_config=ScorerSamplingConfig(sample_rate=0.8),)safety_judge = safety_judge.stop()delete_scorer(name="safety_check")

## Manage scorers[​](#manage-scorers "Direct link to Manage scorers")

The following APIs are available to manage scorers.

## List scorers[​](#-list-scorers "Direct link to -list-scorers")

To view all registered scorers for your experiment:

Python

    from mlflow.genai.scorers import list_scorers# List all registered scorersscorers = list_scorers()for scorer in scorers:    print(f"Name: {scorer.name}")    print(f"Sample rate: {scorer.sample_rate}")    print(f"Filter: {scorer.filter_string}")    print("---")

## Get and update a scorer[​](#-get-and-update-a-scorer "Direct link to -get-and-update-a-scorer")

Use `get_scorer()` to retrieve a scorer by name, then `update()` to modify its configuration. Because scorers are immutable, `update()` returns a new instance.

Python

    from mlflow.genai.scorers import get_scorer, ScorerSamplingConfig# Get existing scorer and update its configuration (immutable operation)safety_judge = get_scorer(name="safety_monitor")updated_judge = safety_judge.update(sampling_config=ScorerSamplingConfig(sample_rate=0.8))# The original scorer remains unchanged; update() returns a new scorer instanceprint(f"Original sample rate: {safety_judge.sample_rate}")  # Original rateprint(f"Updated sample rate: {updated_judge.sample_rate}")   # New rate

## Stop and delete scorers[​](#-stop-and-delete-scorers "Direct link to -stop-and-delete-scorers")

Stopping a scorer sets its sample rate to 0 but keeps it registered. Deleting a scorer removes it from the server entirely.

Python

    from mlflow.genai.scorers import get_scorer, delete_scorer, ScorerSamplingConfig# Get existing scorerdatabricks_scorer = get_scorer(name="databricks_mentions")# Stop monitoring (sets sample_rate to 0, keeps scorer registered)stopped_scorer = databricks_scorer.stop()print(f"Sample rate after stop: {stopped_scorer.sample_rate}")  # 0# Restart monitoring from a stopped scorerrestarted_scorer = stopped_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))# Or remove scorer entirely from the serverdelete_scorer(name=databricks_scorer.name)

## Immutable updates[​](#immutable-updates "Direct link to Immutable updates")

Scorers, including LLM Judges, are immutable objects. When you update a scorer, an updated copy is created rather than modifying the original. This immutability helps ensure that scorers meant for production are not accidentally modified.

Python

    from mlflow.genai.scorers import Safety, ScorerSamplingConfigoriginal_judge = Safety().register(name="safety")original_judge = original_judge.start(   sampling_config=ScorerSamplingConfig(sample_rate=0.3),)# Update returns new instanceupdated_judge = original_judge.update(    sampling_config=ScorerSamplingConfig(sample_rate=0.8),)# Original remains unchangedprint(f"Original: {original_judge.sample_rate}")  # 0.3print(f"Updated: {updated_judge.sample_rate}")    # 0.8

## Best practices[​](#best-practices "Direct link to Best practices")

*   Check the scorer state before operations using `sample_rate`.
*   Use the immutable pattern. Assign the results of `.start()`, `.update()`, `.stop()` to variables.
*   Understand the difference between `.stop()` (preserves registration) and `delete_scorer()` (removes entirely).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Monitor GenAI apps in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Set up production monitoring.
*   [Backfill historical traces with scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/backfill-scorers) - Apply scorers to historical traces.
*   [Scorer lifecycle management API reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring) - Full API reference for scorer lifecycle management.
