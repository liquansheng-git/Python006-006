'''
作业二：在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
已知有如下函数：
复制代码
 def sendsms(telephone_number: int, content: string, key=None)： 
 # 短信发送逻辑, 作业中可以使用 print 来代替 
 pass 
 # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后 
 pass 
 print("发送成功") 
期望执行结果：
sendsms(12345654321, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 发送成功
…
sendsms(88887777666, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 1 分钟内发送次数超过 5 次, 请等待 1 分钟
sendsms(88887777666, content=“hello”) # 发送成功
'''

import redis

sr = redis.StrictRedis(host='127.0.0.1', 
                       password='redis!@#$')

def sendsms(telephone_number: int, content: str): 
    print('发送消息...')
    count_number = 1
    if sr.get(str(telephone_number) + 'count') is None:
        sr.set(str(telephone_number) + 'count', '1')
    else:
        count_number = (sr.incr(str(telephone_number) + 'count'))
    if count_number <= 5:
        print(f'sendsms({telephone_number}, content="{content}")')
        print(f'发送成功，{telephone_number}用户能够接收到发送的消息是：{content}')
    else:
        print('1 分钟内发送次数超过 5 次, 请等待 1 分钟')
        sr.set(str(telephone_number) + 'count', '5', ex=60)

def main():
    telephone_number = int(input('需要发送的号码是：'))
    content = str(input('发送的消息是：'))
    msg = sr.set(telephone_number, content)
    sendsms(telephone_number, content)

if __name__ == '__main__':
    main()

