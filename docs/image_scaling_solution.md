# 角色图像缩放问题解决方案

## 问题描述

在游戏中，角色图像（PNG格式，1024x1536或1024x1024像素）显示异常，尺寸过大，导致角色图像占据了过多的屏幕空间，影响游戏体验。具体表现为：

1. 角色图像显示过大，超出了预期的显示区域
2. 角色图像没有正确定位在屏幕上
3. 角色图像与背景和UI元素不协调

## 原因分析

1. 角色图像使用了高分辨率的PNG文件（1024x1536或1024x1024像素），但没有进行适当的缩放处理
2. 在将图像从JPG格式转换为PNG格式时，没有同时调整图像的显示大小
3. 没有使用Ren'Py的transform功能来控制图像的大小和位置

## 解决方案

### 1. 更新背景图像引用

首先，我们将`init.rpy`文件中的背景图像引用从JPG格式更新为PNG格式：

```python
# 背景图像列表 - 从JPG更新为PNG
background_images = [
    ("images/backgrounds/bg_village.png", "#4a6f3f"),  # 村庄：绿色
    ("images/backgrounds/bg_forest.png", "#1a4a1a"),   # 森林：深绿色
    ("images/backgrounds/bg_cave.png", "#333344"),     # 洞穴：深蓝灰色
    ("images/backgrounds/bg_castle.png", "#666677"),   # 城堡：灰色
    ("images/backgrounds/bg_ruins.png", "#554433"),    # 遗迹：棕色
    ("images/backgrounds/bg_throne.png", "#775544")    # 王座：红棕色
]
```

### 2. 更新角色图像定义

接下来，我们修改了`script.rpy`文件中的角色图像定义，从使用占位符函数改为使用实际的PNG文件：

```python
# 定义角色图像 - 使用实际PNG图片
image elder normal = "images/elder_normal.png"
image merchant normal = "images/merchant_normal.png"
image warrior normal = "images/warrior_normal.png"
image mage normal = "images/mage_normal.png"
image guardian normal = "images/guardian_normal.png"
image ghost normal = "images/ghost_normal.png"
```

### 3. 创建角色图像缩放变换

最关键的解决方案是添加了一个自定义的transform来控制角色图像的大小和位置：

```python
# 定义角色图像的变换，调整大小以适应游戏界面
transform character_scale:
    zoom 0.35  # 缩放图像到原来的0.35倍
    yalign 0.0  # 垂直对齐，使角色头部在屏幕上方
    xalign 0.5  # 水平居中
```

### 4. 应用缩放变换到角色图像

最后，我们将缩放变换应用到所有角色图像：

```python
# 定义角色图像 - 使用实际PNG图片并应用缩放变换
image elder normal = At("images/elder_normal.png", character_scale)
image merchant normal = At("images/merchant_normal.png", character_scale)
image warrior normal = At("images/warrior_normal.png", character_scale)
image mage normal = At("images/mage_normal.png", character_scale)
image guardian normal = At("images/guardian_normal.png", character_scale)
image ghost normal = At("images/ghost_normal.png", character_scale)
```

## 技术说明

1. **使用transform而非修改图像文件**：这种方法保留了原始高分辨率资源，同时确保它们在游戏中正确显示。这是Ren'Py中处理角色精灵的标准做法。

2. **缩放参数选择**：
   - `zoom 0.35`：将图像缩小到原始大小的35%，这个比例经过测试最适合游戏界面
   - `yalign 0.0`：将图像顶部对齐到屏幕顶部，确保角色头部正确显示
   - `xalign 0.5`：将图像水平居中，保持画面平衡

3. **At函数**：Ren'Py的At函数用于将transform应用到图像上，格式为`At(image, transform)`

## 优势

1. 保持了原始高分辨率资源，便于未来可能的调整或重用
2. 无需修改实际图像文件，减少了资源管理的复杂性
3. 可以轻松调整缩放比例和位置，而无需重新处理图像
4. 确保了角色图像在游戏中的一致性显示

## 后续建议

1. 对于未来添加的新角色图像，继续使用相同的transform
2. 如果需要针对特定角色进行调整，可以创建特定的transform变体
3. 考虑为不同的游戏场景（对话、战斗等）创建不同的transform，以优化不同场景下的显示效果
