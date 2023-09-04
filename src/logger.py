import logging
from datetime import datetime #type:ignore
import os

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(), 'logs', log_file)
os.makedirs(os.path.dirname(file_path), exist_ok=True)

logging.basicConfig(
    filename=file_path,
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
