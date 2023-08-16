#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


def test_default_log_level():
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_change_log_level():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_custom_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('This is DEBUG')
    logger.info('This is INFO')
    logger.warning('This is WARNING')
    logger.error('This is ERROR')
    logger.critical('This is CRITICAL')


test_default_log_level()
print('-----------')
test_change_log_level()
print('-----------')
test_custom_logger()
