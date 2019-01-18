# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import subprocess,time,os,requests,time
from adbhelper import AdbHelper
from log import Log
from const import SYSTEM

logger = Log.get_logger(__name__)


class Server(object):

    def __init__(self, isnoreset=False):
        self.my_adbhelper = AdbHelper()
        self.IP = '127.0.0.1'
        self.port = '4723'
        self.deviceId = self.my_adbhelper.getDeviceName()
        self.subp = None
        self.isnoreset = ''
        logger.debug('isnoreset: ' + str(isnoreset))
        if isnoreset:
            self.isnoreset = '--no-reset'

    def start(self):
        cmd = "appium -a %s -p %s -U %s --session-override %s"%(self.IP, self.port, self.deviceId, self.isnoreset)
        logger.debug(cmd)

        with open('myappiumserver.txt', 'w', encoding='utf-8') as f:
            self.subp = subprocess.Popen(cmd, shell=True, stdout=f)

        time.sleep(10)
        if self.isServerStartOk():
            logger.info('启动appium服务成功')
        else:
            logger.warn('启动appium失败，尝试杀进程')
            self.killNodePro()

    def killNodePro(self):
        if SYSTEM == 'Windows':
            cmd = 'taskkill /f /im node.exe'
        elif SYSTEM == 'Linux':
            cmd = 'killall -9 node'
        else:
            return False
        s = subprocess.Popen(cmd, shell=True)
        s.wait()
        s.kill()

    def stop(self):
        #windows
        self.killNodePro()
        if self.subp is not None:
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
    t = ''
    print('sfe%s'%(t))
