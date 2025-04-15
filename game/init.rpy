################################################################################
# 游戏初始化
################################################################################

# 为了解决当图像文件是文本注释时的问题，我们用纯色替代缺失的图像
init -10 python:
    # 角色图像替代函数
    def character_placeholder(name, color="#ffffff"):
        return Solid(color, xsize=300, ysize=500)
    
    # 背景图像替代函数
    def background_placeholder(color="#333333"):
        return Solid(color, xsize=1280, ysize=720)

# 检查并替换缺失的角色图像
init -5 python:
    import os
    
    # 角色图像列表
    character_images = [
        ("images/elder_normal.png", "#c8c8ff"),
        ("images/merchant_normal.png", "#ffc8c8"),
        ("images/warrior_normal.png", "#ff8c8c"),
        ("images/mage_normal.png", "#8c8cff"),
        ("images/guardian_normal.png", "#ffcc00"),
        ("images/ghost_normal.png", "#aaaaff")
    ]
    
    # 检查每个角色图像
    for img_path, color in character_images:
        full_path = os.path.join(config.gamedir, img_path)
        try:
            if not os.path.isfile(full_path) or os.path.getsize(full_path) < 100:
                # 如果文件不存在或大小太小（可能只是注释），用纯色替代
                renpy.image(img_path, character_placeholder(img_path, color))
        except:
            # 出错时也用纯色替代
            renpy.image(img_path, character_placeholder(img_path, color))

# 检查并替换缺失的背景图像
init -5 python:
    # 背景图像列表
    background_images = [
        ("images/backgrounds/bg_village.jpg", "#4a6f3f"),  # 村庄：绿色
        ("images/backgrounds/bg_forest.jpg", "#1a4a1a"),   # 森林：深绿色
        ("images/backgrounds/bg_cave.jpg", "#333344"),     # 洞穴：深蓝灰色
        ("images/backgrounds/bg_castle.jpg", "#666677"),   # 城堡：灰色
        ("images/backgrounds/bg_ruins.jpg", "#554433"),    # 遗迹：棕色
        ("images/backgrounds/bg_throne.jpg", "#775544")    # 王座：红棕色
    ]
    
    # 检查每个背景图像
    for img_path, color in background_images:
        full_path = os.path.join(config.gamedir, img_path)
        try:
            if not os.path.isfile(full_path) or os.path.getsize(full_path) < 100:
                # 如果文件不存在或大小太小（可能只是注释），用纯色替代
                renpy.image(img_path, background_placeholder(color))
        except:
            # 出错时也用纯色替代
            renpy.image(img_path, background_placeholder(color))

# 定义通用定时器
init python:
    # 定义通用延迟函数，用于游戏中的定时效果
    def delay_callback(st, at, duration=1.0):
        if st > duration:
            return None
        return 0.0
    
    # 注册状态屏幕，让它在游戏中显示
    config.overlay_screens.append("stats") 