# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-18
# Author:  pangjian
import subprocess

class Server():

    def __init__(self):
        self.IP = '127.0.0.1'
        self.port = '4723'
        self.deviceId = '26eda776'
        self.subp = None

    def start(self):
        #log 启动appium服务
        cmd = "appium -a %s -p %s -U %s --session-override"%(self.IP, self.port, self.deviceId)
        #log 启动appium服务成功
        self.subp = subprocess.Popen(cmd, shell=True)

    def stop(self):
        if self.subp is not None:
            #log 关闭appium服务
            self.subp.kill()
            #log 关闭appium服务成功

    def __del__(self):
        pass
        # self.stop()

if __name__ == '__main__':
    s = Server()
    s.start()
