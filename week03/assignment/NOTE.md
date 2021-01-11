学习笔记
1.4
关系型数据库--MySQL
    安装
        企业级MySQL部署在Linux操作系统上，需要注意的重点：
            1.注意操作系统的平台（32、64位）
            2.注意安装的MySQL的版本（MySQL企业版、社区版、MariaDB）
            3.注意安装后避免yum自动更新--生产环境会把yum源取消
            4.注意数据库的安全性

1.5 
查看字符集：
    MariaDB [(none)]> show variables like '%character%';
查看校对规则：
    MariaDB [(none)]> show variables like '%character%';

注意:MySQL中的utf8不是UTF-8字符集
显示utf8mb4就是utf-8
重置后要重启mysql
_ci大小写不敏感 _cs大小敏感 默认_ci

MariaDB [(none)]> show create database testdb;
+----------+--------------------------------------------------------------------+
| Database | Create Database                                                    |
+----------+--------------------------------------------------------------------+
| testdb   | CREATE DATABASE `testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ |
+----------+--------------------------------------------------------------------+
1 row in set (0.000 sec)

1.10
Python连接MySQL的方法
    统一概念：连接器、绑定、binding
    Python的语言：Python database API、DB-API
    注意MySQLdb是Python2.0的包，适用于MySQL5.5和Python2,7

Python3连接MySQL”
    Python安装的MySQLdb包叫做mysqlclient，加载的依然是MySQLdb
        pip install mysqlclient
    其他DB-API：
        pip3 install pymysql  #流行度最高
        pip3 install mysql-connector-python #MySQL官方
    使用orm，代表更先进的生产力
        pip3 install sqlalchemy（其中一种，还有Django框架）
SQL 函数有哪些？
    算术函数、字符串函数、日期函数、转换函数、聚合函数
