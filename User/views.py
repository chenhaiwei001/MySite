from django.shortcuts import render
from django.http import HttpResponse
from User.models import User  #导入用户表
from User.libs.Md5 import md5  #MD5加密
import time     #时间模块


#用户注册功能
def register(request):
   #获取参数
   user=request.POST.get("user")       #获取用户名，必填参数
   passwd=request.POST.get("passwd")   #获取密码，必填参数
   name=request.POST.get("name")       #获取用户名，选填
   email=request.POST.get("email")     #获取邮箱，选填参数
   CreateTime=int(time.time())         #获取当前时间戳

   #判断用户名及密码是否为空
   if user and passwd:
       #如果用户名和密码不为空则：
       user_ORM= User.objects.filter(user__exact=user)  # 查询user是否在表中
       passwd_md5=md5(passwd)                           #对密码进行MD5加密

          #判断用户是否被注册
       if  not user_ORM :
           #如果没有注册则写入数据并保存
           DATA=User(
               user=user,
               passwd=passwd_md5,
               name=name,
               email=email,
               CreateTime=CreateTime,
               status=0
           )
           DATA.save()
           return   HttpResponse("200,Register OK!")

       else:
            # 如果表中有该用户则返回错误提示
            return HttpResponse("error,User already registered")

   else:
       #如果传入的用户名或密码为空时则返回以下信息：
       return HttpResponse("error,User name or password is empty！！！")





