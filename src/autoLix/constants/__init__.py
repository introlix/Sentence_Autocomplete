import os

from datetime import datetime

# Common Constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = "inbound-density-419701.appspot.com"
ZIP_FILE_NAME = 'data_file.zip'


# Data Pusher Constants
DATA_ZIP_FILE_DIR = 'zip_data'
DATA_ZIP_FILE_NAME = 'data_file.zip'

# Data Ingestion Constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_REDDIT_DATA_DIR = 'reddit_data.txt'
DATA_INGESTION_WIKI_DATA_DIR = 'wiki_data.txt'
DATA_INGESTION_EXTERNAL_DATA_DIR = 'external_data.txt'

# Data transformation constants 
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_FILE_NAME = 'data.txt'
DATA_DIR = 'data'