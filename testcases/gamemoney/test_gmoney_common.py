# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-12-17
# Author:  pangjian
import unittest,time
from testcasehelper import initAppium, verifyElement, initLogcat, capture
from gmoneyres import GMoneyRes
from selenium.common.exceptions import NoSuchElementException
from appium_util import AppiumUtil
from log import Log
logger = Log.get_logger(__name__)

class CommonTest(unittest.TestCase):
    IS_DEBUG = False

    def setUp(self):
        self.driver = initAppium()
        # initLogcat()
        self.GMR = GMoneyRes(self.driver)
        self.appiumutil = AppiumUtil(self.driver)

        try:
            if self.GMR.welcomtip:
                self.driver.back()
                # self.GMR.welcomtip_close_btn.click()
        except NoSuchElementException as e:
            logger.info('can not find hongbao tip, skip')
            return True

    def login(self):
        self.GMR.tab_my.click()
        self.GMR.mytitle.click()
        # self.GMR.other_login_btn.click()
        self.GMR.login_qqtype.click()

        if self.GMR.qqbtn_confirm is not False:
            self.GMR.qqbtn_confirm.click()
        elif self.GMR.qqbtn_confirm2 is not False:
            self.GMR.qqbtn_confirm2.click()
        else:
            logger.info('错误，找不到qq登录button')

        if self.GMR.invite_friends:
            self.GMR.invite_friends_closebtn.click()


    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    @capture
    def test01_login_logout(self):
        self.login()
        verifyElement(self.GMR.withdraw_btn)

        time.sleep(2)
        self.appiumutil.swipeUp()
        self.GMR.my_account.click()
        self.GMR.logout_btn.click()
        self.GMR.logout_confirm_btn.click()
        verifyElement(self.GMR.invite_btn)

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    @capture
    def test02_primary_click(self):
        self.login()

        self.GMR.mytitle.click()
        verifyElement(self.GMR.account_bottombtn)
        self.driver.back()

        self.GMR.withdraw_btn.click()
        verifyElement(self.GMR.withdraw_commitbtn)
        self.driver.back()

        self.GMR.invite_btn.click()
        verifyElement(self.GMR.invite_page)
        self.driver.back()

        # self.GMR.mall_btn.click()
        # verifyElement(self.GMR.mall_page)
        # self.driver.back()

        self.GMR.wallet_btn.click()
        verifyElement(self.GMR.wallet_getcash)
        self.driver.back()
