################################################################################
# Path of Destiny - A Ren'Py RPG Game
################################################################################

# Define characters
define mc = Character("[player_name]", color="#c8ffc8")
define elder = Character("村长", color="#c8c8ff")
define merchant = Character("商人", color="#ffc8c8")
define warrior = Character("战士", color="#ff8c8c")
define mage = Character("法师", color="#8c8cff")
define guardian = Character("遗迹守护者", color="#ffcc00")
define ghost = Character("古代幽灵", color="#aaaaff")

# Define images for characters - 使用动态生成的角色图像替代不存在的图片文件
init python:
    # 创建角色占位图像的函数
    def character_placeholder(name, color):
        # 创建一个圆形头像和名字标签
        base = Solid(color, xsize=300, ysize=500)
        circle = Solid("#ffffff33", xsize=200, ysize=200)
        text_name = Text(name, size=30, color="#ffffff", font="fonts/wqy-microhei.ttc")
        return Composite(
            (300, 500),
            (0, 0), base,
            (50, 100), circle,
            (50, 350), text_name
        )

# 定义角色图像的变换，调整大小以适应游戏界面
transform character_scale:
    zoom 0.3  # 缩放图像到原来的0.3倍，缩小一点
    yalign 1.0  # 垂直对齐到底部，使角色站在地上
    xalign 0.5  # 水平居中

# 定义角色图像 - 使用实际PNG图片并应用缩放变换
image elder normal = At("images/elder_normal.png", character_scale)
image merchant normal = At("images/merchant_normal.png", character_scale)
image warrior normal = At("images/warrior_normal.png", character_scale)
image mage normal = At("images/mage_normal.png", character_scale)
image guardian normal = At("images/guardian_normal.png", character_scale)
image ghost normal = At("images/ghost_normal.png", character_scale)

# Define backgrounds - 使用实际PNG图片文件替代占位符
# 定义背景图像
image bg village = "images/backgrounds/bg_village.png"
image bg forest = "images/backgrounds/bg_forest.png"
image bg cave = "images/backgrounds/bg_cave.png"
image bg castle = "images/backgrounds/bg_castle.png"
image bg ruins = "images/backgrounds/bg_ruins.png"
image bg throne = "images/backgrounds/bg_throne.png"

# Initialize variables
init python:
    # Player stats
    player_name = "勇者"
    player_strength = 5
    player_intelligence = 5
    player_charisma = 5
    player_gold = 10
    player_health = 100
    
    # Inventory
    has_sword = False
    has_shield = False
    has_potion = False
    has_magic_scroll = False
    has_ancient_key = False
    has_destiny_heart = False
    
    # Quest flags
    village_quest_complete = False
    forest_quest_complete = False
    cave_quest_complete = False
    castle_quest_complete = False
    ruins_quest_complete = False
    
    # Function to display player stats
    def show_stats():
        renpy.say(None, "【状态】\n姓名: [player_name]\n力量: [player_strength]\n智力: [player_intelligence]\n魅力: [player_charisma]\n生命值: [player_health]\n金币: [player_gold]")
    
    # Function to check player health
    def check_health():
        if player_health <= 0:
            renpy.jump("game_over")
        return

# The game starts here

# 开始游戏时显示状态屏幕
label start:
    # Show stats screen
    show screen stats
    
    # Introduction
    scene black
    "欢迎来到《命运之路》"
    "在这个世界中，你的选择将决定你的命运..."
    
    # Character creation
    $ player_name = renpy.input("请输入你的名字:", default="勇者")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "勇者"
    
    "你选择了名字: [player_name]"
    
    menu:
        "选择你的起始属性偏好:"
        
        "力量型 (力量+2)":
            $ player_strength += 2
            "你选择了力量型角色。"
            
        "智力型 (智力+2)":
            $ player_intelligence += 2
            "你选择了智力型角色。"
            
        "魅力型 (魅力+2)":
            $ player_charisma += 2
            "你选择了魅力型角色。"
    
    $ show_stats()
    
    # Start the game in the village
    jump village_hub

