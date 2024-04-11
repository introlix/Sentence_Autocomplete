import os
import sys
from src.autoLix.components.data_pusher import DataPusher
from src.autoLix.entity.config_entity import DataPusherConfig

def upload_data():
    data_pusher_config = DataPusherConfig()
    datafolders = ["./data/external_data", "./data/reddit_data", "./data/wiki_data"]
    datapusher = DataPusher(datafolders, data_pusher_config)
    datapusher.ziping_data()
    datapusher.upload_data()


if __name__ == '__main__':
    upload_data()