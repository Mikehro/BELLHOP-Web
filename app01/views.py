from django.shortcuts import render,HttpResponse,redirect
import numpy as np
import matlab.engine
from io import BytesIO
import base64
from PIL import Image


# def home(request):
#     return HttpResponse("欢迎来到水声射线模拟系统-正在跳转...")
def Page01(request):
    #优先去根目录的templates中寻找html文件（需要在setting文件中配置）
    #去app01目录下面的templates文件寻找html文件（根据app的注册顺序逐一从templates文件中寻找）

    return render(request,"MainPage.html")

def task_02(request):
    #name="bellhop"
    #data=["射线模拟","水声信号"]
    #data_info={"name":"刘炜","role":"web前端开发"}
    #return render(request,"task_02.html",{"n1":name, "n2":data,"n3":data_info})
    #启动 MATLAB 引擎
    eng = matlab.engine.start_matlab()
    eng.cd('E:\MatlabWorkPlace\参考1_BELLHOP_General_Description\Task_GD_2_Gauss', nargout=0)

    #执行 MATLAB 脚本文件
    eng.eval("run('command_draft_Task2_MountainLine3Fig.m');", nargout=0)
    #获取当前图形句柄
    fig_handle = eng.gcf()

    #将图像数据传输到 Python 中
    matlab_image_data = eng.getframe(fig_handle, nargout=1)
    #检查数据类型并转换为 NumPy 数组
    if isinstance(matlab_image_data, dict) and 'cdata' in matlab_image_data:
        matlab_image = np.asarray(matlab_image_data['cdata'], dtype=np.uint8)
    else:
        raise ValueError("Unexpected image data format from MATLAB")

    #关闭 MATLAB 引擎
    eng.quit()

    #将图像数据转换为 PIL 图像对象
    image = Image.fromarray(matlab_image)
    image.show()

    #将 PIL 图像对象转换为字节流
    image_stream = BytesIO()
    image.save(image_stream, format='PNG')  # 你可以根据实际情况选择图像格式

    #获取字节流的 Base64 编码
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    #将图像数据传递到模板
    return render(request, 'task_02.html', {'image_data': image_base64})

def Page02(request):
    #获取请求方式 GET/POST
    #print(request.method)
    #在URL上传递值
    #print(request.GET)
    #在请求体中提交数据
    #print(request.POST)
    #将字符串内容返回给请求者
    #return HttpResponse(request.method)
    #读取HTML的内容+渲染（替换）-》字符串，并返回给用户浏览器
    #return render(request,"MainPage.html")
    #浏览器重定向到其它页面
    #return redirect("https://www.bilibili.com/")
    if request.method =="GET":
        return render(request,"MainPage02.html")
    else:
        return HttpResponse("OK")