# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
import unittest,os,time

from testcases import appium_util,gamemaster_util
from testcases.testcasehelper import initAppium
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
# import appium_util,gamemaster_util
# from testcasehelper import initAppium


class CommonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = initAppium()


    def setUp(self):
        ID_WELCOME_TIP = "com.cmcm.gamemaster.main:id/guide_submit_iv"
        self.driver.find_element_by_id(ID_WELCOME_TIP).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(ID_WELCOME_TIP).click()
        self.driver.implicitly_wait(30)
        print('setup end')

    def dtest01_view_information_flow(self):
        time.sleep(5)
        print('start test01_view_information_flow')
        gamemaster_util.nav_shequ(self.driver)
        self.driver.implicitly_wait(30)
        print('start swipLeft')
        time.sleep(3)
        appium_util.swipLeft(self.driver)
        time.sleep(3)
        appium_util.swipeDown(self.driver)
        kj = None
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/comment_ly")
        except:
            pass
        print(kj)
        assert kj is not None
        kj = None
        print('start swipRight')
        appium_util.swipRight(self.driver)
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/tv_name")
        except Exception as e:
            pass
        assert kj is not None
        kj = None
        print('start swipRight')
        appium_util.swipRight(self.driver)
        self.driver.implicitly_wait(30)
        time.sleep(5)
        try:
            kj = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/iv_empty")
        except Exception as e:
            pass

        assert kj is not None

    def dtest02_publish(self):
        self.login()
        gamemaster_util.nav_shequ(self.driver)
        time.sleep(5)
        appium_util.swipRight(self.driver)
        time.sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/iv_publish").click()
        self.driver.implicitly_wait(30)
        editext = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/et_moment_content")
        print(editext)
        editext.send_keys('test')
        self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/btn_publish").click()
        time.sleep(3)
        publishtext = self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/tv_user_publish_text")[0]
        assert publishtext.text == "test"
        time.sleep(5)
        gamemaster_util.nav_my(self.driver)
        self.driver.implicitly_wait(30)
        appium_util.swipeUp(self.driver)
        time.sleep(5)
        gamemaster_util.nav_sub_shequ(self.driver)
        moment = self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/feed_root_layout")[0]
        appium_util.my_longpress(self.driver, moment)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/iv_content_delete_self").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/btn_confirm_pos").click()
        # moment = self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/feed_root_layout")[0]
        #判断元素不在或第一个元素text不是test



    def login(self):
        ID_QQ_LOGIN_TEXT = ['登录', '登 录']
        time.sleep(5)
        print('start test01_view_information_flow')
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.cmcm.gamemaster.account:id/tv_begin_game").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.cmcm.gamemaster.account:id/qq_button").click()
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        except NoSuchElementException as e:
            print('try other')
            self.driver.find_element_by_xpath("//android.widget.Button[@text='登 录']").click()
        self.driver.implicitly_wait(30)

    def logout(self):
        time.sleep(5)
        #log
        #sleep规范化
        gamemaster_util.nav_my(self.driver)
        time.sleep(3)
        self.driver.implicitly_wait(30)
        appium_util.swipeUp(self.driver)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('com.cmcm.gamemaster.main:id/setting_item_view').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('com.cmcm.gamemaster.main:id/account_logout_button').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('com.cmcm.gamemaster.main:id/game_master_dialog_define_btn').click()
        self.driver.implicitly_wait(30)


    def dtest03_videoplay(self):
        print('start')
        gamemaster_util.nav_shequ(self.driver)
        print('end')
        self.driver.implicitly_wait(30)
        time.sleep(3)
        appium_util.swipLeft(self.driver)
        print('start2')
        self.driver.implicitly_wait(30)
        videolist = self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/iv_outline")
        if videolist[0].is_displayed() == True:
            self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/media_video_btn")[0].click()
            time.sleep(10)
            self.driver.back()
        else:
            return False

    def dtest04_login_logout(self):
        self.login()
        time.sleep(5)
        self.logout()

    def test05_videotab(self):
        ID_TEXT = '看视频'
        gamemaster_util.nav_common(self.driver, ID_TEXT)
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
