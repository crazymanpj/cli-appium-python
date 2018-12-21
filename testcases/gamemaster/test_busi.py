# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-30
# Author:  pangjian
import unittest
from testcasehelper import initAppium

class BusiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = initAppium()

    def dtest(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
