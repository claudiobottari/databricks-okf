---
title: Train XGBoost model on a single GPU | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-xgboost
ingestedAt: "2026-06-18T08:09:11.483Z"
---

    import xgboost as xgbfrom sklearn.datasets import fetch_california_housingfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import root_mean_squared_error# Load California Housing datasetX, y = fetch_california_housing(return_X_y=True)X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)# Convert to DMatrixdtrain = xgb.DMatrix(X_train, label=y_train)dtest = xgb.DMatrix(X_test, label=y_test)# GPU training parameters for regressionparams = {    "tree_method": "hist",        # Use GPU histogram    "device": "cuda",    "objective": "reg:squarederror",  # Regression objective    "eval_metric": "rmse",            # Root Mean Squared Error    "max_depth": 6,    "learning_rate": 0.1,}# Train the modelbst = xgb.train(    params=params,    dtrain=dtrain,    num_boost_round=200,    evals=[(dtest, "eval"), (dtrain, "train")],    verbose_eval=10,    callbacks=[checkpoint_cb])# Predicty_pred = bst.predict(dtest)# Evaluatermse = root_mean_squared_error(y_test, y_pred)print(f"✅ RMSE on test set: {rmse:.4f}")
