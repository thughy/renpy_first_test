#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import os

# 确保目录存在
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# 创建纯色图像
def create_solid_image(path, width, height, color):
    img = Image.new('RGBA', (width, height), color)
    img.save(path, 'PNG')
    print(f"Created: {path}")

# 创建带边框的图像
def create_frame_image(path, width, height, bg_color, border_color, border_width):
    img = Image.new('RGBA', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 绘制边框
    draw.rectangle(
        [(border_width//2, border_width//2), 
         (width-border_width//2-1, height-border_width//2-1)],
        outline=border_color,
        width=border_width
    )
    
    img.save(path, 'PNG')
    print(f"Created: {path}")

# 主目录
gui_dir = "game/gui"

# 创建按钮图像
button_dir = os.path.join(gui_dir, "button")
ensure_dir(button_dir)

# 按钮状态
create_solid_image(os.path.join(button_dir, "idle.png"), 100, 40, (50, 50, 50, 200))
create_solid_image(os.path.join(button_dir, "hover.png"), 100, 40, (80, 80, 80, 200))
create_solid_image(os.path.join(button_dir, "selected_idle.png"), 100, 40, (70, 70, 100, 200))
create_solid_image(os.path.join(button_dir, "selected_hover.png"), 100, 40, (100, 100, 150, 200))

# 创建滚动条图像
scrollbar_dir = os.path.join(gui_dir, "scrollbar")
ensure_dir(scrollbar_dir)

# 水平滚动条
create_solid_image(os.path.join(scrollbar_dir, "horizontal_idle_bar.png"), 300, 10, (30, 30, 30, 200))
create_solid_image(os.path.join(scrollbar_dir, "horizontal_idle_thumb.png"), 60, 10, (80, 80, 80, 200))
create_solid_image(os.path.join(scrollbar_dir, "horizontal_hover_bar.png"), 300, 10, (40, 40, 40, 200))
create_solid_image(os.path.join(scrollbar_dir, "horizontal_hover_thumb.png"), 60, 10, (120, 120, 120, 200))

# 垂直滚动条
create_solid_image(os.path.join(scrollbar_dir, "vertical_idle_bar.png"), 10, 300, (30, 30, 30, 200))
create_solid_image(os.path.join(scrollbar_dir, "vertical_idle_thumb.png"), 10, 60, (80, 80, 80, 200))
create_solid_image(os.path.join(scrollbar_dir, "vertical_hover_bar.png"), 10, 300, (40, 40, 40, 200))
create_solid_image(os.path.join(scrollbar_dir, "vertical_hover_thumb.png"), 10, 60, (120, 120, 120, 200))

# 创建存档槽图像
slot_dir = os.path.join(gui_dir, "slot")
ensure_dir(slot_dir)

# 存档槽状态
create_frame_image(os.path.join(slot_dir, "idle_background.png"), 300, 150, (20, 20, 20, 200), (50, 50, 50, 255), 2)
create_frame_image(os.path.join(slot_dir, "hover_background.png"), 300, 150, (30, 30, 30, 200), (80, 80, 80, 255), 2)
create_frame_image(os.path.join(slot_dir, "selected_idle_background.png"), 300, 150, (25, 25, 35, 200), (60, 60, 100, 255), 2)
create_frame_image(os.path.join(slot_dir, "selected_hover_background.png"), 300, 150, (35, 35, 45, 200), (90, 90, 140, 255), 2)
create_solid_image(os.path.join(slot_dir, "bottom.png"), 300, 10, (40, 40, 40, 200))

print("所有GUI图像创建完成！")
