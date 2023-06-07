#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   common_logging.py
@Time    :   2023/03/29 14:26:52
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

import logging
import os

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
    
    # Check if the directory of the logfile is exists, ifnot, create it
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # Now open the log file in write mode; if it doesn't exist, it will be created automaticately
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write('') # create a new log file
    
    # Log format strings
    log_format = '%(asctime)s [%(levelname)s] %(module)s:%(lineno)d - %(message)s'
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
