#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   database.py
@Time    :   2023/04/09 17:15:34
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

class Database:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, echo=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False,bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()
        self.db = SQLAlchemy()
    
    def init_app(self, app):
        with app.app_context():
            self.db.init_app(app)
            self.Base.metadata.create_all(bind=self.engine)