# Village hub - central location
label village_hub:
    scene bg village
    "你来到了宁静的村庄。这里是你的冒险起点。"
    
    menu:
        "你想去哪里？"
        
        "拜访村长":
            jump visit_elder
            
        "去商店":
            jump visit_merchant
            
        "前往森林探险" if player_strength >= 6 or has_sword:
            jump forest_entrance
            
        "探索神秘洞穴" if forest_quest_complete:
            jump cave_entrance
            
        "前往城堡" if cave_quest_complete:
            jump castle_entrance
            
        "查看状态":
            $ show_stats()
            jump village_hub

# Visit the village elder
label visit_elder:
    scene bg village
    show elder normal
    
    elder "欢迎，[player_name]。我们村庄最近遇到了一些麻烦。"
    
    if not village_quest_complete:
        elder "森林里的野兽越来越多，威胁到了我们的安全。"
        elder "如果你能帮助我们解决这个问题，我会给予你丰厚的报酬。"
        
        menu:
            "你的回应是？"
            
            "我会帮助你们 (魅力检定)":
                if player_charisma >= 6:
                    elder "你真是太好了！这是一些金币，希望对你的旅程有所帮助。"
                    $ player_gold += 5
                    $ player_charisma += 1
                    "你的魅力提升了！"
                else:
                    elder "谢谢你的好意，但请务必小心。"
                
            "这对我有什么好处？":
                elder "除了金币报酬，你还能获得村民们的尊敬和感激。"
                elder "而且，这将是锻炼你战斗技能的好机会。"
                
            "我需要先准备一下":
                elder "当然，请做好充分准备再出发。"
    else:
        elder "感谢你为村庄做的一切，[player_name]。"
        elder "你已经证明了自己是一位真正的英雄。"
    
    elder "如果你有任何问题，随时来找我。"
    
    hide elder
    jump village_hub

# Visit the merchant
label visit_merchant:
    scene bg village
    show merchant normal
    
    merchant "欢迎光临我的小店，旅行者！有什么我能帮你的吗？"
    
    menu:
        "你想做什么？"
        
        "购买物品":
            jump buy_items
            
        "出售物品":
            jump sell_items
            
        "询问情报":
            merchant "听说城堡里的国王正在寻找勇敢的冒险者执行一项重要任务。"
            merchant "不过，你得先证明自己的实力才行。"
            jump visit_merchant
            
        "离开":
            merchant "欢迎下次光临！"
            hide merchant
            jump village_hub

# Buy items from merchant
label buy_items:
    merchant "这是我现在的库存，看看有什么你需要的吗？"
    
    menu:
        "剑 (10金币)" if not has_sword and player_gold >= 10:
            $ player_gold -= 10
            $ has_sword = True
            $ player_strength += 2
            merchant "好剑！这会让你在战斗中更有优势。"
            "你获得了剑！力量+2"
            jump buy_items
            
        "盾牌 (8金币)" if not has_shield and player_gold >= 8:
            $ player_gold -= 8
            $ has_shield = True
            merchant "这面盾牌会在危险时刻保护你。"
            "你获得了盾牌！"
            jump buy_items
            
        "药水 (5金币)" if not has_potion and player_gold >= 5:
            $ player_gold -= 5
            $ has_potion = True
            merchant "这种药水可以在紧急情况下恢复你的生命力。"
            "你获得了药水！"
            jump buy_items
            
        "魔法卷轴 (12金币)" if not has_magic_scroll and player_gold >= 12:
            $ player_gold -= 12
            $ has_magic_scroll = True
            $ player_intelligence += 2
            merchant "这卷轴包含了古老的魔法知识。"
            "你获得了魔法卷轴！智力+2"
            jump buy_items
            
        "没什么需要的了":
            merchant "如果你改变主意，随时欢迎回来。"
            jump visit_merchant

