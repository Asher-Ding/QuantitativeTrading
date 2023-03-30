from price_watcher import PriceWatcher
import time

# 监控策略，监控主流加密币的市场变动情况
# price_watcher = PriceWatcher()
# while True:
#     price_watcher.watch_price('BTC-USD')
#     price_watcher.watch_price('ETH-USD')
#     time.sleep(30) # 设置时间间隔

from utils.sqlitedb import SqliteDataBase

import sys
for a_path in sys.path:
    print(a_path)

# db = SqliteDataBase('app/database/diary.db')
# db.create_diary_table()
# print('diray table created')

