import sys
from autoLix.logger import logging
from autoLix.exception import CustomException
from autoLix.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()

obj.sync_folder_from_gcloud("inbound-density-419701.appspot.com", "orcas-doctrain-queries.tsv.gz", "download/dataset.tsv.gz")