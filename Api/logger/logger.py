import logging
import colorlog
from logging.handlers import RotatingFileHandler


def init_logger(name, file, level = logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = RotatingFileHandler(file, maxBytes=10**6, backupCount=5)
    console_handler = logging.StreamHandler()



    file_formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
    console_formatter = colorlog.ColoredFormatter('%(asctime)s - %(name)s - %(log_color)s%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
)

    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    logger = init_logger("Main", "main.log")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")