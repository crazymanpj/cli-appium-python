# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian

import json,os,subprocess,inspect
from appium import webdriver
from log import Log
from const import PICPATH
import time
import traceback
from adbhelper import AdbHelper

logger = Log.get_logger(__name__)

PROJECT_PATH = os.getcwd()

def initAppium():
    configeFile = os.path.join(PROJECT_PATH, 'config.json')
    with open(configeFile, 'r') as f:
        desired_caps = json.load(f)
        # print(type(desired_caps))
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def verifyElement(element, isdisplay=True):
    if isdisplay:
        assert element is not False and element is not None
    else:
        assert element is False and element is None

def initLogcat():
    cmd = 'adb logcat -v time *:E'
    with open('mylog.txt', 'w', encoding='utf-8') as f:
        subprocess.Popen(cmd, shell=True, stdout=f)

def capture(func):
    def wrapper(self):
        logger.info(func)
        try:
            func(self)
        except Exception as e:
            logger.info(traceback.format_exc())
            savepath = os.path.join(PROJECT_PATH, PICPATH)
            AdbHelper.screenShot(savepath)
            logger.debug('capture end')
            raise AssertionError

    return wrapper


if __name__=='__main__':
    pass
