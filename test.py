from sqlalchemy import create_engine #连接mysql函数
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer  #导入数据库类型

engine = create_engine("mysql+pymysql://root:bai940126@111.67.196.17/Mysite",encoding="utf-8",echo=True)
Base = declarative_base() #生成orm基类
class User(Base): #继承生成的orm基类
    __tablename__ = "sql_test" #表名
    id = Column(Integer,primary_key=True) #设置主键
    user_name = Column(String(32))
    user_password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构