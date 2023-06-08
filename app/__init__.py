# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： __init__.py
# @date：2023/6/5
# @github: https://github.com/Karleung

# 项目初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from interceptors.error_handler import registry_error_handler
from settings.config import config_dict

db = SQLAlchemy()

# 创建redis数据库对象[全局变量]
redis_cli = None  # type: StrictRedis


def create_flask_app(config_name):
    """
    内部调用创建app对象的工厂方法
    :param config_name: 配置名称
    :return: app对象
    """
    app = Flask(__name__)

    # 2.先读取配置类的配置信息
    config_class = config_dict[config_name]
    app.config.from_object(config_class)

    return app


def create_app(config_name):
    """
    外部调用工厂方法创建app对象
    :param config_name: 配置名称
    :return: app
    """

    # 1.创建app
    app = create_flask_app(config_name)
    registry_error_handler(app)
    # 2.注册拓展组件
    register_extensions(app)
    # 3.注册蓝图
    register_bp(app)

    return app


def register_extensions(app: Flask):
    # 1.Mysql数据库对象关联app
    db.init_app(app)
    global redis_cli
    # decode_responses=True 响应解码
    redis_cli = StrictRedis(host=app.config["REDIS_HOST"],
                            port=app.config["REDIS_PORT"],
                            decode_responses=True)


def register_bp(app: Flask):
    # 1.注册用户模块的蓝图对象
    # 注意：避免循环导包，用到的时候再导入
    from app.user import user_bp
    app.register_blueprint(user_bp)
