import sys
from src.autoLix.logger import logging
from src.autoLix.exception import CustomException
from src.autoLix.components.data_ingestion import DataIngestion

from src.autoLix.entity.config_entity import (DataIngestionConfig)
from src.autoLix.entity.artifact_entity import (DataIngestionArtifact)

class TrainPipeline:
    """
    Class For Training Pipeline
    """
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Function For Starting Data Ingestion

        Args:
            None

        Returns:
            DataIngestionArtifact: Contains all data file with path
        """
        logging.info("Entered The start_data_ingestion Function of TrainPipeline Class")

        try:
            logging.info("Fetching Data From GCloud")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from gcloud")
            logging.info("Existing from start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact

        except CustomException as e:

            raise CustomException(e, sys) from e 
    
    def run_pipeline(self):
        """
        Function to run all TrainPipelines

        Args:
            None
        
        Returns:
            None
        """

        logging.info("Entered The run_pipeline Function of TrainPipeline Class")
        
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            logging.info("Existing the run_pipeline method of TrainPipeline class")
        except Exception as e:
            raise CustomException(e, sys) from e 