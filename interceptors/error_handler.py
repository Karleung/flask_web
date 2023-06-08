# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： error_handler.py
# @date：2023/6/8
# @github: https://github.com/Karleung
import traceback

from common.errors import Error
from common.response_code import code_message


def registry_error_handler(app):
    @app.errorhandler(404)
    def error_404(error):
        return code_message(-6, '资源不存在')

    @app.errorhandler(Exception)
    def error_handler(error):
        traceback.print_exc()
        return code_message(-1, message='内部异常')

    @app.errorhandler(Error)
    def error_handler(error):
        return code_message(error.code, message=error.message, data=error.data)
