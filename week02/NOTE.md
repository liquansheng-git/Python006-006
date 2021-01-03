学习笔记
12.29
socket API
socket()
bind()
listen()
accept()
recv()
send()
close()
AF_INEF IPV4地址， SCOK_STREAM TCP协议
Python是后端的开发语言
开发后端开发，会设计模板这个这知识点
对于浏览器上面的如果是HTML就可以直接抓取数据了，如果是加密的一种形式，例如JS，利用Python的库，处理JS的脚步，
写的爬虫，模拟浏览器的行为
 HTTP的状态码：
    1xx 信息响应
    2xx 成功响应
    3xx 重定向
    4xx 客户端响应
    5xx 服务端响应
请求方式：get、post
User-Agent模拟浏览器的请求
爬虫：提出需求，编码，代码run起来，修正和完善
异常的捕获
    异常也是一个类，baseexception，查看异常原因最好是从往下面往上看
__init__ 初始化方法， __str__ 魔术方法 补充：__ 为魔术方法
安装pretty_error，可以让终端输出的信息高亮
1.1
自顶向下设计
什么是自顶像下设计
    从整体分析一个比较复杂的大问题
    分析方法可以重用
    拆分到你能解决的范畴
实战将爬虫代码拆解模拟Scrapy
