"""
张三给李四通过网银转账 100 极客币，现有数据库中三张表：
一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，
转账过程中数据库 crash 等情况需保证数据一致性。
"""
from sqlalchemy.orm import sessionmaker 
import pymysql
from sqlalchemy import create_engine,Column,Integer,String,Enum,Date,Float
# Table, , MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

class Person(object):
    def __init__(self, user_id, name, coin):
        self.user_id = user_id
        self.name = name
        self.coin = coin
    def per_asset(seif):
        print("%s有%d集客币" %(self.name, self.coin))

    def __person_create(self):
        self.person_table = Person_Table(
            user_id = self.user_id,
            name = self.name
        ) 
        dburl="mysql+pymysql://user01:1234@localhost:3306/testdb?charset=utf8mb4"
        engine=create_engine(dburl, echo=True, encoding="utf-8")
        Base.metadata.create_all(engine)
        SessionClass = sessionmaker(bind=engine)
        session = SessionClass()
        session.add(self.person_table)
        session.commit()

    def __asset_table(self):
        self.asset_table = Asset_Table(
            user_id = self.user_id,
            coin = self.coin
        ) 
        dburl="mysql+pymysql://user01:1234@localhost:3306/testdb?charset=utf8mb4"
        engine=create_engine(dburl, echo=True, encoding="utf-8")
        Base.metadata.create_all(engine)
        SessionClass = sessionmaker(bind=engine)
        session = SessionClass()
        session.add(self.person_table)
        session.commit()

        
    def transfer_account(self):
        self.__person_create()
        self.__asset_table()
        print("%s一共有%d" %(self.name, self.coin))
        transfer_coin= input("%s请输入要转多少钱:")
        transfer_name = input("请输入要转给谁：") 
        if self.coin >= transfer_coin:
            remain_coin = self.coin - transfer_coin
            print("%s还剩下多少钱" % self.name )
        else:
            print("不好意思，余额不足，无法完成转账！")
                   
Base = declarative_base()
class Person_Table(Base):
    __tablename__ = 'person'
    user_id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False,unique=True)
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)
class Asset_Table(Base):
    __tablename__ = 'asset'
    user_id = Column(Integer(), primary_key=True)
    coin= Column(Float(), nullable=False)
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)



if __name__ == "__main__":
    user_id = input("请输如id：")
    name = input("请输入姓名：")
    coin = input("请输入充多少极客币：")
    person1 = Person(user_id, name, coin)
    person1.transfer_account()