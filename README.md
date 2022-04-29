# firstDjangoProject
## How to Create Django Project
- 查看python 版本 ```python --version```
- 跟新管理工具 ```pip3 install -U pip```
- 安装Django ```pip3 install Django==3.0.3``` (因为我的python 版本是 3.8)
- 创建Django 项目 ```django-admin startdproject HelloDjango```
- 用pycharm 打开 
- 创建虚拟环境 ()
- 安装项目依赖 ```pip install Django==3.0.3```
  下图展示了Django版本和Python版本的对应关系，请大家自行对号入座。

   | Django版本 | Python版本                                |
   | ---------- | ----------------------------------------- |
   | 1.8        | 2.7、3.2、3.3、3.4、3.5                   |
   | 1.9、1.10  | 2.7、3.4、3.5                             |
   | 1.11       | 2.7、3.4、3.5、3.6、3.7（Django 1.11.17） |
   | 2.0        | 3.4、3.5、3.6、3.7                        |
   | 2.1        | 3.5、3.6、3.7                             |
   | 2.2        | 3.5、3.6、3.7、3.8（Django 2.2.8）        |
   | 3.0        | 3.6、3.7、3.8                             |
 - 在terminal 输入 python manage.py runserver
 - 点击蓝色```http://127.0.0.1:8000``` 查看结果
 
 ## How to Create Django app
 - 创建名为 first 的项目 ```python manage.py startapp first```
 - 修改 views.py
