import logging
import os,sys
from datetime import datetime


# Creating logs directory to store log in files
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)


os.makedirs(LOG_DIR, exist_ok=True)


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"


log_file_path = os.path.join(LOG_DIR, file_name)


logging.basicConfig( format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
                     handlers=[logging.FileHandler(log_file_path),logging.StreamHandler(sys.stdout)],
                    level=logging.INFO)