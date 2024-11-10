import logging
import logging.handlers

LOGGER_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

def setup_logger(name: str, level=logging.DEBUG):
    """
    Set up a logger with the specified name and log level.

    Args:
        name (str): The name of the logger.
        level (int, optional): The log level to set for the logger. Defaults to logging.DEBUG.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(LOGGER_FORMAT)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
