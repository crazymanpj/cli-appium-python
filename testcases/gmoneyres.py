# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-12-17
# Author:  pangjian
from appiumobject import AppiumElement, AppiumObject, AppiumElement

class GMoneyRes(AppiumObject):

    #弹框
    #红包
    welcomtip = AppiumElement(id='com.cmcm.gamemoney:id/luckMoneyMiddle')
    welcomtip_close_btn = AppiumElement(id='com.cmcm.gamemoney:id/dismissBtn')

    #登录
    login_qqtype = AppiumElement(id='com.cmcm.gamemoney:id/qq_button')
    login_wxtype = AppiumElement(id='com.cmcm.gamemoney:id/wechat_button')
    qq_login_btn = AppiumElement(id='com.tencent.mobileqq:id/name')
    logout_btn = AppiumElement(id='com.cmcm.gamemoney:id/bottomButton')
    logout_confirm_btn = AppiumElement(id='com.cmcm.gamemoney:id/common_dialog_define_btn')
    getluckymoney_btn = AppiumElement(id='com.cmcm.gamemoney:id/btnGetLuckMoney')

    qqbtn_confirm = AppiumElement(xpath="//android.widget.Button[@text='登录']")
    qqbtn_confirm2 = AppiumElement(xpath="//android.widget.Button[@text='登 录']")

    #首页tab
    tab_game = AppiumElement(xpath="//android.widget.TextView[@text='游戏']")
    tab_task = AppiumElement(xpath="//android.widget.TextView[@text='任务']")
    tab_my = AppiumElement(xpath="//android.widget.TextView[@text='我的']")


    #我的页面
    withdraw_btn = AppiumElement(id='com.cmcm.gamemoney:id/withdrawBtn')
    invite_btn = AppiumElement(id='com.cmcm.gamemoney:id/inviteBtn')
    mall_btn = AppiumElement(id='com.cmcm.gamemoney:id/mallBtn')
    wallet_btn = AppiumElement(id='com.cmcm.gamemoney:id/walletBtn')

    my_account = AppiumElement(xpath="//android.widget.TextView[@text='账号管理']")

    #test游戏
    game_rich = AppiumElement(xpath="//android.widget.TextView[@text='小小首富']")
