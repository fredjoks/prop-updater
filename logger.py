from datetime import datetime

import logging


def logger(name):

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)

    f_handler = logging.FileHandler(
        'log/{:%Y-%m-%d}.log'.format(datetime.now()))
    f_handler.setLevel(logging.WARNING)

    f_format = logging.Formatter(
        '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    f_handler.setFormatter(f_format)

    logger.addHandler(f_handler)

    return logger
