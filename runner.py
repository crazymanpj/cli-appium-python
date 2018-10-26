# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import os,unittest
from androidhelper import AndroidHelper
from adbhelper import AdbHelper
from testcases.gamemaster_test import MomentTest
from server import Server
import json

class Runner(object):

    def __init__(self, testpath):
        self.testpath = testpath
        self.my_adbhelper = AdbHelper()

    def inittest(self):
        desired_caps = {}
        desired_caps['platformName'] = self.my_adbhelper.getPlatformName()
        desired_caps['platformVersion'] = self.my_adbhelper.getPlatformVersion()
        desired_caps['deviceName'] = self.my_adbhelper.getDeviceName()
        desired_caps['appPackage'] = self.my_androidhelper.packagename
        desired_caps['appActivity'] = self.my_androidhelper.appActivity
        desired_caps['app'] = self.getTestApk()
        print(desired_caps)
        with open('config.json', 'w') as f:
            json.dump(desired_caps, f)

    def runTestCase(self):
        apkpath = self.getTestApk()
        self.my_androidhelper = AndroidHelper(apkpath)
        s = Server()
        s.start()
        desired_caps = self.inittest()
        print('tt1')
        suite = unittest.TestLoader().loadTestsFromTestCase(MomentTest)

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


if __name__ == '__main__':
    r = Runner(r'd:\kuaipan\python\cli-appium-python\apk')
    r.runTestCase()
