# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-11-06
# Author:  pangjian
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from log import Log
logger = Log.get_logger(__name__)

LOCATOR_LIST = {
    'id' : By.ID,
    'xpath' : By.XPATH,
    'name' : By.NAME,
    'mclass' : By.CLASS_NAME,
    'css' : By.CSS_SELECTOR,
    'link_text' : By.LINK_TEXT,
    'partial_link_text' : By.PARTIAL_LINK_TEXT,
    'tag' : By.TAG_NAME,
}

class AppiumObject():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)


class AppiumElement():

    def __init__(self, **kwargs):
        self.m = By.ID
        self.value = ''

        for method, value in kwargs.items():
            self.m = LOCATOR_LIST[method]
            self.v = value

    def find(self, driver):
        try:
            element = driver.find_element(self.m, self.v)
            return element
        except NoSuchElementException as e:
            logger.warn('find element error')
            logger.warn(str(e))
            return False

    def __get__(self, instance, owner):
        return self.find(instance.driver)

class AppiumElements(AppiumElement):

    def find(self, driver):
        try:
            return driver.find_elements(self.m, self.v)
        except NoSuchElementException as e:
            logger.warn('find elements error')
            logger.warn(str(e))
            return False


if __name__=='__main__':
    driver = ''
