import json
import os
import re
from tools import *
from src.configs import *

def rpdesc(desc):
    for rp in configs_characters.rpdesc_text:
        desc = re.sub(rp[0], rp[1], desc)
    return desc

def characters_id(file, character_type):

    docs_character = "" # 设置该角色文档缓存
    docs_list = "" # 设置该角色文档列表缓存
    docs_index = "" # 设置该角色文档索引缓存
    docs_config = "" # 设置该角色文档配置缓存
    used_files = [] # 已使用的立绘文件
    docs_index_list = "" # 设置该角色文档列表缓存

    with open(f'data/characters/{file}', 'r', encoding='utf-8') as data_file: # 读取数据
        data = json.loads(data_file.read())

    for ename_config in configs_characters.ename_configs: # 替换角色英文名
        if data["id"] == ename_config[0]:
            data["ename"] = ename_config[1]

# 设置标题
    docs_character += f'''# `{data["id"]}` {data["name"]} {data["ename"]}
''' 

    if data["quality"] == "6": # 角色品质字符串
        str_quality = "☆☆☆☆☆☆ "
    elif data["quality"] == "5":
        str_quality = "☆☆☆☆☆ "
    elif data["quality"] == "4":
        str_quality = "☆☆☆☆ "
    elif data["quality"] == "3":
        str_quality = "☆☆☆ "
    else:
        str_quality = ""

    if data.get("nClass") is None: # 角色属地字符串
        data["nClass"] = data["id"][:1]
    if 71000 <= int(data["id"]) < 72000:
        str_type = "总队长"
    elif int(data["id"]) >= 99000:
        str_type = "NPC"
    else:
        if data["nClass"] == "1":
            str_type = "山脉"
        elif data["nClass"] == "2":
            str_type = "乐团"
        elif data["nClass"] == "3":
            str_type = "不朽"
        elif data["nClass"] == "4":
            str_type = "气象"
        elif data["nClass"] == "5":
            str_type = "虫洞"
        elif data["nClass"] == "6":
            str_type = "灭刃"
        else:
            str_type = "碎星"

    if data.get('pos_enum',"") != "":
        pos_enum_str = " -"
        for pos_enum in data['pos_enum'].split(','):
            if pos_enum == "1":
                pos_enum_str += " 护盾"
            elif pos_enum == "2":
                pos_enum_str += " 输出"
            elif pos_enum == "3":
                pos_enum_str += " 反击"
            elif pos_enum == "4":
                pos_enum_str += " 反伤"
            elif pos_enum == "5":
                pos_enum_str += " 治疗"
            elif pos_enum == "6":
                pos_enum_str += " 防御"
            elif pos_enum == "7":
                pos_enum_str += " 辅助"
            elif pos_enum == "8":
                pos_enum_str += " 控制"
            elif pos_enum == "9":
                pos_enum_str += " 协击"
    else:
        pos_enum_str = ""

    if data.get('cv_cn') != "???" and data.get('cv_jp') != "???": # 角色声优表字符串
        str_cv = f" | CV: {data['cv_cn']} / {data['cv_jp']}"
    elif data.get("cv_cn") != "???":
        str_cv = f" | CV: {data['cv_cn']}"
    elif data.get("cv_jp") != "???":
        str_cv = f" | CV: {data['cv_jp']}"
    else:
        str_cv = ""

    if data["desc"] != "": # 角色描述字符串
        desc_str = f"\n\n*{data['desc']}*"
    else:
        desc_str = ""

    skinlists = {} # 创建角色皮肤列表
    for _quality in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]:
        for _type in ["静态立绘", "表情差分", "动态立绘", "战斗头像", "大招立绘", "战斗模型", "战斗效果", "宿舍模型"]:
            skinlists[_quality+_type] = []

    skinidlist_ = [] # 获取角色皮肤编号 在 skinidlist
    for skinid in list(data):
        if skinid.startswith('skin'):
            skinidlist_.append(skinid)
    skinidlist=list(set(skinidlist_))
    skinidlist.sort(key=skinidlist_.index)

    skin_name = "???" # 皮肤从 data 存入表 skinlists
    for skinid in skinidlist:
        for _quality in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]:
            if data[skinid].get("type") == _quality:
                if data[skinid].get("type") == "限定":
                    if skin_name != "???":
                        print(f"[WARN] id: {data['id']}, skin_name: {skin_name} -> {data[skinid]['name']}")
                    skin_name = data[skinid]["name"]
                if data[skinid].get("draw", None) is not None:
                    append_unique(skinlists[_quality+"静态立绘"], data[skinid]["draw"].lower())
                if data[skinid].get("draw_face", None) is not None:
                    append_unique(skinlists[_quality+"表情差分"], data[skinid]["draw_face"].lower())
                if data[skinid].get("spine", None) is not None:
                    if is_number(data[skinid]["spine"][:1]):
                        append_unique(skinlists[_quality+"动态立绘"], data[skinid]["spine"])
                    else:
                        append_unique(skinlists[_quality+"动态立绘"], data[skinid]["spine"].replace("_spine", ""))
                if data[skinid].get("fight_head", None) is not None:
                    append_unique(skinlists[_quality+"战斗头像"], data[skinid]["fight_head"])
                if data[skinid].get("cast2_card", None) is not None:
                    append_unique(skinlists[_quality+"大招立绘"], data[skinid]["cast2_card"])
                if data[skinid].get("model", None) is not None:
                    if data[skinid].get("skin_model", None) is not None:
                        append_unique(skinlists[_quality+"战斗模型"], data[skinid]["skin_model"])
                    else:
                        append_unique(skinlists[_quality+"战斗模型"], data[skinid]["model"])
                    append_unique(skinlists[_quality+"战斗效果"], data[skinid]["model"])
                    append_unique(skinlists[_quality+"宿舍模型"], data["id"])
        if data[skinid].get("type") not in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]:
            print(f"[WARN] id: {data[id]}, skin: {skinid} - _type not found.")

        '''
            if data[skinid].get("draw", None) is not None:
                append_unique(skinlists["特殊静态立绘"], data[skinid]["draw"].lower())
            if data[skinid].get("draw_face", None) is not None:
                append_unique(skinlists["特殊表情差分"], data[skinid]["draw_face"].lower())
            if data[skinid].get("spine", None) is not None:
                append_unique(skinlists["特殊动态立绘"], data[skinid]["spine"].replace("_spine", ""))
            if data[skinid].get("fight_head", None) is not None:
                append_unique(skinlists["特殊战斗头像"], data[skinid]["fight_head"])
            if data[skinid].get("cast2_card", None) is not None:
                append_unique(skinlists["特殊大招立绘"], data[skinid]["cast2_card"])
        '''
                    
    for removed_skin in configs_characters.removed_skins: # 移除皮肤
        if data["id"] == removed_skin[0]:
            skinlists[removed_skin[1]].remove(removed_skin[2])

    for added_skin in configs_characters.added_skins: # 增加皮肤
        if data["id"] == added_skin[0]:
            append_unique(skinlists[added_skin[1]], added_skin[2])
            if added_skin[1][:2] == "限定" and added_skin[3] is not None: # 如果为限定 则尝试增加皮肤名字
                if skin_name != "???":
                    print(f"[WARN] id: {data[id]}, skin_name: {skin_name} -> {data[skinid]['name']}")
                skin_name = added_skin[3]

    img_true = {} # 创建角色本地图像存在列表 img_true
    for _quality in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]:
        for _type in ["静态立绘", "表情差分", "动态立绘", "战斗头像", "大招立绘", "战斗模型", "战斗效果", "宿舍模型"]:
            img_true[_quality+_type] = []
        
        if len(skinlists[_quality+"静态立绘"]) != 0: # 检测静态立绘图像
            for j in range(0, len(skinlists[_quality+"静态立绘"])):
                if skinlists[_quality+"静态立绘"][j]+".png" in os.listdir(configs_general.img_dir):
                    img_true[_quality+"静态立绘"].append(j)

        if len(skinlists[_quality+"动态立绘"]) != 0: # 检测动态立绘图像
            for j in range(0, len(skinlists[_quality+"动态立绘"])):
                if skinlists[_quality+"动态立绘"][j]+".mp4" in os.listdir(configs_general.img_dir):
                    img_true[_quality+"动态立绘"].append(j)

        if len(skinlists[_quality+"战斗模型"]) != 0: # 检测动态立绘图像
            for j in range(0, len(skinlists[_quality+"战斗模型"])):
                if "prefabs_characters_" + skinlists[_quality+"战斗模型"][j] in configs_characters.custom_files:
                    img_true[_quality+"战斗模型"].append(j)

        if len(skinlists[_quality+"战斗效果"]) != 0: # 检测动态立绘图像
            for j in range(0, len(skinlists[_quality+"战斗效果"])):
                if "prefabs_effects_" + skinlists[_quality+"战斗效果"][j] in configs_characters.custom_files:
                    img_true[_quality+"战斗效果"].append(j)

        if len(skinlists[_quality+"宿舍模型"]) != 0: # 检测动态立绘图像
            for j in range(0, len(skinlists[_quality+"宿舍模型"])):
                if "prefabs_dormitory_" + skinlists[_quality+"宿舍模型"][j] in configs_characters.custom_files:
                    img_true[_quality+"宿舍模型"].append(j)

    # 设置图片字符串
    img_str1 = ""
    img_str2 = ""
    img_str3 = ""

    ## 如果 默认静态立绘 存在 且 任何突破立绘 存在
    if len(img_true["默认静态立绘"]) and len(img_true["突破静态立绘"]) + len(img_true["突破动态立绘"]):
        img_str1 = f''' | [预览默认立绘](/img/{skinlists["默认静态立绘"][img_true["默认静态立绘"][0]]}.png)'''


    ## 如果 限定动态立绘 存在 且 任何其他立绘 存在
    if len(img_true["限定动态立绘"]) and len(img_true["默认静态立绘"]) + len(img_true["突破静态立绘"]) + len(img_true["突破动态立绘"]):
        img_str2 = f''' | [预览限定立绘({skin_name})](/img/{skinlists["限定动态立绘"][img_true["限定动态立绘"][0]]}.mp4)'''

    ## 如果 限定静态立绘 存在 且 任何其他立绘 存在
    elif len(img_true["限定静态立绘"]) and len(img_true["默认静态立绘"]) + len(img_true["突破静态立绘"]) + len(img_true["突破动态立绘"]):
        img_str2 = f''' | [预览限定立绘({skin_name})](/img/{skinlists["限定静态立绘"][img_true["限定静态立绘"][0]]}.png)'''


    ## 如果 突破动态立绘
    if len(img_true["突破动态立绘"]):
        img_str3 = f'''\n<video autoplay loop><source src="/img/{skinlists["突破动态立绘"][img_true['突破动态立绘'][0]]}.mp4" type="video/mp4"></video>\n'''

    ## 如果 突破静态立绘
    elif len(img_true["突破静态立绘"]):
        img_str3 = f'''\n![](/img/{skinlists["突破静态立绘"][img_true["突破静态立绘"][0]]}.png)\n'''

    ## 如果 默认静态立绘
    elif len(img_true["默认静态立绘"]):
        img_str3 = f'''\n![](/img/{skinlists["默认静态立绘"][img_true["默认静态立绘"][0]]}.png)\n'''

    ## 如果 限定动态立绘
    elif len(img_true["限定动态立绘"]):
        img_str3 = f'''\n<video autoplay loop><source src="/img/{skinlists["限定动态立绘"][img_true['限定动态立绘'][0]]}.mp4" type="video/mp4"></video>\n'''

    ## 如果 限定静态立绘
    elif len(img_true["限定静态立绘"]):
        img_str3 = f'''\n![](/img/{skinlists["限定静态立绘"][img_true["限定静态立绘"][0]]}.png)\n'''


