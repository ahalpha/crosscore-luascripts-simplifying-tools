import json
import os
from tqdm import tqdm
from tools import *

def story_convert(data = False):
    if not data:
        try:
            with open(f'data_story.json', 'r', encoding='utf-8') as data_files:
                data = json.loads(data_files.read())
        except:
            print("[WARN] data_characters_convert: Not data.")
            return

    os.makedirs(f"data/story", exist_ok=True)
    print("> Story Convert:")
    for a in tqdm(list(data)):
        data_cache = {}
        data_cache["id"] = a

# 关卡
        if data[a].get("cfgStoryInfo.name","") != "":
            data_cache["name"] = data[a].get("cfgStoryInfo.name","")
        if data[a].get("cfgStoryInfo.section_name","") != "":
            data_cache["sname"] = data[a].get("cfgStoryInfo.section_name","")
        if data[a].get("cfgStoryInfo.desc","") != "":
            data_cache["desc"] = data[a].get("cfgStoryInfo.desc","")
        if data[a].get("cfgStoryInfo.type","") != "":
            data_cache["type"] = data[a].get("cfgStoryInfo.type","")

# 对话
        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgTalkInfo') or stri.startswith('cfgTalkOption'):
                append_unique(strilist,stri.split('.')[0])
        
        for stri in strilist:

            if stri.startswith('cfgTalkInfo'):
                talk_cache = {}
                if data[a].get(stri+".talk", "") != "":
                    talk_cache["talk"] = data[a].get(stri+".talk", "")
                if data[a].get(stri+".talk_en", "") != "":
                    talk_cache["talk_en"] = data[a].get(stri+".talk_en", "")
                if data[a].get(stri+".content", "") != "":
                    talk_cache["content"] = data[a].get(stri+".content", "")
                if data[a].get(stri+".imgContent", "") != "":
                    talk_cache["img"] = data[a].get(stri+".imgContent", "")
                if data[a].get(stri+".bgm", "") != "":
                    talk_cache["bgm"] = data[a].get(stri+".bgm", "")
                if data[a].get(stri+".roleInfos", "") != "":
                    talk_cache["role"] = json.loads(data[a].get(stri+".roleInfos", ""))
                
                data_cache["talk_"+stri[11:]] = talk_cache
            
            elif stri.startswith('cfgTalkOption'):
                option_cache = {}
                if data[a].get(stri+".content", "") != "":
                    option_cache["content"] = data[a].get(stri+".content", "")
                
                data_cache["option_"+stri[13:]] = option_cache

            else:
                print(f"Unknown talk: {stri}")


        with open(f"data/story/{a}.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data_cache, ensure_ascii=False, indent=4, separators=(',', ':')))

    return