# Sell items to merchant
label sell_items:
    merchant "你有什么想卖给我的吗？"
    
    menu:
        "剑 (7金币)" if has_sword:
            $ player_gold += 7
            $ has_sword = False
            $ player_strength -= 2
            merchant "这是个不错的剑，我给你7金币。"
            "你卖出了剑。力量-2"
            jump sell_items
            
        "盾牌 (5金币)" if has_shield:
            $ player_gold += 5
            $ has_shield = False
            merchant "盾牌状态不错，给你5金币。"
            "你卖出了盾牌。"
            jump sell_items
            
        "药水 (3金币)" if has_potion:
            $ player_gold += 3
            $ has_potion = False
            merchant "药水总是有市场的，给你3金币。"
            "你卖出了药水。"
            jump sell_items
            
        "魔法卷轴 (9金币)" if has_magic_scroll:
            $ player_gold += 9
            $ has_magic_scroll = False
            $ player_intelligence -= 2
            merchant "这卷轴很珍贵，我给你9金币。"
            "你卖出了魔法卷轴。智力-2"
            jump sell_items
            
        "没什么要卖的了":
            merchant "好的，有东西要卖时再来找我。"
            jump visit_merchant

# Forest area
label forest_entrance:
    scene bg forest
    "你来到了森林入口。这里树木茂密，隐约能听到野兽的声音。"
    
    menu:
        "你想做什么？"
        
        "深入森林探索":
            jump forest_exploration
            
        "返回村庄":
            jump village_hub

# Forest exploration
label forest_exploration:
    scene bg forest
    "你小心翼翼地在森林中前进。"
    
    if not forest_quest_complete:
        "突然，一个身影从树后走出。"
        
        show warrior normal
        
        warrior "站住！这片森林很危险，你为什么来这里？"
        
        menu:
            "我是来帮助村庄解决野兽问题的":
                warrior "原来如此。我也是为了同样的目的而来。"
                warrior "也许我们可以合作？"
                
                menu:
                    "接受合作":
                        $ player_charisma += 1
                        warrior "明智的选择。一起行动会更安全。"
                        "你和战士一起深入森林，成功消灭了威胁村庄的野兽。"
                        $ forest_quest_complete = True
                        $ player_gold += 15
                        $ player_strength += 1
                        "你完成了森林任务！获得15金币，力量+1"
                        
                    "拒绝合作":
                        warrior "随你便，但要小心。"
                        "你独自面对森林的危险，经过一番激战..."
                        
                        if player_strength >= 7 or has_sword:
                            "你成功击退了野兽！"
                            $ forest_quest_complete = True
                            $ player_gold += 10
                            $ player_strength += 2
                            "你完成了森林任务！获得10金币，力量+2"
                        else:
                            "你勉强逃脱，但受了伤。"
                            "也许下次应该更加谨慎，或者寻求帮助。"
                            jump village_hub
            
            "我只是在探索 (智力检定)":
                if player_intelligence >= 7:
                    warrior "你看起来很聪明，知道自己在做什么。"
                    warrior "这片森林深处有一个神秘洞穴，据说里面藏有宝藏。"
                    warrior "不过，那里也有危险的生物守卫。"
                    $ player_intelligence += 1
                    "你获得了有价值的情报！智力+1"
                else:
                    warrior "这里不是随便探索的地方。如果你不小心，可能会有生命危险。"
                
                warrior "无论如何，祝你好运。"
        
        hide warrior
    else:
        "森林现在安全多了，村民们可以放心地采集资源。"
        "你发现了一些有价值的草药。"
        $ player_gold += 3
        "你获得了3金币！"
    
    jump forest_entrance

# Cave area
label cave_entrance:
    scene bg cave
    "你来到了神秘洞穴的入口。洞内漆黑一片，散发着神秘的气息。"
    
    menu:
        "你想做什么？"
        
        "进入洞穴探索":
            jump cave_exploration
            
        "返回村庄":
            jump village_hub

