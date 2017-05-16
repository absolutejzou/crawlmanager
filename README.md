# crawlmanager
该项目创建的目的是用来进行个人爬虫管理

需要生成配置文件
内容如下:
```
[POSTGRESQL]
# postgresql配置
DATABASE=***
USER=***
PASSWORD=***
HOST=***
PORT=***

[SERVER]
# 服务启动模式 dev/prod
MODE=dev

[HOSTS]
# 可配置多个，以逗号隔开
ALLOWED_HOSTS=***
```
django 启动前,需要使用parse.sh脚本解析并将其配置到环境变量中