# 设置描述
    docs_character += f'''
{str_quality}{str_type}{pos_enum_str}{str_cv}{img_str1}{img_str2}{desc_str}
{img_str3}'''
    

    sklist_ = [] # 获取角色技能编号 在 sklist
    for skill_ in list(data):
        if skill_.startswith('skill'):
           sklist_.append(skill_)
    sklist=list(set(sklist_))
    sklist.sort(key=sklist_.index)
    
    for skill in sklist: # 获取单个技能
        
        # NP / SP 显示
        _np, _sp = ["", ""]
        if data[skill].get("sp") != "0" and data[skill].get("sp") is not None:
            _sp = f" | 同步 {data[skill]['sp']}"
        if data[skill].get("np") != "0" and data[skill].get("np") is not None:
            _np = f" | 能量 {data[skill]['np']}"
        if _np != "" or _sp != "":
            _rq = _np + _sp
        else:
            _rq = " | 能量 0"

        # 技能等级显示
        _lv = "Lv." + skill[-1:]

        # 设置技能范围字符串
        if data[skill].get("range_key") in ["one", "one_except_self", "myself"]:
            skrange_str = '''
```
⬛
```'''
        elif data[skill].get("range_key") in ["one_row"]:
            skrange_str = '''
```
⬛
⬛
⬛
```'''
        elif data[skill].get("range_key") in ["one_col"]:
            skrange_str = '''
```
⬛⬛⬛
```'''
        elif data[skill].get("range_key") in ["all"]:
            skrange_str = '''
```
⬛⬛⬛
⬛⬛⬛
⬛⬛⬛
```'''
        elif data[skill].get("range_key") in ["tian"]:
            skrange_str = '''
```
⬛⬛
⬛⬛
```'''
        elif data[skill].get("range_key") in ["shizi1"]:
            skrange_str = '''
```
  ⬛
⬛⬛⬛
  ⬛
```'''
        else:
            skrange_str = ""

        # 设置技能标题字符串
        if skill[:9] == "skillJC01":
            skname_str = f"## 普攻 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif skill[:9] == "skillJC02":
            skname_str = f"## 战技 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif skill[:9] == "skillJC03":
            skname_str = f"## 终结技 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif skill[:9] == "skillJC05" or (skill[:9] == "skillJC04" and "skillJC05_lv1" not in sklist):
            skname_str = f"## 爆发终结技 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif skill[:9] == "skillJC04":
            skname_str = f"## 超终结技 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif skill[:9] == "skillJC13":
            skname_str = f"### 核心爆发效果"
        elif skill[:8] == "skillTFM":
            skname_str = f"## 天赋 - {data[skill].get('name','???')} {_lv}{skrange_str}"
        elif skill[:7] == "skillTC":
            skname_str = f"## 特殊能力 - {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"
        elif len(skill) == 16:
            skname_str = f"## 被动 - {data[skill].get('name','???')} {_lv}{skrange_str}"
        elif len(skill) == 21:
            skname_str = f"## 天赋 - {data[skill].get('name','???')} {_lv}{skrange_str}"
        else:
            skname_str = f"## {data[skill].get('name','???')} {_lv}{_rq}{skrange_str}"

        # 设置技能描述字符串
        skdesc_str = "\n> "
        skdesc = rpdesc(data[skill].get("desc","???")).split("\n") # 分割多行为 list
        i=1
        for desc_s in skdesc: # 多行换行并适配粗体
            if i != 1:
                 skdesc_str += f"\n\n"
            skdesc_str += f"**{desc_s}**"
            i += 1

