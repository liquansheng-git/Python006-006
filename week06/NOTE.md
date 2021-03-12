学习笔记
1.类属性与对象属性
    类是什么东西
    接触类的时候 婴儿时期
    积木是对象
    属性
    不同作用域 定义了什么属性
    父类 object类
    查询属性__dict__
    一切皆对象

2.类的属性作用域
    setattr增加一些内置属性
    __init__ 

3.类方法描述器
    @ 语法糖
    三种方法
        普通方法 self
        类方法 cls参数
        静态方法 由类调用，无参数
    __init__ 初始化函数

4.静态方法描述器
    静态方法，StaticMethod方法
    django的静态方法怎么写的

5.描述高级应用__getattrbute__
    存在的属性返回取值
    super，当前实例的父类
    不存在的属性会有相应的属性值

6.描述器高级应用__getattr__
    getattr定义的是取不到属性值，设置的函数
    getattr和getattrbute同时存在时的执行顺序

7.描述器原理&属性描述器
    举例实现HTTP协议
    描述器：实现特定协议（描述符）的类
    self实例本身
    属性描述符 @property
        property类需要实现 __get__ __set__ __delete__
        property的优点
    设置明文密码    

8.面向对象编程-继承
    missing
    Python2的类为经典类 Python3为新式类
    object为基类
    type这个类 是元类
    类的继承
        单一继承
        多重继承 继承多个类 有相同技能的情况
        菱形继承（钻石继承）
        MRO的C3算法
    左右类
    多重继承的顺序问题

9.solid设计原则与设计模式&单例模式
    设计模式 造桥
    五个字母对应的设计原则
    SOLID设计原则
    S.O.L.I.D是面向对象设计和编程(OOD&OOP)中几个重要编码原则(Programming Priciple)的首字母缩写。
    简写	            全拼	                   中文翻译
    SRP	 The Single Responsibility Principle	单一责任原则
    OCP	 The Open Closed Principle	            开放封闭原则
    LSP	 The Liskov Substitution Principle	    里氏替换原则
    DIP	 The Dependency Inversion Principle	    依赖倒置原则
    ISP	 The Interface Segregation Principle    接口分离原则
    构造函数 __new__ 

10.工厂模式
    设计模式22个
    简单的工厂模式
    动态工厂模式
    工厂角色
    抽象产品角色
    具体产品角色
    动态的创建类

11.元类
    创建类的类，是类的模板
    创建元类的两种方法
        type
        class
    元类要求，必须继承自type
        元类要求，必须实现new方法

12.mixin模式
    元类在框架中比较常用
    抽象基类 好处：三个好处
    mixin重定向类的继承
        动态改变继承的关系

        