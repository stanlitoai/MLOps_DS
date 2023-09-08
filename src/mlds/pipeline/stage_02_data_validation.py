from mlds.config.configuration import ConfigurationManager
from mlds.components.data_validation import DataValiadtion
from mlds import logger



STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_val_config = config.get_data_validation_config()
        data_val = DataValiadtion(config=data_val_config)
        data_val.validate_all_columns()
        logger.info(f"Data Ingestion stage completed!")
        
        
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
    except Exception as e:
        logger.exception(e)
        raise e