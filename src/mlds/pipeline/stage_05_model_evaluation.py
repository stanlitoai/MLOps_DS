from mlds.config.configuration import ConfigurationManager
from mlds.components.model_evalulation import ModelEvaluation
from mlds import logger



STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evl_config = config.get_model_evaluation_config()
        model_evl = ModelEvaluation(config=model_evl_config)
        model_evl.log_into_mlflow()
        logger.info(f"Model Evaluation stage completed!")
        
        
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
    except Exception as e:
        logger.exception(e)
        raise e