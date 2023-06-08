# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： response_code.py
# @date：2023/6/8
# @github: https://github.com/Karleung
from flask import jsonify


def code_message(code=0, message='成功', data=None):
    resp = {
        'code': code,
        'message': message,
    }
    if data:
        resp['data'] = data
    return jsonify(resp)


if __name__ == '__main__':
    code_message()
