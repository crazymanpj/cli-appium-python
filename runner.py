# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import os,unittest,json
from androidhelper import AndroidHelper
from adbhelper import AdbHelper
from testcases.gamemaster_test import CommonTest
from server import Server
from log import Log

logger = Log.get_logger()

class Runner(object):

    def __init__(self, testpath):
        self.testpath = testpath
        # logger.info(testpath)
        self.my_adbhelper = AdbHelper()

    def inittest(self):
        desired_caps = {}
        desired_caps['platformName'] = self.my_adbhelper.getPlatformName()
        desired_caps['platformVersion'] = self.my_adbhelper.getPlatformVersion()
        desired_caps['deviceName'] = self.my_adbhelper.getDeviceName()
        desired_caps['appPackage'] = self.my_androidhelper.packagename
        desired_caps['appActivity'] = self.my_androidhelper.appActivity
        desired_caps['app'] = self.getTestApk()
        if self.isHigherAndroid(desired_caps['platformVersion']) == True:
            desired_caps['automationName'] = 'uiautomator2'

        logger.info(desired_caps)
        with open('config.json', 'w') as f:
            json.dump(desired_caps, f)

    def runTestCase(self):
        apkpath = self.getTestApk()
        logger.info(apkpath)
        self.my_androidhelper = AndroidHelper(apkpath)
        s = Server()
        s.start()
        desired_caps = self.inittest()
        suite = unittest.TestLoader().loadTestsFromTestCase(CommonTest)

        with open('UnitestTextReport.txt', 'w') as f:
            runner = unittest.TextTestRunner(stream=f, verbosity=2)
            runner.run(suite)

        s.stop()

    def parseTestCase(self):
        pass

    def getTestApk(self):
        if os.path.isdir(self.testpath):
            for root, dirs, files in os.walk(self.testpath):
                return os.path.join(root, files[0])

    def isHigherAndroid(self, version):
        num = int(version[0])
        if num >= 7:
            return True
        else:
            return False
