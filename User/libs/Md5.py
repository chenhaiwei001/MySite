import hashlib         #导入hashlib模块

def md5(data):
    da=str(data)    #传入数据转换成字符串
    md5 = hashlib.md5()    #创建一个md5对像
    md5.update(da.encode("utf-8"))  #对数据进行加密
    md5_result = md5.hexdigest()    #获取加密后的数据
    return md5_result      #返回加密后的md5

'''
 1、该模块只针对传入的数据进行加密
 2、内部对数据进行字符串转换处理，所以可以传入非字符串数据
'''