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
    def watch_price(self, params={}) -> None:
        """ Watch the BTC price

        Args:
            coin (str): coin to  watch
        """

        url = '/api/v5/market/ticker'
        method = "GET"
        
        response = self.request_handler.send_to_sokx(method=method, path = url, params=params)
        
        # print(response.status_code)
        # print(response)

        if response.status_code == 200:
            data = response.json()
            
            tick = data.get('data')
            # self.send_alert(str(data.get('data')))
            print(tick[0].get('last'))
            
            # if (tick[0].get('last') - tick[0].get('lastPrice'))/tick[0].get('openPrice') > 0.05:
            #      self.send_alert("BTC Price Experienced Sudden Change!")
        else:
            print(response.status_code)
            # self.send_alert("status_code: " + str(response.status_code))
if __name__ == '__main__':
    ss = PriceWatcher()
    ss.watch_price({'instId': 'BTC-USD-SWAP'})
    # while True:
    #     time.sleep(10)
    #     ss.watch_price("SWAP")
