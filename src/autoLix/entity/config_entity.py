from dataclasses import dataclass
from src.autoLix.constants import *

@dataclass
class DataPusherConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.DATA_ZIP_FILE_NAME = DATA_ZIP_FILE_NAME
        self.DATA_ZIP_FILE_DIR = os.path.join(os.getcwd(), 'data', DATA_ZIP_FILE_DIR)
        self.DATA_ZIP_FILE_PATH = os.path.join(os.getcwd(), 'data', DATA_ZIP_FILE_DIR, DATA_ZIP_FILE_NAME)

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_INGESTION_REDDIT_DATA_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_REDDIT_DATA_DIR)
        self.DATA_INGESTION_WIKI_DATA_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_WIKI_DATA_DIR)
        self.DATA_INGESTION_EXTERNAL_DATA_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_EXTERNAL_DATA_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_FILE_NAME)