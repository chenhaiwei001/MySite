from django.urls import path
from User.views import register,Login,change

urlpatterns = [
    path("register/", register.register),  #注册接口
    path("login/",Login.login),        #登陆接口
    path("change/",change.change),     #更改密码

]
