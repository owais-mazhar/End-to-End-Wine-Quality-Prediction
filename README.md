# mlproject2

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

export MLFLOW_TRACKING_URI=https://dagshub.com/owaisraza78617/mlproject2.mlflow
export MLFLOW_TRACKING_USERNAME=owaisraza78617
export MLFLOW_TRACKING_PASSWORD=08656d333fe1cc29629679545571fc599ea0cec1

DagsHub Commnads:

import dagshub
dagshub.init(repo_owner='owaisraza78617', repo_name='mlproject2', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)