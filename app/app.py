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

from flask import Flask

from config.setting import APP_CONFIG, NAVBAR_LINKS
from modules.common.database import Database
# Import Modules Which Contain Blueprints
from modules.home import home_pages
from modules.error import error_pages
from modules.diary import diary_pages
from modules.alert import alert_pages

from modules.common.logging import setup_logging
from modules.common.database import Database

def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.update(APP_CONFIG)
    return app

# initialize database
def db_init(app):
    """ Initialize the database """
    try:
        db_url = app.config['SQLALCHEMY_DATABASE_URI']
        db = Database(db_url)
        db.init_app(app)
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

# register blueprints
def register_blueprint(app):
    """ Register Flask blueprints """
    app.register_blueprint(home_pages)
    app.register_blueprint(error_pages)
    app.register_blueprint(diary_pages)
    app.register_blueprint(alert_pages)

if __name__ == '__main__':
    app = create_app()
    register_blueprint(app)
    db_init(app)
    
    # 通过使用Flask上下文处理函数来自动传递菜单变量，避免每个路由函数都要传递这个变量
    # 上下文处理器 (context processor) 是向模板上下文中添加变量以便在模板中使用
    @app.context_processor # 通过装饰器来注册上下文处理器
    def inject_navbar_links():
        """ Inject navbar links into all templates """
        return dict(navbar_links=NAVBAR_LINKS)
    
    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     """ Remove the database session after each request """
    #     db.session.remove()
    
    app.run(debug=True)