# 设置技能
        docs_character += f'''
{skname_str}{skdesc_str}
'''


    tllist_ = [] # 获取角色天赋编号 在 tllist
    for talent_ in list(data):
        if talent_.startswith('talent'):
            tllist_.append(talent_) # 获取天赋
    tllist=list(set(tllist_))
    tllist.sort(key=tllist_.index)
    
    for talent in tllist: # 获取单个天赋

        # 天赋等级显示
        _lv = "Lv." + talent[-1:]

        # 设置天赋标题字符串
        if talent[:8] == "talent01":
            tlname_str = f"## 跃升 I - {data[talent].get('name','???')} {_lv}"
        elif talent[:8] == "talent02":
            tlname_str = f"## 跃升 II - {data[talent].get('name','???')} {_lv}"
        elif talent[:8] == "talent03":
            tlname_str = f"## 跃升 III - {data[talent].get('name','???')} {_lv}"
        elif talent[:8] == "talent04":
            tlname_str = f"## 跃升 IV - {data[talent].get('name','???')} {_lv}"
        else:
            tlname_str = f"## {data[talent].get('name','???')} {_lv}"

        # 设置天赋描述字符串
        tldesc_str = "\n> "
        tldesc = rpdesc(data[talent].get("desc","???")).split("\n") # 分割多行为 list
        i=1
        for desc_s in tldesc: # 多行换行并适配粗体
            if i != 1:
                 tldesc_str += f"\n\n"
            tldesc_str += f"**{desc_s}**"
            i += 1

