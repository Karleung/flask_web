# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： config.py
# @date：2023/6/5
# @github: https://github.com/Karleung
import pymysql

pymysql.install_as_MySQLdb()


# 配置父类
class BaseConfig(object):
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    user = 'root'
    passwd = 'mysql'
    db_host = '127.0.0.1'
    db_port = 3306
    db = 'flask_web'

    # Mysql数据库配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{passwd}@{db_host}:{db_port}/{db}"
    # 输出底层执行的sql语句
    SQLALCHEMY_ECHO = False
    # 关闭数据库修改跟踪[优化性能]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 防止中文编码问题
    JSON_AS_ASCII = False
    RESTFUL_JSON = {"ensure_ascii": False}

    JWT_SECRET = b'off_line_secret_key'  # token的密钥


# 给别的模块调用提供接口
config_dict = {
    "dev": BaseConfig,
}
