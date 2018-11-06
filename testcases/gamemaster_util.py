# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-26
# Author:  pangjian
from appium_util import AppiumUtil
import time
from selenium.common.exceptions import NoSuchElementException
from log import Log
logger = Log.get_logger(__name__)

def nav_shequ(d):
    d.find_element_by_xpath("//android.widget.RadioButton[@text='社区']").click()

def nav_my(d):
    d.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()

def nav_sub_shequ(d):
    d.find_element_by_xpath("//android.widget.TextView[@text='我的社区']").click()

def nav_common(d, navtext):
    xpath_text = "//android.widget.RadioButton[@text='%s']"%(navtext)
    d.find_element_by_xpath(xpath_text).click()

def login(d):
    ID_QQ_LOGIN_TEXT = ['登录', '登 录']
    time.sleep(5)
    d.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()
    time.sleep(5)
    d.implicitly_wait(30)
    d.find_element_by_id("com.cmcm.gamemaster.account:id/tv_begin_game").click()
    d.implicitly_wait(30)
    d.find_element_by_id("com.cmcm.gamemaster.account:id/qq_button").click()
    d.implicitly_wait(30)
    try:
        d.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
    except NoSuchElementException as e:
        print('try other')
        d.find_element_by_xpath("//android.widget.Button[@text='登 录']").click()
        d.implicitly_wait(30)

def logout(d):
    myappiumutil = AppiumUtil(d)
    time.sleep(5)
    #log
    #sleep规范化
    nav_my(d)
    time.sleep(3)
    d.implicitly_wait(30)
    myappiumutil.swipeUp()
    d.implicitly_wait(30)
    d.find_element_by_id('com.cmcm.gamemaster.main:id/setting_item_view').click()
    d.implicitly_wait(30)
    d.find_element_by_id('com.cmcm.gamemaster.main:id/account_logout_button').click()
    d.implicitly_wait(30)
    d.find_element_by_id('com.cmcm.gamemaster.main:id/game_master_dialog_define_btn').click()
    d.implicitly_wait(30)

def islogin(d):
    ID_FIGHT_BUTTON = 'com.cmcm.gamemaster.account:id/account_fight_button'
    nav_my(d)
    try:
        fight = d.find_element_by_id(ID_FIGHT_BUTTON)
        if fight:
            logger.info('已登录')
            return True
        else:
            logger.info('未登录')
            return False
    except NoSuchElementException as e:
        logger.info(str(e))
        logger.info('异常，未登录')
        return False
