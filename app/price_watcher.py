# from Report import AlertSender

from utils.common_utils import RequestHandler, send_alert
from utils.common_logging import setup_logging
import time


# 市场价格监控
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
        response = self.request_handler.send_to_okx(method=method, path = url, params=params)
        
        # print(response.status_code)
        # print(response)

        if response.status_code == 200:
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
                self.send_alert(watch_coin + "has changed" + price_change + "in one minute")
            else:
                self.logger.info("正在持续监听" + watch_coin + "的市场波动\n")
                time.sleep(30)
        else:
            self.logger.error(response.status_code)
                
    def set_alert(self, watch_coin, alert_price):
        url = "/api/v5/market/ticker"
        method = "GET"
        params = {"instId": watch_coin}
        
        # 从okx获取行情数据
        response = self.request_handler.send_to_okx(method=method, path = url, params=params)
        
        if response.status_code == 200:
            self.logger.info("正在监听"+watch_coin+"的价格")
            data = response.json().get('data')
            last_price = data[0]["last"]
            # print(last_price)
            
            if last_price > alert_price:
                self.send_alert(watch_coin+"'s price is "+last_price+" and bid yours"+alert_price)
                return False
            else:
                return True
        else: 
            self.logger.error("status code")
            
if __name__ == '__main__':
    ss = PriceWatcher()

    while ss.set_alert("BTC-USD-SWAP","30000"):
        time.sleep(10)
    # while True:
    #     time.sleep(10)
    #     ss.watch_price("SWAP")