# Cave exploration
label cave_exploration:
    scene bg cave
    "你小心地进入洞穴，借助微弱的光线前进。"
    
    if not cave_quest_complete:
        "在洞穴深处，你发现了一位正在研究古老符文的法师。"
        
        show mage normal
        
        mage "你是谁？很少有人能找到这个地方。"
        
        menu:
            "我是探险者，想了解这个洞穴的秘密 (智力检定)":
                if player_intelligence >= 8 or has_magic_scroll:
                    mage "我能感觉到你对知识的渴望。也许你能帮我解开这些符文的秘密。"
                    "你和法师一起研究古老符文，发现了隐藏的魔法知识。"
                    $ cave_quest_complete = True
                    $ player_intelligence += 2
                    $ player_gold += 10
                    "你完成了洞穴任务！智力+2，获得10金币"
                else:
                    mage "你似乎对魔法知识了解不多。这些符文非常危险，不是随便什么人都能研究的。"
                    "也许你应该先增强自己的智力，或者寻找魔法知识。"
            
            "我是来寻宝的":
                mage "又一个寻宝者...这里确实有宝藏，但它们受到魔法保护。"
                mage "如果你想获得宝藏，必须先通过我的测试。"
                
                menu:
                    "接受测试":
                        mage "很好。我会给你三个谜题，你需要至少答对两个。"
                        
                        $ correct_answers = 0
                        
                        mage "第一个谜题：我无形无状，却能填满任何容器。我是什么？"
                        
                        menu:
                            "水":
                                mage "不完全正确。水有形状。"
                            
                            "空气":
                                mage "正确！"
                                $ correct_answers += 1
                            
                            "光":
                                mage "不正确。光不能填满所有容器。"
                        
                        mage "第二个谜题：我越减越多，越加越少。我是什么？"
                        
                        menu:
                            "洞穴":
                                mage "有创意，但不是我想的答案。"
                            
                            "数字":
                                mage "不正确。"
                            
                            "空洞":
                                mage "正确！"
                                $ correct_answers += 1
                        
                        mage "最后一个谜题：我能被创造也能被打破，但你永远看不见我。我是什么？"
                        
                        menu:
                            "承诺":
                                mage "正确！"
                                $ correct_answers += 1
                            
                            "思想":
                                mage "有道理，但不是我想的答案。"
                            
                            "声音":
                                mage "不正确。声音是可以听到的。"
                        
                        if correct_answers >= 2:
                            mage "恭喜你通过了测试！"
                            "法师给了你一把神秘钥匙，并指引你到达了宝藏所在地。"
                            $ cave_quest_complete = True
                            $ player_gold += 20
                            "你完成了洞穴任务！获得20金币"
                        else:
                            mage "很遗憾，你没有通过测试。"
                            mage "也许你应该先增强自己的智力，再回来尝试。"
                    
                    "拒绝测试":
                        mage "明智的选择。这些测试并不简单，准备不足的话很危险。"
            
            "我迷路了":
                $ player_charisma += 1
                mage "这种事情常有发生。这个洞穴确实错综复杂。"
                mage "我可以帮你找到出路，但作为交换，你需要帮我带一封信给村里的长老。"
                "你同意了法师的请求，安全地回到了村庄。"
                "你的魅力提升了！"
                jump village_hub
        
        hide mage
    else:
        "你已经探索过这个洞穴，解开了它的秘密。"
        "洞穴深处的宝藏已经被你取走，但这里的魔法气息依然很强。"
    
    jump cave_entrance

# Castle area
label castle_entrance:
    scene bg castle
    "你来到了雄伟的城堡前。卫兵严阵以待，检查着每一位来访者。"
    
    "卫兵拦住了你，要求你表明身份和来意。"
    
    menu:
        "我是来自村庄的冒险者，有重要事情要见国王 (魅力检定)":
            if player_charisma >= 8:
                "卫兵被你的气质和言辞打动，允许你进入城堡。"
                jump castle_interior
            else:
                "卫兵不为所动。"
                "卫兵" "没有预约，任何人都不能见国王。"
                "也许你应该提高自己的魅力，或者寻找其他方式进入城堡。"
        
        "我有解决森林和洞穴问题的经验，可以帮助王国":
            if forest_quest_complete and cave_quest_complete:
                "卫兵" "原来是你！我们听说过你的事迹。"
                "卫兵让你通过了。"
                jump castle_interior
            else:
                "卫兵" "我们需要确凿的证据证明你的能力。"
                "也许你应该先完成森林和洞穴的任务。"
        
        "返回村庄":
            jump village_hub

