#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   alert_views.py
@Time    :   2023/04/05 16:44:05
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

from . import alert_pages
from flask import render_template, request

@alert_pages.route('/alert', methods=['GET'])
def alert():
    crypto = request.args.get('crypto')
    # price_alerter.alert_price(crypto)
    # return "You are now watcing "+crypto
    return render_template('alert.html')

@alert_pages.route('/alert_list')
def alert_list():
    # alert_list = price_alerter.get_alert_list()
    return render_template('alert_list.html')
