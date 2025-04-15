################################################################################
# 屏幕和界面
################################################################################

################################################################################
# 初始化
################################################################################

init offset = -1

################################################################################
# 菜单导航样式
################################################################################

style default:
    font "fonts/wqy-microhei.ttc"
    size 24
    color "#ffffff"
    language "unicode"
    outlines [ (1, "#000000", 0, 0) ]

style input:
    color "#ffffff"
    adjust_spacing False

style hyperlink_text:
    color "#0099cc"
    hover_underline True

style gui_text:
    color "#ffffff"

style button:
    background Frame("gui/button/idle.png", 5, 5, 5, 5)
    hover_background Frame("gui/button/hover.png", 5, 5, 5, 5)
    padding (20, 10)
    xsize 300

style button_text is gui_text:
    color "#888888"
    hover_color "#66c1e0"
    selected_color "#ffffff"
    yalign 0.5
    font "fonts/wqy-microhei.ttc"
    outlines [ (1, "#000000", 0, 0) ]

style label_text is gui_text:
    color "#0099cc"

style prompt_text is gui_text:
    color "#ffffff"

################################################################################
# 游戏内菜单
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    # 如果有对话框图像，显示它
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 0.99
    ysize 185

    background Frame("gui/textbox.png", 25, 25, 25, 25)

style namebox:
    xpos 240
    xanchor 0.0
    xsize 168
    ypos 0
    ysize 39

    background Frame("gui/namebox.png", Borders(5, 5, 5, 5), tile=False, xalign=0.0)
    padding (5, 5, 5, 5)

style say_label:
    color "#ffffff"
    xalign 0.0
    yalign 0.5

style say_dialogue:
    xpos 268
    xsize 744
    ypos 50

################################################################################
# 游戏主菜单
################################################################################

screen main_menu():
    tag menu

    style_prefix "main_menu"

    add Solid("#000000")  # 使用纯黑色背景

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text _("命运之路") style "main_menu_title"

        textbutton _("开始游戏") action Start() xalign 0.5
        textbutton _("载入游戏") action ShowMenu("load") xalign 0.5
        textbutton _("设置") action ShowMenu("preferences") xalign 0.5
        textbutton _("关于") action ShowMenu("about") xalign 0.5
        textbutton _("帮助") action Help() xalign 0.5
        textbutton _("退出") action Quit(confirm=not main_menu) xalign 0.5

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset 0
    xmaximum 800
    yalign 0.5
    yoffset 0

style main_menu_text:
    color "#ffffff"
    xalign 0.5

style main_menu_title:
    color "#fff"
    outlines [ (2, "#000", 0, 0) ]
    size 45
    font "fonts/wqy-microhei.ttc"
    xalign 0.5

################################################################################
# 游戏菜单通用样式
################################################################################

style menu_header:
    variant "small"
    ysize 90

################################################################################
# 确认屏幕
################################################################################

screen confirm(message, yes_action, no_action):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

style confirm_frame is default
style confirm_prompt is default
style confirm_prompt_text is default
style confirm_button is button
style confirm_button_text is button_text

################################################################################
# 选择菜单
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22
        
        for i in items:
            textbutton i.caption:
                action i.action
                xminimum 400
                xmaximum 900
                xalign 0.5

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 22

style choice_button:
    background Frame("gui/button/idle.png", 5, 5, 5, 5)
    hover_background Frame("gui/button/hover.png", 5, 5, 5, 5)
    xalign 0.5
    padding (20, 10)

style choice_button_text:
    color "#888888"
    hover_color "#66c1e0"
    selected_color "#ffffff"
    xalign 0.5
    size 24
    font "fonts/wqy-microhei.ttc"
    outlines [ (1, "#000", 0, 0) ]

################################################################################
# 快速菜单
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

################################################################################
# 统计屏幕（用于显示角色状态）
################################################################################

screen stats():
    modal False
    zorder 200

    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 20
        background Solid("#22222299")

        vbox:
            spacing 10
            xsize 200

            text _("玩家状态") xalign 0.5 size 20

            text _("姓名: [player_name]")
            text _("力量: [player_strength]")
            text _("智力: [player_intelligence]")
            text _("魅力: [player_charisma]")
            text _("生命值: [player_health]")
            text _("金币: [player_gold]")

            null height 10

            text _("装备:") xalign 0.5

            if has_sword:
                text _("- 剑")
            if has_shield:
                text _("- 盾")
            if has_potion:
                text _("- 药水")
            if has_magic_scroll:
                text _("- 魔法卷轴")
            if has_ancient_key:
                text _("- 古老钥匙")
            if has_destiny_heart:
                text _("- 命运之心")

################################################################################
# 关于屏幕
################################################################################

screen about():
    tag menu
    style_prefix "about"
    
    add Solid("#000000")
    
    frame:
        style "about_frame"
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        
        vbox:
            spacing 20
            
            label _("{b}关于 命运之路{/b}"):
                xalign 0.5
            
            text _("命运之路是一款角色扮演冒险游戏，玩家将踏上一段充满挑战与选择的旅程。")
            text _("版本: 1.0.0")
            text _("开发者: 游戏开发团队")
            text _("© 2025 版权所有")
            
            null height 20
            
            textbutton _("返回") action Return() xalign 0.5

style about_frame is default
style about_label is default
style about_text is default
style about_button is default
style about_button_text is default

style about_frame:
    background Solid("#222222")
    xsize 600

style about_label_text:
    color "#ffffff"
    size 30
    xalign 0.5

style about_text:
    color "#cccccc"
    size 22
    xalign 0.5

style about_button:
    xalign 0.5

style about_button_text:
    xalign 0.5

################################################################################
# 初始化默认界面
################################################################################

init python:
    # 基本常量定义
    config.thumbnail_width = 160
    config.thumbnail_height = 120

    # 定义UI界面所需的默认参数
    gui.init(1280, 720)

    # 定义文本大小
    gui.text_size = 24
    gui.title_text_size = 45
    
    # 定义对话框位置和大小
    gui.textbox_height = 185
    gui.textbox_yalign = 0.99
    
    # 定义名字框的位置和大小
    gui.name_xpos = 240
    gui.name_ypos = 0
    gui.name_xalign = 0.0
    gui.namebox_width = 168
    gui.namebox_height = 39
    gui.namebox_borders = Borders(5, 5, 5, 5)
    gui.namebox_tile = False
    
    # 定义对话框文本的位置和大小
    gui.dialogue_xpos = 268
    gui.dialogue_width = 744
    gui.dialogue_ypos = 50
    
    # 定义对话框的边框
    gui.textbox_borders = Borders(25, 25, 25, 25)
    
    # 定义菜单按钮间距
    gui.choice_spacing = 22
    
    # 定义语言（默认为中文）
    gui.language = "unicode"
    
    # 为可能缺失的函数提供默认实现
    gui.text_properties = lambda prefix="", accent=False: {}
    gui.button_properties = lambda prefix="": {}
    gui.button_text_properties = lambda prefix="": {} 