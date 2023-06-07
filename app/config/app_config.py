import os
# print(os.path.dirname(__file__))

APP_CONFIG = {
    "SQLALCHEMY_DATABASE_URI": "sqlite:///" + "app/database/quant.db",
    # os.path.join(os.path.dirname(__file__), "database/quant.db") 返回当前 Python 文件所在文件夹的绝对路径，再加上 database/quant.db，得到数据库文件的绝对路径。
}

