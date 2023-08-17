#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import inspect

# Note: default is warning log level in Python 3.11.3
# Only print warning and above level
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


test_change_log_level()
