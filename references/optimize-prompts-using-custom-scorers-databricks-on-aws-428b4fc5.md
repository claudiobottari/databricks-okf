---
title: Optimize prompts using custom scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/custom-scorers
ingestedAt: "2026-06-18T08:18:23.258Z"
---

This notebook walks you through how to make custom scorers using MLflow `make_judge`.

Often, built-in scorers and judges don't fit all use cases. Take advantage of custom scorers or judges to ensure you have accurate evaluations to optimize against.

The notebook walks you through a markdown judge that optimizes a prompt to output in a more markdown format.

Python

    %pip install --upgrade mlflow databricks-sdk dspy openaidbutils.library.restartPython()

## Use MLflow `make_judge`[​](#use-mlflow-make_judge "Direct link to use-mlflow-make_judge")

MLflow's recent release of make\_judge allows you to make any judge catered to your specific use case.

Python

    from mlflow.genai.judges import make_judge# Create a scorer for customer support qualitymarkdown_output_judge = make_judge(    name="markdown_quality",    instructions=(        "Evaluate if the answer in {{ outputs }} follows a markdown formatting and accurately answers the question in {{ inputs }} and matches {{ expectations }}. Rate as high, medium or low quality"    ),    model="databricks:/databricks-claude-sonnet-4-5")

## Objective function to map feedback[​](#objective-function-to-map-feedback "Direct link to objective-function-to-map-feedback")

The feedback provided by the judge needs to be mapped to a numerical number that the optimizer can use. The optimizer also incorporates the feedback from the judge.

You need a function to provide this mapping back to the optimizer.

Python

    def feedback_to_score(scores: dict) -> float:    """Convert feedback values to numerical scores."""    feedback_value = scores["markdown_quality"]    # Map categorical feedback to numerical values    feedback_mapping = {        "high": 1.0,        "medium": 0.5,        "low": 0.0    }    # Handle Feedback objects by accessing .value attribute    if hasattr(feedback_value, 'value'):        feedback_str = str(feedback_value.value).lower()    else:        feedback_str = str(feedback_value).lower()    return feedback_mapping.get(feedback_str, 0.0)

## Test the model[​](#test-the-model "Direct link to test-the-model")

You can test this model as is. In the following example, the model doesn't output in a Markdown format.

Python

    import mlflowimport openaifrom mlflow.genai.optimize import GepaPromptOptimizerfrom databricks_openai import DatabricksOpenAI# Change this to your workspace catalog and schemacatalog = ""schema = ""prompt_location = f"{catalog}.{schema}.markdown"openai_client = DatabricksOpenAI()# Register initial promptprompt = mlflow.genai.register_prompt(    name=prompt_location,    template="Answer this question: {{question}}",)# Define your prediction functiondef predict_fn(question: str) -> str:    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/1")    completion = openai_client.chat.completions.create(        model="databricks-gpt-oss-20b",        messages=[{"role": "user", "content": prompt.format(question=question)}],    )    return completion.choices[0].message.content

Python

    from IPython.display import Markdownoutput = predict_fn("What is the capital of France?")Markdown(output[1]['text'])

## Run the optimizer[​](#run-the-optimizer "Direct link to run-the-optimizer")

Some example data has been provided for you.