# Castle interior
label castle_interior:
    scene bg castle
    "你进入了城堡内部，华丽的装饰和高大的拱顶令人印象深刻。"
    
    "国王的顾问迎接了你，并带你到了王座厅。"
    
    "顾问" "国王陛下正在处理重要事务，但他听说了你的事迹，想要委托你一项任务。"
    "顾问" "王国正面临一个古老预言的威胁，需要一位勇敢的冒险者去寻找传说中的神器来保护王国。"
    
    menu:
        "我愿意接受这个任务":
            "顾问" "太好了！这将是一段艰难但值得的旅程。"
            "顾问" "作为报酬，国王将赐予你丰厚的财富和王国的荣誉。"
            "顾问" "神器被称为'命运之心'，据说它能抵御任何邪恶力量。"
            "顾问" "它被藏在远古遗迹中，那里充满了陷阱和守卫。"
            
            "顾问从他的抽屉里取出一把古老的钥匙，递给你。"
            
            "顾问" "这把钥匙据说能打开远古遗迹的入口。它是王室世代相传的宝物。"
            
            $ has_ancient_key = True
            $ castle_quest_complete = True
            
            "你获得了古老钥匙！"
            
            "顾问" "远古遗迹位于王国东部的山脉中。祝你好运，勇士。"
            
            menu:
                "立即前往远古遗迹":
                    "你告别顾问，立即动身前往远古遗迹。"
                    jump ancient_ruins
                
                "先做准备再出发":
                    "你决定先回村庄做些准备，再前往远古遗迹。"
                    jump village_hub
        
        "我需要更多信息":
            "顾问" "当然。这个神器被称为'命运之心'，据说它能抵御任何邪恶力量。"
            "顾问" "它被藏在远古遗迹中，那里充满了陷阱和守卫。"
            "顾问" "你的力量、智慧和魅力都将在这次冒险中接受考验。"
            
            menu:
                "我接受挑战":
                    "顾问" "勇气可嘉！"
                    
                    "顾问从他的抽屉里取出一把古老的钥匙，递给你。"
                    
                    "顾问" "这把钥匙据说能打开远古遗迹的入口。它是王室世代相传的宝物。"
                    
                    $ has_ancient_key = True
                    $ castle_quest_complete = True
                    
                    "你获得了古老钥匙！"
                    
                    "顾问" "远古遗迹位于王国东部的山脉中。祝你好运，勇士。"
                    
                    menu:
                        "立即前往远古遗迹":
                            "你告别顾问，立即动身前往远古遗迹。"
                            jump ancient_ruins
                        
                        "先做准备再出发":
                            "你决定先回村庄做些准备，再前往远古遗迹。"
                            jump village_hub
                
                "我需要先做准备":
                    "顾问" "明智的决定。这样的任务确实需要充分准备。"
                    "顾问" "当你准备好了，随时可以回来接受任务。"
                    jump village_hub
        
        "我对这个任务不感兴趣":
            "顾问" "我理解。这确实是一项危险的任务。"
            "顾问" "如果你改变主意，国王的大门随时为你敞开。"
            jump village_hub

# Ancient Ruins area
label ancient_ruins:
    scene bg ruins
    "你来到了古老的遗迹前。这座建筑物已有数千年历史，散发着神秘的气息。"
    
    "入口被一道神秘的力场封闭着，上面刻着古老的符文。"
    
    if has_ancient_key:
        "你拿出古老钥匙，感觉到它与力场产生共鸣。"
        "力场消失了，露出了一条通往遗迹内部的道路。"
        jump ruins_interior
    else:
        "你需要找到打开这道力场的方法。"
        "也许城堡或其他地方会有线索。"
        
        menu:
            "继续探索其他地方":
                jump village_hub
            
            "尝试强行通过 (力量检定)":
                if player_strength >= 10:
                    "你集中全身力量推向力场。"
                    "力场微微波动，但你付出了代价。"
                    $ player_health -= 20
                    "你受到了20点伤害！"
                    $ check_health()
                    "你勉强穿过了力场，但感觉虚弱不少。"
                    jump ruins_interior
                else:
                    "你尝试强行通过，但力场纹丝不动。"
                    "你受到了反噬！"
                    $ player_health -= 30
                    "你受到了30点伤害！"
                    $ check_health()
                    "你需要找到更好的方法，或者提高自己的力量。"
                    jump village_hub

