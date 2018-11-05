# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
from appium.webdriver.common.touch_action import TouchAction

class AppiumUtil():

    def __init__(self, driver):
        self.d = driver

    def getSize(self):
        x = self.d.get_window_size()['width']
        y = self.d.get_window_size()['height']
        return (x, y)

    def swipeUp(self):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.85)
        y2 = int(l[1] * 0.25)
        self.d.swipe(x1, y1, x1, y2)

    #屏幕向下滑动
    def swipeDown(self):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.35)
        y2 = int(l[1] * 0.85)
        self.d.swipe(x1, y1, x1, y2)

    #屏幕向左滑动
    def swipLeft(self):
        l = self.getSize()
        x1 = int(l[0]*0.85)
        y1 = int(l[1]*0.15)
        x2 = int(l[0]*0.05)
        self.d.swipe(x1,y1,x2,y1)

    #屏幕向右滑动
    def swipRight(self):
        l = self.getSize()
        x1 = int(l[0]*0.05)
        y1 = int(l[1]*0.15)
        x2 = int(l[0]*0.99)
        self.d.swipe(x1,y1,x2,y1)

    def my_longpress(self, element):
        action1 = TouchAction(self.d)
        action1.long_press(element)
        action1.perform()
