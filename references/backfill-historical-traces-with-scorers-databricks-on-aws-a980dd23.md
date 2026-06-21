---
title: Backfill historical traces with scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/backfill-scorers
ingestedAt: "2026-06-18T08:14:40.016Z"
---

    from databricks.agents.scorers import backfill_scorers, BackfillScorerConfigfrom datetime import datetimefrom mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfigsafety_judge = Safety()safety_judge = safety_judge.register(name="safety_check")safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))@scorer(aggregations=["mean", "min", "max"])def response_length(outputs):    """Measure response length in characters"""    return len(outputs)response_length = response_length.register(name="response_length")response_length = response_length.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))# Define custom sample rates for backfillcustom_scorers = [    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),    BackfillScorerConfig(scorer=response_length, sample_rate=0.9)]job_id = backfill_scorers(    experiment_id=YOUR_EXPERIMENT_ID,    scorers=custom_scorers,    start_time=datetime(2024, 6, 1),    end_time=datetime(2024, 6, 30))
