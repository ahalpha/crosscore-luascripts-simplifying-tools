import json
import os
import re
from tools import *
from src.configs import *

rptalk_text = [
    ["%s","你"],
    ["<size=.*?>","</br><center><font size=\"5\">"],
    ["</size>","</font></center>"],
]
rptalk_txt_text = [
    ["……","。"],
    ["<size=.*?>",""],
    ["</size>",""],
]

def rptalk(talk):
    for rp in rptalk_text:
        talk = re.sub(rp[0], rp[1], talk)
    talk = tranlate(talk, "auto2ja")
    return talk

def rptalk_txt(talk):
    for rp in rptalk_txt_text:
        talk = re.sub(rp[0], rp[1], talk)
    talk = tranlate(talk, "auto2ja")
    return talk

def story_id(file):

    docs_story = "" # 设置该角色文档缓存
    docs_list = "" # 设置该角色文档列表缓存
    docs_index = "" # 设置该角色文档索引缓存
    docs_config = "" # 设置该角色文档配置缓存
    used_files = [] # 已使用的立绘文件
    docs_index_list = "" # 设置该角色文档列表缓存
    txt_story = "" # 设置该角色文档列表缓存

    with open(f'data/story/{file}', 'r', encoding='utf-8') as data_file: # 读取数据
        data = json.loads(data_file.read())

# 基础信息
    
    if data.get("name","") != "" and data.get("sname","") != "":
        name_str = f' {data["name"]} - {data["sname"]}'
    elif data.get("name","") != "":
        name_str = f' {data["name"]}'
    elif data.get("sname","") != "":
        name_str = f' {data["sname"]}'
    else:
        name_str = f''

    if data.get("desc","") != "":
        desc_str = f'*{data["desc"]}*'
    else:
        desc_str = ""

    docs_story += f'''# `{data["id"]}`{name_str}
{desc_str}
'''
    txt_story += f'''{data.get("name","")}。{data.get("sname","")}
{rptalk_txt(data.get("desc",""))}'''
    
    docs_index += f'''## `{data["id"]}`{name_str}'''

# 对话列表

    tklist = []
    for talk in list(data):
        if talk.startswith('talk_') or talk.startswith('option_'):
            append_unique(tklist,talk)
    
    for talk in tklist:
        if data[talk].get("img",False):
            for img in data[talk]["img"].split(","):
                if img[:-4]+".png" in os.listdir(configs_general.img_dir):
                    docs_story += f'\n---\n\n<img src="/img/{img[:-4]}.png" width="1920px"/>\n'
                    docs_index += f'\n- [静态立绘](/img/{img[:-4]}.png) `textures_bigs_uis_plot_{img[:-4]}`'
                    append_unique(used_files,f"textures_bigs_uis_plot_{img[:-4]}")
                else:
                    docs_story += f'\n---\n\n```\n[图片缺失]: {img[:-4]}.png\n```\n'
                    docs_index += f'\n- 静态立绘 `textures_bigs_uis_plot_{img[:-4]}`'
                    append_unique(used_files,f"textures_bigs_uis_plot_{img[:-4]}")
        docs_story += f'\n'
        if data[talk].get("talk",False):
            docs_story += f'[<Badge type="info"><b>{rptalk(data[talk]["talk"])}</b></Badge>](##) '
            txt_story += f'\n{rptalk_txt(data[talk]["talk"])}：'
        if data[talk].get("content",False):
            docs_story += f'{rptalk(data[talk]["content"])}\n'
            txt_story += f'“{rptalk_txt(data[talk]["content"])}”'




    docs_config += f'''  {{ text: '{name_str[1:]}', link: '/data/story/sid/{data["id"]}' }},'''

    if name_str != "":
        lname_str = " >" + name_str
    else:
        lname_str = ""

    docs_list += f'''[<Badge type="tip"><b>`{data["id"]}`{lname_str}</b></Badge>](sid/{data["id"]})'''

    name_link_str = name_str.replace(" ", "-").replace("“", "-").replace("”", "").lower()
    while name_link_str[-1:] == "-":
        name_link_str = name_link_str[:-1]
    while name_link_str.find("--") != -1:
        name_link_str = name_link_str.replace("--", "-")

    docs_index_list += f'''[<Badge type="tip"><b>`{data["id"]}`{lname_str}</b></Badge>](illvstration_story#_{data["id"]}{name_link_str})'''

    return [docs_story, docs_config, txt_story, docs_index, docs_list, docs_index_list, used_files]