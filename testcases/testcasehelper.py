# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian

import json,os
from appium import webdriver

PROJECT_PATH = os.getcwd()

def initAppium():
    configeFile = os.path.join(PROJECT_PATH, 'config.json')
    with open(configeFile, 'r') as f:
        desired_caps = json.load(f)
        # print(type(desired_caps))
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


if __name__=='__main__':
    initAppium()
