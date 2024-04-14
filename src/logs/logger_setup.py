# logger_setup.py
import logging
import logging.handlers
import sys

def setup_logger():

    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    return logger

    # # Set up logging
    # logger = logging.getLogger('discord')
    # logger.setLevel(logging.DEBUG)
    # logging.getLogger('discord.http').setLevel(logging.INFO)

    # handler = logging.handlers.RotatingFileHandler(
    #     filename='src/logs/botlog.txt',
    #     encoding='utf-8',
    #     maxBytes=32 * 1024 * 1024,  
    #     backupCount=5,  
    # )
    # dt_fmt = '%Y-%m-%d %H:%M:%S'
    # formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    # return logger