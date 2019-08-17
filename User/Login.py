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

        #判断帐号和密码是否正确
        if user_ORM:
            #获取用户的所有数据
            Stuts=user_ORM.values() #获取用户的信息(返回数组)
            status=Stuts[0]  #将用户信息转换为字典
            #判断帐号是否为正常状态，0为正常状态
            if status['status'] == 0:
                User.objects.filter(user__exact=user).update(LoginTime=LoginTime1) #更新登陆时间
                uid=User.objects.filter(user__exact=user).values('uid')  #查询用户id
                return HttpResponse(uid) #返回用户id


            else:
                # 如果帐号被冻结则返回错误提示
                return HttpResponse("error,Account number exception!")

        else:
            #如果帐号密码不正确,则返回错误提示
            return HttpResponse("error,Account number or password error!")

    #帐号和密码为空则返回错误
    else:
         return HttpResponse("error,The account number and password are empty！")










