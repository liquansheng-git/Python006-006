学习笔记
框架的介绍
Django最新3.0班班，目前比较多的是2.2.13(LTS)
安装命令：
pip install --upgrade django==2.2.13
使用：
import django
django.__version
推荐使用Django web2.2版本

1.16
URL正则和自定义过滤器
    日期
    字符的转化
    URL的匹配

view视图快捷方式
    处理用户的请求
    数值返回
    view视图 响应类型（说明）
    Diango的快捷函数 
        render()  url()
        rederct()

用orm创建数据库
    操作数据库
    模型与数据库
    typename
    创建表
    遇到的问题：找不到MySQL文件
    pymysql替换mymqldb
    加上mysql的环境变量
    在setting文件找到mysql的配置
    desc [表名]

ORM API
    字段的类型 autofield
    manger.py 可以启动shell的功能 启动可以进入交互模式
    models   直接查询ame  update修改了会返回修改的行数
    fiter where 

Djangp模块开发
    模板 模板语言 变量 内容 for遍历
    url的传指
    template

展示数据库中的内容
    获取本地的变量  
    取出属性

豆瓣页面展示功能的需求分析
    爬虫数据的采集
    传变量到template 
    实现的界面
    实现的想法
    豆瓣的书评展示
    urlconf的处理 先做index 通过manger.py把豆瓣和DJango结合
    前面加/会报错，后面加/，有进行拼接
    正向创建表，反向创建表
    mata类，元数据，不属于任何字段数据

views视图的编写
    会生成.sql文件
    django检索的功能
    Quaryset
    filter要怎么用 判断条件
    取得正向和负向的数量
    queryset的聚合函数

结合bootstrap模板进行开发
    前端内容的开发
    左边管理工具，右边是一系列功能
    四个卡片，根据页面动态变化
    ajax

如何阅读Django的源代码
    程序的入库 哪一个程序先运行
    main函数
    根据功能分析

manger.py源码分析
    跟踪路径 追踪分析    
    fetch_command








