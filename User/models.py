from django.db import models

#用户帐号信息表
class User(models.Model):
    uid=models.AutoField(primary_key=True)        #用户唯一id,自增型
    user=models.TextField()                       #用户帐号，登陆及识别号，不允许重复
    passwd=models.TextField()                     #用户密码，MD5加密后存储
    name=models.TextField(default="")             #用户昵称，可以是中文
    email=models.TextField()                      #用户邮箱，用于收发邮件及验证码
    CreateTime=models.TextField()                 #帐号创建时间，作为信息记录(时间戳)
    LoginTime=models.TextField()                  #最后一次登陆时间（日期格式）
    status = models.IntegerField(max_length=8,default='0')  # 帐号状态，0为正常，1为冻结，2为注销

    #表名
    class Meta:
        db_table='User'