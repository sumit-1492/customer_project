from customerpersonality.logging import logging
from customerpersonality.constants import *
from customerpersonality.utils.common import read_yaml, create_directories
from customerpersonality.entity import DataIngestionConfiguration

class ConfigurationManager:

    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):

        try:

            #self.config_file_path = CONFIG_FILE_PATH

            self.config = read_yaml(config_file_path) ## read config.yaml file

            create_directories([self.config.artifacts_dir])

            logging.info(f"artifacts directory created: {self.config.artifacts_dir}")

        except Exception as e:

            raise e

        
    def get_data_ingestion_config(self) -> DataIngestionConfiguration:

        try:

            artifacts_dir = self.config.artifacts_dir
            config = self.config.data_ingestion_config
            
            data_ingestion_dir = os.path.join(artifacts_dir,config.root_dir)
            create_directories([data_ingestion_dir])

            raw_data_dir = os.path.join(data_ingestion_dir,config.zip_data_dir)
            create_directories([raw_data_dir])

            ingested_unzip_csv_file_dir = os.path.join(data_ingestion_dir,config.unzip_data_dir)
            create_directories([ingested_unzip_csv_file_dir])

            data_ingestion_config = DataIngestionConfiguration( 
                                        root_dir = config.root_dir,
                                        dataset_download_url = config.dataset_download_url,
                                        zip_data_dir = raw_data_dir,
                                        unzip_data_dir = ingested_unzip_csv_file_dir,
                                    )
            logging.info(f" Data ingestion configuration: {data_ingestion_config}")

            return data_ingestion_config
        
        except Exception as e:
            raise e