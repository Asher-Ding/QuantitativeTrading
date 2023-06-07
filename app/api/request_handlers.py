import datetime
import requests
import hmac
import base64
# from Authorization import API_KEY, SECRET_KEY, PASSPHRASE
from app.config.setting import API_KEY, SECRET_KEY, PASSPHRASE

# 交易所交易地址
BASE_URL = "https://www.okx.com"
PUBLIC_URI = "wss://ws.okx.com:8443/ws/v5/public"
PRIVATE_URI = "wss://ws.okx.com:8443/ws/v5/private"

class OKXRequestHandle:
    """
    处理request请求
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    # 1. 初始化
    def __init__(self):
        """
        This is a constructor
        """
        self.requests = requests
        self.api_key = API_KEY
        self.secret_key = SECRET_KEY
        self.passphrase = PASSPHRASE
    
    def _get_header(self, method, path, body=None, headers=None):
        if headers is None:
            headers = {}
        headers.update({
            "Content-Type": "application/json",
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-PASSPHRASE": self.passphrase
        })
        # 时间戳
        timestamp = datetime.datetime.utcnow().isoformat('T', 'milliseconds') + 'Z'
        headers.update({"OK-ACCESS-TIMESTAMP": timestamp})

        # 签名
        if body == None:
            body = ''
        msg = str(timestamp) + str.upper(method) + str(path) + str(body)
        
        headers.update({"OK-ACCESS-SIGN": self._sign(msg)})
        return headers
        
    def _sign(self, msg):
        # 使用hamc、sha256方法加密，base64编码输出        
        sign = base64.b64encode(hmac.new(bytes(self.secret_key,encoding='utf-8'),bytes(msg,encoding='utf-8'),digestmod='sha256').digest()) # type: ignore
        return sign

    def send(self, method, path, params=None, data=None, json=None, headers=None, **kwargs):
        """_summary_

        Args:
            method (_type_): _description_
            path (_type_): _description_
            params (_type_, optional): _description_. Defaults to None.
            data (_type_, optional): _description_. Defaults to None.
            json (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        # 设置请求头
        headers = self._get_header(method,path,body=json,headers=headers)
        # print(headers)
        url = "%s%s" % (BASE_URL,path)
        
        return self.requests.request(method,url,params=params,data=data,json=json,headers=headers,timeout=180,verify=True,**kwargs)
    
if __name__ == "__main__" :
    # 测试
    req = OKXRequestHandle()
    headers = {"x-simulated-trading": "0"} # 模拟环境：1，真实环境：0
    get = req.send("GET", "/api/v5/asset/currencies", headers=headers)
    
    print(get.status_code)
    print(get.text)