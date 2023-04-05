#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/03/29 14:25:44
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

from flask import Flask, current_app
from config.setting import APP_CONFIG, NAVBAR_LINKS
# Import blueprints
from views import main_pages
from error_pages import error_pages
from diary_pages import diary_pages
from alert_pages import alert_pages

app = Flask(__name__)
# 加载配置文件
app.config.update(APP_CONFIG)
# Register blueprints
app.register_blueprint(main_pages)
app.register_blueprint(error_pages)
app.register_blueprint(diary_pages)
app.register_blueprint(alert_pages)


# 通过使用Flask上下文处理函数来自动传递菜单变量，避免每个路由函数都要传递这个变量
@app.context_processor  # 是否可以理解为定义了一个全局变量
def inject_navbar_links():
    """ Inject navbar links into all templates """
    return dict(navbar_links=NAVBAR_LINKS)


if __name__ == '__main__':
    app.run(debug=True)
