# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import os
from androidhelper import AndroidHelper
from adbhelper import AdbHelper

class Runner(object):

    def __init__(self, testpath):
        self.testpath = testpath
        self.my_androidhelper = AndroidHelper()
        self.my_adbhelper = AdbHelper()
        self.appPackage = ''
        self.appActivity = ''

    def inittest(self):
        desired_caps = {}
        desired_caps['platformName'] = self.my_adbhelper.getPlatformName()
        desired_caps['platformVersion'] = self.my_adbhelper.getPlatformVersion()
        desired_caps['deviceName'] = self.my_adbhelper.getDeviceName()
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        print(desired_caps)

    def runTestCase(self):
        apkpath = self.getTestApk()
        self.appPackage, self.appActivity = self.my_androidhelper.getApkInfo(apkpath)
        desired_caps = self.inittest()



    def parseTestCase(self):
        pass

    def getTestApk(self):
        if os.path.isdir(self.testpath):
            for root, dirs, files in os.walk(self.testpath):
                return os.path.join(root, files[0])


if __name__ == '__main__':
    r = Runner(r'd:\kuaipan\python\cli-appium-python\apk')
    print(r.runTestCase())