Python

    # Training data with inputs and expected outputsdataset = [    {        # The inputs schema should match with the input arguments of the prediction function.        "inputs": {"question": "What is the capital of France?"},        "expectations": {"expected_response": """## Paris - Capital of France**Paris** is the capital and largest city of France, located in the *north-central* region.### Key Facts:- **Population**: ~2.2 million (city), ~12 million (metro area)- **Founded**: 3rd century BC- **Nickname**: *"City of Light"* (La Ville Lumière)### Notable Landmarks:1. **Eiffel Tower** - Iconic iron lattice tower2. **Louvre Museum** - World's largest art museum3. **Notre-Dame Cathedral** - Gothic masterpiece4. **Arc de Triomphe** - Monument honoring French soldiers> Paris is not only the political center but also a global hub for art, fashion, and culture."""},    },    {        "inputs": {"question": "What is the capital of Germany?"},        "expectations": {"expected_response": """## Berlin - Capital of Germany**Berlin** is Germany's capital and largest city, situated in the *northeastern* part of the country.### Historical Significance:| Period | Importance ||--------|------------|| 1961-1989 | Divided by the **Berlin Wall** || 1990 | Reunification capital || Present | Political & cultural center |### Must-See Attractions:1. **Brandenburg Gate** - Neoclassical monument2. **Reichstag Building** - Seat of German Parliament3. **Museum Island** - UNESCO World Heritage site4. **East Side Gallery** - Open-air gallery on Berlin Wall remnants> *"Ich bin ein Berliner"* - Famous quote by JFK highlighting Berlin's symbolic importance during the Cold War."""},    },    {        "inputs": {"question": "What is the capital of Japan?"},        "expectations": {"expected_response": """## Tokyo (東京) - Capital of Japan**Tokyo** is the capital of Japan and the world's most populous metropolitan area, located on the *eastern coast* of Honshu island.### Demographics & Economy:- **Population**: ~14 million (city), ~37 million (Greater Tokyo Area)- **GDP**: One of the world's largest urban economies- **Status**: Global financial hub and technology center### Districts & Landmarks:1. **Shibuya** - Famous crossing and youth culture2. **Shinjuku** - Business district with Tokyo Metropolitan Government Building3. **Asakusa** - Historic area with *Sensō-ji Temple*4. **Akihabara** - Electronics and anime culture hub### Cultural Blend:- Ancient temples ⛩️ alongside futuristic skyscrapers 🏙️- Traditional tea ceremonies 🍵 and cutting-edge technology 🤖> Tokyo seamlessly combines **centuries-old traditions** with *ultra-modern innovation*, making it a unique global metropolis."""},    },    {        "inputs": {"question": "What is the capital of Italy?"},        "expectations": {"expected_response": """## Rome (Roma) - The Eternal City**Rome** is the capital of Italy, famously known as *"The Eternal City"* (*La Città Eterna*), with over **2,750 years** of history.### Historical Timeline:753 BC → Founded (according to legend)27 BC → Capital of Roman Empire1871 → Capital of unified ItalyPresent → Modern capital with ancient roots### UNESCO World Heritage Sites:1. **The Colosseum** - Ancient amphitheater (80 AD)2. **Roman Forum** - Center of ancient Roman life3. **Pantheon** - Best-preserved ancient Roman building4. **Vatican City** - Independent city-state within Rome   - *St. Peter's Basilica*   - *Sistine Chapel* (Michelangelo's ceiling)### Famous Quote:> *"All roads lead to Rome"* - Ancient proverb reflecting Rome's historical importance as the center of the Roman Empire### Cultural Significance:- Birthplace of **Western civilization**- Center of the *Catholic Church*- Home to countless masterpieces of ***Renaissance art and architecture***"""},    },]# Optimize the promptresult = mlflow.genai.optimize_prompts(    predict_fn=predict_fn,    train_data=dataset,    prompt_uris=[prompt.uri],    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),    scorers=[markdown_output_judge],    aggregation=feedback_to_score)# Use the optimized promptoptimized_prompt = result.optimized_prompts[0]print(f"Optimized template: {optimized_prompt.template}")

## Review your prompt[​](#review-your-prompt "Direct link to review-your-prompt")

Open the link to your MLflow experiment and complete the following steps to have the prompts appear in your experiment:

1.  Ensure your experiment type is set to GenAI apps and agents.
2.  Navigate to the prompt tab.
3.  Click **select a schema** on the top right and enter the same schema you set above to see your prompt.

## Load the new prompt and test again[​](#load-the-new-prompt-and-test-again "Direct link to load-the-new-prompt-and-test-again")

Review what the prompt looks like and load it into your predict function to see how differently the model performs.

Python

    from IPython.display import Markdownprompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/10")Markdown(prompt.template)

Python

    from IPython.display import Markdowndef predict_fn(question: str) -> str:    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}/10")    completion = openai_client.chat.completions.create(        model="databricks-gpt-oss-20b",        # load prompt template using PromptVersion.format()        messages=[{"role": "user", "content": prompt.format(question=question)}],    )    return completion.choices[0].message.contentoutput = predict_fn("What is the capital of France?.")Markdown(output[1]['text'])

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The following is a runnable notebook that shows prompt opitimization using custom scorers.

#### Prompt opitimization using custom scorers
