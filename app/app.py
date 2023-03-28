from flask import Flask, render_template, request
from price_watcher import PriceWatcher

app = Flask(__name__)

price_watcher = PriceWatcher()

# Navigation bar links
navbar_links = {
    'Index': '/',
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
    date = request.form['date']
    price = request.form['price']
    remarks = request.form['remarks']
    # 这里可以把收集到的数据保存到数据库中
    return render_template('submit.html', date=date, price=price, remarks=remarks,navbar_links=navbar_links)

@app.route('/watch_list')
def watch_list():
    watch_list = price_watcher.get_watch_list()
    return render_template('watch_list.html', watch_list=watch_list,navbar_links=navbar_links)

if __name__ == '__main__':
    app.run(debug=True) 