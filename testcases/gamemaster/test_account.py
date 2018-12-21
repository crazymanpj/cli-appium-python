# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-11-01
# Author:  pangjian
import time
import unittest
from testcases.gamemaster import gamemaster_util
from gmres import GMRes
from testcasehelper import initAppium, initLogcat, capture
from selenium.common.exceptions import NoSuchElementException
from log import Log
logger = Log.get_logger(__name__)


class AccountTest(unittest.TestCase):
    IS_DEBUG = False

    def setUp(self):
        self.driver = initAppium()
        initLogcat()
        self.gmres = GMRes(self.driver)

        time.sleep(10)
        try:
            for i in range(2):
                if self.gmres.welcomtip:
                    self.gmres.welcomtip.click()
        except NoSuchElementException as e:
            logger.warning('can not find welcome tip, skip')
            return True

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    @capture
    def test01_traver(self):
        account_elements = []

        if gamemaster_util.islogin(self.gmres) is False:
            logger.debug('need login...')
            gamemaster_util.login(self.gmres)

        if self.gmres.account_task_btn is False:
            account_elements.extend([self.gmres.account_mail, self.gmres.account_package])
            account_elements.extend([self.gmres.account_ranking, self.gmres.account_coin])
        else:
            account_elements.extend([self.gmres.accout_usertitle, self.gmres.account_cointoday, self.gmres.account_cointotal])
            account_elements.extend([self.gmres.account_package_n, self.gmres.account_fight_btn_n, self.gmres.account_money])
            # account_elements.extend([self.gmres.account_mail, self.gmres.account_task_btn])

        for i in account_elements:
            i.click()
            time.sleep(3)
            self.driver.back()


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
