import logging
import datetime
import pathlib
import os
"""
编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
"""


# 1.写一个函数
def func():
    # 获取当前的时间
    current_time = datetime.datetime.today()
    # print(current_time)
    # 开班时间
    start_time = datetime.datetime(2020,12,21,0,0,0)
    # 学习的天数
    studydays = (current_time - start_time).days + 1
    print("学习Python进阶班%d天..." % studydays)

# 2.调用日志模块
def studylogs():
    p = pathlib.Path()
    current_load = p.resolve()
    current_date_log = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    current_date_file = datetime.datetime.today().strftime('%Y-%m-%d')
# 3.把日志写到/var/log/python- 当前日期 /xxxx.log
    filedir = str(current_load) + "/var/log/"
    filename =  str(current_load) + "/var/log/python-" + current_date_file + ".log"
    # print(filename)
    if os.path.exists(filename):
        logging.basicConfig(filename=filename,
                        level=logging.DEBUG,
                        datefmt= "%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s")
        logging.info("func函数在%s使用" % current_date_log)
    else:
        os.makedirs(filedir)
        os.system(r"touch %s" % filename)

# 防止main函数其他模块调用，首先创建__main__出来
if __name__ == "__main__":
    func()
    studylogs()