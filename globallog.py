import logging


logging.basicConfig(filename='app.log', level=logging.DEBUG)


def log_message(message: str):
    logging.info(message)
    return
