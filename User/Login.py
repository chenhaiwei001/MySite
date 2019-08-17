from django.http import HttpResponse
from User.models import User  #导入用户表
from User.libs.Md5 import md5  #MD5加密
import datetime     #时间模块


#用户登陆模块
def login(request):
    user = request.POST.get("user")  # 获取用户名，必填参数
    passwd = request.POST.get("passwd")  # 获取密码，必填参数
    LoginTime1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   #获取当前日期时间
    # #判断帐号和密码是否为空
    if user and passwd:
         #如果帐号和密码都存在，则：
        passwd_md5=md5(passwd)  #对密进行MD5加密
        user_ORM=User.objects.filter(user=user,passwd=passwd_md5)  #查询帐号和密码都相等的数据
        passwd_ORM=User.objects.filter(passwd__exact=passwd_md5)  #查询密码是否正确

        #判断帐号和密码是否正确
        if user_ORM:
            Status = User.objects.filter(user__exact=user).values('status')
            print(Status)
            return HttpResponse(Status)
            # if status == 0:
            #     #更新登陆时间
            #     User.objects.filter(user__exact=user).update(LoginTime=LoginTime1)
            #     uid=User.objects.filter(user__exact=user).values('uid')
            #     return HttpResponse(uid)
            # else:
            #     return HttpResponse("error,Account number exception!")

        else:
            return HttpResponse("error,Account number or password error!")

    #帐号和密码为空则返回错误
    else:
         return HttpResponse("error,The account number and password are empty！")










