import json
from tqdm import tqdm
from tools import *
from src.configs import *

def story_collect():
    data = {}
    excel = {}

    print("> Story Collect: [1/2]")
    story_list = {}
    excel[0] = read_lua_excel_id("cfgStoryInfo.lua")
    if excel[0]:
        for i in tqdm(excel[0]):
            _id = excel[0][i]["id"]
            _data = excel[0][i]

            if i > 0:
                if excel[0][i]["beginId"] != "":
                    story_list[i-1] += excel[0][i]["beginId"]
                else:
                    story_list[i-1] += story_list[i-1][:1] + "999999"
            if excel[0][i]["beginId"] != "":
                story_list[i] = excel[0][i]["beginId"] + ","
            else:
                story_list[i] = "9999999" + ","
            
            sid = _id
            data[sid] = data.get(sid,{})

            for _name in _data:
                data[sid][f"cfgStoryInfo.{_name}"] = _data[_name]
        
        story_list[len(story_list)-1] += story_list[len(story_list)-1][:1] + "999999"

    print("> Story Collect: [2/2]")
    excel[1] = read_lua_excel_id("cfgTalkInfo1.lua")
    excel[2] = read_lua_excel_id("cfgTalkInfo3.lua")
    excel[3] = read_lua_excel_id("cfgTalkInfo2.lua")
    excel[4] = read_lua_excel_id("cfgTalkInfo4.lua")
    excel[5] = read_lua_excel_id("cfgTalkOption.lua")
    excel[6] = read_lua_excel("cfgcharacter.lua")
    if excel[0] and excel[1] and excel[2] and excel[3] and excel[4]:
        for i in tqdm(excel[0]):
            sid = excel[0][i]["id"]
            
            fhead = int(story_list[i][0][:1])
            if fhead != 9:
                for j in excel[fhead]:
                    _id = excel[fhead][j]["id"]
                    _data = excel[fhead][j]

                    if int(story_list[i].split(",")[0]) <= int(_id) < int(story_list[i].split(",")[1]):

                        for _name in _data:
                            data[sid][f"cfgTalkInfo{_id}.{_name}"] = _data[_name]

                        if _data.get("options","") != "":
                            for k in excel[5]:
                                __id = excel[5][k]["id"]
                                __data = excel[5][k]

                                if __id == _data.get("options",""):
                                    for __name in __data:
                                        data[sid][f"cfgTalkOption{__id}.{__name}"] = __data[__name]

                        if _data.get("roleInfos","") != "":
                            skin_dump = json.loads(_data["roleInfos"])
                            if isinstance(skin_dump,list):
                                for skin in skin_dump:
                                    skin_id = str(skin["id"])
                                    data[sid][f"cfgcharacter{skin_id}.img"] = excel[6].get(skin_id,{"img": ""})["img"]
                            else:
                                skin_id = str(skin_dump["id"])
                                data[sid][f"cfgcharacter{skin_id}.img"] = excel[6].get(skin_id,{"img": ""})["img"]

    if configs_general.spawn_data_files:
        with open(f"data_story.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ':')))

    return data