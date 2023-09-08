from mlds.config.configuration import ConfigurationManager
from mlds.components.data_transformation import DataTransformation
from mlds import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_val = DataTransformation(config=data_transformation_config)
                data_val.train_test_spliting()
                logger.info(f"Data Train_test_split stage completed!")
            else:
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            print(e)
        
        
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx====================================================x")
    except Exception as e:
        logger.exception(e)
        raise e