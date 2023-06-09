#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   common_utils.py
@Time    :   2023/03/29 14:26:59
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

import datetime
import requests
import json
import hmac
import base64
from app.config import API_KEY, SECRET_KEY, PASSPHRASE
from app.config import OKX_BASE_URL, PUBLIC_URI, PRIVATE_URI


class RequestHandler:
    """一个请求处理类
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    # 1. 初始化
    def __init__(self):
        """
        This is a constructor
        """
        self.requests = requests
        self.api_key = API_KEY
        self.secret_key = SECRET_KEY
        self.passphrase = PASSPHRASE
        self.okx_url = OKX_BASE_URL
        self.public_uri = PUBLIC_URI
        self.private_uri = PRIVATE_URI
    
    def _get_header(self, method, path, body=None, headers=None):
        """设置请求头

        Args:
            method (_type_): 请求方式
            path (_type_): 请求路径
            body (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if headers is None:
            headers = {}
        headers.update({
            "Content-Type": "application/json",
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-PASSPHRASE": self.passphrase
        })
        # 时间戳
        timestamp = datetime.datetime.utcnow().isoformat('T', 'milliseconds') + 'Z'
        headers.update({"OK-ACCESS-TIMESTAMP": timestamp})
        # 签名
        if body == None:
            body = ''
        msg = str(timestamp) + str.upper(method) + path + body
        
        headers.update({"OK-ACCESS-SIGN": self._sign(msg)})
        return headers
        
    def _sign(self, msg):
        """对信息进行签名

        Args:
            msg (_type_): _description_

        Returns:
            str: 返回签名
        """
        # 使用hamc、sha256方法加密，base64编码输出
        sign = base64.b64encode(hmac.new(bytes(self.secret_key,encoding='utf-8'),bytes(msg,encoding='utf-8'),digestmod='sha256').digest())
        return sign

    def send_to_okx(self, method, path, params=None, data=None, json=None, headers=None, **kwargs):
        """向OKX发送请求

        Args:
            method (_type_): _description_
            path (_type_): 请求路径
            params (_type_, optional): _description_. Defaults to None.
            data (_type_, optional): _description_. Defaults to None.
            json (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            response: 返回response
        """
        # 设置请求头
        headers = self._get_header(method,path,body=json,headers=headers)
        # print(headers)
        url = "%s%s" % (OKX_BASE_URL,path)
        
        return self.requests.request(method,url,params=params,data=data,json=json,headers=headers,timeout=180,verify=True,**kwargs)

