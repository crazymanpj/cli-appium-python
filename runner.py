# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import os,unittest,json,time
from androidhelper import AndroidHelper
from adbhelper import AdbHelper
from server import Server
from log import Log
import HTMLTestRunner
from per import PerTest
from const import PROCESSUINAME, APKPATH

logger = Log.get_logger(__name__)
PROJECTPATH = os.getcwd()

class Runner(object):

    #argv: testset or testpath
    def __init__(self, testset):
        self.testpath = testset
        # logger.info(testpath)
        self.my_adbhelper = AdbHelper()
        self.exception_define = 'Runner() run test Error'

    def inittest(self):
        desired_caps = {}
        desired_caps['platformName'] = self.my_adbhelper.getPlatformName()
        desired_caps['platformVersion'] = self.my_adbhelper.getPlatformVersion()
        desired_caps['deviceName'] = self.my_adbhelper.getDeviceName()
        desired_caps['appPackage'] = self.my_androidhelper.packagename
        desired_caps['appActivity'] = self.my_androidhelper.appActivity
        desired_caps['app'] = self.getTestApk()
        if self.isHigherAndroid(desired_caps['platformVersion']) == True:
            logger.warn('hight android system, use uiautomator2')
            desired_caps['automationName'] = 'uiautomator2'

        logger.debug(desired_caps)
        with open('config.json', 'w') as f:
            json.dump(desired_caps, f)

    def runTestCase(self, isnoreset=False, ispertest = False):
        apkpath = self.getTestApk()
        # testpath = os.path.join(PROJECTPATH, 'testcases')
        logger.info(apkpath)
        self.my_androidhelper = AndroidHelper(apkpath)
        reportfile = os.path.join(PROJECTPATH, 'report', 'report.html')

        s = Server(isnoreset=isnoreset)
        s.start()
        desired_caps = self.inittest()
        logger.debug('ispertest: ' + str(ispertest))
        if ispertest:
            pertest = PerTest(PROCESSUINAME)
            pertest.startMon()

        logger.debug(self.testpath)
        discover = unittest.defaultTestLoader.discover(self.testpath, pattern='test*.py')

        with open(reportfile, 'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况：')
            runner.run(discover)
            if ispertest:
                runner.addPerdataToReport(pertest.cpu_aver, pertest.mem_aver, pertest.rx_total_mb, pertest.tx_total_mb)

        s.stop()

    def parseTestCase(self):
        pass

    def getTestApk(self):
        if os.path.isdir(APKPATH):
            for root, dirs, files in os.walk(APKPATH):
                return os.path.join(root, files[0])

    def isHigherAndroid(self, version):
        num = int(version[0])
        if num >= 7:
            return True
        else:
            return False
