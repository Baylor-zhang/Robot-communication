import os.path
import json
from datetime import datetime
from typing import Any
from pydantic import BaseModel
from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

#创建fastapi实例
app = FastAPI(title="FastAPI案例1")

#挂载静态资源文件目录.app.mount指的是在app.mount下面挂在一个目录，/static指的是任何访问/static路径的请求都到这里来处理,resource/static指的是请求的静态资源文件目录,name是FastAPI内部使用的别名
app.mount("/static",StaticFiles(directory="resource/static"),name="static")
#BaseModel类是FastAPI中用于定义数据模型的类，它继承了BaseModel类，BaseModel类是Pydantic库中用于定义数据模型的类,用于定义FastAPI中的数据类型
#通过查看浏览器的请求头信息，我们知道，有一个请求头是post类型，在RESTful API中，post请求一般用于创建资源，请求路径是/api/sessions
#所以我们开发新建会话功能的时候首先顶一个新建会话的API的POST接口，且路径为/api/sessions,然后再创建一个新建会话的接口函数
#创建会话存放的目录,检查目录是否存在，如果不存在，再创建目录
if not os.path.exists("sessions"):
    os.mkdir("sessions")

#生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

#定义数据模型
class APIresponse(BaseModel):
    code:int
    message:str
    data:Any        #表示任意类型的数据

##session_id和message为请求体中的参数内容,定义数据模型，用于接收session_id和message参数
class ChatRequest(BaseModel):
    session_id:str
    message:str

#定义路径操作参数  -->http://127.0.0.1:8000/
@app.get("/")
def root():
    #FileResponse函数的作用是返回静态文件
    print("访问了根路径,返回文件")
    return FileResponse("resource/static/index.html")


#创建会话的函数
@app.post("/api/sessions")
def create_session():
    print("创建会话")

    #1.生成会话的标识(会话的ID)
    session_id = generate_session_id()

    #2.组装会话的信息，保存到文件中
    session_data = {"current_session":session_id,"messages":[]}
    with open(f"sessions/{session_id}.json","w",encoding="utf-8") as f:
        #json.dump()函数的作用是把Python对象转换成JSON对象,indent参数是缩进，ensure_ascii参数是保证中文不乱码
        json.dump(session_data,f,ensure_ascii=False,indent=2)
    #3.返回数据
    # return {"code":200,"message":"会话创建成功","data":session_id}
    #3.返回值，基于对象的属性创建返回数据，但是需要提前定义数据模型Model，这里返回给客户端的数据为对象，但是BaseModel会调用Pydantic库，将数据模型转换成字典，然后返回给客户端
    return APIresponse(code=200,message="会话创建成功",data=session_id)

#AI会话交互功能
@app.post("/api/chat")
def chat(request:ChatRequest): #将它们作为参数传递给FastAPI发给送服务器端,定义request参数的值为ChatRequest对象,格式为JSON格式，这里接收到的信息为用户输入的信息
    print(f"开始对话，与AI交互:{request.session_id}:{request.message}")     #在pycharm中输出信息
    return  APIresponse(code=200,message="AI会话请求相应成功",data="AI大模型返回的数据")  #从服务器段返回消息给客户端，可以在浏览器的resopnse中查看

#与AI大模型交互的逻辑实现
#1.加载json文件中的会话数据，并构建消息列表
#2.调用deepseek API
#3.获取响应数据
#4.更新消息列表，并保存到json文件中
#5.响应数据





#启动函数
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)

