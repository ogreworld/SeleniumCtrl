#!/usr/bin/env python
# -*- coding: UTF-8 -*

###############################################################################
# Copyright (C), 2013, TP-LINK Technologies Co., Ltd.
#
# Firename   : quick_setup_tlwr740n_v5_like.py
# Version    : 1.0.0
# Description: Module for TP-LINK access control.
# Author     : libo
# History:
#   1. 2013-6-7, libo, first created. 
###############################################################################

from ...lib.config_constant import ConfigConstant
from ...lib.xpath_parser import Widget
from ...lib.widget_constant import WidgetConstant
from widget_base import WidgetBase


class QuickSetupWidget(WidgetBase):
    
    QS_SETTING_START_URL         = 'userRpm/WzdStartRpm.htm'
    QS_SETTING_WAN_TYPE_URL      = 'userRpm/WzdWanTypeRpm.htm'
    QS_SETTING_WAN_MAC_CLONE_URL = 'userRpm/WzdWanMacRpm.htm'
    QS_SETTING_WAN_STATIC_URL    = 'userRpm/WzdStaticIpRpm.htm'
    QS_SETTING_WAN_PPPOE_URL     = 'userRpm/WzdPPPoERpm.htm'
    QS_SETTING_WLAN_URL          = 'userRpm/WzdWlanRpm.htm'
    QS_SETTING_END_URL           = 'userRpm/WzdEndRpm.htm'
    
    def __init__(self):
    
        self.QS_SETTING_URL_PAGE_DICT = {self.QS_SETTING_START_URL:WidgetConstant.QS_SETTING_START_PAGE,
                                         self.QS_SETTING_WAN_TYPE_URL:WidgetConstant.QS_SETTING_WAN_TYPE_PAGE,
                                         self.QS_SETTING_WAN_MAC_CLONE_URL:WidgetConstant.QS_SETTING_WAN_MAC_CLONE_PAGE,
                                         self.QS_SETTING_WAN_STATIC_URL:WidgetConstant.QS_SETTING_WAN_STATIC_PAGE,
                                         self.QS_SETTING_WAN_PPPOE_URL:WidgetConstant.QS_SETTING_WAN_PPPOE_PAGE,
                                         self.QS_SETTING_WLAN_URL:WidgetConstant.QS_SETTING_WLAN_PAGE,
                                         self.QS_SETTING_END_URL:WidgetConstant.QS_SETTING_END_PAGE}
        
        ## Quick Setup Link
        self.QS_SETTING_LINK = Widget(name='QS_SETTING_LINK',
                                 xpath="//a[@href='/userRpm/WzdStartRpm.htm']",
                                 type=ConfigConstant.WIDGET_TYPE_LINK,
                                 frame='bottomLeftFrame')


        ## Quick Setup Start
        self.QS_SETTING_START_NEXT = Widget(name='QS_SETTING_START_NEXT',
                                       xpath="//input[@name='Next']",
                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                       frame='mainFrame',
                                       belongs={'QS_SETTING_LINK':None},
                                       url=self.QS_SETTING_START_URL,
                                       save_button=True)


        ## Quick Setup Wan
        # wan type
        self.QS_SETTING_WAN_TYPE_AUTO = Widget(name='QS_SETTING_WAN_TYPE_AUTO',
                                          xpath="//input[@name='wan' and @value='16']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL,
                                          )
        self.QS_SETTING_WAN_TYPE_STATIC = Widget(name='QS_SETTING_WAN_TYPE_STATIC',
                                          xpath="//input[@name='wan' and @value='1']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL)
        self.QS_SETTING_WAN_TYPE_DYNAMIC = Widget(name='QS_SETTING_WAN_TYPE_DYNAMIC',
                                          xpath="//input[@name='wan' and @value='0']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL,
                                          default_value=True)
        self.QS_SETTING_WAN_TYPE_PPPOE = Widget(name='QS_SETTING_WAN_TYPE_PPPOE',
                                          xpath="//input[@name='wan' and @value='2']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL)
        self.QS_SETTING_WAN_TYPE_L2TP = Widget(name='QS_SETTING_WAN_TYPE_L2TP',
                                          xpath="//input[@name='wan' and @value='5']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL)
        self.QS_SETTING_WAN_TYPE_PPTP = Widget(name='QS_SETTING_WAN_TYPE_PPTP',
                                          xpath="//input[@name='wan' and @value='6']",
                                          type=ConfigConstant.WIDGET_TYPE_RADIO,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL)
        self.QS_SETTING_WAN_TYPE_NEXT = Widget(name='QS_SETTING_WAN_TYPE_NEXT',
                                          xpath="//input[@name='Next']",
                                          type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL,
                                          save_button=True)
        self.QS_SETTING_WAN_TYPE_BACK = Widget(name='QS_SETTING_WAN_TYPE_BACK',
                                          xpath="//input[@name='Return']",
                                          type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                          frame='mainFrame',
                                          belongs={'QS_SETTING_START_NEXT':None},
                                          url=self.QS_SETTING_WAN_TYPE_URL)

        # wan static
        self.QS_SETTING_WAN_STATIC_IP      = Widget(name='QS_SETTING_WAN_STATIC_IP',
                                               xpath="//input[@name='wanip']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
        self.QS_SETTING_WAN_STATIC_MASK    = Widget(name='QS_SETTING_WAN_STATIC_MASK',
                                               xpath="//input[@name='wanmask']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
        self.QS_SETTING_WAN_STATIC_GATEWAY = Widget(name='QS_SETTING_WAN_STATIC_GATEWAY',
                                               xpath="//input[@name='gateway']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
        self.QS_SETTING_WAN_STATIC_DNS1    = Widget(name='QS_SETTING_WAN_STATIC_DNS1',
                                               xpath="//input[@name='dnsserver']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
        self.QS_SETTING_WAN_STATIC_DNS2    = Widget(name='QS_SETTING_WAN_STATIC_DNS2',
                                               xpath="//input[@name='dnsserver2']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
        self.QS_SETTING_WAN_STATIC_NEXT    = Widget(name='QS_SETTING_WAN_STATIC_NEXT',
                                               xpath="//input[@name='Next']",
                                               type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL,
                                               save_button=True)
        self.QS_SETTING_WAN_STATIC_BACK    = Widget(name='QS_SETTING_WAN_STATIC_BACK',
                                               xpath="//input[@name='Return']",
                                               type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 'QS_SETTING_WAN_TYPE_STATIC':True},
                                               url=self.QS_SETTING_WAN_STATIC_URL)
                             
        # wan pppoe
        self.QS_SETTING_WAN_PPPOE_USERNAME         = Widget(name='QS_SETTING_WAN_PPPOE_USERNAME',
                                                       xpath="//input[@name='acc']",
                                                       type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 
                                                                'QS_SETTING_WAN_TYPE_PPPOE':True},
                                                       url=self.QS_SETTING_WAN_PPPOE_URL)
        self.QS_SETTING_WAN_PPPOE_PASSWORD         = Widget(name='QS_SETTING_WAN_PPPOE_PASSWORD',
                                                       xpath="//input[@name='psw']",
                                                       type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 
                                                                'QS_SETTING_WAN_TYPE_PPPOE':True},
                                                       url=self.QS_SETTING_WAN_PPPOE_URL)
        self.QS_SETTING_WAN_PPPOE_PASSWORD_CONFIRM = Widget(name='QS_SETTING_WAN_PPPOE_PASSWORD_CONFIRM',
                                                       xpath="//input[@name='confirm']",
                                                       type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 
                                                                'QS_SETTING_WAN_TYPE_PPPOE':True},
                                                       url=self.QS_SETTING_WAN_PPPOE_URL)
        self.QS_SETTING_WAN_PPPOE_NEXT             = Widget(name='QS_SETTING_WAN_PPPOE_NEXT',
                                                       xpath="//input[@name='Next']",
                                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 
                                                                'QS_SETTING_WAN_TYPE_PPPOE':True},
                                                       url=self.QS_SETTING_WAN_PPPOE_URL,
                                                       save_button=True)
        self.QS_SETTING_WAN_PPPOE_BACK             = Widget(name='QS_SETTING_WAN_PPPOE_BACK',
                                                       xpath="//input[@name='Return']",
                                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None, 
                                                                'QS_SETTING_WAN_TYPE_PPPOE':True},
                                                       url=self.QS_SETTING_WAN_PPPOE_URL)
                             
        # wan mac clone
        self.QS_SETTING_WAN_MAC_CLONE_YES        = Widget(name='QS_SETTING_WAN_MAC_CLONE_YES',
                                                  xpath="//input[@name='is_need_clone' and @value='0']",
                                                  type=ConfigConstant.WIDGET_TYPE_RADIO,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL,
                                                  default_value=True)
        self.QS_SETTING_WAN_MAC_CLONE_NO         = Widget(name='QS_SETTING_WAN_MAC_CLONE_NO',
                                                  xpath="//input[@name='is_need_clone' and @value='1']",
                                                  type=ConfigConstant.WIDGET_TYPE_RADIO,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL,
                                                  default_value=True)                                          
        self.QS_SETTING_WAN_MAC_CLONE_WAN_MAC    = Widget(name='QS_SETTING_WAN_MAC_CLONE_WAN_MAC',
                                                  xpath="//input[@name='wan_mac']",
                                                  type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL)
        self.QS_SETTING_WAN_MAC_CLONE_PC_MAC    = Widget(name='QS_SETTING_WAN_MAC_CLONE_PC_MAC',
                                                  xpath="//input[@name='pc_mac']",
                                                  type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL)                                                           
        self.QS_SETTING_WAN_MAC_CLONE_RESTORE   = Widget(name='QS_SETTING_WAN_MAC_CLONE_RESTORE',
                                                  xpath="//input[@id='restore']",
                                                  type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL)         
        self.QS_SETTING_WAN_MAC_CLONE_CLONE     = Widget(name='QS_SETTING_WAN_MAC_CLONE_CLONE',
                                                  xpath="//input[@id='clone']",
                                                  type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                  frame='mainFrame',
                                                  belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                           'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                  url=self.QS_SETTING_WAN_MAC_CLONE_URL)         
        self.QS_SETTING_WAN_MAC_CLONE_NEXT      = Widget(name='QS_SETTING_WAN_MAC_CLONE_NEXT',
                                                       xpath="//input[@name='Next']",
                                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                                'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                       url=self.QS_SETTING_WAN_MAC_CLONE_URL,
                                                       save_button=True)
        self.QS_SETTING_WAN_MAC_CLONE_BACK      = Widget(name='QS_SETTING_WAN_MAC_CLONE_BACK',
                                                       xpath="//input[@name='Return']",
                                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                                       frame='mainFrame',
                                                       belongs={'QS_SETTING_WAN_TYPE_NEXT':None,
                                                                'QS_SETTING_WAN_TYPE_DYNAMIC':None},
                                                       url=self.QS_SETTING_WAN_MAC_CLONE_URL)
                   

        ## Quick Setup Wlan
        self.QS_SETTING_WLAN_STATUS        = Widget(name='QS_SETTING_WLAN_STATUS',
                                               xpath="//input[@name='ap']",
                                               type=ConfigConstant.WIDGET_TYPE_CHECK_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_SSID          = Widget(name='QS_SETTING_WLAN_SSID',
                                               xpath="//input[@id='ssid']",
                                               type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_REGION        = Widget(name='QS_SETTING_WLAN_REGION',
                                               xpath="//input[@name='region']",
                                               type=ConfigConstant.WIDGET_TYPE_MANU,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_CHANNEL       = Widget(name='QS_SETTING_WLAN_CHANNEL',
                                               xpath="//input[@name='channel']",
                                               type=ConfigConstant.WIDGET_TYPE_MANU,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_MODE          = Widget(name='QS_SETTING_WLAN_MODE',
                                               xpath="//input[@name='mode']",
                                               type=ConfigConstant.WIDGET_TYPE_MANU,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_BANDWIDTH     = Widget(name='QS_SETTING_WLAN_BANDWIDTH',
                                               xpath="//input[@name='chanWidth']",
                                               type=ConfigConstant.WIDGET_TYPE_MANU,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_SSID_BROADCAST= Widget(name='QS_SETTING_WLAN_SSID_BROADCAST',
                                               xpath="//input[@name='broadcast']",
                                               type=ConfigConstant.WIDGET_TYPE_CHECK_BOX,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_SECURITY_AES  = Widget(name='QS_SETTING_WLAN_SECURITY_AES',
                                               xpath="//input[@name='secType' and @value='3']",
                                               type=ConfigConstant.WIDGET_TYPE_RADIO,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_SECURITY_NONE = Widget(name='QS_SETTING_WLAN_SECURITY_NONE',
                                               xpath="//input[@name='secType' and @value='0']",
                                               type=ConfigConstant.WIDGET_TYPE_RADIO,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL,
                                               default_value=True)
        self.QS_SETTING_WLAN_SECURITY_NO_CHANGE = Widget(name='QS_SETTING_WLAN_SECURITY_NO_CHANGE',
                                                    xpath="//input[@name='secType' and @value='4']",
                                                    type=ConfigConstant.WIDGET_TYPE_RADIO,
                                                    frame='mainFrame',
                                                    belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                                    url=self.QS_SETTING_WLAN_URL)
        self.QS_SETTING_WLAN_SECURITY_AES_KEY   = Widget(name='QS_SETTING_WLAN_SECURITY_AES_KEY',
                                                    xpath="//input[@name='pskSecret']",
                                                    type=ConfigConstant.WIDGET_TYPE_TEXT_BOX,
                                                    frame='mainFrame',
                                                    belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                                    url=self.QS_SETTING_WLAN_URL)
                                                    
        self.QS_SETTING_WLAN_NEXT          = Widget(name='QS_SETTING_WLAN_NEXT',
                                               xpath="//input[@name='Next']",
                                               type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL,
                                               save_button=True)
        self.QS_SETTING_WLAN_BACK          = Widget(name='QS_SETTING_WLAN_BACK',
                                               xpath="//input[@name='Return']",
                                               type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                               frame='mainFrame',
                                               belongs={'QS_SETTING_WAN_MAC_CLONE_NEXT':None},
                                               url=self.QS_SETTING_WLAN_URL)
                             

        ## Quick Setup End
        self.QS_SETTING_END_FINISH = Widget(name='QS_SETTING_END_FINISH',
                                       xpath="//input[@name='Complete']",
                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                       frame='mainFrame',
                                       belongs={'QS_SETTING_WLAN_NEXT':None},
                                       url=self.QS_SETTING_END_URL,
                                       save_button=True)
        self.QS_SETTING_END_REBOOT = Widget(name='QS_SETTING_END_REBOOT',
                                       xpath="//input[@name='Reboot']",
                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                       frame='mainFrame',
                                       belongs={'QS_SETTING_WLAN_NEXT':None},
                                       url=self.QS_SETTING_END_URL,
                                       save_button=True)
        self.QS_SETTING_END_BACK   = Widget(name='QS_SETTING_END_BACK',
                                       xpath="//input[@name='Return']",
                                       type=ConfigConstant.WIDGET_TYPE_BUTTON,
                                       frame='mainFrame',
                                       belongs={'QS_SETTING_WLAN_NEXT':None},
                                       url=self.QS_SETTING_END_URL)       