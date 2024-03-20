import os
import re
from tqdm import tqdm
from tools import *
from src.configs import *
from .characters_id import characters_id

# 导出角色
def characters_main():
    docs_text = {}
    used_list = []

    os.makedirs(f"{configs_general.docs_dir}/characters/cid", exist_ok=True)
    print("> Characters Spawn Docs:")
    for a in tqdm(os.listdir("data/characters")):
        cid = a.split('.')[0]

    # 导出实装角色
        if cid in configs_characters.not_new_cid and cid not in configs_characters.variation_cid:
            cache = characters_id(a, "ic")
            write_files(f"{configs_general.docs_dir}/characters/cid/{cid}.md", cache[0])
            if 71000 <= int(cid) < 72000:
                dist_create(docs_text, "ic_list8", cache[1]+" ")
                dist_create(docs_text, "ic_index_list8", cache[5]+" ")
            else:
                dist_create(docs_text, "ic_list"+cid[:1], cache[1]+" ")
                dist_create(docs_text, "ic_index_list"+cid[:1], cache[5]+" ")
            dist_create(docs_text, "ic_index", cache[2]+"\n\n")
            dist_create(docs_text, "ic_configs", cache[3]+"\n")
            append_unique(used_list, cache[4])

    # 导出未实装角色
        elif int(cid) < 80000 and cid not in configs_characters.not_new_cid and cid not in configs_characters.variation_cid:
            cache = characters_id(a, "uc")
            write_files(f"{configs_general.docs_dir}/characters/cid/{cid}.md", cache[0])
            if 71000 <= int(cid) < 72000:
                dist_create(docs_text, "uc_list8", cache[1]+" ")
                dist_create(docs_text, "uc_index_list8", cache[5]+" ")
            else:
                dist_create(docs_text, "uc_list"+cid[:1], cache[1]+" ")
                dist_create(docs_text, "uc_index_list"+cid[:1], cache[5]+" ")
            dist_create(docs_text, "uc_index", cache[2]+"\n\n")
            dist_create(docs_text, "uc_configs", cache[3]+"\n")
            append_unique(used_list, cache[4])

    # 导出机神
        elif 80000 <= int(cid) < 85000 and cid not in configs_characters.variation_cid:
            cache = characters_id(a, "kishins")
            write_files(f"{configs_general.docs_dir}/characters/cid/{cid}.md", cache[0])
            dist_create(docs_text, "kishins_list", cache[1]+" ")
            dist_create(docs_text, "kishins_index", cache[2]+"\n\n")
            dist_create(docs_text, "kishins_configs", cache[3]+"\n")
            dist_create(docs_text, "kishins_index_list", cache[5]+" ")
            append_unique(used_list, cache[4])

    # 导出敌对生物
        elif int(cid) < 99000:
            cache = characters_id(a, "monster")
            write_files(f"{configs_general.docs_dir}/characters/cid/{cid}.md", cache[0])
            dist_create(docs_text, "monster_list", cache[1]+" ")
            dist_create(docs_text, "monster_index", cache[2]+"\n\n")
            dist_create(docs_text, "monster_configs", cache[3]+"\n")
            dist_create(docs_text, "monster_index_list", cache[5]+" ")
            append_unique(used_list, cache[4])

    # 导出无战斗型角色
        else:
            cache = characters_id(a, "npc")
            write_files(f"{configs_general.docs_dir}/characters/cid/{cid}.md", cache[0])
            dist_create(docs_text, "npc_list", cache[1]+" ")
            dist_create(docs_text, "npc_index", cache[2]+"\n\n")
            dist_create(docs_text, "npc_configs", cache[3]+"\n")
            dist_create(docs_text, "npc_index_list", cache[5]+" ")
            append_unique(used_list, cache[4])
    
    # 生成文档
    def spawn_docs(docs): # index_list
        cache = {}
        exec(f"text = configs_characters_docs.{docs}_text", globals(), cache)
        cache = cache["text"]
        names = re.findall('__(.*?)__', cache)
        for name in names:
            cache = cache.replace("__" + name + "__", docs_text.get(name, "")[:-1])
        return cache

    # 生成索引文档
    os.makedirs(f"{configs_general.index_dir}", exist_ok=True)
    write_files(f"{configs_general.index_dir}/characters.md", spawn_docs("index_list"))
    write_files(f"{configs_general.index_dir}/characters_ic.md", spawn_docs("ic_index"))
    write_files(f"{configs_general.index_dir}/characters_uc.md", spawn_docs("uc_index"))
    write_files(f"{configs_general.index_dir}/characters_kishins.md", spawn_docs("kishins_index"))
    write_files(f"{configs_general.index_dir}/characters_monster.md", spawn_docs("monster_index"))
    write_files(f"{configs_general.index_dir}/characters_npc.md", spawn_docs("npc_index"))

    # 生成列表文档
    write_files(f"{configs_general.docs_dir}/characters/ic.md", spawn_docs("ic_list"))
    write_files(f"{configs_general.docs_dir}/characters/uc.md", spawn_docs("uc_list"))
    write_files(f"{configs_general.docs_dir}/characters/kishins.md", spawn_docs("kishins_list"))
    write_files(f"{configs_general.docs_dir}/characters/monster.md", spawn_docs("monster_list"))
    write_files(f"{configs_general.docs_dir}/characters/npc.md", spawn_docs("npc_list"))

    # 生成侧栏文档
    if configs_general.enable_export_configs:
        os.makedirs(f"{configs_general.configs_dir}", exist_ok=True)
        write_files(f"{configs_general.configs_dir}/characters_ic.mts", spawn_docs("ic_configs"))
        write_files(f"{configs_general.configs_dir}/characters_uc.mts", spawn_docs("uc_configs"))
        write_files(f"{configs_general.configs_dir}/characters_kishins.mts", spawn_docs("kishins_configs"))
        write_files(f"{configs_general.configs_dir}/characters_monster.mts", spawn_docs("monster_configs"))
        write_files(f"{configs_general.configs_dir}/characters_npc.mts", spawn_docs("npc_configs"))

    # 获取文件列表
    used_files = used_list
    append_unique(used_files, configs_characters.disabled_index)
    custom_files = configs_characters.custom_files

    # 显示 Index 缺少的文件
    if configs_characters.print_index_false:
        index_false = []
        for file in custom_files:
            if file not in used_files:
                append_unique(index_false, file)
        if len(index_false) > 0:
            print(f'\n[WARN] Docs 索引缺少的文件: {index_false}\n')

    # 显示 Custom 缺少的文件
    if configs_characters.print_custom_false:
        custom_false = []
        for file in used_files:
            if file not in custom_files:
                append_unique(custom_false, file)
        if len(custom_false) > 0:
            print(f'\n[WARN] Custom 文件夹缺少的文件: {custom_false}\n')
    
    return used_list