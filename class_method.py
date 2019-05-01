#! /usr/bin/env python3
# _*_ conding:utf-8 _*_
# @Author :Frank1126lin
# @Date   :5/1/19
# @File   :class_attribute.py


class Tool(object):

    # 使用赋值语句定义类属性， 记录工具数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具类对象的数量是%d" % cls.count)
        return cls.count

    def __init__(self, name):
        self.name = name

        Tool.count +=1
        print(Tool.count)


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("钉子")

# 2. 输出工具对象的总数
tool3.count = 99
print("工具对象的总数是：%s" % tool3.count)
print("========>> %d" % Tool.count)
Tool.count = 66
print("========>> %d" % Tool.count)
Tool.show_tool_count()

print(Tool.count == Tool.show_tool_count())