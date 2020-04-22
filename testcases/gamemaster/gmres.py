# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-11-08
# Author:  pangjian
from appiumobject import AppiumElement,AppiumObject,AppiumElements

class GMRes(AppiumObject):
    #首页

    #欢迎tip
    welcomtip = AppiumElement(id='com.cmcm.gamemaster.main:id/guide_icon_iv')
    #首页tab
    tab_type='android.widget.RadioButton'
    tab_video = AppiumElement(xpath="//%s[@text='看视频']"%(tab_type))
    tab_live = AppiumElement(xpath="//%s[@text='看直播']"%(tab_type))
    tab_moment = AppiumElement(xpath="//%s[@text='社区']"%(tab_type))
    tab_my = AppiumElement(xpath="//%s[@text='我的']"%(tab_type))

    #社区
    #关注,星球，推荐
    moment_follow = AppiumElement(xpath="//android.widget.TextView[@text='关注']")
    moment_planet = AppiumElement(xpath="//android.widget.TextView[@text='星球']")
    moment_recommend = AppiumElement(xpath="//android.widget.TextView[@text='推荐']")
    #动态发布
    moment_publish = AppiumElement(id='com.cmcm.gamemaster.moment:id/iv_publish')
    moment_edittext = AppiumElement(id='com.cmcm.gamemaster.moment:id/et_moment_content')
    moment_publish_btn = AppiumElement(id='com.cmcm.gamemaster.moment:id/btn_publish')
    #默认图
    moment_empty = AppiumElement(id='com.cmcm.gamemaster.moment:id/iv_empty')
    #动态帖子列表
    moment_publish_list = AppiumElements(id='com.cmcm.gamemaster.moment:id/tv_user_publish_text')
    #我的社区
    moment_subtab = AppiumElement(xpath="//android.widget.TextView[@text='我的社区']")
    moment_m_publist = AppiumElements(id='com.cmcm.gamemaster.moment:id/feed_root_layout')
    #社区删除
    moment_delete = AppiumElement(id='com.cmcm.gamemaster.moment:id/iv_content_delete_self')
    moment_del_confirm = AppiumElement(id='com.cmcm.gamemaster.moment:id/btn_confirm_pos')

    #星球 星球列表名称
    planet_name = AppiumElement(id='com.cmcm.gamemaster.moment:id/tv_name')

    #推荐视频
    moment_rec_videos = AppiumElements(id='com.cmcm.gamemaster.moment:id/iv_outline')
    #推荐视频播放按钮
    moment_video_playbtn = AppiumElements(id='com.cmcm.gamemaster.moment:id/media_video_btn')

    #帐号系统
    #消息
    account_mail = AppiumElement(id='com.cmcm.gamemaster.account:id/account_image_user_mail')
    #背包
    account_package = AppiumElement(id='com.cmcm.gamemaster.account:id/image_account_package')
    #排行榜
    account_ranking = AppiumElement(id='com.cmcm.gamemaster.account:id/image_account_ranking_list')
    #升级
    account_uplevel = AppiumElement(id='com.cmcm.gamemaster.account:id/account_level_image')
    #抽奖
    account_lottery = AppiumElement(id='com.cmcm.gamemaster.account:id/account_lottery_image')
    #头像
    account_avatar = AppiumElement(id='com.cmcm.gamemaster.account:id/image_user_icon')
    #金币icon
    account_coin = AppiumElement(id='com.cmcm.gamemaster.account:id/account_coin_layout')
    #合力杀敌
    account_fight_btn = AppiumElement(id='com.cmcm.gamemaster.account:id/account_fight_button')
    #登录氪星
    account_login_btn = AppiumElement(id='com.cmcm.gamemaster.account:id/tv_begin_game')
    #qq登录,登录确认
    account_qq_loginbtn = AppiumElement(id='com.cmcm.gamemaster.account:id/qq_button')
    account_qqbtn_confirm = AppiumElement(xpath="//android.widget.Button[@text='登录']")
    account_qqbtn_confirm2 = AppiumElement(xpath="//android.widget.Button[@text='登 录']")

    #新版帐号系统
    accout_usertitle = AppiumElement(id='com.cmcm.gamemaster.account:id/account_user_layout')
    account_cointoday = AppiumElement(id='com.cmcm.gamemaster.account:id/account_task_coin_daily')
    account_cointotal = AppiumElement(id='com.cmcm.gamemaster.account:id/account_task_icon_total')
    account_package_n = AppiumElement(id='com.cmcm.gamemaster.account:id/task_package')
    account_fight_btn_n = AppiumElement(id='com.cmcm.gamemaster.account:id/task_team')
    account_money = AppiumElement(id='com.cmcm.gamemaster.account:id/task_money')
    account_mall = AppiumElement(id='com.cmcm.gamemaster.account:id/task_market')
    account_task_btn = AppiumElement(id='com.cmcm.gamemaster.account:id/task_goto')
    #新人红包弹窗关闭按钮
    account_newuserwin_closebtn = AppiumElement(id='com.cmcm.gamemaster.account:id/redpacket_close_btn')

    #设置
    setting_btn = AppiumElement(id='com.cmcm.gamemaster.main:id/setting_item_view')
    setting_logout_btn = AppiumElement(id='com.cmcm.gamemaster.main:id/account_logout_button')
    setting_logout_confirm = AppiumElement(id='com.cmcm.gamemaster.main:id/game_master_dialog_define_btn')
