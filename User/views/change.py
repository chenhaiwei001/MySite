from django.http import HttpResponse,JsonResponse
from User.models import User  #导入用户表
from User.libs.Md5 import md5  #MD5加密

def change(request):
     #获取所有参数
     user=request.POST.get("user")        #用户名
     uid=request.POST.get("uid")          #uid,用户唯一标识
     passwd=request.POST.get("passwd")    #旧密码
     passwd_new=request.POST.get("passwd_new") #新密码

     #判断用户名和uid是否为空
     if user and uid:
         # 判断用新旧密码是否存在
         if passwd and passwd_new:
             passwd_md5 = md5(passwd)        #旧密码进行Md5加密
             passwdnew_MD5 = md5(passwd_new)   #对新密码进行Md5加密
             USER= User.objects.filter(user__exact=user,uid__exact=uid,passwd__exact=passwd_md5)   #查询用户

             if USER:     #判断用户是否存在

                USER.update(passwd=passwdnew_MD5)  #更改密码
                return JsonResponse({"Success":"Successful revision!"})    #返回成功的提示

             else:   #查询不到帐号密码一致的用户信息，则返回
                return JsonResponse({"Error":"User does not exist!"})
         else:    #传入密码为空则返回
             return JsonResponse({"Error":"The password is error!"})
     else:
        #传入帐号和uid为空则返回错误提示
        return JsonResponse({"Error":"The user and uid is empty!"})
