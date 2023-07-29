import os
import urllib.request as request
import zipfile
from customerpersonality.logging import logging
from customerpersonality.utils.common import get_file_size
from customerpersonality.entity import DataIngestionConfiguration

class DataIngestion:

    def __init__(self, config : DataIngestionConfiguration):

        try:
            self.config = config
        except Exception as e:
            raise e
        
    def download_zip_file(self):

        try:
            zip_file_name = os.path.basename(self.config.dataset_download_url)
            zip_data_path = os.path.join(self.config.zip_data_dir,zip_file_name)
            self.zip_data_path_ = zip_data_path
            if not os.path.exists(zip_data_path):
                filename, headers = request.urlretrieve(
                    url = self.config.dataset_download_url,
                    filename = zip_data_path
                )
                logging.info(f"{filename} download! with following info: \n{headers}")
            else:
                logging.info(f"File already exists of size: {get_file_size(Path(zip_data_path))}") 

        except Exception as e:
            raise e
        
    def extract_zip_file(self):

        try:
            unzip_data_path = self.config.unzip_data_dir
            with zipfile.ZipFile(self.zip_data_path_, 'r') as zip_file:
                zip_file.extractall(unzip_data_path)
            
            logging.info(f"Data unzipped in: {unzip_data_path}")

        except Exception as e:
            raise e