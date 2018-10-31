# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import subprocess,time,os
from adbhelper import AdbHelper
from log import Log

logger = Log.get_logger()

class Server(object):

    def __init__(self):
        self.my_adbhelper = AdbHelper()
        self.IP = '127.0.0.1'
        self.port = '4723'
        self.deviceId = self.my_adbhelper.getDeviceName()
        self.subp = None

    def start(self):
        logger.info('启动appium服务')
        cmd = "appium -a %s -p %s -U %s --session-override"%(self.IP, self.port, self.deviceId)
        logger.info('启动appium服务成功')
        with open('myappiumserver.txt', 'w') as f:
            self.subp = subprocess.Popen(cmd, shell=True, stdout=f)

    def killNodePro(self):
        cmd = 'taskkill /f /im node.exe'
        s = subprocess.Popen(cmd, shell=True)
        s.wait()
        s.kill()

    def stop(self):
        print('stop')
        #windows
        self.killNodePro()
        if self.subp is not None:
            logger.info('关闭appium服务')
            self.subp.kill()
            logger.info('关闭appium服务成功')

    def __del__(self):
        pass
        # self.stop()

if __name__ == '__main__':
    s = Server()
    s.start()
