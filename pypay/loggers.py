import logging
import time
import os

from pypay.settings import BASE_DIR

timestr = time.strftime("%Y-%m-%d")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log_path = os.path.join(BASE_DIR, 'loggers/' + timestr + '.log')
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_pay(message):
    return logger.info(message)