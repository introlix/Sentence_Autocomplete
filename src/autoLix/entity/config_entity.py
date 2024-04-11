from dataclasses import dataclass
from src.autoLix.constants import *

@dataclass
class DataPusherConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.DATA_ZIP_FILE_NAME = DATA_ZIP_FILE_NAME
        self.DATA_ZIP_FILE_DIR = os.path.join(os.getcwd(), 'data', DATA_ZIP_FILE_DIR)
        self.DATA_ZIP_FILE_PATH = os.path.join(os.getcwd(), 'data', DATA_ZIP_FILE_DIR, DATA_ZIP_FILE_NAME)