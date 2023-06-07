#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   controller.py
@Time    :   2023/04/06 21:11:31
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''


from flask import render_template, request
from . import diary_pages
from .diary_model import Diary
# from app import db # 不能这样导入，会报错
from api.okx import get_positions_history

@diary_pages.route('/diary')
def diary():
    return render_template('diary.html')

# Add diary entry
@diary_pages.route('/add_diary', methods=["POST"])
def add_diary():
    time = request.form.get('time')
    status = request.form.get('status')
    profit = request.form.get('profit')
    profit_rate = request.form.get('profit_rate')
    direction = request.form.get('direction')
    leverage = request.form.get('leverage')
    margin = request.form.get('margin')
    price = request.form.get('price')
    trade_id = request.form.get('trade_id')
    db.session.add(Diary(time=time, status=status, profit=profit, profit_rate=profit_rate, direction=direction, leverage=leverage, margin=margin, price=price, trade_id=trade_id))
    db.session.commit()
    return render_template('diary.html')
    

# Select all diary entries
@diary_pages.route('/diary_list', methods=["GET"])
def diary_list():
    # get_positions_history()
    # [ ]增加model存储数据，增加api获取数据
    #     1. 定义model


    diaries = db.session.query(Diary).all()
    return render_template('diary_list.html', diaries=diaries)


