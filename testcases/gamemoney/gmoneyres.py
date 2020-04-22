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
    invite_friends = AppiumElement(id='com.cmcm.gamemoney:id/dialogAnimView')
    invite_friends_closebtn = AppiumElement(id='com.cmcm.gamemoney:id/closeBtnAnimView')

    #帐号管理button
    account_bottombtn = AppiumElement(id='com.cmcm.gamemoney:id/bottomButton')
    #提现页面
    withdraw_commitbtn = AppiumElement(id='com.cmcm.gamemoney:id/submitBtn')
    #邀请好友页面
    invite_page = AppiumElement(id='com.cmcm.gamemoney:id/web_view_new_friend_pull')
    #商城页面
    mall_page = AppiumElement(id='com.cmcm.gamemoney:id/web_root_view')
    #我的钱包页面
    wallet_getcash = AppiumElement(id='com.cmcm.gamemoney:id/getCashBtn')

    #登录
    login_qqtype = AppiumElement(id='com.cmcm.gamemoney:id/qq_button')
    login_wxtype = AppiumElement(id='com.cmcm.gamemoney:id/wechat_button')
    qq_login_btn = AppiumElement(id='com.tencent.mobileqq:id/name')
    logout_btn = AppiumElement(id='com.cmcm.gamemoney:id/bottomButton')
    logout_confirm_btn = AppiumElement(id='com.cmcm.gamemoney:id/common_dialog_cancel_btn')
    logout_cancel_btn = AppiumElement(id='com.cmcm.gamemoney:id/common_dialog_define_btn')
    getluckymoney_btn = AppiumElement(id='com.cmcm.gamemoney:id/btnGetLuckMoney')

    qqbtn_confirm = AppiumElement(xpath="//android.widget.Button[@text='登录']")
    qqbtn_confirm2 = AppiumElement(xpath="//android.widget.Button[@text='登 录']")

    #首页tab
    tab_game = AppiumElement(xpath="//android.widget.TextView[@text='游戏']")
    tab_task = AppiumElement(xpath="//android.widget.TextView[@text='任务']")
    tab_my = AppiumElement(xpath="//android.widget.TextView[@text='我的']")


    #我的页面
    myicon = AppiumElement(id='com.cmcm.gamemoney:id/avatarIv')
    mytitle = AppiumElement(id='com.cmcm.gamemoney:id/nicknameTv')
    wx_login_btn = AppiumElement(id='com.cmcm.gamemoney:id/newWechatLoginButton')
    other_login_btn = AppiumElement(id='com.cmcm.gamemoney:id/tvOtherLoginWay')
    qq_login_btn = AppiumElement(id='com.cmcm.gamemoney:id/qq_button')
    withdraw_btn = AppiumElement(id='com.cmcm.gamemoney:id/withdrawBtn')
    invite_btn = AppiumElement(id='com.cmcm.gamemoney:id/inviteBtn')
    mall_btn = AppiumElement(id='com.cmcm.gamemoney:id/mallBtn')
    wallet_btn = AppiumElement(id='com.cmcm.gamemoney:id/walletBtn')

    task_center = AppiumElement(xpath="//android.widget.TextView[@text='任务中心']")
    friend_hongbao = AppiumElement(xpath="//android.widget.TextView[@text='好友红包']")
    my_account = AppiumElement(xpath="//android.widget.TextView[@text='账号管理']")
    feedback = AppiumElement(xpath="//android.widget.TextView[@text='帮助反馈']")
    update_btn = AppiumElement(xpath="//android.widget.TextView[@text='检查更新']")
    about = AppiumElement(xpath="//android.widget.TextView[@text='关于我们']")
