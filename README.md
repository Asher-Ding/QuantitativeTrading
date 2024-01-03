## 项目名称及概述

[查看WIKI](https://github.com/Asher-Ding/QuantitativeTrading/wiki)

![](assets/README/img20230328202733.png)
**暂定项目名称：** Quantitative Trading

**概述：** Quantitative Trading 是一个面向个人的，可扩展的，易于开发和部署的量化交易程序。

**关于我：**
### 基础架构设计
整体采用微服务架构，后端包括策略引擎、订单管理、交易接口等不同模块，同时也有消息中间件。前端与后端采用常见的网络通信协议 RESTful API 进行交互。在后端与外围容器之间利用 Flask 和 Gunicorn 两个框架提高服务器性能。
代码存放于GitHub平台，每个模块托管于不同仓库中，便于分工协同开发和产品交付.

## 安装说明

克隆本项目

```bash
git clone --recursive https://github.com/Asher-Ding/QuantitativeTrading.git
```

安装依赖

```bash
npx tailwindcss-cli@latest build -i ./app/static/css/tailwind.css -o ./app/static/css/style.css
```

```bash
cd app
python app.py
```

<!-- ```python
python setup.py install 
``` -->

## 使用说明

## 特性&示例
实时行情推送：能够保持与交易所同步更新数据，当市场发生剧烈变化时，可以通过机器人向用户发送消息提醒
高可配置型：能够方便地修改、添加和删除策略
兼容性：支持OKX交易所

<!-- ## 贡献方式 -->

<!-- ## 计划&路线图

- [ ] 需求分析和功能规划
- [ ] 设计并完成监听市场剧烈变动的功能
- [ ] 确定程序架构
- [ ] 便携基础框架
- [ ] 实现代码细节
- [ ] ...
- [ ] 优化代码组织结构，组织代码的方法是，每个子文件夹都可以为单独的Git仓库，然后通过Git Submodule指向主目录下的文件。这样设计的优点是，使每个服务可以单独开发、调试和部署，同时有助于跨团队合作管理 -->


文档结构参考

```bash
── data
│   └── data_file
├── MANIFEST.in
├── README.rst
├── sample
│   ├── __init__.py
│   └── package_data.dat
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    └── test_simple.py
```

## 相关资源
[如何打包. 官方文档](https://packaging.python.org/en/latest/)

<!-- ## 社区 -->

<!-- ## 版权声明 -->

