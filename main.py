import lupa
import os
import json
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)

cfg_list = {
}


def org_cfg():
    pass

def tr_cfg():
    pass

data = {}



try:
    with open('./luascripts/cfgCardData.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCardData = lua.eval(f'function() {data_files.read()} end')
except:
    print("[ERROR] 没有加载基础文件\"cfgCardData.lua\"")
    exit()

ccd_names = list(cfgCardData()["names"].values())

for a in list(cfgCardData()["data"]):
    chr_data = {}
    row = list(cfgCardData()["data"][a].values())
    for i in range(len(ccd_names)):
        chr_data["cfgCardData."+ccd_names[i]] = row[i]
    data[row[0]] = chr_data # 保存用户数据



try:
    with open('./luascripts/cfgCfgCardRole.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCfgCardRole = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

cccr_names = list(cfgCfgCardRole()["names"].values())

for a in list(cfgCfgCardRole()["data"]):
    row = list(cfgCfgCardRole()["data"][a].values())
    chr_data = data.get(row[0],{})
    for i in range(len(cccr_names)):
        chr_data["cfgCfgCardRole."+cccr_names[i]] = row[i]
    data[row[0]] = chr_data # 保存用户数据




try:
    with open('./luascripts/cfgcharacter.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgcharacter = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

cc_names = list(cfgcharacter()["names"].values())

for a in list(cfgcharacter()["data"]):
    row = list(cfgcharacter()["data"][a].values())
    chr_data = data.get(row[0][:5],{})
    for i in range(len(cc_names)):
        chr_data["cfgcharacter"+row[0][5:]+"."+cc_names[i]] = row[i]
    data[row[0][:5]] = chr_data # 保存用户数据




try:
    with open('./luascripts/cfgCfgArchiveMonster.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCfgArchiveMonster = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

ccam_names = list(cfgCfgArchiveMonster()["names"].values())

for a in list(cfgCfgArchiveMonster()["data"]):
    row = list(cfgCfgArchiveMonster()["data"][a].values())
    chr_data = data.get(row[0][:4]+"0",{})
    for i in range(len(ccam_names)):
        chr_data["cfgCfgArchiveMonster"+"."+ccam_names[i]] = row[i]
    data[row[0][:4]+"0"] = chr_data # 保存用户数据




try:
    with open('./luascripts/cfgMonsterData.lua', 'r', encoding='utf-8') as data_files: 
        cfgMonsterData = lua.eval(f'function() {data_files.read()} end') # 读取数据为 lua 表
except:
    print("[WARNING] 没有加载文件")

cmd_names = list(cfgMonsterData()["names"].values()) # 读取 lua 表标题

for a in list(cfgMonsterData()["data"]): # 读取每行
    row = list(cfgMonsterData()["data"][a].values()) #读取一行
    chr_data = data.get(row[4][:5],{}) # 获取这一行之前的数据
    for i in range(len(cmd_names)): # 导入每一个字典
        b = 1
        while chr_data.get("cfgMonsterData"+format(b,'0>2d')+"."+cmd_names[i]) is not None: # 查重
            b += 1
        chr_data["cfgMonsterData"+format(b,'0>2d')+"."+cmd_names[i]] = row[i]
    data[row[4][:5]] = chr_data # 保存用户数据




try:
    with open('./luascripts/cfgCfgSkillDesc.lua', 'r', encoding='utf-8') as data_files: 
        cfgCfgSkillDesc = lua.eval(f'function() {data_files.read()} end') # 读取数据为 lua 表
except:
    print("[WARNING] 没有加载文件")

ccsd_names = list(cfgCfgSkillDesc()["names"].values()) # 读取 lua 表标题

skill_dict = {}
for a in list(cfgCfgSkillDesc()["data"]): # 读取每行
    row = list(cfgCfgSkillDesc()["data"][a].values())
    skill_dict[a] = row[0][:-2]


acc_skill = []

for chr_data in data:
    chr_skill = data[chr_data].get("cfgCardData.jcSkills","").split(',') # 读取单个角色技能
    chr_skill.extend(data[chr_data].get("cfgCardData.tcSkills","").split(',')) # 读取单个角色技能

    for i in range(len(chr_skill)): # 减少字典值 2 位
        chr_skill[i] = chr_skill[i][:-2]

    for skill_id in skill_dict:
        if skill_dict[skill_id] in chr_skill: # 查找符合条件的技能
            acc_skill.append(skill_id)
            row = list(cfgCfgSkillDesc()["data"][skill_id].values())
            for j in range(len(ccsd_names)): # 导入每一个字典
                data[chr_data].update({f"cfgCfgSkillDesc{row[0][-4:]}.{ccsd_names[j]}": row[j]})

for chr_data in data:
    chr_skill = data[chr_data].get("cfgCardData.tfSkills","").split(',') # 读取单个角色技能

    for i in range(len(chr_skill)): # 减少字典值 2 位
        chr_skill[i] = chr_skill[i][:-2]

    for skill_id in skill_dict:
        if skill_dict[skill_id] in chr_skill: # 查找符合条件的技能
            acc_skill.append(skill_id)
            
            row = list(cfgCfgSkillDesc()["data"][skill_id].values())
            for j in range(len(ccsd_names)): # 导入每一个字典
                data[chr_data].update({f"cfgCfgSkillDesc{row[0][-2:]}.{ccsd_names[j]}": row[j]})
#nAbilityId

#print(list(skill_dict))
#print(acc_skill)
#print(list(set(list(skill_dict))-set(acc_skill)))


try:
    with open('./luascripts/cfgCfgSubTalentSkillPool.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCfgSubTalentSkillPool = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

ccstsp_names = list(cfgCfgSubTalentSkillPool()["names"].values())



for a in list(cfgCfgSubTalentSkillPool()["data"]):
    row = list(cfgCfgSubTalentSkillPool()["data"][a].values())
    if row[3] != "":
        if data.get(row[0],False):
            for j in range(len(ccstsp_names)): # 导入每一个字典
                data[row[0]].update({f"cfgCfgSubTalentSkillPool{row[3]}.{ccstsp_names[j]}": row[j]})
        #else:
            #print(f"{row[3]} - {row[4]}")


try:
    with open('./luascripts/cfgCfgSubTalentSkill.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCfgSubTalentSkill = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

ccsts_names = list(cfgCfgSubTalentSkill()["names"].values())

talent_list = {}
for a in list(cfgCfgSubTalentSkill()["data"]): # 读取每行
    row = list(cfgCfgSubTalentSkill()["data"][a].values())
    talent_list[row[0]] = a

for a in list(data): # 读取一个角色
    talen_str = []
    chr_data = data[a]
    for str in list(chr_data):
        if str.startswith('cfgCfgSubTalentSkillPool'):
            talen_str.append(str[:25]) # 获取天赋
    #print(list(set(talen_str)))
    talen_strs=list(set(talen_str))
    talen_strs.sort(key=talen_str.index)


    for talen in talen_strs: # 循环读取天赋列表
        #print(data[talen+".id"])
        data_id = data[a][talen+".id"]
        for talent_id in talent_list:
            if data_id[:-1] == talent_id[:-1]:
                #print(f"{a} - {data_id}")
                row = list(cfgCfgSubTalentSkill()["data"][talent_list[talent_id]].values())
                for j in range(len(ccsts_names)):
                    data[a].update({f"cfgCfgSubTalentSkillSkill0{talen[-1:]}0{row[4]}.{ccsts_names[j]}": row[j]})


"""
        for b in list(cfgCfgSubTalentSkill()["data"]):
            #print(list(cfgCfgSubTalentSkill()["data"][b].values()))
            row = list(cfgCfgSubTalentSkill()["data"][b].values())
            if row[0][:-1] == data[a].get(talen+".id","")[:-1]:
        # row_1 = list(cfgCfgSubTalentSkill()["data"][talent_id[row[talen+".id"]]].values())
                for j in range(len(ccsts_names)): # 导入每一个字典
                    data[a].update({f"cfgCfgSubTalentSkillSkill0{talen[-1:]}0{row[4]}.{ccsts_names[j]}": row[j]})
            """




try:
    with open('./luascripts/cfgCfgCardRoleAbilityPool.lua', 'r', encoding='utf-8') as data_files: # 读取数据
        cfgCfgCardRoleAbilityPool = lua.eval(f'function() {data_files.read()} end')
except:
    print("[WARNING] 没有加载文件")

cccrap_names = list(cfgCfgCardRoleAbilityPool()["names"].values())

for a in list(data):
    talent_id = {}
    for b in list(cfgCfgCardRoleAbilityPool()["data"]): # 读取每行
        row = list(cfgCfgCardRoleAbilityPool()["data"][b].values())
        if row[0] == data[a].get("cfgCfgCardRole.nAbilityId",""):
            for j in range(len(cccrap_names)): # 导入每一个字典
                if row[9] == "":
                    row[9] = "0"
                data[a].update({f"cfgCfgCardRoleAbilityPool0{row[9]}.{cccrap_names[j]}": row[j]})



with open(f"data.json", 'w', encoding='utf-8') as data_files:
    data_files.write(json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ':')))


os.makedirs(f"data/characters", exist_ok=True)
os.makedirs(f"data/kishins", exist_ok=True)
os.makedirs(f"data/monster", exist_ok=True)



for a in list(data):
    if int(a) < 72000 and int(a) not in ["70020","70040","70060","70100","70120","70140","86130","86140"]:
        data_cache = {}
        data_cache["id"] = data[a].get("cfgCardData.id","")
        data_cache["name"] = data[a].get("cfgCardData.name","")
        data_cache["desc"] = data[a].get("cfgCardData.m_Desc","")
        data_cache["quality"] = data[a].get("cfgCardData.quality","")
        data_cache["cv_cn"] = data[a].get("cfgCfgCardRole.sSounder_cn","")
        data_cache["cv_jp"] = data[a].get("cfgCfgCardRole.sSounder_jp","")



        #row = data[a]
        strlist = []
        for str in list(data[a]):
            if str.startswith('cfgcharacter'):
                strlist.append(str.split('.')[0]) # 获取天赋

        strlists=list(set(strlist))
        strlists.sort(key=strlist.index)
        
        for str in strlists:
            #print(str)
            skin_cache = {}
            if data[a].get(str+".skinType", "") == "":
                skin_cache["type"] = "默认"
            elif data[a].get(str+".skinType", "") == "1":
                skin_cache["type"] = "限定"
                skin_cache["name"] = data[a].get(str+".desc", "")
                skin_cache["desc"] = data[a].get(str+".model_desc", "")
            elif data[a].get(str+".skinType", "") == "2":
                skin_cache["type"] = "突破"
            elif data[a].get(str+".skinType", "") == "3":
                skin_cache["type"] = "核心同调"
            else:
                skin_cache["type"] = "特殊"
                skin_cache["name"] = data[a].get(str+".desc", "")
                skin_cache["desc"] = data[a].get(str+".model_desc", "")

            if data[a].get(str+".img", "") not in ["", "test_draw"]:
                skin_cache["draw"] = "textures_bigs_character_" + data[a].get(str+".img", "")

            if data[a].get(str+".faceID", "") not in ["", "test_draw"]:
                skin_cache["draw_face"] = "textures_bigs_character_" + data[a].get(str+".img", "") + "_face"

            if data[a].get(str+".l2dName", "") not in ["", "test_draw"]:
                skin_cache["spine"] = "prefabs_spine_" + data[a].get(str+".l2dName", "")

            data_cache["skin"+str[-2:]] = skin_cache




        strlist = []
        for str in list(data[a]):
            if str.startswith('cfgCfgSkillDesc'):
                strlist.append(str.split('.')[0][:-2]) # 获取天赋

        strlists=list(set(strlist))
        strlists.sort(key=strlist.index)
        
        for str in strlists:
            skill_cache = {}


            if data[a].get(str+"05.name", "") != "":
                skill_cache["name"] = data[a].get(str+"05.name", "")
            else:
                skill_cache["name"] = "???"

            if data[a].get(str+"05.desc", "") != "":
                skill_cache["desc"] = data[a].get(str+"05.desc", "")
            elif data[a].get(str+"05.desc1", "") != "":
                skill_cache["desc"] = data[a].get(str+"05.desc1", "")
            elif data[a].get(str+"05.desc4", "") != "":
                skill_cache["desc"] = data[a].get(str+"05.desc4", "")
            elif data[a].get(str+"05.desc5", "") != "":
                skill_cache["desc"] = data[a].get(str+"05.desc5", "")
            elif data[a].get(str+"05.desc2", "") != "":
                skin_cache["desc"] = data[a].get(str+"05.desc2", "")
            elif data[a].get(str+"05.desc3", "") != "":
                skill_cache["desc"] = data[a].get(str+"05.desc3", "")
            else:
                skill_cache["desc"] = "???"

            data_cache["skill"+str[15:]+"_lv5"] = skill_cache




        strlist = []
        for str in list(data[a]):
            if str.startswith('cfgCfgSubTalentSkillSkill'):
                strlist.append(str.split('.')[0][:-2]) # 获取天赋

        strlists=list(set(strlist))
        strlists.sort(key=strlist.index)

        for str in strlists:
            #print(str)

            talent_cache = {}

            
            if data[a].get(str+"05.name", "") != "":
                talent_cache["name"] = data[a].get(str+"05.name", "")
            else:
                talent_cache["name"] = "???"

            if data[a].get(str+"05.desc", "") != "":
                talent_cache["desc"] = data[a].get(str+"05.desc", "")
            elif data[a].get(str+"05.desc1", "") != "":
                talent_cache["desc"] = data[a].get(str+"05.desc1", "")
            elif data[a].get(str+"05.desc2", "") != "":
                talent_cache["desc"] = data[a].get(str+"05.desc2", "")
            else:
                talent_cache["desc"] = "???"

            data_cache["talent"+str[25:]+"_lv5"] = talent_cache


        data_cache["na"] = {}
        data_cache["na"]["name"] = data[a].get("cfgCfgCardRoleAbilityPool03.remarks","")
        data_cache["na"]["desc"] = data[a].get("cfgCfgCardRoleAbilityPool03.desc","")

        

        with open(f"data/characters/{a}.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data_cache, ensure_ascii=False, indent=4, separators=(',', ':')))

    elif 80000 <= int(a) < 90000:
        data_cache = data[a]





        with open(f"data/kishins/{a}.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data_cache, ensure_ascii=False, indent=4, separators=(',', ':')))

    else:
        data_cache = data[a]



        with open(f"data/monster/{a}.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data_cache, ensure_ascii=False, indent=4, separators=(',', ':')))




