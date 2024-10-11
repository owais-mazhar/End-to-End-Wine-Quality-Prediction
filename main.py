from mlproject2 import logger
from mlproject2.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e