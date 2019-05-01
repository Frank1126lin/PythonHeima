#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#@File  : stastic_method.py
#@Author: Frank1126lin
#@Date  : 5/1/19

class Dog():
	# 创建Dog类
	# 定义静态方法
	# 注意： 静态方法不需要传入self对象
	@staticmethod
	def run():
		print("小狗要跑步...")

# 不需要创建实例对象即可调用类的静态方法
Dog.run()
