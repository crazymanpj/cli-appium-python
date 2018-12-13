# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-12-10
# Author:  pangjian
import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

class MyMonkeyRunner():

    def __init__(self, configfile):
        self.splitsymbol = '*'
        self.cordlist = []
        self.configfile = configfile
        # self.device = MonkeyRunner.waitForConnection()


    def parse(self):
        f = open(self.configfile)
        for i in f.readlines():
            ret = i.split(self.splitsymbol)
            item = (int(ret[0]), int(ret[1]))
            self.cordlist.append(item)
        f.close()

    def run(self):
        self.parse()
        self.device = MonkeyRunner.waitForConnection()
        ret = self.device.startActivity(component='com.cmcm.gamemaster/com.cm.game.launcher.ui.main.GameMainActivity')
        time.sleep(5)
        print(self.cordlist)
        for i in self.cordlist:
            print(i[0])
            self.device.touch(i[0], i[1],  'DOWN_AND_UP')
            time.sleep(1)


if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print('need configfile')
        sys.exit(0)

    m = MyMonkeyRunner(sys.argv[1])
    m.run()
