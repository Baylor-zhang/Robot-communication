#前端程序网页一般有三个部分组成，HTML(负责网页的结构)、CSS(负责网页的样式和布局)、JavaScript(负责网页的交互效果和动作行为)三个部分
#服务端程序：可以基于python中的Django、Flask或者FastAPI来进行开发
#数据库：负责数据的存储与管理
#API接口：应用程序编程接口(Application programming interface),就是对外提供的功能入口，允许其他程序调用
#FastAPI 入门
#安装FastAPI pip install fastapi
#使用步骤
#1.导入FastAPI  from fastapi import FastAPI
#2.创建FastAPI实例对象
#3.创建路径操作函数，定义访问路径
#4.运行FastAPI服务 fastapi dev "xxx.py"  or  uvicorn "xxx:app" --reload   xxx指的是文件名，app指的是实例名
#运行方式3
#import uvicorn
#uvicorn.run(app,host="0.0.0.0",port=8000)  app是实例名 ,host="0.0.0.0"指的是那台服务器可以访问这个API ,port=8000指的是可以通过哪个端口号访问
from fastapi import FastAPI

#创建fastapi实例
app = FastAPI()
#定义API接口
@app.get("/")   #接口的访问路径为/ ，该路径下的访问方式必须为get
#该函数的返回值表示API接口的返回值的数据
def root():
    return {"message":"hello world"}

#定义API接口
@app.get("/users")  #请求路径为/users，请求方式为 get
#定义所有用户数据的函数
def get_users():
    return [
        {
            "id":1,
            "name":"张三",
        },
        {
            "id":2,
            "name":"李四",
        }
    ]
#通过命令行启动FastAPI服务
#在终端输入(.venv) PS D:\Python_Project_Learning\Web应用> fastapi dev '.\01_FastAPIWeb框架.py'
#在终端输入(.venv) PS D:\Python_Project_Learning\Web应用> uvicorn 01_FastAPIWeb框架:app --reload
#在浏览器输入 http://127.0.0.1:8000/users
#在浏览器中输入http://127.0.0.1:8000
#在python程序中启动FastAPI服务 运行方式3
if __name__ == "__main__":
    import uvicorn   #启动fastapi之前需要导入uvicorn包
    uvicorn.run(app,host="0.0.0.0",port=8000)

#在浏览器输入 http://127.0.0.1:8000/users
#在浏览器中输入http://127.0.0.1:8000

#Restful指的是遵循RESTful架构的API接口，而REST(REpresentational state Transfer),表述性状态转换，是一种软件架构风格
#REST风格API是通过请求方式的不同对用户的操作也不同，相同的URL，GET请求用于获取数据，POST请求用于创建数据，PUT请求用于更新数据，DELETE请求用于删除数据
#通过URL定位资源，通过请求方式获取、创建、更新、删除资源
#REST是风格，是约定方式，约定不是强制规定，可以被打破
#描述功能模块通常使用复数形式(加s),表示此类资源，而非单个资源，如users, books, posts
