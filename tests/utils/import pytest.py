import pytest,json
from unittest import mock
from app.utils.common_utils import RequestHandler, send_alert

class TestRequestHandler:

    @pytest.fixture(autouse=True)
    def setup(self):
        # 初始化 RequestHandler 实例
        self.req_handler = RequestHandler()

    # 测试 _get_header 函数是否设置了正确的请求头
    def test_get_header(self):
        method = "GET"
        path = "/test"
        body = {"param1": "hello", "param2": 123456}
        headers = {"Content-Type": "application/json"}
        expected_headers = {
            "Content-Type": "application/json",
            "OK-ACCESS-KEY": "your_access_key",
            "OK-ACCESS-PASSPHRASE": "your_passphrase",
            "OK-ACCESS-TIMESTAMP": "2023-03-29T14:26:59.000Z",
            "OK-ACCESS-SIGN": "expected_sign"
        }
        with mock.patch.object(self.req_handler, "_sign", return_value="expected_sign") as mock_sign:
            result = self.req_handler._get_header(method, path, json.dumps(body), headers)
            assert result == expected_headers

    # 测试 _sign 函数是否能正确生成签名
    def test_sign(self):
        msg = "123test321"
        expected_sign = "expected_sign"
        with mock.patch("common_utils.base64.b64encode", return_value=expected_sign) as mock_b64encode, \
             mock.patch("common_utils.hmac.new", return_value=mock.Mock(digest=mock.Mock(return_value="message_digest"))) as mock_hmac_new:
            result = self.req_handler._sign(msg)
            assert result == expected_sign

    # 测试 send_to_okx 函数是否能正确发送请求，并返回了正确的 response
    def test_send_to_okx(self):
        method = "GET"
        path = "/test"
        expected_url = "https://www.okx.com/test"
        expected_response = "expected_response"
        with mock.patch.object(self.req_handler, "_get_header", return_value={"OK-ACCESS-KEY": "your_access_key"}) as mock_get_header, \
             mock.patch.object(self.req_handler.requests, "request", return_value=mock.Mock(text=expected_response)) as mock_request:
            result = self.req_handler.send_to_okx(method, path)
            assert result.text == expected_response

class TestSendAlert:

    # 测试 send_alert 函数是否能正确发送钉钉机器人消息
    def test_send_alert(self):
        expected_status_code = 200
        with mock.patch("common_utils.requests.post", return_value=mock.Mock(status_code=expected_status_code)) as mock_post:
            send_alert("hello world")
            mock_post.assert_called_once()
