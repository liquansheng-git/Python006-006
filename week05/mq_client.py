import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)

# 阻塞方法
connection = pika.BlockingConnection(parameters) 
# 建立信道
channel = connection.channel()
# 声明消息队列 
channel.queue_declare(queue='direct_demo', durable=False)

channel.basic_publish(exchange='', routing_key='direct_demo',
                      body='send message to rabbitmq' )       

# 关闭与rabbitmq server的连接
connection.close()