# 设置天赋
        docs_character += f'''
{tlname_str}{tldesc_str}
'''

    # 设置基地技能字符串
    if data.get("na","").get("name","") != "":
        na_str = f'''
## 基地 - {data["na"]["name"]} Lv.3
> **{data["na"]["desc"]}**
'''
    else:
        na_str = ""

# 设置基地技能
    docs_character += f'''{na_str}'''

# 其他 - 文档列表
    if data["ename"] != "???": # 设置角色英文名字符串
        en_str = " "+data["ename"]
    else:
        en_str = ""
    if int(data["id"]) < 80000 and data["id"] not in configs_characters.variation_cid:
        docs_list += f'''[<Badge type="danger"><b>`{data["id"]}` > {data["name"]}{en_str} {str_quality[:-1]}</b></Badge>](cid/{data["id"]})'''
    else:
        docs_list += f'''[<Badge type="info"><b>`{data["id"]}` > {data["name"]}{en_str} {str_quality[:-1]}</b></Badge>](cid/{data["id"]})'''

# 其他 - 文档索引列表
    if data["ename"] != "???": # 设置角色英文名字符串
        en_link_str = "-"+data["ename"].replace(" ", "-").lower()
    else:
        en_link_str = ""
    name_link_str = data["name"].replace(" ", "-").replace("“", "-").replace("”", "").lower()
    while name_link_str[-1:] == "-":
        name_link_str = name_link_str[:-1]
    name_link_str.replace("--", "-")
    if int(data["id"]) < 80000 and data["id"] not in configs_characters.variation_cid:
        docs_index_list += f'''[<Badge type="danger"><b>`{data["id"]}` > {data["name"]}{en_str} {str_quality[:-1]}</b></Badge>](characters_{character_type}#_{data["id"]}-{name_link_str}{en_link_str})'''
    else:
        docs_index_list += f'''[<Badge type="info"><b>`{data["id"]}` > {data["name"]}{en_str} {str_quality[:-1]}</b></Badge>](characters_{character_type}#_{data["id"]}-{name_link_str}{en_link_str})'''


