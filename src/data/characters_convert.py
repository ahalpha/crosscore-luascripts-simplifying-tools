import json
import os
from tqdm import tqdm
from tools import *
from src.configs import *

def characters_convert(data = False):
    if not data:
        try:
            with open(f'data_characters.json', 'r', encoding='utf-8') as data_files:
                data = json.loads(data_files.read())
        except:
            print("[WARN] data_characters_convert: Not data.")
            return


    os.makedirs(f"data/characters", exist_ok=True)
    print("> Characters Convert:")
    for a in tqdm(list(data)):
        data_cache = {}
        data_cache["id"] = str(a)

        if data[a].get("cfgCardData.id","") != "":
            data_cache["name"] = data[a].get("cfgCardData.name","")
        elif data[a].get("cfgcharacter01.key","") != "":
            data_cache["name"] = data[a].get("cfgcharacter01.key","")
        else:
            data_cache["name"] = "???"

        if data[a].get("cfgCfgCardRole.eName","") != "":
            data_cache["ename"] = data[a].get("cfgCfgCardRole.eName","")
        elif data[a].get("cfgCfgArchiveMonster.name_en","") != "":
            data_cache["ename"] = data[a].get("cfgCfgArchiveMonster.name_en","")
        else:
            data_cache["ename"] = "???"
        

        data_cache["desc"] = data[a].get("cfgCardData.m_Desc","")
        data_cache["quality"] = data[a].get("cfgCardData.quality","")

        if data[a].get("cfgCardData.pos_enum","") != "":
            data_cache["pos_enum"] = data[a].get("cfgCardData.pos_enum","")

        if data[a].get("cfgCfgCardRole.sSounder_cn","") == "？？？":
            data_cache["cv_cn"] = "???"
        elif data[a].get("cfgCfgCardRole.sSounder_cn","") != "":
            data_cache["cv_cn"] = data[a].get("cfgCfgCardRole.sSounder_cn","")
        else:
            data_cache["cv_cn"] = "???"
            

        if data[a].get("cfgCfgCardRole.sSounder_jp","") == "？？？":
            data_cache["cv_jp"] = "???"
        elif data[a].get("cfgCfgCardRole.sSounder_jp","") != "":
            data_cache["cv_jp"] = data[a].get("cfgCfgCardRole.sSounder_jp","")
        else:
            data_cache["cv_jp"] = "???"

        if data[a].get("cfgCardData.nClass","") != "":
            data_cache["nClass"] = data[a].get("cfgCardData.nClass","")


        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgcharacter'):
                append_unique(strilist,stri.split('.')[0])

        for stri in strilist:
            skin_cache = {}
            if data[a].get(stri+".skinType", "") == "":
                skin_cache["type"] = "默认"
            elif data[a].get(stri+".skinType", "") == "1":
                skin_cache["type"] = "限定"
                skin_cache["name"] = data[a].get(stri+".desc", "")
                skin_cache["desc"] = data[a].get(stri+".model_desc", "")
            elif data[a].get(stri+".skinType", "") == "2":
                skin_cache["type"] = "突破"
            elif data[a].get(stri+".skinType", "") == "3":
                skin_cache["type"] = "核心同调"
            else:
                skin_cache["type"] = "特殊"
                skin_cache["name"] = data[a].get(stri+".desc", "")
                skin_cache["desc"] = data[a].get(stri+".model_desc", "")

            if data[a].get(stri+".img", "") not in ["", "test_draw"]:
                skin_cache["draw"] = data[a].get(stri+".img", "")

            if data[a].get(stri+".faceID", "") not in ["", "test_draw"]:
                skin_cache["draw_face"] = data[a].get(stri+".img", "") + "_face"

            if data[a].get(stri+".l2dName", "") not in ["", "test_draw"]:
                skin_cache["spine"] = data[a].get(stri+".l2dName", "")

            if data[a].get(stri+".Fight_head", "") not in ["", "test_F"]:
                skin_cache["fight_head"] = data[a].get(stri+".Fight_head", "")

            if data[a].get(stri+".cast2_card", "") not in ["", "test_ohead"]:
                skin_cache["cast2_card"] = data[a].get(stri+".cast2_card", "")

            if data[a].get(stri+".name", "") != "":
                skin_cache["model"] = data[a].get(stri+".name", "")

            if data[a].get(stri+".skin", "") != "":
                skin_cache["skin_model"] = data[a].get(stri+".skin", "")

            data_cache["skin"+stri[-2:]] = skin_cache

        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgCfgSkillDesc') and stri.startswith('cfgCfgSkillDescTFO') == False and stri.startswith('cfgCfgSkillDescTC') == False:
                append_unique(strilist,stri.split('.')[0][:-2])
        
        for stri in strilist:
            skill_cache = {}
            skill_level = 5
            skill_break = False
            while skill_level > 0 and skill_break == False:


                if data[a].get(f"{stri}0{str(skill_level)}.name", "") != "":
                    skill_cache["name"] = data[a].get(f"{stri}0{str(skill_level)}.name", "")
                    skill_break = True
                else:
                    skill_level -= 1
                    skill_cache["name"] = "???"

                if data[a].get(f"{stri}0{str(skill_level)}.desc", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc", "")
                elif data[a].get(f"{stri}0{str(skill_level)}.desc1", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc1", "")
                elif data[a].get(f"{stri}0{str(skill_level)}.desc4", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc4", "")
                elif data[a].get(f"{stri}0{str(skill_level)}.desc5", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc5", "")
                elif data[a].get(f"{stri}0{str(skill_level)}.desc2", "") != "":
                    skin_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc2", "")
                elif data[a].get(f"{stri}0{str(skill_level)}.desc3", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc3", "")
                else:
                    skill_cache["desc"] = "???"

            data_cache["skill"+stri[15:]+"_lv"+str(skill_level)] = skill_cache

        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgCfgSkillDescTFO') or stri.startswith('cfgCfgSkillDescTC'):
                append_unique(strilist,stri.split('.')[0])
        
        for stri in strilist:
            skill_cache = {}
            skill_level = 5
            skill_break = False
            while skill_level > 0 and skill_break == False:


                if data[a].get(f"{stri}.name", "") != "":
                    skill_cache["name"] = data[a].get(f"{stri}.name", "")
                    skill_break = True
                else:
                    skill_level -= 1
                    skill_cache["name"] = "???"

                if data[a].get(f"{stri}.desc", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}.desc", "")
                elif data[a].get(f"{stri}.desc1", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}.desc1", "")
                elif data[a].get(f"{stri}.desc4", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}.desc4", "")
                elif data[a].get(f"{stri}.desc5", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}.desc5", "")
                elif data[a].get(f"{stri}.desc2", "") != "":
                    skin_cache["desc"] = data[a].get(f"{stri}.desc2", "")
                elif data[a].get(f"{stri}.desc3", "") != "":
                    skill_cache["desc"] = data[a].get(f"{stri}.desc3", "")
                else:
                    skill_cache["desc"] = "???"

            data_cache["skill"+stri[15:]+"_lv1"] = skill_cache




        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgCfgSubTalentSkillSS'):
                append_unique(strilist, stri.split('.')[0][:-2]) # 获取天赋

        for stri in strilist:
            talent_cache = {}
            talent_level = 5
            talent_break = False
            while talent_level > 0 and talent_break == False:
            
                if data[a].get(f"{stri}0{str(talent_level)}.name", "") != "":
                    talent_cache["name"] = data[a].get(f"{stri}0{str(talent_level)}.name", "")
                    talent_break = True
                else:
                    talent_level -= 1
                    talent_cache["name"] = "???"

                if data[a].get(f"{stri}0{str(talent_level)}.desc", "") != "":
                    talent_cache["desc"] = data[a].get(f"{stri}0{str(talent_level)}.desc", "")
                elif data[a].get(f"{stri}0{str(talent_level)}.desc1", "") != "":
                    talent_cache["desc"] = data[a].get(f"{stri}0{str(talent_level)}.desc1", "")
                elif data[a].get(f"{stri}0{str(talent_level)}.desc2", "") != "":
                    talent_cache["desc"] = data[a].get(f"{stri}0{str(talent_level)}.desc2", "")
                else:
                    talent_cache["desc"] = "???"

            data_cache["talent"+stri[22:]+"_lv"+str(talent_level)] = talent_cache


        data_cache["na"] = {}
        data_cache["na"]["name"] = data[a].get("cfgCfgCardRoleAbilityPoolNA03.remarks","")
        data_cache["na"]["desc"] = data[a].get("cfgCfgCardRoleAbilityPoolNA03.desc","")

        


        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgskill') and stri.startswith('cfgskillTFO') == False and stri.startswith('cfgskillTC') == False:
                strilist.append(stri.split('.')[0][:-2]) # 获取天赋

        strilists=list(set(strilist))
        strilists.sort(key=strilist.index)
        
        for stri in strilists:
            skill_level = 5
            skill_break = False
            while skill_level > 0 and skill_break == False:
                skill_cache = data_cache.get("skill"+stri[8:]+"_lv"+str(skill_level),{})

                if skill_cache.get("name", "???") == "???":
                    if data[a].get(f"{stri}0{str(skill_level)}.name", "") != "":
                        skill_cache["name"] = data[a].get(f"{stri}0{str(skill_level)}.name", "")

                if skill_cache.get("desc", "???") == "???":
                    if data[a].get(f"{stri}0{str(skill_level)}.desc", "") != "":
                        skill_cache["desc"] = data[a].get(f"{stri}0{str(skill_level)}.desc", "")
                
                
                if data[a].get(f"{stri}0{str(skill_level)}.name", "") != "":
                    skill_break = True
                else:
                    skill_level -= 1

                for st in ["sp", "np", "xp", "range_key"]:
                    if data[a].get(f"{stri}0{str(skill_level)}."+st, "") != "":
                        skill_cache[st] = data[a].get(f"{stri}0{str(skill_level)}."+st, "")


            data_cache["skill"+stri[8:]+"_lv"+str(skill_level)] = skill_cache



        strilist = []
        for stri in list(data[a]):
            if stri.startswith('cfgskillTFO') or stri.startswith('cfgskillTC'):
                strilist.append(stri.split('.')[0]) # 获取天赋

        strilists=list(set(strilist))
        strilists.sort(key=strilist.index)
        
        for stri in strilists:
            skill_level = 5
            skill_break = False
            while skill_level > 0 and skill_break == False:
                skill_cache = data_cache.get("skill"+stri[8:]+"_lv1",{})

                if skill_cache.get("name", "???") == "???":
                    if data[a].get(f"{stri}.name", "") != "":
                        skill_cache["name"] = data[a].get(f"{stri}.name", "")

                if skill_cache.get("desc", "???") == "???":
                    if data[a].get(f"{stri}.desc", "") != "":
                        skill_cache["desc"] = data[a].get(f"{stri}.desc", "")
                
                
                if data[a].get(f"{stri}.name", "") != "":
                    skill_break = True
                else:
                    skill_level -= 1

                for st in ["sp", "np", "xp", "range_key"]:
                    if data[a].get(f"{stri}."+st, "") != "":
                        skill_cache[st] = data[a].get(f"{stri}."+st, "")


            data_cache["skill"+stri[8:]+"_lv1"] = skill_cache


        with open(f"data/characters/{a}.json", 'w', encoding='utf-8') as data_files:
            data_files.write(json.dumps(data_cache, ensure_ascii=False, indent=4, separators=(',', ':')))

    return