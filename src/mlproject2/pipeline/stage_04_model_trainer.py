from mlproject2.config.configuration import ConfigurationManager
from mlproject2.components.model_trainer import ModelTrainer
from mlproject2 import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e