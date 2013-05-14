#!/usr/bin/env python
#-*- encoding:utf-8 -*-
'''
File: test_log.py
Author: Eric Su
Description:
'''
import logging

log_file='./sys.log'

def init_log(log_file=log_file,level=logging.NOTSET):
    logger = logging.getLogger()
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('[%(asctime)s - %(name)s]%(levelname)s:%(message)s - %(filename)s:%(lineno)d')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger