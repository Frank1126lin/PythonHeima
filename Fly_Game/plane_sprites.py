#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : plane_sprites.py
# @Author: Frank1126lin
# @Date  : 5/11/19

import random
import pygame

# 调整屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# print(SCREEN_RECT.size)

# 设置刷新帧率
FRAME_PER_SECOND = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT =pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
	"""飞机大战游戏精灵"""

	def __init__(self, image_name, speed=1):

		# 调用父类的初始化方法
		super().__init__()

		# 定义对象的属性
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):

		# 在屏幕的垂直方向上移动
		self.rect.y += self.speed


class BackGround(GameSprite):
	"""游戏背景类"""
	def __init__(self, is_alt=False):

		# 1. 调用父类方法，完成精灵创建（image/rect/speed）
		super().__init__("./jpg/background.png")
		# 2. 判断是否是交替图像，如果是，设置初始位置
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):

		# 1. 调用父类的方法实现
		super().update()
		# 2. 判断是否移出屏幕，如移出，重置于上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height


class Enemy(GameSprite):
	"""敌机精灵"""

	def __init__(self):

		# 1. 调用父类方法，创建敌机精灵， 同时指定敌机图片
		super().__init__("./jpg/enemy0.png")

		# 2. 指定敌机的随机速度
		self.speed = random.randint(1, 3)

		# 3. 指定敌机的随机位置
		self.rect.bottom = 0

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)

	def update(self):

		# 1. 调用父类方法， 保持垂直方向飞行
		super().update()

		# 2. 判断是否飞出屏幕， 如果是， 需要从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:
			# print("敌机飞出屏幕， 需要从精灵组删除...")
			# kill 方法可以讲精灵从精灵组删除，精灵就会被自动销毁
			self.kill()

	def __del__(self):
		# print("敌机歼灭 %s " % self.rect)
		pass


class Hero(GameSprite):
	"""开发英雄类"""

	def __init__(self):

		# 1. 调用父类方法，设置image&speed
		super().__init__("./jpg/hero1.png", 0)

		# 2. 设置英雄的初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.y = SCREEN_RECT.bottom - 120

	def update(self):

		# 英雄在水平方向移动
		self.rect.x += self.speed

		# 控制英雄不能离开屏幕
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
