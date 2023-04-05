#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   setting.py
@Time    :   2023/04/05 17:54:24
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   将所有配置集中存储在 settings.py 中，并可以将其按功能分组到单独的 .py 文件中。这样做可以使代码更易于维护和管理，并提高可重用性和可扩展性。
'''
import os
# pip install python-dotenv
from dotenv import load_dotenv
from .navbar_links import NAVBAR_LINKS
from .url_config import OKX_BASE_URL, PUBLIC_URI, PRIVATE_URI, WEBHOOK_URL

load_dotenv()
# Define your configuration variables here
DEBUG = True
# OKX的密钥信息
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
PASSPHRASE = os.getenv('PASSPHRASE')
# DingTalk Robot
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
# 添加Token生成新的WEBHOOK_URL
WEBHOOK_URL = WEBHOOK_URL + ACCESS_TOKEN




