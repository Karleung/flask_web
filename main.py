# coding=utf-8
# @project: flask_web
# @Author：Karleung
# @file： main.py
# @date：2023/6/5
# @github: https://github.com/Karleung
import logging
from app import create_app
from common.response_code import code_message

# 1.调用工厂方法创建app
app = create_app("dev")

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
# logging.basicConfig(filename='db_hd.log', level=logging.INFO, format=LOG_FORMAT)


# 2.定义视图函数绑定路由
@app.route('/')
def index():
    rule_dict = {rule.rule: rule.endpoint for rule in app.url_map.iter_rules()}
    return code_message(rule_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
