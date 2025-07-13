import logging


def log_gen():
    logger = logging.getLogger()
    file_handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger