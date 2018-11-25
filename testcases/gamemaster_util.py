# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-26
# Author:  pangjian
from appium_util import AppiumUtil
import time
from selenium.common.exceptions import NoSuchElementException
from log import Log
logger = Log.get_logger(__name__)

def login(gmres):
    gmres.tab_my.click()
    gmres.account_login_btn.click()
    gmres.account_qq_loginbtn.click()

    if gmres.account_qqbtn_confirm is not False:
        gmres.account_qqbtn_confirm.click()
    elif gmres.account_qqbtn_confirm2 is not False:
        gmres.account_qqbtn_confirm2.click()
    else:
        logger.info('错误，找不到登录button')

def logout(gmres, d):
    myappiumutil = AppiumUtil(d)
    gmres.tab_my.click()
    time.sleep(3)
    myappiumutil.swipeUp()
    time.sleep(3)
    gmres.setting_btn.click()
    gmres.setting_logout_btn.click()
    gmres.setting_logout_confirm.click()


def islogin(gmres):
    gmres.tab_my.click()
    if gmres.account_newuserwin_closebtn:
        gmres.account_newuserwin_closebtn.click()

    try:
        if gmres.account_login_btn:
            logger.info('未登录')
            return False
        else:
            logger.info('已登录')
            return True
    except NoSuchElementException as e:
        logger.info(str(e))
        logger.info('异常，未登录')
        return False
