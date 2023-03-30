#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   setup.py
@Time    :   2023/03/29 15:56:35
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

import os
import re
from setuptools import setup

# 这段代码获取当前文件的上级目录路径，并将其赋值给变量 ROOT，实现了动态获取项目根目录的功能
ROOT = os.path.dirname(__file__)
# 获取版本号的文本
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

# 获取版本号
def get_version():
    init = open(os.path.join(ROOT, 'app', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)
# ['"]([0-9.]+)['"] : 这个正则表达式被用于隔离版本号。['"] 的意思是允许使用单引号或双引号，并将该字符与版本号包围起来。( ) 用于捕获版本号。之后的内容 [0-9.]+ 让它匹配一个或多个数字以及小数点。结果是我们得到了版本号文本。如果匹配成功，GROUP[1] 将是所请求的版本号（即“$1”）


# requirements = open('requirements.txt').readlines() # read requirements

setup(
    name='quantitative_training',
    version=get_version(),
    author= 'asher',
    author_email= 'asherding@icloud.com',
    description='initializing Quantitative'
)
    