# Ruins interior
label ruins_interior:
    scene bg ruins
    "你进入了遗迹内部，古老的墙壁上布满了精美的浮雕和符文。"
    
    "这里似乎曾是某种仪式场所，中央是一个巨大的祭坛。"
    
    "突然，一个声音从黑暗中传来。"
    
    show guardian normal
    
    guardian "又一个寻宝者...你知道自己在找什么吗？"
    
    menu:
        "我在寻找'命运之心' (智力检定)":
            if player_intelligence >= 10:
                guardian "你确实知道你在找什么。"
                guardian "但知道并不意味着你有资格获得它。"
                guardian "命运之心不仅仅是一件物品，它是整个王国命运的象征。"
                $ player_intelligence += 1
                "你的智力提升了！"
            else:
                guardian "你甚至不知道它意味着什么。"
                guardian "也许你应该先了解更多，再来尝试获取它。"
        
        "我受国王委托来取回它":
            guardian "国王？多么短暂的头衔..."
            guardian "这件神器已经存在了千年，见证了无数帝国的兴衰。"
            guardian "你真的认为它应该被用于一个王国的政治目的吗？"
        
        "我只是一个探险家，对这里的历史感兴趣":
            $ player_charisma += 1
            guardian "至少你比大多数人诚实。"
            guardian "我欣赏你的坦率。"
            "你的魅力提升了！"
    
    guardian "无论如何，如果你想获得'命运之心'，你必须通过三个考验。"
    guardian "力量的考验，智慧的考验，以及心灵的考验。"
    guardian "你准备好了吗？"
    
    menu:
        "我准备好了":
            guardian "很好。让我们开始。"
            jump ruins_trials
        
        "我需要做更多准备":
            guardian "明智的选择。当你准备好了，再回来吧。"
            jump village_hub

