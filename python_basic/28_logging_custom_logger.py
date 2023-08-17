#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import inspect


# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


def test_custom_logger():
    print(f"------{inspect.stack()[0][3]} called------")
    myLogger1 = logging.getLogger('myLogger1')
    myLogger1.setLevel(logging.DEBUG)
    myLogger1.addHandler(logging.StreamHandler())
    # @see https://stackoverflow.com/a/44426266
    myLogger1.propagate = False
    myLogger1.debug('This is DEBUG')
    myLogger1.info('This is INFO')
    myLogger1.warning('This is WARNING')
    myLogger1.error('This is ERROR')
    myLogger1.critical('This is CRITICAL')


test_custom_logger()
