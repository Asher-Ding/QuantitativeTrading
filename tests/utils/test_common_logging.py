import os
import logging
import shutil

from app.utils.common_logging import setup_logging


def test_setup_logging():
    log_dir = 'test_logs'
    log_file= log_dir + '/logging.log'
    
    # Test that the log directory is created if it doesn't exist
    assert not os.path.exists(log_dir)
    logger = setup_logging(level=logging.DEBUG,log_file=log_file )
    assert os.path.exists(log_dir)
    shutil.rmtree(log_dir)
    
    # Test that the log file is created if it doesn't exist
    assert not os.path.exists(log_file)
    logger = setup_logging(level=logging.DEBUG, log_file=log_file)
    assert os.path.exists(log_file)

    # Test that the logger level is correctly set
    logger = setup_logging(level=logging.WARNING)
    assert logger.level == logging.WARNING

    # Test that the file handler and stream handler are correctly configured
    logger = setup_logging(level=logging.DEBUG)
    # assert len(logger.handlers) == 2
    assert type(logger.handlers[0]) == logging.FileHandler
    assert type(logger.handlers[1]) == logging.StreamHandler
    shutil.rmtree(log_dir)
