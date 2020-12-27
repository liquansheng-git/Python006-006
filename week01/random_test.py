import random

a = random.random()
print(a)  
# 步长为2的随机数
b = random.randrange(0, 100, 2)
print(b)

c = random.sample([1, 2, 3, 4, 5], k = 4)
print(c)