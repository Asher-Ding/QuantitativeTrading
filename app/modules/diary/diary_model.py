#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   diary_model.py
@Time    :   2023/04/09 15:59:08
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for the models
Base = declarative_base()

class Diary(Base):
    """Diary model.
    """
    
    __tablename__ = 'diary'
    
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    status = Column(String(20))
    profit = Column(Float)
    profit_rate = Column(Float)
    direction = Column(String(20))
    leverage = Column(Integer)
    margin = Column(Float)
    price = Column(Float)
