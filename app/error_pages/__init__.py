#!/usr/bin/env python
# -*-coding:utf-8 -*-
#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/04/05 14:58:23
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   异常捕捉
'''

# 导入所需的库
from flask import Blueprint

# 声明蓝图对象并设置其名称
error_bp = Blueprint('views',
                     __name__,
                     template_folder='./templates')
""" error_bp = Blueprint('views', __name__, template_folder='error_pages/templates')
@Desc: 将可选的 template_folder 参数设置为包含错误页面模板的目录路径，以便 Flask 能够正确地加载它们
"""

from . import views
# 定义该蓝图所需的所有视图函数和 URL 规则，这些规则都会自动添加到蓝图对象的 routes 属性中 
