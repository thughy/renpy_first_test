################################################################################
# GUI配置
################################################################################

init python:
    ######### 定义主要颜色 #########
    gui.accent_color = '#0099cc'
    gui.idle_color = '#888888'
    gui.hover_color = '#66c1e0'
    gui.selected_color = '#ffffff'
    gui.insensitive_color = '#5555557f'
    gui.interface_text_color = '#ffffff'
    gui.button_text_idle_color = '#888888'
    gui.button_text_hover_color = '#66c1e0'
    gui.button_text_selected_color = '#ffffff'
    
    ######### 创建基本GUI图像 #########
    # 这些是为了让游戏能运行而创建的最小化GUI图像
    # 实际项目中应该替换为真实美术资源
    
    # 创建纯色背景
    gui.main_menu_background = Solid("#000000")
    
    # 创建对话框背景
    gui.textbox_bg = Frame(Solid("#222222"), 25, 25)
    
    # 创建名称框背景
    gui.namebox_bg = Frame(Solid("#444444"), 5, 5)
    
    # 创建确认界面背景
    gui.overlay_bg = Solid("#00000080")
    
    # 创建状态屏幕背景
    gui.stats_bg = Frame(Solid("#22222299"), 10, 10)
    
    # 创建按钮背景
    gui.button_idle = Frame(Solid("#444444"), 5, 5)
    gui.button_hover = Frame(Solid("#666666"), 5, 5)
    gui.button_selected = Frame(Solid("#0099cc"), 5, 5)
    
    ######### 覆盖基础图像 #########
    # 用Python重新定义图像
    renpy.image("gui/textbox.png", gui.textbox_bg)
    renpy.image("gui/namebox.png", gui.namebox_bg)
    renpy.image("gui/overlay/confirm.png", gui.overlay_bg)
    renpy.image("gui/overlay/main_menu.png", Solid("#00000000"))
    renpy.image("gui/stats_bg.png", gui.stats_bg)
    
    # 定义按钮图像
    renpy.image("gui/button/idle.png", gui.button_idle)
    renpy.image("gui/button/hover.png", gui.button_hover)
    renpy.image("gui/button/selected_idle.png", gui.button_selected)
    renpy.image("gui/button/selected_hover.png", gui.button_selected)
    
    ######### 字体设置 #########
    # 使用系统默认字体
    gui.default_font = ""
    
    # 主菜单转场特效
    gui.main_menu_transition = dissolve
    
    # 游戏菜单转场特效
    gui.game_menu_transition = dissolve
    
    # 自定义文本属性函数
    def text_properties(prefix="", accent=False):
        """
        返回文本样式的属性字典。
        """
        properties = {}
        
        if prefix:
            properties["color"] = gui.accent_color if accent else gui.interface_text_color
        
        properties["font"] = gui.default_font
        properties["size"] = 24
        
        return properties
    
    # 自定义按钮属性函数
    def button_properties(prefix=""):
        """
        返回按钮样式的属性字典。
        """
        properties = {}
        properties["background"] = "gui/button/idle.png" 
        properties["hover_background"] = "gui/button/hover.png"
        
        return properties
    
    # 自定义按钮文本属性函数
    def button_text_properties(prefix=""):
        """
        返回按钮文本样式的属性字典。
        """
        properties = {}
        properties["color"] = gui.button_text_idle_color
        properties["hover_color"] = gui.button_text_hover_color
        properties["selected_color"] = gui.button_text_selected_color
        
        return properties

# 定义按钮样式
init:
    style button:
        background "gui/button/idle.png"
        hover_background "gui/button/hover.png"
        selected_background "gui/button/selected_idle.png"
        selected_hover_background "gui/button/selected_hover.png" 