from django.http import JsonResponse
from User.models import User  #导入用户表
from User.libs.Md5 import md5  #MD5加密
import time     #时间模块


#用户注册功能
def register(request):
   #获取参数
   user=request.POST.get("user")       #获取用户帐号
   passwd=request.POST.get("passwd")   #获取密码
   name=request.POST.get("name")       #获取用户昵称
   email=request.POST.get("email")     #获取邮箱
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
           return  JsonResponse({"Success":"Register OK!"})

       else:
            # 如果表中有该用户则返回错误提示
            return JsonResponse({"Error":"User already registered"})

   else:
       #如果传入的用户名或密码为空时则返回以下信息：
       return JsonResponse({"Error":"User name or password is empty!"})




