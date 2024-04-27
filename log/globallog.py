import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

log_filename = os.path.join(script_dir, 'app.log')

logging.basicConfig(filename=log_filename, level=logging.DEBUG)


def log_message(message: str):
    logging.info(message)
    return
