#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   views.py
@Time    :   2023/04/05 16:58:06
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   一些全局的或者通用的视图函数，比如首页、关于页面等，或者其他一些不属于任何蓝图的路由和视图函数。
'''
from flask import Blueprint, render_template

# Create a Blueprint object
main_pages = Blueprint('main_pages', __name__, template_folder='./templates')
""" main = Blueprint('main', __name__, template_folder='main/templates') """

# Index page
@main_pages.route('/')
def index():
    return render_template('index.html')


# About page
@main_pages.route('/about')
def about():
    return render_template('about.html')
