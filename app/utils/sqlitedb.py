import sqlite3

class SqliteDataBase:
    """Sqlite database class
    
    :param db_name: database name
    :type db_name: str
    """
    def __init__(self, db_name):
        self.db_name = db_name
        # 连接Sqlite数据库
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    
    # 创建表
    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.connection.commit()

    # 插入数据
    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.connection.commit()

    # 查询数据
    def select(self, table_name, columns, condition):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    # 更新数据
    def update(self, table_name, column, value, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {column} = {value} WHERE {condition}")
        self.connection.commit()

    # 删除数据
    def delete(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.connection.commit()

    # 关闭数据库连接
    def __del__(self):
        self.connection.close()
    
    # create table named 'diary'
    def create_diary_table(self):
        self.create_table('diary', 'date text, price real, remarks text')