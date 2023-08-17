#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import inspect

# @see https://stackoverflow.com/a/13627881
def get_shared_logger():
    if 'something' not in globals():
        print("once called")
        # create logger
        logger = logging.getLogger('simple_example')
        logger.setLevel(logging.DEBUG)
        # @see https://stackoverflow.com/a/44426266
        logger.propagate = False

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        if not logger.handlers:
            logger.addHandler(ch)
        globals()['something'] = logger

    return globals()['something']


def test_default_log_level():
    print(f"------{inspect.stack()[0][3]} called------")
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_change_log_level():
    print(f"------{inspect.stack()[0][3]} called------")
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_custom_logger():
    print(f"------{inspect.stack()[0][3]} called------")
    myLogger = logging.getLogger('myLogger')
    myLogger.setLevel(logging.DEBUG)
    myLogger.addHandler(logging.StreamHandler())
    # @see https://stackoverflow.com/a/44426266
    myLogger.propagate = False
    myLogger.debug('This is DEBUG')
    myLogger.info('This is INFO')
    myLogger.warning('This is WARNING')
    myLogger.error('This is ERROR')
    myLogger.critical('This is CRITICAL')


def test_shared_logger():
    print(f"------{inspect.stack()[0][3]} called------")
    get_shared_logger().debug('debug message2')
    get_shared_logger().info('info message')
    get_shared_logger().warning('warn message')
    get_shared_logger().error('error message')
    get_shared_logger().critical('critical message')


test_default_log_level()
test_change_log_level()
test_custom_logger()
test_shared_logger()
