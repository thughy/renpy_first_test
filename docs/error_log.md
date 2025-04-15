# Ren'Py 项目错误记录

本文档记录了《命运之路》RPG游戏项目开发过程中遇到的各种错误以及相应的解决方案，以避免未来重复出现类似问题。

## 1. 环境相关问题

### 1.1 Apple Silicon 兼容性问题

**错误现象**：
```
/Users/ghy/renpy/renpy-8.3.7-sdk/lib/py3-mac-universal/renpy not found.
This game may not support the mac-universal platform.
```

**原因**：
Ren'Py 8.3.7在Apple Silicon (M1/M2/M3) Mac上运行时，需要正确的二进制文件路径，但复制安装过程中出现问题，导致某些必要文件缺失或扩展名不正确。

**解决方案**：
1. 我们尝试创建符号链接解决问题：
   ```bash
   cd ~/renpy/renpy-8.3.7-sdk/lib/py3-mac-universal
   ln -s renpy.macho renpy
   ln -s python.macho python
   ```

2. 最终通过直接使用应用程序包中的二进制文件解决：
   ```bash
   ~/renpy/renpy-8.3.7-sdk/renpy.app/Contents/MacOS/renpy /path/to/game
   ```

## 2. 语法错误

### 2.1 `gui.rpy` 中的 `define` 语句错误

**错误现象**：
```
File "game/gui.rpy", line 61: invalid syntax
    define gui.main_menu_transition = dissolve
            ^
```

**原因**：
在Python代码块内不能使用Ren'Py的`define`语句，它必须在代码块外使用。

**解决方案**：
在Python代码块内将`define`语句改为常规Python赋值：
```python
# 错误写法
define gui.main_menu_transition = dissolve

# 正确写法 (Python代码块内)
gui.main_menu_transition = dissolve

# 或 (Python代码块外)
define gui.main_menu_transition = dissolve
```

### 2.2 样式属性中缺少括号的语法错误

**错误现象**：
```
File "game/screens.rpy", line 94: expected 'word' not found.
    padding 5, 5, 5, 5
```

**原因**：
Ren'Py中，多值参数需要用括号括起来。

**解决方案**：
```python
# 错误写法
padding 5, 5, 5, 5

# 正确写法
padding (5, 5, 5, 5)
```

## 3. 引用错误

### 3.1 引用不存在的 `gui` 属性

**错误现象**：
```
AttributeError: 'StoreModule' object has no attribute 'language'
```

**原因**：
代码中引用了`gui.language`属性，但在`gui.rpy`中没有定义这个属性。

**解决方案**：
1. 添加缺失的属性定义：
   ```python
   gui.language = "unicode"
   ```

2. 或者直接使用字符串字面量：
   ```python
   language "unicode"  # 替代 language gui.language
   ```

### 3.2 引用未定义的样式

**错误现象**：
```
NameError: name 'accent_color' is not defined
```

**原因**：
代码中使用了`gui.text_properties()`等函数，但这些函数在实现中引用了未定义的变量。

**解决方案**：
1. 实现我们自己版本的这些函数：
   ```python
   def text_properties(prefix="", accent=False):
       properties = {}
       properties["color"] = gui.accent_color if accent else gui.interface_text_color
       properties["font"] = gui.default_font
       return properties
   ```

2. 或者简化样式定义，不使用这些函数：
   ```python
   style default:
       font None
       size 24
       color "#ffffff"
       language "unicode"
   ```

## 4. 资源文件问题

**错误现象**：
```
Style style.namebox, property background uses file 'gui/namebox.png', which is not loadable.
```

**原因**：
代码引用了不存在的图像文件，或者图像文件是文本文件而非实际图像。

**解决方案**：
1. 使用`init.rpy`中的代码动态创建这些图像：
   ```python
   # 在gui.rpy中
   gui.namebox_bg = Frame(Solid("#444444"), 5, 5)
   
   # 覆盖基础图像
   renpy.image("gui/namebox.png", gui.namebox_bg)
   ```

2. 这样可以避免要求实际文件存在，而是使用代码生成的图像。

## 5. 最佳实践

1. **使用正确的 API 写法**：避免混合使用Ren'Py风格和Python风格的代码，特别是在不同的上下文中。

2. **简化依赖**：尽量使用直接的属性赋值，而非引用可能不存在的变量或函数。

3. **Lint 检查**：在提交之前始终运行`lint`检查：
   ```bash
   renpy.sh /path/to/game lint
   ```

4. **使用占位图像**：对于需要但实际不存在的图像，使用动态生成的纯色图像代替，避免加载错误。

5. **初始化顺序**：注意`init`块的执行顺序，确保变量在被引用前已定义。

## 6. 字体问题

### 6.1 中文字体显示问题

**错误现象**：
```
Exception: Could not find font 'Arial Unicode MS'.

While running game code:
Exception: Could not find font 'Arial Unicode MS'
```

**原因**：
系统找不到指定的字体文件。在游戏开始界面可以正常显示，但进入游戏后报错，这表明不同的界面可能使用了不同的字体配置，或者某些特定的游戏元素使用了未正确配置的字体。

**尝试的解决方案**：
1. 使用系统字体 PingFang SC：
   ```python
   style.default.font = "PingFang SC"
   ```
   结果：游戏开始界面正常，但进入游戏后仍然报错。

2. 使用 DejaVuSans.ttf 默认字体：
   ```python
   style.default.font = "DejaVuSans.ttf"
   ```
   结果：同样在游戏进行过程中出现字体错误。

3. 下载并使用文泉驿微米黑字体：
   ```python
   style.default.font = "fonts/wqy-microhei.ttc"
   ```
   结果：遇到了 "unknown file format" 错误。

### 6.2 字体加载问题分析

**问题分析**：
1. 游戏开始界面和游戏内界面可能使用了不同的字体配置
2. 在游戏进行过程中，可能有某些特定元素（如对话框、选择菜单等）使用了未正确配置的字体
3. 字体映射配置可能不完整，导致某些元素找不到对应的字体

**解决方向**：
1. 检查所有样式定义，确保一致性使用同一字体
2. 检查 script.rpy 中的菜单和对话框定义，确保它们没有使用特殊字体
3. 确保字体映射覆盖所有可能的字体引用
4. 检查游戏在不同阶段使用的样式和字体配置

## 总结

大部分错误都来自于混合使用不同风格的代码以及引用不存在的属性或资源。通过简化样式定义、提供合适的默认实现，以及动态生成资源文件，我们成功地使游戏能够在Ren'Py中正确运行。

对于字体问题，需要深入分析游戏在不同阶段使用的字体配置，确保一致性和完整性。