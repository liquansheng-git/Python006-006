import pymysql
from datetime import datetime

db = pymysql.connect(
        host="127.0.0.1", 
        port=3306, 
        user="user01", 
        passwd="1234", 
        db="testdb", 
        charset='utf8mb4', 
)
try:
    with db.cursor() as cursor:
        sql = "insert into worker (id,name,age,birthday,sex,edu,create_on,update_on) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        value1 = (2,'刘备',30,'1990,1,1','男','本科',datetime.now(), datetime.now())
        value2 = (3,'关羽',29,'1991,1,1','男','本科',datetime.now(), datetime.now())
        value3 = (4,'张飞',28,'1992,1,1','男','本科',datetime.now(), datetime.now())
                                    
        cursor.execute(sql,value1)
        cursor.execute(sql,value2)
        cursor.execute(sql,value3)
        result = cursor.fetchone()
        print(f"{result}")
    db.commit()
except Exception as e:
    print(f"fetch error {e}")

finally:
    db.close()



