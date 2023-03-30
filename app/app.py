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

from flask import Flask, render_template, request, redirect
from .price_watcher import PriceWatcher
from .utils.sqlitedb import SqliteDataBase

app = Flask(__name__)

price_watcher = PriceWatcher()

DATABASE = 'app/database/diary.db'

# Navigation bar links
navbar_links = {
    'Index': '/',
    'Diary': '/diary',
    'Watch': '/watch',
    'Watch List': '/watch_list',
    'Diary List': '/diary_list'
}

@app.route('/')
def index():
    return render_template('index.html',navbar_links=navbar_links)

@app.route('/watch', methods=['GET'])
def watch():
    crypto = request.args.get('crypto')
    price_watcher.watch_price(crypto)
    # return "You are now watcing "+crypto
    return render_template('watch.html',navbar_links=navbar_links)

@app.route('/submit', methods=['POST'])
def submit():
    # date = request.form['date']
    # price = request.form['price']
    # remarks = request.form['remarks']
    # 这里可以把收集到的数据保存到数据库中
    return render_template('submit.html')

@app.route('/watch_list')
def watch_list():
    watch_list = price_watcher.get_watch_list()
    return render_template('watch_list.html', watch_list=watch_list,navbar_links=navbar_links)


# diary page
@app.route('/diary')
def diary():
    # TODO: 定义日记的模版，然后在这里调用
    print('diary page')
    return render_template('diary.html',navbar_links=navbar_links)

# diary submit page
@app.route('/diary_submit',methods=['POST'])
def diary_submit():
    # print(request.form.get('time'))
    # Create Instance of SqliteDataBase
    diary_db = SqliteDataBase(DATABASE)
    
    # Call create_diary_table method on the instance
    SqliteDataBase.create_diary_table(diary_db)
    
    # Get date, price and remarks params from request
    date_param = request.form.get('date')
    price_param = request.form.get('price')
    remarks_param = request.form.get('remarks')
    
    # Insert diary to table 'diary'
    diary_db.insert_diary(date_param, price_param, remarks_param)

    print('diray table created')
    return redirect('diary'), 301


# Sample list of diaries
diaries = [
    {"title": "First Entry", "entry": "This is my first diary entry!", "date": "2021-01-01", "content": "This is my first diary entry!..."},
    {"title": "Second Entry", "entry": "This is my second diary entry!", "date": "2021-01-02", "content": "This is my second diary entry!..."},
    # Additional entries ...
]


@app.route('/diary_list')
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
    return render_template("diary_list.html",navbar_links=navbar_links,  diaries=diaries_on_page, current_page=page, total_pages=total_pages) 



# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',navbar_links=navbar_links), 404


if __name__ == '__main__':
    app.run(debug=True) 