import os
import sys
from zipfile import ZipFile
from src.autoLix.logger import logging
from src.autoLix.exception import CustomException
from src.autoLix.configuration.gcloud_syncer import GCloudSync
from src.autoLix.entity.config_entity import DataIngestionConfig
from src.autoLix.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config : DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()

    def get_data_from_gcloud(self) -> None:

        try:
            logging.info("Entered the get_data_from_gcloud method of Data ingestion class")

            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)

            self.gcloud.sync_folder_from_gcloud(
                self.data_ingestion_config.BUCKET_NAME,
                self.data_ingestion_config.ZIP_FILE_NAME,
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR
            )

            logging.info("Exited the get_data_from_gcloud method of Data ingestion class")

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def unziping_data(self):
        try:
            logging.info("Entered the unziping_data method of Data ingestion class")

            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the unziping_data method of Data ingestion class")

            return self.data_ingestion_config.DATA_INGESTION_REDDIT_DATA_DIR, self.data_ingestion_config.DATA_INGESTION_WIKI_DATA_DIR, self.data_ingestion_config.DATA_INGESTION_EXTERNAL_DATA_DIR

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the initiate_data_ingestion method of Data ingestion class")
            self.get_data_from_gcloud()
            logging.inof("Fetched the data from gcloud")
            reddit_data_file_path, wiki_data_file_path, external_data_file_path = self.unziping_data()
            logging.info("Unziped the data")

            data_ingestion_artifact = DataIngestionArtifact(
                reddit_data_file_path=reddit_data_file_path,
                wiki_data_file_path=wiki_data_file_path,
                external_data_file_path=external_data_file_path,
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys) from e