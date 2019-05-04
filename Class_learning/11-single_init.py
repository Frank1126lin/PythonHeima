#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 11-single_init.py
# @Author: Frank1126lin
# @Date  : 5/2/19

class MusicPlayer(object):

	instance = None
	init_flag = False
	def __new__(cls, *args, **kwargs):
		# 1.判断雷属性是否是空对象
		if cls.instance is None:

			# 2.如果是空对象，为对象分配一个类属性
			cls.instance = super().__new__(cls)
		return cls.instance


	def __init__(self):
		# 1.判断是否执行过初始化动作
		if MusicPlayer.init_flag:
			return
		# 2.如果没有执行过初始化，那么就执行一次
		print("播放器初始化")

		# 3.初始化完成后， 修改类属性标记
		MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)