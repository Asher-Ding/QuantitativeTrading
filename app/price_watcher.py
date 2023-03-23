# from Report import AlertSender

from utils import RequestHandler, send_alert
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
        # self.alert_sender = AlertSender("ggg")
        self.send_alert = send_alert
        
    # 该方法监测 BTC 价格是否发生剧烈波动，并在变化时调用 AlertSender 对象的 send_alert() 方法发送预警消息。
    def watch_price(self, watch_coin) -> None:
        """ Watch the BTC price

        Args:
            coin (str): coin to  watch
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
                print("正在持续监听" + watch_coin + "的市场波动\n")
                time.sleep(30)
        else:
            print(response.status_code)
                # self.send_alert("status_code: " + str(response.status_code))
if __name__ == '__main__':
    ss = PriceWatcher()
    ss.watch_price("BTC-USD")
    # while True:
    #     time.sleep(10)
    #     ss.watch_price("SWAP")
