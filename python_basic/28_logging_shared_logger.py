#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import inspect


def get_shared_logger():
    """Get a shared logger, @see https://stackoverflow.com/a/13627881"""
    if 'sharedLogger' not in globals():
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

        logger.info(f'{get_shared_logger.__name__} should called once')
        globals()['sharedLogger'] = logger

    return globals()['sharedLogger']


def test_shared_logger():
    print(f"------{inspect.stack()[0][3]} called------")
    get_shared_logger().debug('debug message')
    get_shared_logger().info('info message')
    get_shared_logger().warning('warn message')
    get_shared_logger().error('error message')
    get_shared_logger().critical('critical message')


test_shared_logger()