# 其他 - 文档配置
    docs_config += f'''  {{ text: '{data["id"]} - {data["name"]}', link: '/data/characters/cid/{data["id"]}' }},'''

# 其他 - 索引
    
    if data["id"] in configs_characters.new_skins_cid:
        skin_name = "(未实装)" + skin_name

# 设置角色标题
    docs_index += f'''## `{data["id"]}` {data["name"]} {data["ename"]}\n'''

    for _quality in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]: # 遍历品质
        name_true = False
        for _type in ["静态立绘", "表情差分", "动态立绘", "战斗头像", "大招立绘"]:
            if len(skinlists[_quality+_type]) != 0 :
# 设置类型标题
                if name_true == False: # 创建标题
                    if _quality == "限定":
                        docs_index += f'\n### {_quality} - {skin_name}\n'
                    else:
                        docs_index += f'\n### {_quality}\n'
                    name_true = True

# 设置索引 - 有图像
                for i in range(0,len(skinlists[_quality+_type])):
                    if i in img_true[_quality+_type]:
                        if _type == "静态立绘":
                            docs_index += f'''- [静态立绘](/img/{skinlists[_quality+_type][i].lower()}.png) `textures_bigs_character_{skinlists[_quality+_type][i].lower()}`\n'''
                            used_files += [f"textures_bigs_character_{skinlists[_quality+_type][i].lower()}"]

                        elif _type == "动态立绘":
                            docs_index += f'''- [动态立绘](/img/{skinlists[_quality+_type][i].lower()}.mp4) `prefabs_spine_{skinlists[_quality+_type][i].lower()}`\n'''
                            used_files += [f"prefabs_spine_{skinlists[_quality+_type][i].lower()}"]