# Ruins trials
label ruins_trials:
    scene bg ruins
    show guardian normal
    
    guardian "第一个是力量的考验。"
    
    "遗迹的地面突然震动，一个石头战士从地上升起，向你发起攻击！"
    
    menu:
        "正面迎战 (力量检定)":
            if player_strength >= 9 or has_sword:
                "你勇敢地迎向石头战士，与之展开激烈的战斗。"
                "经过一番激战，你成功击败了石头战士！"
                guardian "力量的考验通过了。"
            else:
                "你尝试与石头战士战斗，但它太强大了。"
                "你被击中了几次，感到非常疼痛。"
                $ player_health -= 40
                "你受到了40点伤害！"
                $ check_health()
                "你勉强击退了石头战士，但受了伤。"
                guardian "你通过了考验，但付出了代价。"
        
        "寻找弱点 (智力检定)":
            if player_intelligence >= 8:
                "你仔细观察石头战士，发现它胸口有一道裂缝。"
                "你精准地攻击了那个弱点，石头战士瞬间崩塌！"
                guardian "聪明。有时力量不是唯一的解决方案。"
                $ player_intelligence += 1
                "你的智力提升了！"
            else:
                "你尝试寻找弱点，但没有足够的时间。"
                "石头战士击中了你。"
                $ player_health -= 30
                "你受到了30点伤害！"
                $ check_health()
                "你最终击败了石头战士，但受了伤。"
    
    guardian "接下来是智慧的考验。"
    
    "墙壁上出现了三个不同的符文，闪烁着神秘的光芒。"
    
    guardian "选择代表'永恒'的符文。选择错误会有惩罚。"
    
    menu:
        "左边的符文 (圆形图案)":
            guardian "正确。圆形没有开始，也没有结束，代表永恒。"
            $ player_intelligence += 1
            "你的智力提升了！"
        
        "中间的符文 (直线图案)":
            guardian "错误。直线代表命运的单一路径，而非永恒。"
            "符文发出一道闪光，击中了你！"
            $ player_health -= 20
            "你受到了20点伤害！"
            $ check_health()
        
        "右边的符文 (波浪图案)":
            guardian "错误。波浪代表生命的起伏，而非永恒。"
            "符文发出一道闪光，击中了你！"
            $ player_health -= 20
            "你受到了20点伤害！"
            $ check_health()
    
    guardian "最后是心灵的考验，也是最难的一个。"
    
    "空气中出现了一团迷雾，从中走出一个与你长得一模一样的人影。"
    
    show ghost normal
    
    ghost "我是你内心的阴影，代表你最深的恐惧和欲望。"
    ghost "告诉我，你为什么要寻找'命运之心'？"
    
    menu:
        "为了权力和财富":
            ghost "至少你很诚实。但这种动机不足以掌握'命运之心'。"
            "你感到一阵剧痛！"
            $ player_health -= 30
            "你受到了30点伤害！"
            $ check_health()
        
        "为了保护王国和人民 (魅力检定)":
            if player_charisma >= 9:
                ghost "你的话语中有真诚的力量。"
                ghost "但记住，即使是最崇高的目标也可能导致毁灭。"
                ghost "权力会改变人，希望你能保持初心。"
                $ player_charisma += 1
                "你的魅力提升了！"
            else:
                ghost "你的话听起来很伟大，但缺乏真诚。"
                "你感到一阵不适！"
                $ player_health -= 15
                "你受到了15点伤害！"
                $ check_health()
        
        "为了探索未知，了解这个世界的奥秘":
            ghost "求知是高尚的动机，但也可能带来危险。"
            ghost "知识和力量总是伴随着责任。"
            "阴影点了点头，似乎接受了你的回答。"
    
    hide ghost
    
    guardian "你已经通过了全部考验。"
    guardian "无论是成功还是失败，你都展现了自己的品质。"
    
    "守护者从祭坛上取下一个发光的宝石，递给你。"
    
    guardian "这就是'命运之心'。使用它时要谨慎，它的力量远超你的想象。"
    
    $ has_destiny_heart = True
    $ ruins_quest_complete = True
    
    "你获得了命运之心！"
    
    guardian "现在你可以回到国王那里，或者...你也可以选择其他道路。"
    guardian "命运之心给予持有者选择的权力。"
    guardian "你的决定将影响整个王国的未来。"
    
    hide guardian
    
    menu:
        "返回王城，将命运之心交给国王":
            jump final_castle
        
        "保留命运之心，寻找自己的道路":
            jump alternative_ending

