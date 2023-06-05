# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： __init__.py.py
# @date：2023/6/5
# @github: https://github.com/Karleung
from flask import Blueprint

# 1.创建蓝图对象
user_bp = Blueprint("user", __name__)

# 2.给类视图添加路由信息
