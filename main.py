from mlds import logger
from mlds.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlds.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlds.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlds.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlds.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline




STAGE_NAME = "Data Ingestion stage"



try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
except Exception as e:
    logger.exception(e)
    raise e

 
 
STAGE_NAME = "Data Validation stage"

        
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Evaluation stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
except Exception as e:
    logger.exception(e)
    raise e