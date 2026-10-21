from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

#创建fastapi实例
app = FastAPI(title="FastAPI案例1")

#挂载静态资源文件目录.app.mount指的是在app.mount下面挂在一个目录，/static指的是任何访问/static路径的请求都到这里来处理,rsource/static指的是请求的静态资源文件目录,name是FastAPI内部使用的别名
app.mount("/static",StaticFiles(directory="resource/static"),name="static")

#定义路径操作参数  -->http://127.0.0.1:8000/
@app.get("/")
def root():
    #FileResponse函数的作用是返回静态文件
    print("访问了根路径,返回文件")
    return FileResponse("resource/static/index.html")

#启动函数
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)

