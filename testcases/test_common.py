# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
import unittest,os,time
from appium_util import AppiumUtil
from gmres import GMRes
from testcases import gamemaster_util
from testcases.testcasehelper import initAppium, verifyElement, initLogcat
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
        initLogcat()
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
        myappiumutil.swipLeft()
        myappiumutil.swipeDown()
        verifyElement(self.gmres.moment_rec_videos[0])
        myappiumutil.swipRight()
        verifyElement(self.gmres.planet_name)
        myappiumutil.swipRight()
        verifyElement(self.gmres.moment_empty)


    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test02_publish(self):
        myappiumutil = AppiumUtil(self.driver)
        if gamemaster_util.islogin(self.gmres) is False:
            logger.info('need login...')
            gamemaster_util.login(self.gmres)

        self.gmres.tab_moment.click()
        self.gmres.moment_follow.click()
        self.gmres.moment_publish.click()
        self.gmres.moment_edittext.send_keys('test')
        self.gmres.moment_publish_btn.click()
        publishtext = self.gmres.moment_publish_list[0]
        assert publishtext.text == "test"
        self.gmres.tab_my.click()
        myappiumutil.swipeUp()
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
        if gamemaster_util.islogin(self.gmres):
            gamemaster_util.logout(self.gmres, self.driver)
        gamemaster_util.login(self.gmres)
        gamemaster_util.logout(self.gmres, self.driver)

    @unittest.skipIf(IS_DEBUG==True, u'debug模式跳过')
    def test05_videotab(self):
        self.gmres.tab_video.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
