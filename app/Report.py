import requests
import json

from Config import WEBHOOK_URL

headers = {
#   "token": "DI****LK",
  "content-type": "application/json; charset=utf-8",
  "content-length": "630",
#   "host": "hz*****80",
  "connection": "Keep-Alive",
  "accept-encoding": "gzip",
  "user-agent": "okhttp/3.5.0"   
}

class AlertSender:
    """使用钉钉机器人发送群聊消息提醒
    https://open.dingtalk.com/document/orgapp/custom-robot-access
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    def __init__(self,message):
        # self.client = Client(account_sid, auth_token)
        self.message = message

    def send_alert(self):
        """ send alert

        Args:
            message (str): 消息内容
        """
        msg = {
            "msgtype": "text",
            "text": {
                "content": "okx:" + self.message
            },
            "at": {
                # "atMobiles": ["1234567890"],
                # "isAtAll": False
            }
        }
        url = "https://oapi.dingtalk.com/robot/send?access_token=1950809a42492175541c02540f9b15e2c8f180f677dcfc7af2745e959e6f74a3"


        response = requests.post(url = url, headers=headers, data=json.dumps(msg))
        print(response.status_code)
       
    