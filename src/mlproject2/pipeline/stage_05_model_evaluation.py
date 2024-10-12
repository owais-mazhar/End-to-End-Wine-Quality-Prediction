from mlproject2.config.configuration import ConfigurationManager
from mlproject2.components.model_evaluation import ModelEvaluation
from mlproject2 import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e