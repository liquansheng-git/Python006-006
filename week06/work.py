'''
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
这个类可以使用如下形式为动物园增加一只猫：
复制代码
 if __name__ == '__main__': 
 # 实例化动物园 
 z = Zoo('时间动物园') 
 # 实例化一只猫，属性包括名字、类型、体型、性格 
 cat1 = Cat('大花猫 1', '食肉', '小', '温顺') 
 # 增加一只猫到动物园 
 z.add_animal(cat1) 
 # 动物园是否有猫这种动物 
 have_cat = hasattr(z, 'Cat') 
具体要求：
定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''

from abc import ABCMeta, abstractmethod


# 动物园类
# 要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
class Zoo(object):
    animals = []
    def __init__(self, name):
        self.name = name
    @classmethod
    def add_animal(cls, animal):
        if animal.name in cls.animals:
            print('不要重复添加一个动物！')
        else:
            cls.animals.append(animal.name)
            print(f'添加成功，现有动物：{cls.animals}')  
    
        exec('cls.'+type(animal).__name__+'=True')

# 动物类 不允许实例化 
# 属性：”类型“、“体型”、“性格”、“是否属于凶猛动物” 
# 凶猛动物：体型 >= 中等”并且是“食肉类型”同时“性格凶猛”
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, somatotype, character):
        self.type = type
        self.somatotype = somatotype
        self.character = character

    @property
    def is_ferocious(self):
        if self.type and self.character == '凶猛' and self.somatotype in ('中等', '大型'):
            print('凶猛动物')
            return True
        else:
            print('温顺动物')
            return False



# 猫类 有“叫声”、“是否适合作为宠物”以及“名字”三个属性 其中“叫声”作为类属性 除凶猛动物外都适合作为宠物
class Cat(Animal):
    voice = 'miao~'
    def __init__(self, name, type, somatotype, character):
        self.name = name 
        super().__init__(type, somatotype, character)

    @property
    def is_pet(self):
        if self.character != '凶猛':
            print('作为宠物')
            return True
        else:
            print('不作为宠物')
            return False

    
# 狗类
# 狗类属性与猫类相同
class Dog(Animal):
    voice = 'wowo~'
    def __init__(self, name, type, somatotype, character):
        self.name = name 
        super().__init__(type, somatotype, character)

    @property
    def is_pet(self):
        if self.character != '凶猛':
            print('作为宠物')
            return True
        else:
            print('不作为宠物')
            return False


if __name__ == '__main__':
    zoo = Zoo('时间动物园')
    # 实例化动物
    cat1 = Cat('大花猫 1', '食肉', '小型', '温顺') 
    dog1 = Dog('藏獒', '食肉', '大型', '凶猛')
    print(f'猫叫声{cat1.voice}')
    print(f'狗叫声{dog1.voice}')
    cat1.is_ferocious
    cat1.is_pet
    dog1.is_ferocious
    dog1.is_pet

    # 把动物添加到动物园
    zoo.add_animal(cat1)
    have_cat = hasattr(zoo, 'Cat')
    # 动物园是否有猫这种动物 
    print(have_cat)

    # 不能够添加重复同一个动物
    zoo.add_animal(dog1)
    zoo.add_animal(dog1)
