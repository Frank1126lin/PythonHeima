#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : fly_game_1.py
# @Author: Frank1126lin
# @Date  : 5/6/19

import pygame
import time

# 游戏的初始化
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 800))

# 屏幕绘制图像
# 1:加载图像数据
bg = pygame.image.load("./jpg/background.png")
# 2:blit 绘制图像
screen.blit(bg, (0, 0))
# # 3:update 更新屏幕显示
# pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./jpg/hero1.png")
# screen.blit(hero, (200, 700))

# # 所有绘制工作完成后，统一调用update方法
# pygame.display.update()

# 游戏循环 -> 意味着游戏的开始
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的位置
hero_rect = pygame.Rect(200, 700, 100, 124)

while True:

	# 可以指定循环内部的代码执行的频率
	clock.tick(60)

	# 修改飞机的位置
	if hero_rect.y <= -124:
		hero_rect.y = 800
	hero_rect.y -=10

	# 调用blit方法绘制图像
	screen.blit(bg, (0, 0))
	screen.blit(hero, hero_rect)

	# 调用update方法更新图像
	pygame.display.update()

# pygame.quit()

