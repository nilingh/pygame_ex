#!/usr/bin/env python3

import pygame
# 导入pygame库

from sys import exit
# 向sys模块借一个exit函数用来退出程序
from os import path

# 生成随机数
import random


# 设置图片目录
main_path = path.dirname(__file__)
assets_folder = path.join(main_path, 'data')

print(assets_folder)

# 初始化pygame,为使用硬件做准备
pygame.init()

# 创建了一个窗口
screen = pygame.display.set_mode((1300, 876), 0, 32)

# 设置窗口标题
pygame.display.set_caption("Catch me if you can")

# 导入背景图
bg_img = path.join(assets_folder, 'cat_bg.jpg')
background = pygame.image.load(bg_img).convert()


def rand_cats(cat_list):
    """ 随机得到一只猫"""
    i = random.randint(0, len(cat_list) - 1)
    cat_img = path.join(assets_folder, cat_list[i])
    cat = pygame.image.load(cat_img).convert_alpha()
    return cat


# 讲话用的字体
font_name = pygame.font.SysFont('comicsansms', 72)

text = font_name.render('Meow~', True, (0, 128, 0))


# 就这么几只猫
cats = ['fun_cat1.jpg', 'fun_cat2.jpg',
        'fun_cat3.jpg', 'fun_cat4.jpg', 'fun_cat5.jpg']

# 将背景图画上去
screen.blit(background, (0, 0))
mouse_cursor = rand_cats(cats)
screen.blit(mouse_cursor, (random.randint(0, 1000), random.randint(0, 700)))

while True:
    """ 游戏主循环"""

    pygame.display.update()

    # 等待输入
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        # 接收到退出事件后退出程序
        exit()
    elif event.type == pygame.MOUSEBUTTONUP:
        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()
        # 准备下一个猫
        mouse_cursor = rand_cats(cats)

        # 获取猫头的尺寸
        width = mouse_cursor.get_width()
        height = mouse_cursor.get_height()

        # 获得新的随机位置
        if x < 650:
            x = random.randint(650, 1300 - width)
            y = random.randint(0, 876 - height)
        else:
            x = random.randint(0, 650 - width)
            y = random.randint(0, 876 - height)

        # 画新猫
        screen.blit(background, (0, 0))
        screen.blit(mouse_cursor, (x, y))
        screen.blit(text, (x, y))

    else:
        pass
