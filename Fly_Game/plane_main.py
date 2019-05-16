#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : plane_main.py
# @Author: Frank1126lin
# @Date  : 5/12/19

import pygame
from plane_sprites import *


class PlaneGame(object):
	"""飞机大战主游戏"""

	def __init__(self):
		print("游戏初始化")

		# 1. 创建游戏的窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2. 创建游戏的时钟
		self.clock = pygame.time.Clock()
		# 3. 调用私有方法，创建精灵和精灵组
		self.__creat_sprite()

		# 4. 设置定时器事件， 创建敌机 1s
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)



	def __creat_sprite(self):

		"""创建精灵和精灵组"""
		bg1 = BackGround()
		bg2 = BackGround(True)
		self.back_group = pygame.sprite.Group(bg1, bg2)

		# 创建敌机的精灵组
		self.enemy_group = pygame.sprite.Group()

		# 创建英雄的精灵和精灵组
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

	def __event_handler(self):
		"""事件监听"""

		for event in pygame.event.get():

			# 判断是否退出
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场...")

				# 创建敌机精灵
				enemy = Enemy()

				# 将敌机精灵增加到敌机精灵组
				self.enemy_group.add(enemy)

			# elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			# 	print("向右移动")

		# 使用键盘提供的方法获取键盘按键 - 按键元组
		keys_pressed = pygame.key.get_pressed()
		# 判断元组中对应的按键索引值
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
		else:
			self.hero.speed = 0

	def __check_collide(self):
		"""检测碰撞"""
		pass

	def __update_sprites(self):

		"""更新绘制精灵和精灵组"""
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

	@staticmethod
	def __game_over():
		"""游戏结束"""
		print("游戏结束")

		pygame.quit()
		exit()

	def start_game(self):
		"""游戏开始"""
		print("游戏开始...")

		while True:
			# 1. 设置刷新帧率
			self.clock.tick(FRAME_PER_SECOND)
			# 2. 事件监听
			self.__event_handler()
			# 3. 碰撞检测
			self.__check_collide()
			# 4. 更新/绘制精灵组
			self.__update_sprites()
			# 5. 更新显示
			pygame.display.update()


if __name__ == '__main__':

	# 创建游戏对象
	game = PlaneGame()
	# 启动游戏
	game.start_game()