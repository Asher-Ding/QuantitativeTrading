#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   Diary.py
@Time    :   2023/03/30 20:36:42
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

import sqlite3

class Diary:
    """A class that facilitates database operations"""

    def __init__(self, db_name):
        """
        Initializes the class with a connection to the specified database.

        Args:
            db_name (str): The name of the database to connect to.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS entries (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                content TEXT,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                              )""" )
        self.conn.commit()

    # 创造表格
    def create_entry(self, title, content):
        sql = "INSERT INTO entries (title, content) VALUES (?, ?)"
        params = (title, content)
        return self.execute(sql, params)

    # 按照创造时间顺序读取所有的日记
    def read_entries(self):
        sql = "SELECT * FROM entries ORDER BY created_at DESC"
        return self.query(sql)

    # 更新日记
    def update_entry(self, entry_id, title, content):
        sql = "UPDATE entries SET title=?, content=? WHERE id=?"
        params = (title, content, entry_id)
        return self.execute(sql, params)

    # 删除日记
    def delete_entry(self, entry_id):
        sql = "DELETE FROM entries WHERE id=?"
        params = (entry_id,)
        return self.execute(sql, params)

    def query(self, sql, params=tuple()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute(self, sql, params=tuple()):
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
