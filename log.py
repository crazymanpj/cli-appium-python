#!/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-30
# Author:  pangjian
import logging


class Log():

    @classmethod
    def get_logger(cls, name=__name__):
        return logging.getLogger(name)

    @classmethod
    def set_log_level(cls, loglevel):
        logging.basicConfig(level=loglevel)
