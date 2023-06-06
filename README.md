### git项目提交：

[init] 初始化

[feat] 新特性、新功能

[modify] 修改功能

[delete] 删除功能或文件

[fix] 修复问题或解决冲突

[docs] 修改文档

[opt] 功能优化、代码重构

[build] 改变构建流程、新增依赖、工具

[style] 仅修改代码格式（空格、缩进、注释）

[test] 测试用例新增、修改

[revert] 回滚上一个版本



### 目录结构说明
```
│  main.py				程序主入口
│  README.md			README
│  requirements.txt		依赖文件
│  
├─app		app应用目录
│  │  __init__.py	app初始化/注册
│  │  
│  └─user	子应用
│          models.py	数据模型类
│          urls.py		url路由入口
│          views.py		视图函数
│          __init__.py	子应用初始化/注册
│          
├─settings	项目配置
│      config.py
│      __init__.py
│      
└─utils		项目通用工具
        interceptor.py
        __init__.py

```
