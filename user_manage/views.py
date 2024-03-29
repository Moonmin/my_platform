from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth


# Create your views here.

def index(request):

    # return HttpResponse("hey")
    return render(request, "login.html")

# 处理登录请求
def  user_login(request):

    # 获取请求的方法是否为POST
    if request.method == 'POST':
        #默认赋空值
        user_name = request.POST.get('username','')
        user_pwd = request.POST.get('password','')
        print("user_name",user_name)
        print("user_pwd",user_pwd)
        if(user_name == '' or user_pwd == ''):
            #当用户名或密码为空时，跳转回登录页面,并给出提示
            return render(request, 'login.html',
                          {'error':'用户名或密码为空'})

        else:
            #如果用户名密码不为空，则到数据库校验
            user_name = auth.authenticate(username=user_name,password=user_pwd) #用户认证
            if user_name != None:
                # 如果数据返回值不为None,说明登录信息正确，
                auth.login(request,user_name)   # 负责用户登录状态的保持，将用户保存在session中
                #return render(request, 'index.html', {'user_name': user_name})#跳转登录页面
                #存储用户名到cookie中
                # response.set_cookie("cuser_name",user_name,3600)
                #对应用户名存入cookie的另一种方式，存入session表中
                print("user_name111=", user_name)
                # request.session['cuser_name'] = user_name
                response =  HttpResponseRedirect("/manage/project_manage/")
                response.set_cookie("user", user_name, 3600)
                # 重定向请求

            else:
                # 如果数据返回值为None,说明用户或密码错误，跳回登录页
                return render(request, 'login.html',
                              {'error': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'login.html')
    else:
        return render(request, 'login.html', {'error': '非法请求！'})




'''
从session里面读取用户信息  
重定向请求跳转至新页面
'''

#退出功能
@login_required()
def logout(request):
    auth.logout(request) #清除用户登录状态
    return HttpResponseRedirect("/") #重定向至登录页面