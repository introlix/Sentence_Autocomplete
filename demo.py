import sys
from src.autoLix.logger import logging
from src.autoLix.exception import CustomException
from src.autoLix.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()

obj.sync_folder_from_gcloud("inbound-density-419701.appspot.com", "orcas-doctrain-queries.tsv.gz", "download/dataset.tsv.gz")