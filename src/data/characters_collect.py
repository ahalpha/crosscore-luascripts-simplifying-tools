import json
from tqdm import tqdm
from tools import *
from src.configs import *

def characters_collect():
    data = {}
    mcid = [str(_mcid) for _mcid in range(85000,99000)] + ["70020", "70040", "70060", "70100", "70120", "70140", "70250", "70270", "70300"]

# 基础数据
    print("> Characters Collect: [1/7]")
    _excel = read_lua_excel("cfgCardData.lua")
    if _excel:
        for _id in tqdm(_excel):
            _data = _excel[_id]

            cid = _id
            data[cid] = data.get(cid,{})

            for _name in _data:
                data[cid][f"cfgCardData.{_name}"] = _data[_name]

# 资料数据
    print("> Characters Collect: [2/7]")
    _excel = read_lua_excel("cfgCfgCardRole.lua")
    if _excel:
        for _id in tqdm(_excel):
            _data = _excel[_id]

            cid = _id
            data[cid] = data.get(cid,{})

            for _name in _data:
                data[cid][f"cfgCfgCardRole.{_name}"] = _data[_name]

# 模型数据
    print("> Characters Collect: [3/7]")
    _excel = read_lua_excel("cfgcharacter.lua")
    if _excel:
        for _id in tqdm(_excel):
            _data = _excel[_id]

            cid = _id[:5]
            data[cid] = data.get(cid,{})

            for _name in _data:
                data[cid][f"cfgcharacter{_id[5:]}.{_name}"] = _data[_name]

# 敌人资料数据
    print("> Characters Collect: [4/7]")
    _excel = read_lua_excel("cfgCfgArchiveMonster.lua")
    if _excel:
        for _id in tqdm(_excel):
            _data = _excel[_id]

            cid = _id[:4]+"0"
            data[cid] = data.get(cid,{})

            for _name in _data:
                data[cid][f"cfgCfgArchiveMonster.{_name}"] = _data[_name]

# 敌人数据
    print("> Characters Collect: [5/7]")
    _excel = read_lua_excel("cfgMonsterData.lua")
    if _excel:
        for _id in tqdm(_excel):
            _data = _excel[_id]

            cid = _data["model"][:5]
            data[cid] = data.get(cid,{})

            _num = 1
            while data[cid].get(f"cfgMonsterData{format(_num,'0>2d')}.id"):
                _num += 1

            for _name in _data:
                data[cid][f"cfgMonsterData{format(_num,'0>2d')}.{_name}"] = _data[_name]

# 跃升技能列表
    print("> Characters Collect: [6/7]")
    _excel = read_lua_excel_id("cfgCfgSubTalentSkillPool.lua")
    if _excel:
        for i in tqdm(_excel):
            _data = _excel[i]

            cid = _data["id1"]
            data[cid] = data.get(cid,{})

            if _data['index'] != "":
                for _name in _data:
                    data[cid][f"cfgCfgSubTalentSkillPool0{_data['index']}.{_name}"] = _data[_name]
            else:
                for _name in _data:
                    data[cid][f"cfgCfgSubTalentSkillPool00.{_name}"] = _data[_name]

# 技能描述数据
    print("> Characters Collect: [7/7]")
    _excel1 = read_lua_excel("cfgCfgSkillDesc.lua")
    _excel2 = read_lua_excel("cfgCfgSubTalentSkill.lua")
    _excel3 = read_lua_excel_id("cfgCfgCardRoleAbilityPool.lua")
    _excel4 = read_lua_excel_id("cfgskill.lua")

    if _excel1 and _excel2:
        _excel1_id_9 = [_id for _id in _excel1 if len(_id) == 9]
        _excel1_id_7 = [_id for _id in _excel1 if len(_id) == 7]
        _excel1_id_6 = [_id for _id in _excel1 if len(_id) == 6]
        _excel1_id_4 = [_id for _id in _excel1 if len(_id) == 4]

        _excel2_id_6 = [_id for _id in _excel2 if len(_id) == 6]
        _excel2_id_4 = [_id for _id in _excel2 if len(_id) == 4]

        _excel3_id_5 = [_id for _id in _excel3 if len(_excel3[_id]["id"]) == 5]
        _excel3_id_4 = [_id for _id in _excel3 if len(_excel3[_id]["id"]) == 4]

        _excel4_id_9 = [_id for _id in _excel4 if len(_excel4[_id]["id"]) == 9]
        _excel4_id_7 = [_id for _id in _excel4 if len(_excel4[_id]["id"]) == 7]
        _excel4_id_6 = [_id for _id in _excel4 if len(_excel4[_id]["id"]) == 6]
        _excel4_id_4 = [_id for _id in _excel4 if len(_excel4[_id]["id"]) == 4]

        for cid in tqdm(data):
