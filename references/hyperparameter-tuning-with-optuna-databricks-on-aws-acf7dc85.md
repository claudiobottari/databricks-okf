---
title: Hyperparameter tuning with Optuna | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna
ingestedAt: "2026-06-18T08:09:52.969Z"
---

    import sklearndef objective(trial):    # Invoke suggest methods of a Trial object to generate hyperparameters.    regressor_name = trial.suggest_categorical('classifier', ['SVR', 'RandomForest'])    if regressor_name == 'SVR':        svr_c = trial.suggest_float('svr_c', 1e-10, 1e10, log=True)        regressor_obj = sklearn.svm.SVR(C=svr_c)    else:        rf_max_depth = trial.suggest_int('rf_max_depth', 2, 32)        regressor_obj = sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth)    X, y = sklearn.datasets.fetch_california_housing(return_X_y=True)    X_train, X_val, y_train, y_val = sklearn.model_selection.train_test_split(X, y, random_state=0)    regressor_obj.fit(X_train, y_train)    y_pred = regressor_obj.predict(X_val)    error = sklearn.metrics.mean_squared_error(y_val, y_pred)    return error  # An objective value linked with the Trial object
