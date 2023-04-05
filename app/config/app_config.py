# app_config.py

APP_CONFIG = {
    # 钉钉机器人用于发送预警信息, 请自行申请; 申请地址: https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq；申请成功后会生成一个access_token，将其填入app_config.py中的ACCESS_TOKEN中
    "WEBHOOK_URL": "https://https://oapi.dingtalk.com/robot/send?access_token=",
    # 交易所交易地址
    "OKX_BASE_URL":"https://www.okx.com",
    "PUBLIC_URI":"wss://ws.okx.com:8443/ws/v5/public",
    "PRIVATE_URI":"wss://ws.okx.com:8443/ws/v5/private",
    # 用于生成导航栏的链接
    "NAVBAR_LINKS" : { 
        '首页': '/',
        '日记': {
            '添加日记': '/diary',
            '日记列表': '/diary_list'
        },
        '预警': {
            '添加预警': '/alert',
            '预警列表': '/alert_list'
        },
        '设置': {
            '设置': '/setting',
        },
    }
}