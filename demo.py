import os
from src.autoLix.configuration.gcloud_syncer import GCloudSync
from src.autoLix.entity.config_entity import DataIngestionConfig

obj = GCloudSync()
obj2 = DataIngestionConfig()

os.makedirs(obj2.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
print(obj2.DATA_INGESTION_ARTIFACTS_DIR)
obj.sync_folder_from_gcloud(obj2.BUCKET_NAME, obj2.ZIP_FILE_NAME, obj2.DATA_INGESTION_ARTIFACTS_DIR)

