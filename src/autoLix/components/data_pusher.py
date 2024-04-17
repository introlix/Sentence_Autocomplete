import os
import sys
import pathlib
from zipfile import ZipFile, ZIP_DEFLATED
from src.autoLix.logger import logging
from src.autoLix.exception import CustomException
from src.autoLix.configuration.gcloud_syncer import GCloudSync
from src.autoLix.entity.config_entity import DataPusherConfig

class DataPusher():
    def __init__(self, datafolder:list, data_pusher_config:DataPusherConfig) -> None:
        """
        DataPusher class fist compress the data into zip file then upload it to gcloud

        Args:
            datafolder (list): datafolder is the list of folders that contains the file which will be compressed into zip
            data_pusher_config: it is the entity config for data pusher config 
        """
        self.datafolder = datafolder
        self.datapaths = []
        self.gcloud = GCloudSync()
        self.data_pusher_config = data_pusher_config

    
    def ziping_data(self):
        """
        Function to conpresses data into zip file
        """
        try:
            logging.info("Start Ziping The Data")


            os.makedirs(self.data_pusher_config.DATA_ZIP_FILE_DIR, exist_ok=True)

            with ZipFile(self.data_pusher_config.DATA_ZIP_FILE_PATH, 'w', ZIP_DEFLATED) as zip:
                for folder in self.datafolder:
                    path = pathlib.Path(folder)
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            file_path = pathlib.Path(file_path)
                            zip.write(file_path)

            logging.info(f"Zip file is saved in {self.data_pusher_config.DATA_ZIP_FILE_PATH}")
                
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def upload_data(self):
        """
        Function to upload zip data into gcloud
        """
        try:
            logging.info("Uploading Folder To Gcloud")

            self.gcloud.sync_folder_to_gcloud(
                self.data_pusher_config.BUCKET_NAME,
                self.data_pusher_config.DATA_ZIP_FILE_PATH,
                self.data_pusher_config.DATA_ZIP_FILE_NAME
            )

        except Exception as e:
            raise CustomException(e, sys) from e