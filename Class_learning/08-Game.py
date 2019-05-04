#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 08-Game.py
# @Author: Frank1126lin
# @Date  : 5/2/19


class Game(object):


# 历史最高分
	top_score = 0


	def __init__(self, player_name):
		self.name = player_name


	@staticmethod
	def show_help():
		print("帮助信息：========>>")


	@classmethod
	def show_topscore(cls):
		print("历史最高分：%d" % cls.top_score)


	def start_game(self):
		print("%s开始游戏：======>>>>" % self.name)


# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_topscore()

# 3.创建游戏对象并开始游戏
game = Game("张三")
game.start_game()
