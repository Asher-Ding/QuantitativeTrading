# 调用okx的api接口
from request_handlers import OKXRequestHandle

req = OKXRequestHandle()
# 查看历史持仓信息
# 获取最近3个月有更新的仓位信息，按照仓位更新时间倒序排列。
# GET /api/v5/account/positions-history
def get_positions_history():
    res = req.send("GET", "/api/v5/account/positions-history")
    return res.text

if __name__ == "__main__" :
    positions_history =  get_positions_history()
    print(positions_history)

