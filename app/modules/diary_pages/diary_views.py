#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   views.py
@Time    :   2023/04/05 16:29:15
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   包含与蓝图相关的所有路由和视图函数代码。视图函数处理从浏览器发送到应用程序的 HTTP 请求。这个文件还定义了与此蓝图相关的其他功能，比如表单类、过滤器等。
'''

from flask import render_template, request
from . import diary_pages


@diary_pages.route('/diary')
def diary():
    return render_template('diary.html')


DATABASE = 'app/database/diary.db'

# Sample list of diaries
diaries = [
    {
        "title": "First Entry",
        "entry": "This is my first diary entry!",
        "date": "2021-01-01",
        "content": "This is my first diary entry!..."
    },
    {
        "title": "Second Entry",
        "entry": "This is my second diary entry!",
        "date": "2021-01-02",
        "content": "This is my second diary entry!..."
    },
    # Additional entries ...
]


@diary_pages.route('/diary_list')
def diary_list():
    # Get query parameters
    page = int(request.args.get("page", 1))
    per_page = 10

    # Calculate pagination variables
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    diaries_on_page = diaries[start_idx:end_idx]
    total_pages = len(diaries) // per_page + (len(diaries) % per_page != 0)

    # Render template
    return render_template("diary_list.html",
                           diaries=diaries_on_page,
                           current_page=page,
                           total_pages=total_pages)
