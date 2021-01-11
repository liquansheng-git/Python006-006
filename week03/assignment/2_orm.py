"""
使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
"""

from sqlalchemy.orm import sessionmaker 
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey,Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class Worker(Base):
    __tablename__ = 'Worker'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(String(), nullable=False)
    edu = Column(Enum("中学", "专科","本科", "硕士", "博士"))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)

    def __repr__(self):
        return "work(id='{self.id}', " \
        "name={self.name})".format(self=self)

dburl="mysql+pymysql://root:1234@localhost:3306/testdb?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

worker1 = Worker(id= 1,
                name="小明",
                age=18,
                # birthday=datetime(1990, 1, 1),
                sex="男",   
                edu="本科"
                )
print(worker1)
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
session.add(worker1)
session.commit()