# Final return to castle
label final_castle:
    scene bg castle
    "你回到了城堡，卫兵立刻认出了你，让你直接进入王座厅。"
    
    scene bg throne
    "国王正在王座上等待你的归来。"
    
    "国王" "勇敢的[player_name]！你回来了。你找到'命运之心'了吗？"
    
    "你拿出闪烁着光芒的命运之心。"
    
    "国王" "太棒了！有了它，我们的王国将永远繁荣昌盛！"
    
    menu:
        "将命运之心交给国王":
            "你将命运之心交给了国王。"
            "国王" "你将被载入史册，成为王国的英雄！"
            "国王兑现了承诺，赐予你丰厚的财富和崇高的地位。"
            "在接下来的岁月里，王国在命运之心的护佑下繁荣发展。"
            "你的名字被传颂，成为了传奇。"
            
            "恭喜你完成了《命运之路》的主线剧情！"
            "你成功将命运之心带回王国，成为了英雄。"
            "你的最终状态："
            $ show_stats()
            
            "感谢游玩！"
            return
        
        "最后一刻决定保留命运之心 (魅力检定)":
            if player_charisma >= 10:
                "你突然意识到将如此强大的力量交给一个人可能不是最好的选择。"
                "你" "陛下，在守护者的考验中，我明白了命运之心不应被任何一个人独占。"
                "你" "它的力量应该用于保护整个王国，而不是掌握在个人手中。"
                "你" "我建议成立一个由王国最睿智的人组成的委员会，共同决定如何使用它。"
                
                "国王沉思片刻，然后点了点头。"
                
                "国王" "你说得有道理。权力确实应该有所制衡。"
                "国王" "就按你说的办。你将成为委员会的一员，帮助指导王国的未来。"
                
                "在你的建议下，王国进入了前所未有的和平与繁荣时期。"
                "你不仅是一位勇士，更成为了一位受人尊敬的智者。"
                
                "恭喜你完成了《命运之路》的真实结局！"
                "你的智慧为王国带来了更美好的未来。"
                "你的最终状态："
                $ show_stats()
                
                "感谢游玩！"
                return
            else:
                "你尝试说服国王，但他变得不耐烦。"
                "国王" "我们的协议是你帮我取回命运之心。现在履行你的承诺！"
                "卫兵们开始向你靠近。"
                
                menu:
                    "顺从国王的要求":
                        "你不情愿地交出了命运之心。"
                        "国王" "明智的选择。作为回报，你将得到承诺的奖赏。"
                        "你获得了财富和地位，但总感觉做了错误的决定。"
                        
                        "你完成了《命运之路》的结局之一。"
                        "虽然获得了奖励，但你对自己的选择感到怀疑。"
                        "你的最终状态："
                        $ show_stats()
                        
                        "感谢游玩！"
                        return
                    
                    "拒绝交出命运之心":
                        "你" "不，我不能将这么强大的力量交给任何人。"
                        "国王" "叛徒！卫兵，抓住他！"
                        "你不得不逃离城堡，成为了王国的通缉犯。"
                        "但你保护了命运之心不被滥用。"
                        
                        "你完成了《命运之路》的叛逆结局！"
                        "虽然成为了通缉犯，但你保护了世界免受可能的灾难。"
                        "你的最终状态："
                        $ show_stats()
                        
                        "感谢游玩！"
                        return

# Alternative ending
label alternative_ending:
    scene bg forest
    "你决定不回王城，而是带着命运之心踏上自己的旅程。"
    "有了命运之心的力量，你可以做出更多的改变，帮助更多的人。"
    
    menu:
        "成为流浪的英雄，游历各地帮助有需要的人":
            "你选择成为一名流浪英雄，用命运之心的力量帮助那些需要帮助的人。"
            "你的事迹逐渐传开，人们称你为'命运使者'。"
            "虽然国王一开始派人追捕你，但随着你善行的传播，他最终放弃了追捕。"
            "你的旅程仍在继续，命运之路延伸向未知的远方..."
            
            "你完成了《命运之路》的英雄结局！"
            "你选择了自己的道路，成为了传说中的英雄。"
            "你的最终状态："
            $ show_stats()
            
            "感谢游玩！"
            return
        
        "寻找其他古老遗迹，探索世界的秘密":
            "你对古老文明和神秘力量产生了浓厚的兴趣。"
            "带着命运之心，你踏上了探索其他遗迹的旅程。"
            "你的旅途充满危险，但也充满了惊喜和发现。"
            "随着你了解到更多秘密，你开始理解命运之心真正的用途..."
            "这是另一个故事的开始。"
            
            "你完成了《命运之路》的探索者结局！"
            "你的冒险才刚刚开始，更多的秘密等待你去发现。"
            "你的最终状态："
            $ show_stats()
            
            "感谢游玩！"
            return
        
        "建立自己的王国，成为一位明智的统治者":
            "你决定用命运之心的力量建立自己的王国。"
            "你找到了一片无人统治的土地，开始聚集追随者。"
            "在你的领导下，这片土地迅速繁荣起来。"
            "你创建了一个公平、和平的国度，被人们爱戴。"
            "多年后，你的王国成为了大陆上最强盛的国家之一。"
            
            "你完成了《命运之路》的君王结局！"
            "你建立了自己的传奇，成为了一位伟大的统治者。"
            "你的最终状态："
            $ show_stats()
            
            "感谢游玩！"
            return

# Game over state
label game_over:
    scene black
    "你的生命值降至零，无法继续冒险..."
    "也许命运给你安排了不同的道路，或者你需要做出不同的选择。"
    
    menu:
        "重新开始游戏":
            jump start
        
        "退出游戏":
            return
