import logging

def setup_logging(level=logging.INFO, log_file='logs/logging.log'):
    """
    Configures the logging system and returns a logger instance.
    :param level: The minimum loglevel to output to the console/filehandler
    :param log_file: The path of the logfile to write logs to
    Example:
        logger = setup_logging(level=logging.DEBUG)
        logger.debug('This is a debug-level message')
        logger.info('This is an info-level message')
        logger.warning('This is a warning-level message')
    """
    # Log format strings
    log_format = '%(asctime)s [%(levelname)8s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # Creating file handler
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))

    # Creating stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))

    # Create and return a logger with the given name
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
