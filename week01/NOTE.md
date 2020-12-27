学习笔记
这一周是开始学习极客时间的Python进阶班，由于白天要进行工作，只能够晚上尽量早些回来听课学习，
之前学习Python是没有人来监督的，现在报班了，就想着有人监督一把，使学习效率高高一些。

整理一下列表、字典、元组、集合数据类型
使用的符号：
    ()：元祖 例：yuanzu = (1,2,3,4)
    []:列表 例：liebiao = [1,2,3,4]
    {}：字典、集合 例：zidian = {'a':123,'b':'apple','c':'456'}  
                    jije = {'apple','pear','apple'}
差异：
列表是可以修改的，而元组是不可修改的。
字典和集合存储的数据都是无序的，每份元素占用不同的内存，其中字典元素以 key-value 的形式保存。

下面是我听课的一些记录：
pip安装加速
升级pip：https://docs.python.org/zh-cn/3.7/whatsnew/3.7.html
vscode 调整代码快捷键：option shift + F

一般开发流程
1.搞清需求
2.编写源代码
3.使用Python解释器转换为目标代码
4.运行程序
5.测试
6.修改错误
7.再运行、测试
8.。。。
迁移部署
虚拟环境的用途和使用方法
如何使用官方文档
注意：
1.在生产环境中虚拟环境是保持环境一致性必备的工具
2.开发环境中可以不配置虚拟环境

虚拟环境可以增加Python的环境
source venv1/bin/activate  --激活虚拟环境

基本的数据类型
高级数据类型
collections 容器数据类型
nametuple() 命名元祖
deque 双端队列
Counter 计数器
OrderedDict 有顺序的字典
常见的Python模块
1.time
2.datetime
3.logging
4.random
5.json
6.pathlib
7.os.path

