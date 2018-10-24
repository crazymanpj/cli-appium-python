# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-23
# Author:  pangjian
from const import PLATFORMNAME, APKPATH
from androidhelper import AndroidHelper
import os

PROJECTPATH = os.getcwd()
print(PROJECTPATH)

class AdbHelper(object):

    def __init__(self):
        pass

    def getPid(self, packageName):
        cmd = 'adb shell ps | findstr ' + packageName
        text = os.popen(cmd).read()
        return text.split()[1]

    def getUid(self, pid):
        cmd = 'adb shell cat /proc/%s/status'%(pid,)
        text = os.popen(cmd).readlines()
        for i in text:
            if i.find('Uid') >=0:
                return i.split()[1]

        return None

    def getDataUsage(self, packageName):
        rx_bytes = 0
        tx_bytes = 0
        uid = self.getUid(self.getPid(packageName))
        cmd = 'adb shell cat /proc/net/xt_qtaguid/stats | findstr ' + uid
        text = os.popen(cmd).readlines()
        for i in text:
            rx_bytes = rx_bytes + int(i.split()[5])
            tx_bytes = tx_bytes + int(i.split()[7])

        return rx_bytes,tx_bytes

    def getPlatformName(self):
        return PLATFORMNAME

    def getPlatformVersion(self):
        cmd = 'adb shell getprop ro.build.version.release'
        return os.popen(cmd).read().strip('\n')

    def getDeviceName(self):
        cmd = 'adb get-serialno'
        # cmd2 = 'adb shell getprop ro.serialno'
        return os.popen(cmd).read().strip('\n')

    def getMobilePhoneModel(self):
        cmd = 'adb -d shell getprop ro.product.model'
        return os.popen(cmd).read().strip('\n')

    def getPhoneResolution(self):
        cmd = 'adb shell "dumpsys window | grep mUnrestrictedScreen"'
        return os.popen(cmd).read().split()[1]

if __name__ == '__main__':
    a =AdbHelper()
    print(a.getPhoneResolution())
