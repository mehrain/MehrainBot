import logging
import logging.handlers
import colorlog

def setup_logger():
    # Set up logging
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)  # Set the logger's level to DEBUG

    # Set up file handler
    file_handler = logging.handlers.RotatingFileHandler(
        filename='src/logs/botlog.txt',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  
        backupCount=5,  
    )
    file_handler.setLevel(logging.DEBUG)  # Set the file handler's level to DEBUG

    # Set up stream handler
    stream_handler = colorlog.StreamHandler()
    stream_handler.setLevel(logging.INFO)  # Set the stream handler's level to INFO

    # Set up formatter
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    file_formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    stream_formatter = colorlog.ColoredFormatter(
        "{log_color}[{asctime}] [{levelname:<8}] {name}: {message}",
        datefmt=dt_fmt,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='{'
    )

    # Add formatter to handlers
    file_handler.setFormatter(file_formatter)
    stream_handler.setFormatter(stream_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger