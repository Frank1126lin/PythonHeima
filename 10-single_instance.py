#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 09-re_write_new.py
# @Author: Frank1126lin
# @Date  : 5/2/19

class MusicPlayer(object):

	instance = None
	def __new__(cls, *args, **kwargs):
		# 1.判断雷属性是否是空对象
		if cls.instance is None:

			# 2.如果是空对象，为对象分配一个类属性
			cls.instance = super().__new__(cls)
		return cls.instance


	def __init__(self):
		print("播放器初始化")


# 创建播放器对象

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
