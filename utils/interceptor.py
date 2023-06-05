# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： interceptor.py
# @date：2023/6/5
# @github: https://github.com/Karleung
from flask import Response
from main import app


@app.after_request
def process(response: Response):  # 必须定义形参接收响应对象
    print('after_request:')
    # print(response.headers)
    # print(response.data)
    # print(response.status_code)
    return response
