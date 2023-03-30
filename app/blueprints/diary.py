#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   diary.py
@Time    :   2023/03/30 21:10:33
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

from . import diary_blueprint

@diary_blueprint.route('/diary')
def diary():
    print('diary page')
    # return render_template('diary.html')



def buy_stock():
    # implement buying stock
    return 'Buying stock...'
