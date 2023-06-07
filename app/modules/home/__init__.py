#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/04/05 19:23:07
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   将首页和导航栏打包成一个模块，并将其放置在modules目录中是一种常见的组织Flask应用程序的方式，尤其是当你的应用程序开始变得复杂时。
'''

from flask import Blueprint

home_pages = Blueprint('home_pages', __name__, template_folder='./templates')

from . import views