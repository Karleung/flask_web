# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： errors.py
# @date：2023/6/8
# @github: https://github.com/Karleung
class Error(Exception):
    code = 0
    message = '内部异常'

    def __init__(self, data=None, code=None, message=None):
        self.code = code or self.code
        self.message = message or self.message
        self.data = data


class ParamsError(Error):
    code = -2
    message = '参数异常'


class LoginError(Error):
    code = -3
    message = '登录失败，帐号或密码错误！'


class PermissionError(Error):
    code = -4
    message = '权限不足'


class UserError(Error):
    code = -5
    message = '用户已禁用'


class NotLogin(Error):
    code = -7
    message = '用户未登录'


class NoUser(Error):
    code = -8
    message = '用户不存在'


class UserExist(Error):
    code = -9
    message = '用户已存在'


if __name__ == '__main__':
    c = Error()
    print(c.code)
