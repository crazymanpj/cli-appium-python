# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import subprocess,time,os,requests,time
from adbhelper import AdbHelper
from log import Log

logger = Log.get_logger(__name__)

class Server(object):

    def __init__(self, isnoreset=False):
        self.my_adbhelper = AdbHelper()
        self.IP = '127.0.0.1'
        self.port = '4723'
        self.deviceId = self.my_adbhelper.getDeviceName()
        self.subp = None
        self.isnoreset = ''
        logger.info('isnoreset: ' + str(isnoreset))
        if isnoreset:
            self.isnoreset = '--no-reset'

    def start(self):
        logger.info('启动appium服务')
        cmd = "appium -a %s -p %s -U %s --session-override %s"%(self.IP, self.port, self.deviceId, self.isnoreset)
        logger.info(cmd)

        with open('myappiumserver.txt', 'w') as f:
            self.subp = subprocess.Popen(cmd, shell=True, stdout=f)

        time.sleep(10)
        if self.isServerStartOk():
            logger.info('启动appium服务成功')
        else:
            logger.warn('启动appium失败，尝试杀进程')
            self.killNodePro()

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

    def isServerStartOk(self):
        ret = False
        url = 'http://localhost:4723/wd/hub/status'
        try:
            ret = requests.get(url)
        except Exception as e:
            return False
        if ret:
            return True
        else:
            return False

    def __del__(self):
        pass
        # self.stop()

if __name__ == '__main__':
    s = Server()
    s.start()
