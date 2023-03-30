#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   price_watcher.py
@Time    :   2023/03/29 14:27:16
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''

# from Report import AlertSender

from .utils.common_utils import RequestHandler, send_alert
from .utils.common_logging import setup_logging
import time

# 监控市场行情

# 市场价格监控

# TODO: 重新设计API请求，要求请求一次数据，就可以分析MA、市场剧烈变动、市场预警等功能
class PriceWatcher:
    """
    Watches the market price.

    Attributes
    ----------
    request_handler: RequestHandler
        RequestHandler object.
    alert_sender: AlertSender
        AlertSender object.

    Methods
    -------
    watch_btc_price(self)
        Watches the BTC price.

    """

    def __init__(self):
        self.request_handler = RequestHandler()
        self.send_alert = send_alert
        self.logger = setup_logging()
        self.watch_list = []
        
    def get_watch_list(self):
        return self.watch_list

    # 该方法监测 BTC 价格是否发生剧烈波动，并在变化时调用 AlertSender 对象的 send_alert() 方法发送预警消息。
    def watch_price(self, watch_coin) -> None:
        """ Watch the BTC price

        Args:
            watch_coin (str): coin to  watch
        """

        # Retrieve the candlestick charts of the index from recent years.
        url = '/api/v5/market/history-index-candles'
        method = "GET"
        params = {}

        params.update({'instId': watch_coin})
        # Number of results per request. The maximum is 100; The default is 100
        params.update({"limit": "2"})
        # print("params: " + str(params))

        # 从okx获取行情数据
        response = self.request_handler.send_to_okx(
            method=method, path=url, params=params)

        # print(response.status_code)
        # print(response)

        if response.status_code == 200:
            self.watch_list.append(watch_coin)
            data = response.json()

            tick = data.get('data')
            # print(tick)
            # 最新价格开盘价
            last_price = float(tick[0][2])
            # 前一分钟的开盘价
            previous_price = float(tick[1][2])
            # 价格波动情况
            price_change = last_price - previous_price
            # 设置波动阈值为最新价格的0.5%
            threshold = last_price * 0.005
            # 判断是否存在剧烈波动
            if abs(price_change) > threshold:
                self.send_alert(watch_coin + "has changed" +
                                price_change + "in one minute")
            else:
                self.logger.info("正在持续监听" + watch_coin + "的市场波动")
        else:
            self.logger.error(response.status_code)

    def set_alert(self, watch_coin, alert_price):
        url = "/api/v5/market/ticker"
        method = "GET"
        params = {"instId": watch_coin}

        # 从okx获取行情数据
        response = self.request_handler.send_to_okx(
            method=method, path=url, params=params)

        if response.status_code == 200:
            self.logger.info("正在监听"+watch_coin+"的价格")
            data = response.json().get('data')
            last_price = data[0]["last"]
            # print(last_price)

            if last_price > alert_price:
                self.send_alert(watch_coin+"'s price is " +
                                last_price+" and bid yours"+alert_price)
                return False
            else:
                return True
        else:
            self.logger.error("status code")

    # TODO: 监听MA生命线，当价格突破或跌破MA线时，发送提醒
    def watch_ma(self,watch_coin, day):
        """_summary_
        监听市场数据并在价格突破或跌破MA线时发送提醒
        
        Args:
            coin (_type_): 监听的市场
            day (_type_): 监听的均线天数
        """
        url = "/api/v5/market/ticker"
        method = "GET"
        params = {"instId": watch_coin}

        # 从okx获取行情数据
        response = self.request_handler.send_to_okx(
            method=method, path=url, params=params)

        if response.status_code == 200:
            self.logger.info("正在监听"+watch_coin+"的价格是否突破均线")
            data = response.json().get('data')
            last_price = data[0]["last"]

        else:
            self.logger.error("status code")
            
    # TODO 判断市场是否发生剧烈变动
    # TODO 1. 监听价格
    # TODO 2. 监听成交量
    # TODO 3. 波动率指标 ATR
    # TODO 4. 开放利润 open interset
    # TODO 5. 合约杠杆情况
    # TODO 6. 上涨股票数量、下跌股票数量
    # TODO 7. 其他技术指标（EMA，RSI）
        
if __name__ == '__main__':
    ss = PriceWatcher()

    while ss.set_alert("BTC-USD-SWAP", "30000"):
        time.sleep(10)
    # while True:
    #     time.sleep(10)
    #     ss.watch_price("SWAP")
    
    



