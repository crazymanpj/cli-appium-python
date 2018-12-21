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
        initLogcat()
        self.gmoneyres = GMoneyRes(self.driver)
        self.appiumutil = AppiumUtil(self.driver)

        try:
            if self.gmoneyres.welcomtip:
                self.gmoneyres.welcomtip_close_btn.click()
        except NoSuchElementException as e:
            logger.info('can not find hongbao tip, skip')
            return True

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    @capture
    def test01_login_logout(self):
        self.gmoneyres.tab_my.click()
        self.gmoneyres.login_qqtype.click()
        self.gmoneyres.qqbtn_confirm.click()
        verifyElement(self.gmoneyres.withdraw_btn)

        time.sleep(3)
        self.appiumutil.swipeUp()
        self.gmoneyres.my_account.click()
        self.gmoneyres.logout_btn.click()
        self.gmoneyres.logout_confirm_btn.click()
        verifyElement(self.gmoneyres.getluckymoney_btn)
