import pymysql

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
        sql = "insert into Worker （'id','name','age','birthday','sex','edu'） 
                                values(1,'刘备',30,(1990,1,1),'男','本科'),
                                    (2,'关羽',29,(1991,1,1),'男','本科'),
                                    (3,'张飞',28,(1992,1,1),'男','本科')
                                    ;"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()
except Exception as e:
    print(f"fetch error {e}")

finally:
    db.close()

print(f"{result}")

