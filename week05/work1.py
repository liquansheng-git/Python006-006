'''
需求描述:
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
请实现以下函数：
复制代码
 counter() 
 def counter(video_id: int): 
 ... 
 return count_number 
函数说明:
counter 函数为统计视频播放次数的函数，每调用一次，播放次数 +1
参数 video_id 每个视频的 id，全局唯一
基于 redis 实现自增操作，确保线程安全
期望执行结果：
conuter(1001) # 返回 1
conuter(1001) # 返回 2
conuter(1002) # 返回 1
conuter(1001) # 返回 3
conuter(1002) # 返回 2
…
'''

import redis

# 连接redis数据库
sr = redis.StrictRedis(host='127.0.0.1', 
                       password='redis!@#$')
def tag():
    return (str(1000 + i) for i in range(10))

tag = tag()

def counter(video_id: int):
    if 1001 <= video_id <= 1010:
        # 如果key不存在，那么key的值会先被初始化为0，然后再执行incr操作
        count_number = (sr.incr(video_id))
        print(f'当前counter()统计 {video_id} 播放了 {count_number} 次')
        print(sr.keys())
        return count_number 
    else:
        print('目前只有id为1001-1010的电影，请输入1001-1010的数字！')

if __name__ == '__main__':
    try:
        count_number = int(input('请输入电影的id：'))
        counter(count_number)
    except Exception as e:
        print(e)