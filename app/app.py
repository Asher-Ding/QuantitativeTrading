from flask import Flask, render_template, request, redirect
from price_watcher import PriceWatcher
from utils.sqlitedb import SqliteDataBase

app = Flask(__name__)

price_watcher = PriceWatcher()

diary_db = SqliteDataBase('app/database/diary.db')

# Navigation bar links
navbar_links = {
    'Index': '/',
    'Diary': '/diary',
    'Watch': '/watch',
    'Watch List': '/watch_list'
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
    return render_template('diary.html',navbar_links=navbar_links)

# diary submit page
@app.route('/diary_submit')
def diary_submit():

    # diary_db.create_diary_table()
    print('diray table created')
    return redirect('diary'), 301


# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',navbar_links=navbar_links), 404


if __name__ == '__main__':
    app.run(debug=True) 