# 设置索引 - 无图像
                    else:
                        if _type == "静态立绘":
                            docs_index += f'''- 静态立绘 `textures_bigs_character_{skinlists[_quality+_type][i].lower()}`\n'''
                            used_files += [f"textures_bigs_character_{skinlists[_quality+_type][i].lower()}"]


                        elif _type == "表情差分":
                            docs_index += f'''- 表情差分 `textures_bigs_character_{skinlists[_quality+_type][i].lower()}`\n'''
                            used_files += [f"textures_bigs_character_{skinlists[_quality+_type][i].lower()}"]

                        elif _type == "动态立绘":
                            docs_index += f'''- 动态立绘 `prefabs_spine_{skinlists[_quality+_type][i].lower()}`\n'''
                            used_files += [f"prefabs_spine_{skinlists[_quality+_type][i].lower()}"]

                        elif _type in ["战斗头像", "大招立绘"]:
                            #tr_true = False
                            if is_number(skinlists[_quality+_type][i]):
                                    docs_index += f'''- {_type} `{skinlists[_quality+_type][i]}`\n'''
                                    used_files += [skinlists[_quality+_type][i]+""]
                            else:
                                for numfiles_config in configs_characters.numfiles_configs:
                                    if numfiles_config[0] == skinlists[_quality+_type][i]:
                                        name = skinlists[_quality+_type][i].replace(numfiles_config[0], numfiles_config[1])
                                        docs_index += f'''- {_type} `{name}`\n'''
                                        used_files += [name]
                                        #tr_true = True

# 设置索引 - 模型
    docs_index_model_cache = {}
    for _quality in ["默认", "突破", "限定", "核心同调", "形态切换", "特殊"]:
        for _type in ["战斗模型", "战斗效果", "宿舍模型"]:
            #if len(skinlists[_quality+_type]) != 0 :
            for num in range(0,len(skinlists[_quality+_type])):
# 设置索引 - 模型文件
                if num in img_true[_quality+_type]:

                    if _quality == "默认" and skinlists[_quality+_type][num] in skinlists["突破"+_type]:

                        if _type == "战斗模型":
                            index_file = "prefabs_characters_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, "通用", f'- 战斗模型 `{index_file}`\n')
                            append_unique(used_files, index_file)

                        elif _type == "战斗效果":
                            index_file = "prefabs_effects_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, "通用", f'- 战斗效果 `{index_file}`\n')
                            append_unique(used_files, index_file)

                        elif _type == "宿舍模型":
                            index_file = "prefabs_dormitory_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, "通用", f'- 宿舍模型 `{index_file}`\n')
                            append_unique(used_files, index_file)

                    elif not (_quality == "突破" and skinlists[_quality+_type][num] in skinlists["默认"+_type]):

                        if _type == "战斗模型":
                            index_file = "prefabs_characters_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, _quality, f'- 战斗模型 `{index_file}`\n')
                            append_unique(used_files, index_file)

                        elif _type == "战斗效果":
                            index_file = "prefabs_effects_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, _quality, f'- 战斗效果 `{index_file}`\n')
                            append_unique(used_files, index_file)

                        elif _type == "宿舍模型":
                            index_file = "prefabs_dormitory_" + skinlists[_quality+_type][num].lower()
                            dist_create(docs_index_model_cache, _quality, f'- 宿舍模型 `{index_file}`\n')
                            append_unique(used_files, index_file)

# 设置索引 - 模型标题
    docs_index_model = ""
    for _quality in docs_index_model_cache:
        if _quality == "限定":
            docs_index_model += f'\n### {_quality} - {skin_name}\n{docs_index_model_cache[_quality]}'
        else:
            docs_index_model += f'\n### {_quality}\n{docs_index_model_cache[_quality]}'
    if docs_index_model != "":
        docs_index_model = f'::: details 角色模型\n{docs_index_model}\n:::'

    docs_index = f'{docs_index}\n{docs_index_model}'

    return [docs_character, docs_list, docs_index, docs_config, used_files, docs_index_list]
                        
