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

import sys
for a_path in sys.path:
    print(a_path)

        
import unittest

from app.utils.sqlitedb import SqliteDataBase

class TestSqliteDataBase(unittest.TestCase):
    # 表示前置条件，它在每一个用例执行之前必须会执行一次 
    def setUp(self):
        self.db = SqliteDataBase('test.db')
        self.db.create_diary_table()
    
    # 表示释放资源，它在每次用例执行完之后会执行一次
    def tearDown(self):
        self.db.delete('diary', '1=1')
        self.db.__del__()
        
    def test_create_table(self):
        self.db.create_diary_table()
        
    def test_insert(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        
    def test_select(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        result = self.db.select('diary', '*', '1=1')
        self.assertEqual(result[0][0], '2021-01-01')
        self.assertEqual(result[0][1], '100')
        self.assertEqual(result[0][2], 'test')
        
    def test_update(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        self.db.update('diary', 'price', '200', '1=1')
        result = self.db.select('diary', '*', '1=1')
        self.assertEqual(result[0][0], '2021-01-01')
        self.assertEqual(result[0][1], '200')
        self.assertEqual(result[0][2], 'test')
        
    def test_delete(self):
        self.db.insert_diary('2021-01-01', '100', 'test')
        self.db.delete('diary', '1=1')
        result = self.db.select('diary', '*', '1=1')
        self.assertEqual(len(result), 0)
        
if __name__ == '__main__':
    unittest.main()
    print('ok')