#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/03/30 21:02:09
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   蓝图，用于将不同的功能模块分离
'''

from flask import Blueprint

diary_blueprint = Blueprint('diary', __name__)
watch_blueprint = Blueprint('watch', __name__)

from . import diary, watch