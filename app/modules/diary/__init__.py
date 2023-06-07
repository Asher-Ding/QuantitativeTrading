#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/04/05 16:29:53
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   定义一些模块级别的变量和配置信息
'''

from flask import Blueprint

diary_pages = Blueprint('diary_pages', __name__, template_folder='./templates')

# 导入所需的库，原因是在蓝图中使用这些库时，需要使用蓝图的上下文，而不是应用的上下文
from . import diary_controller
