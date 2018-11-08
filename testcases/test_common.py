# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
import unittest,os,time
from appium_util import AppiumUtil
from gmres import GMRes
from testcases import gamemaster_util
from testcases.testcasehelper import initAppium, virifyElement
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from log import Log
logger = Log.get_logger(__name__)
# import appium_util,gamemaster_util
# from testcasehelper import initAppium

class CommonTest(unittest.TestCase):
    IS_DEBUG = False

    def setUp(self):
        self.driver = initAppium()
        self.gmres = GMRes(self.driver)
        try:
            for i in range(2):
                self.gmres.welcomtip.click()
            logger.info('setup end')
        except NoSuchElementException as e:
            logger.info('can not find welcome tip, skip')
            return True

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test01_view_information_flow(self):
        myappiumutil = AppiumUtil(self.driver)
        self.gmres.tab_moment.click()
        time.sleep(3)
        myappiumutil.swipLeft()
        time.sleep(3)
        myappiumutil.swipeDown()
        kj = None
        time.sleep(3)
        virifyElement(self.gmres.moment_rec_videos[0])

        kj = None
        myappiumutil.swipRight()
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/tv_name")
        except Exception as e:
            pass
        assert kj is not None
        kj = None
        myappiumutil.swipRight()
        time.sleep(5)
        try:
            kj = self.driver.find_element_by_id("com.cmcm.gamemaster.moment:id/iv_empty")
        except Exception as e:
            pass

        assert kj is not None

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test02_publish(self):
        myappiumutil = AppiumUtil(self.driver)
        if gamemaster_util.islogin(self.driver) is False:
            logger.info('need login...')
            gamemaster_util.login(self.driver)

        self.gmres.tab_moment.click()
        self.gmres.moment_follow.click()
        self.gmres.moment_publish.click()
        self.gmres.moment_edittext.send_keys('test')
        self.gmres.moment_publish_btn.click()
        publishtext = self.gmres.moment_publish_list[0]
        assert publishtext.text == "test"
        self.gmres.tab_my.click()
        myappiumutil.swipeUp()
        time.sleep(3)
        self.gmres.moment_subtab.click()
        moment = self.gmres.moment_m_publist[0]
        myappiumutil.my_longpress(moment)
        self.gmres.moment_delete.click()
        self.gmres.moment_del_confirm.click()
        # moment = self.driver.find_elements_by_id("com.cmcm.gamemaster.moment:id/feed_root_layout")[0]
        #判断元素不在或第一个元素text不是test

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test03_videoplay(self):
        myappiumutil = AppiumUtil(self.driver)
        self.gmres.tab_moment.click()
        time.sleep(3)
        myappiumutil.swipLeft()
        videolist = self.gmres.moment_rec_videos
        if videolist[0].is_displayed() == True:
            video_playbtns = self.gmres.moment_video_playbtn
            video_playbtns[0].click()
            time.sleep(10)
            self.driver.back()
        else:
            return False

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test04_login_logout(self):
        if gamemaster_util.islogin(self.driver):
            gamemaster_util.logout(self.driver)
        time.sleep(3)
        gamemaster_util.login(self.driver)
        time.sleep(5)
        gamemaster_util.logout(self.driver)

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test05_videotab(self):
        self.gmres.tab_video.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
