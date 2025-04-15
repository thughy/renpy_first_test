## 游戏的基本配置文件

# 游戏名称
define config.name = "命运之路"

# 开发者名称
define config.developer = "RPG开发者"

# 游戏版本
define config.version = "1.0"

# 游戏窗口的物理尺寸
define gui.init_size = (1280, 720)

# 游戏窗口的标题
define config.window_title = config.name

# 游戏启动时是否自动全屏
define config.default_fullscreen = False

# 默认的文本显示速度（每秒字符数）
define config.default_text_cps = 30

# 音乐和声音的默认音量
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 0.7

# 游戏的主菜单音乐
define config.main_menu_music = None

# 进入和退出游戏菜单时的淡入淡出效果
define config.enter_transition = dissolve
define config.exit_transition = dissolve

# 在游戏菜单之间转换时的淡入淡出效果
define config.intra_transition = dissolve

# 在游戏开始后进入主菜单时的淡入淡出效果
define config.after_load_transition = None

# 在游戏结束后进入主菜单时的淡入淡出效果
define config.end_game_transition = None

# 当Ren'Py显示对话框时使用的特效
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# 保存目录
define config.save_directory = "PathOfDestiny"

# 禁用渲染的更新，以提高性能
define config.gl_resize = False

# 启用硬件视频加速
define config.hw_video = True

# 游戏图标
# define config.window_icon = "gui/window_icon.png" 