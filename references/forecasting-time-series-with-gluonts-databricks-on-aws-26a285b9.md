---
title: Forecasting time series with GluonTS | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-time-series-gluonts-101
ingestedAt: "2026-06-18T08:09:09.496Z"
---

This notebook demonstrates how to use [GluonTS](https://ts.gluon.ai/stable/) for probabilistic time series forecasting on Databricks serverless GPU compute. GluonTS is a Python library focused on deep learning-based approaches for time series modeling.

GluonTS provides a toolkit for forecasting and anomaly detection, with pre-built implementations of state-of-the-art [models](https://ts.gluon.ai/stable/getting_started/models.html). It supports both PyTorch and MXNet implementations and includes essential components like neural network architectures, feature processing, and [evaluation metrics](https://ts.gluon.ai/stable/api/gluonts/gluonts.evaluation.html).

The notebook covers:

*   Loading and preparing electricity consumption data
*   Creating train/test splits for backtesting
*   Training a DeepAR model for forecasting
*   Evaluating predictions with confidence intervals
*   Saving and loading model checkpoints

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

Click the **Connect** dropdown and select **Serverless GPU**. Open the **Environment** side panel, set **Accelerator** to **1xA10**, and select **AI v5**.

## Install GluonTS and dependencies[​](#install-gluonts-and-dependencies "Direct link to Install GluonTS and dependencies")

Install the GluonTS library with PyTorch support and wget for downloading the dataset.

Python

    # install gluonts package%pip install -q --upgrade gluonts[torch] wget

Python

    dbutils.library.restartPython()

## Configure Unity Catalog storage for model checkpoints[​](#configure-unity-catalog-storage-for-model-checkpoints "Direct link to Configure Unity Catalog storage for model checkpoints")

Set up Unity Catalog parameters for storing model checkpoints. The checkpoint path uses a Unity Catalog volume to persist model state during training.

Python

    # You must have `USE CATALOG` privileges on the catalog, and you must have `USE SCHEMA` privileges on the schema.# If necessary, change the catalog and schema name here.dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_model_name", "custom_transformer")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_VOLUME = dbutils.widgets.get("uc_volume")MODEL_NAME = dbutils.widgets.get("uc_model_name")CHECKPOINT_PATH = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"CHECKPOINT_PATH: {CHECKPOINT_PATH}")

Python

    # show the installed gluonts version%pip show gluonts

## Verify GPU availability and resources[​](#verify-gpu-availability-and-resources "Direct link to Verify GPU availability and resources")

Check that GPU compute is available and display the hardware specifications.

Python

    # show the GPU details!nvidia-smi

Python

    import torchimport psutil# check that GPU is available on the notebook computeassert torch.cuda.is_available(), 'You need to use GPU compute for this notebook'# show GPU, GPU RAM, number of CPUs and total RAMprint(f"""      Number of GPUs available: {torch.cuda.device_count()}      Total GPU RAM: {torch.cuda.get_device_properties(0).total_memory / (1024 ** 3):.2f} GB      Number of CPUs: {psutil.cpu_count()}      Total RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB      """)

## Import required libraries[​](#import-required-libraries "Direct link to Import required libraries")

Import GluonTS components for dataset handling, model training, and evaluation, along with standard data science libraries.

Python

    import osimport jsonimport zipfileimport matplotlib.pyplot as pltimport wgetimport tempfileimport numpy as npimport pandas as pdimport matplotlib.colors as mcolorsfrom itertools import islice# GluonTSfrom gluonts.dataset.pandas import PandasDatasetfrom gluonts.dataset.split import DateSplitterfrom gluonts.dataset.util import to_pandasfrom gluonts.evaluation import Evaluatorfrom gluonts.dataset.field_names import FieldNamefrom gluonts.torch import DeepAREstimatorfrom lightning.pytorch.callbacks import ModelCheckpoint# setup plt environmentplt.rcParams["axes.grid"] = Trueplt.rcParams["figure.figsize"] = (20, 3)colors = list(mcolors.TABLEAU_COLORS)

## Load electricity consumption dataset[​](#load-electricity-consumption-dataset "Direct link to Load electricity consumption dataset")

This notebook uses the electricity consumption [dataset](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) from the University of California, Irvine repository. The dataset contains electricity consumption readings from 370 clients between 2011-2014, with values recorded every 15 minutes in kW.

Configure the dataset source URL and file name for downloading.

Python

    data_file_name = 'LD2011_2014.txt'dataset_url = 'https://archive.ics.uci.edu/static/public/321/electricityloaddiagrams20112014.zip'

The dataset file is approximately 800 MB when extracted, which exceeds the 500 MB workspace file limit for Databricks serverless notebooks. The following code uses a temporary directory to download and extract the data, then loads it into a Pandas DataFrame.

Python

    # download and extract data# the electricity dataset https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014 from the repository of the University of California, Irvinewith tempfile.TemporaryDirectory() as tmp_dir_name:  temp_zip = f'{tmp_dir_name}/ts.zip'  print(f'Downloading data zip file from: {dataset_url}')  wget.download(dataset_url, out=temp_zip)  with zipfile.ZipFile(temp_zip, 'r') as zip_ref:    print(f'Extracting data to: {tmp_dir_name}')    data_file_path = zip_ref.extract(data_file_name, tmp_dir_name)    print(f'Zip extracted to: {data_file_path}')  print('Loading data into Pandas DataFrame')  df_raw = pd.read_csv(    data_file_path,    sep=';',    index_col=0,    decimal=',',    parse_dates=True,  )

Preview the raw electricity consumption data with 15-minute intervals.

## Resample data to hourly intervals[​](#resample-data-to-hourly-intervals "Direct link to Resample data to hourly intervals")

Resample the data from 15-minute to 1-hour intervals to reduce the number of data points and speed up training.

Python

    # resample to 1h intervals to reduce the number of data pointsfreq = "1h"div = 4 # 1 hour contain 4x 15 min intervals, you need to  delete the resampled value by 4data_kw = df_raw.resample(freq).sum() / divdata_kw

## Configure prediction parameters[​](#configure-prediction-parameters "Direct link to Configure prediction parameters")

Set the prediction horizon to 7 days (168 hours) and define the training date range using 2014 data.

Select a subset of time series for faster training. Set `USE_FULL_DATASET = True` to train on all 370 time series.

Python

    # predict for 7 daysprediction_days = 7# 24 hours per dayintervals_per_day = 24prediction_length = prediction_days * intervals_per_day# take the last year of data for a samplestart_training_date = pd.Timestamp('2014-01-01')end_dataset_date = pd.Timestamp('2014-12-31')print(f"Sampling frequency set to {freq}. Generate predictions for {prediction_length} intervals")

Python

    USE_FULL_DATASET = False # By default use only a subset of the time series because training of full dataset can take longer timeSAMPLE_SIZE = 10 # set number of samples in the dataset if you don't use the full datasetMAX_TS_TO_DISPLAY = 10# get the full dataset or a random sample of SAMPLE_SIZE# you can change the selection to include specific time series# ts_sample = data_kw[['item_id1', 'item_id2']]ts_sample = data_kw if USE_FULL_DATASET else data_kw[np.random.choice(data_kw.columns.to_list(), size=SAMPLE_SIZE, replace=False)]

## Convert data to GluonTS format[​](#convert-data-to-gluonts-format "Direct link to Convert data to GluonTS format")

Convert the Pandas DataFrame to GluonTS format and visualize the time series. See the GluonTS [Quick start](https://ts.gluon.ai/stable/tutorials/forecasting/quick_start_tutorial.html) for more examples.

Python

    # convert to GluonTS format, taking only the data between start_training_date and end_dataset_datets_dataset = PandasDataset(    dict(ts_sample[(ts_sample.index > start_training_date) & (ts_sample.index <= end_dataset_date)].astype(np.float32)))# visualize time series in the GluonTS datasetfor i, entry in enumerate(islice(ts_dataset, MAX_TS_TO_DISPLAY)):    to_pandas(entry).plot(label=entry[FieldName.ITEM_ID], color=colors[i % len(colors)])    plt.legend()    plt.tight_layout()    plt.show()print(f'The GluonTS dataset contains {len(ts_dataset)} individual time series from {start_training_date} to {end_dataset_date}')

## Create train/test split for backtesting[​](#create-traintest-split-for-backtesting "Direct link to Create train/test split for backtesting")

Split the dataset into training and test sets using rolling windows. This creates 4 test windows for backtesting model performance.

Python

    # set backtest parametersNUM_WINDOWS = 4 # number of rolling windows for backtest# distance between windows, set to:# < prediction_length for overlapping windows# = prediction length for adjucent windows# > prediction_length for non overapping and non-adjucent windowsDISTANCE = prediction_length# set the training-testing split dateend_training_date = pd.Period(end_dataset_date, freq=freq) - NUM_WINDOWS*prediction_length# split into train and test datasets using GluonTS's DateSplittertrain_ds, test_template = DateSplitter(date=end_training_date).split(ts_dataset)test_pairs = test_template.generate_instances(    prediction_length=prediction_length,    windows=NUM_WINDOWS,    distance=DISTANCE,)print(f"The dataset is splitted in {len(train_ds)} training datasets and {len(test_pairs)} test pairs. Training end is {end_training_date}")

## Train a DeepAR model[​](#train-a-deepar-model "Direct link to Train a DeepAR model")

Train a DeepAR estimator, a recurrent neural network model for probabilistic forecasting. See [Available Models](https://ts.gluon.ai/stable/getting_started/models.html) in the GluonTS documentation for other algorithms.

Configure the DeepAR model hyperparameters and training settings. The model uses a context length of 4 times the prediction length and saves checkpoints after each epoch.

Python

    NUM_EPOCHS = 10os.makedirs(CHECKPOINT_PATH, exist_ok=True)checkpoint_cb = ModelCheckpoint(    dirpath=CHECKPOINT_PATH,    filename="deepar-{epoch:02d}-{step}",    save_top_k=-1,           # keep all checkpoints    every_n_epochs=1,        # save after every epoch    save_on_train_epoch_end=True,)# set required model hyperparameters. See GluonTS repository for the full list of hyperparametersmodel_hyperparameters = {    "freq":freq,    "prediction_length":prediction_length,    "context_length":4*prediction_length,}# set required trainer hyperparameterstrainer_hyperparameters = {    "accelerator":"auto",    "max_epochs":NUM_EPOCHS,    "callbacks":[checkpoint_cb]}# create a DeepAR estimatordeepar_estimator = DeepAREstimator(  **model_hyperparameters,  trainer_kwargs=trainer_hyperparameters,)

Train the DeepAR model on the training dataset. Training for 10 epochs takes approximately 60 seconds on a single GPU.

Python

    # Suppress known compatibility warningsimport warningswarnings.filterwarnings("ignore", message="Using a non-tuple sequence for multidimensional indexing")torch.set_float32_matmul_precision('high')

Python

    # train the network# the training for 10 epochs takes about 60 second on a single GPU in this notebookdeepar_predictor = deepar_estimator.train(train_ds)

## Generate and visualize predictions[​](#generate-and-visualize-predictions "Direct link to Generate and visualize predictions")

Use the trained model to predict the next 7 days for each time series. The visualizations show predicted values with 90% confidence intervals and ground truth values.

Python

    # predictforecasts = deepar_predictor.predict(test_pairs.input, num_samples=20)# ground truthlabels = [to_pandas(l) for l in test_pairs.label]# visualize predictionsfor i, forecast in enumerate(islice(forecasts, MAX_TS_TO_DISPLAY)):    plt.plot(labels[i][-NUM_WINDOWS*prediction_length:].to_timestamp())    forecast.plot(intervals=(0.9,), show_label=True)    plt.legend([f"Ground truth: {forecast.item_id}", "predicted median", "90% confidence interval"])    plt.show()

## Evaluate model performance[​](#evaluate-model-performance "Direct link to Evaluate model performance")

Calculate evaluation metrics using the GluonTS [Evaluator](https://ts.gluon.ai/stable/tutorials/forecasting/quick_start_tutorial.html#Visualize-and-evaluate-forecasts). Metrics include MASE, RMSE, and quantile losses.

Python

    # calculate evaluation metricsevaluator = Evaluator(quantiles=[0.1, 0.5, 0.9])agg_metrics, item_metrics = evaluator(    labels,    deepar_predictor.predict(test_pairs.input, num_samples=20),    num_series=len(test_pairs),)# metrics per time seriesitem_metrics.display()# aggregated metricsprint(json.dumps(agg_metrics, indent=2))

## Resume training from checkpoint[​](#resume-training-from-checkpoint "Direct link to Resume training from checkpoint")

Load a saved checkpoint and continue training for additional epochs. This demonstrates how to resume training from a previously saved model state.

Configure the model to train for an additional 10 epochs starting from the saved checkpoint at epoch 9.

Python

    # set required model hyperparameters. See GluonTS repository for the full list of hyperparametersmodel_hyperparameters = {    "freq": freq,    "prediction_length": prediction_length,    "context_length": 4 * prediction_length,}# set required trainer hyperparameterstrainer_hyperparameters = {    "accelerator": "auto",    "max_epochs": NUM_EPOCHS + 10, # Train for another 10 epochs    "callbacks": [checkpoint_cb],}# create a DeepAR estimator using the model checkpointdeepar_estimator = DeepAREstimator(    **model_hyperparameters,    trainer_kwargs=trainer_hyperparameters,)updated_predictor = deepar_estimator.train(    training_data=train_ds,    ckpt_path=f"{CHECKPOINT_PATH}/deepar-epoch=09-step=500.ckpt",)

## Next steps[​](#next-steps "Direct link to Next steps")

This notebook demonstrated the basics of time series forecasting with GluonTS on Databricks serverless GPU compute. To learn more:

*   [GluonTS extended tutorial](https://ts.gluon.ai/stable/tutorials/forecasting/extended_tutorial.html) - Advanced forecasting examples
*   [GluonTS available models](https://ts.gluon.ai/stable/getting_started/models.html) - Complete list of pre-built models
*   [Databricks serverless GPU compute best practices](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability) - Optimization tips
*   [Troubleshoot serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides) - Common issues and solutions

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Forecasting time series with GluonTS
