# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-23
# Author:  pangjian
from const import PLATFORMNAME, APKPATH
from androidhelper import AndroidHelper
import os,time,re
from log import Log
logger = Log.get_logger(__name__)

PROJECTPATH = os.getcwd()

class AdbHelper(object):

    def __init__(self):
        pass

    @classmethod
    def getPid(cls, packageName):
        cmd = 'adb shell ps | findstr ' + packageName
        text = os.popen(cmd).read()
        if len(text) == 0:
            return False
        return text.split()[1]

    @classmethod
    def getUid(cls, pid):
        if pid is False:
            return False
        cmd = 'adb shell cat /proc/%s/status'%(pid,)

        text = os.popen(cmd).readlines()
        if len(text) == 0:
            return False
        for i in text:
            if i.find('Uid') >=0:
                return i.split()[1]

        return False

    @classmethod
    def getDataUsage(cls, packageName):
        rx_bytes = 0
        tx_bytes = 0
        uid = cls.getUid(cls.getPid(packageName))
        if uid is False:
            return False
        cmd = 'adb shell cat /proc/net/xt_qtaguid/stats | findstr ' + uid
        text = os.popen(cmd).readlines()
        if len(text) == 0:
            return False

        for i in text:
            if i == '\n':
                continue
            logger.debug(i.split())
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

    @classmethod
    def screenShot(cls, savepath):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        os.popen("adb wait-for-device")
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        os.popen("adb pull /data/local/tmp/tmp.png " + os.path.join(savepath, timestamp + ".png"))
        os.popen("adb shell rm /data/local/tmp/tmp.png")

    @classmethod
    def getPssFromText(cls, text):
        pattern = '( +)(TOTAL)( +)(\d+)'
        m = re.match(pattern, text)
        return m.group(4)

    @classmethod
    def getMemory(cls, packageName):
        try:
            cmd = 'adb shell dumpsys meminfo ' + packageName
            text = os.popen(cmd).readlines()
            if len(text) == 0:
                return False
        for i in text:
            if i.find('TOTAL') >= 0:
                return cls.getPssFromText(i)
        except Exception as e:
            logger.debug(str(e))
            return False


    @classmethod
    def getCpu(cls, packageName):
        try:
        cmd = 'adb shell top -n 1 | findstr /E ' + packageName
        text = os.popen(cmd).readlines()
        if len(text) == 0:
            return False
        return text[0].split()[2]
        except Exception as e:
            logger.debug(str(e))
            return False

if __name__ == '__main__':
    a =AdbHelper()
    print(a.getPhoneResolution())
