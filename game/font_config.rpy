################################################################################
# 字体配置
################################################################################

# 这个文件处理游戏中的字体设置

init python:
    # 为中文字符添加字体映射
    config.font_replacement_map = {
        "DejaVuSans.ttf" : "fonts/wqy-microhei.ttc"
    }
    
    # 调整字体一致性设置，改善文本渲染
    style.default.line_spacing = 0
    style.default.line_leading = 2
    
    # 设置默认字体
    if renpy.android or renpy.ios:
        # 移动平台使用默认字体
        style.default.font = "fonts/wqy-microhei.ttc"
    else:
        # 桌面平台使用中文字体
        style.default.font = "fonts/wqy-microhei.ttc"
    
    # 设置断词模式，提高中文文本显示
    style.default.language = "unicode" 