# 攻击技能
            if cid not in mcid:
                cskid = data[cid].get("cfgCardData.jcSkills","").split(',')
            else:
                cskid = data[cid].get("cfgMonsterData01.jcSkills","").split(',')

            for i in range(len(cskid)):
                if len(cskid[i]) == 9:

                    for _id in _excel1_id_9:
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescJC{_id[-4:]}.{_name}"] = _data[_name]

                    for j in _excel4_id_9:
                        _id = _excel4[j]["id"]
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillJC{_id[-4:]}.{_name}"] = _data[_name]

                elif len(cskid[i]) != 0:
                    print(f" [WARN] Unknown JC Skill: {cid} - {cskid[i]}")
# 天赋技能
            if cid not in mcid:
                cskid = data[cid].get("cfgCardData.tfSkills","").split(',')
            else:
                cskid = data[cid].get("cfgMonsterData01.tfSkills","").split(',')

            for i in range(len(cskid)):
                if len(cskid[i]) == 9:

                    for _id in _excel1_id_9:
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescTFO{_id}.{_name}"] = _data[_name]

                    for j in _excel4_id_9:
                        _id = _excel4[j]["id"]
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillTFO{_id}.{_name}"] = _data[_name]

                elif len(cskid[i]) == 7:

                    for _id in _excel1_id_7:
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescTFM{_id[-2:]}.{_name}"] = _data[_name]

                    for j in _excel4_id_7:
                        _id = _excel4[j]["id"]
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillTFM{_id[-2:]}.{_name}"] = _data[_name]

                elif len(cskid[i]) == 6:

                    for _id in _excel1_id_6:
                        if cskid[i] == _id:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescTFO{_id}.{_name}"] = _data[_name]

                    for j in _excel4_id_6:
                        _id = _excel4[j]["id"]
                        if cskid[i] == _id:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillTFO{_id}.{_name}"] = _data[_name]

                elif len(cskid[i]) == 4:

                    for _id in _excel1_id_4:
                        if cskid[i] == _id:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescTFO{_id}.{_name}"] = _data[_name]

                    for j in _excel4_id_4:
                        _id = _excel4[j]["id"]
                        if cskid[i] == _id:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillTFO{_id}.{_name}"] = _data[_name]


                elif len(cskid[i]) != 0:
                    print(f" [WARN] Unknown TF Skill: {cid} - {cskid[i]}")
# 特殊技能
            if cid not in mcid:
                cskid = data[cid].get("cfgCardData.tcSkills","").split(',')
            else:
                cskid = data[cid].get("cfgMonsterData01.tcSkills","").split(',')

            for i in range(len(cskid)):
                if len(cskid[i]) == 9:

                    for _id in _excel1_id_9:
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel1[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSkillDescTC{_id[-4:]}.{_name}"] = _data[_name]

                    for j in _excel4_id_9:
                        _id = _excel4[j]["id"]
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel4[j]

                            for _name in _data:
                                data[cid][f"cfgskillTC{_id[-4:]}.{_name}"] = _data[_name]

                elif len(cskid[i]) != 0:
                    print(f" [WARN] Unknown TC Skill: {cid} - {cskid[i]}")  
# 跃升技能
            cskid = [data[cid][_skid] for _skid in data[cid] if _skid.startswith('cfgCfgSubTalentSkillPool') and _skid[-4:] == ".id2"]

            for i in range(len(cskid)):
                if len(cskid[i]) == 6:

                    for _id in _excel2_id_6:
                        if cskid[i][:-2] == _id[:-2]:
                            _data = _excel2[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSubTalentSkillSS0{i}{_id[-2:]}.{_name}"] = _data[_name]

                elif len(cskid[i]) == 4:

                    for _id in _excel2_id_4:
                        if cskid[i][:-1] == _id[:-1]:
                            _data = _excel2[_id]

                            for _name in _data:
                                data[cid][f"cfgCfgSubTalentSkillSS0{i}0{_id[-1:]}.{_name}"] = _data[_name]

                elif len(cskid[i]) != 0:
                    print(f" [WARN] Unknown SS Skill: {cid} - {cskid[i]}")  
# 基地技能
            cskid = data[cid].get("cfgCfgCardRole.nAbilityId","").split(',')

            for i in range(len(cskid)):
                if len(cskid[i]) == 5:

                    for j in _excel3_id_5:
                        _id = _excel3[j]["id"]
                        if cskid[i] == _id:
                            _data = _excel3[j]

                            if _data["index"] == "":
                                _data['index'] = 0

                            for _name in _data:
                                data[cid][f"cfgCfgCardRoleAbilityPoolNA0{_data['index']}.{_name}"] = _data[_name]

                elif len(cskid[i]) == 4:

                    for j in _excel3_id_4:
                        _id = _excel3[j]["id"]
                        if cskid[i] == _id:
                            _data = _excel3[j]

                            if _data["index"] == "":
                                _data['index'] = 0

                            for _name in _data:
                                data[cid][f"cfgCfgCardRoleAbilityPoolNA0{_data['index']}.{_name}"] = _data[_name]

                elif len(cskid[i]) != 0:
                    print(f" [WARN] Unknown NA Skill: {cid} - {cskid[i]}") 
    
    if configs_general.spawn_data_files:
        with open(f"data_characters.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ':')))

    return data