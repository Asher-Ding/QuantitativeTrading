#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   dingtalk.py
@Time    :   2023/04/06 16:44:26
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   使用钉钉机器人发送群聊消息提醒
'''

from app.config.setting import WEBHOOK_URL
import requests,json

def send_alert(message):
    """ 使用钉钉机器人发送群聊消息提醒
    https://open.dingtalk.com/document/orgapp/custom-robot-access
    
    Args:
        message (str): 消息内容
    
    Returns:
        None
    """
    
    headers = {
      "content-type": "application/json; charset=utf-8",
      "content-length": "630",
      "connection": "Keep-Alive",
      "accept-encoding": "gzip",
      "user-agent": "okhttp/3.5.0"   
    }

    msg = {
        "msgtype": "text",
        "text": {
            "content": "okx:" + message
        },
        "at": {
            # "atMobiles": ["17395711569"],
            "isAtAll": False
        }
    }

    response = requests.post(url=WEBHOOK_URL, headers=headers, data=json.dumps(msg))
    print(response.status_code)
