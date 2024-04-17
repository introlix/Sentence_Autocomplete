# import sys
# from src.autoLix.logger import logging
# from src.autoLix.exception import CustomException
# from src.autoLix.configuration.gcloud_syncer import GCloudSync

# obj = GCloudSync()

# obj.sync_folder_from_gcloud("inbound-density-419701.appspot.com", "data_file.zip", "download/dataset.zip")

from torchtext.data.utils import get_tokenizer

text = "This is a text"

tokenizer = get_tokenizer('basic_english')

token = tokenizer(text)

print(token)