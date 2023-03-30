#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   test_sqlitedb.py
@Time    :   2023/03/30 16:55:54
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

import pytest
from app.utils.sqlitedb import SqliteDataBase

class TestSqliteDataBase:
    # pytest fixture to create database object before each test case.
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = SqliteDataBase('test.db')
        self.db.create_diary_table()
        yield  # this is use to tear down the database object after each test case.
        self.db.delete('diary', '1=1')
        self.db.__del__()

    def test_create_table(self):
        self.db.create_diary_table()
        
    def test_insert(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        
    def test_select(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        result = self.db.select('diary', '*', '1=1')
        assert result[0][0] == '2021-01-01'
        assert result[0][1] == '100'
        assert result[0][2] == 'test'
        
    def test_update(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        self.db.update('diary', 'price', '200', '1=1')
        result = self.db.select('diary', '*', '1=1')
        assert result[0][0] == '2021-01-01'
        assert result[0][1] == '200'
        assert result[0][2] == 'test'
        
    def test_delete(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        self.db.delete('diary', '1=1')
        result = self.db.select('diary', '*', '1=1')
        assert len(result) == 0