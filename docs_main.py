import os
from docs_characters_tr import docs_tr
from tools.append_unique import append_unique
import docs_configs
import docs_characters_spawn

used_files = []


# 导出角色

for a in os.listdir("data/characters"):
    cid = a.split('.')[0]
# 导出实装角色
    if cid in docs_configs.not_new_cid and cid not in docs_configs.variation_cid:
        cache = docs_tr(a, "ic")
        docs_characters_spawn.characters_spawn(cid, cache[0])
        if 71000 <= int(cid) < 72000: docs_characters_spawn.ic_list["71000"] += cache[1]+" "
        else: docs_characters_spawn.ic_list[cid[:1]+"0000"] += cache[1]+" "
        docs_characters_spawn.ic_index += cache[2]+"\n\n"
        docs_characters_spawn.ic_configs += cache[3]+"\n"
        used_files += cache[4]
        if 71000 <= int(cid) < 72000: docs_characters_spawn.ic_index_list["71000"] += cache[5]+" "
        else: docs_characters_spawn.ic_index_list[cid[:1]+"0000"] += cache[5]+" "

# 导出未实装角色
    elif int(cid) < 80000 and cid not in docs_configs.not_new_cid and cid not in docs_configs.variation_cid:
        cache = docs_tr(a, "uc")
        docs_characters_spawn.characters_spawn(cid, cache[0])
        if 71000 <= int(cid) < 72000: docs_characters_spawn.uc_list["71000"] += cache[1]+" "
        else: docs_characters_spawn.uc_list[cid[:1]+"0000"] += cache[1]+" "
        docs_characters_spawn.uc_index += cache[2]+"\n\n"
        docs_characters_spawn.uc_configs += cache[3]+"\n"
        used_files += cache[4]
        if 71000 <= int(cid) < 72000: docs_characters_spawn.uc_index_list["71000"] += cache[5]+" "
        else: docs_characters_spawn.uc_index_list[cid[:1]+"0000"] += cache[5]+" "

# 导出机神
    elif 80000 <= int(cid) < 85000 and cid not in docs_configs.variation_cid:
        cache = docs_tr(a, "kishins")
        docs_characters_spawn.characters_spawn(cid, cache[0])
        docs_characters_spawn.kishins_list += cache[1]+" "
        docs_characters_spawn.kishins_index += cache[2]+"\n\n"
        docs_characters_spawn.kishins_configs += cache[3]+"\n"
        used_files += cache[4]
        docs_characters_spawn.kishins_index_list += cache[5]+" "

# 导出敌对生物
    elif int(cid) < 99000:
        cache = docs_tr(a, "monster")
        docs_characters_spawn.characters_spawn(cid, cache[0])
        docs_characters_spawn.monster_list += cache[1]+" "
        docs_characters_spawn.monster_index += cache[2]+"\n\n"
        docs_characters_spawn.monster_configs += cache[3]+"\n"
        used_files += cache[4]
        docs_characters_spawn.monster_index_list += cache[5]+" "

# 导出无战斗型角色
    else:
        cache = docs_tr(a, "npc")
        docs_characters_spawn.characters_spawn(cid, cache[0])
        docs_characters_spawn.npc_list += cache[1]+" "
        docs_characters_spawn.npc_index += cache[2]+"\n\n"
        docs_characters_spawn.npc_configs += cache[3]+"\n"
        used_files += cache[4]
        docs_characters_spawn.npc_index_list += cache[5]+" "

# 导出索引
docs_characters_spawn.index_spawn()
docs_characters_spawn.ic_index_spawn()
docs_characters_spawn.uc_index_spawn()
docs_characters_spawn.kishins_index_spawn()
docs_characters_spawn.monster_index_spawn()
docs_characters_spawn.npc_index_spawn()

# 导出列表
docs_characters_spawn.ic_list_spawn()
docs_characters_spawn.uc_list_spawn()
docs_characters_spawn.kishins_list_spawn()
docs_characters_spawn.monster_list_spawn()
docs_characters_spawn.npc_list_spawn()

# 导出配置
if docs_configs.enable_export_configs:
    docs_characters_spawn.ic_configs_spawn()
    docs_characters_spawn.uc_configs_spawn()
    docs_characters_spawn.kishins_configs_spawn()
    docs_characters_spawn.monster_configs_spawn()
    docs_characters_spawn.npc_configs_spawn()

# 记录已使用文件列表
used_list = docs_configs.disabled_index
for file in used_files:
    if file != "":
        append_unique(used_list, file)

# 导出 Index 缺少的文件
docs_false_export = True

docs_false = []
for _custom in docs_configs.custom_files:
    if _custom not in used_list:
        docs_false.append(_custom)
if len(docs_false) > 0 and docs_false_export:
    print(f'''\n[WARN] Docs 索引缺少的文件: {docs_false}\n''')

# 导出 Custom 缺少的文件
custom_false_export = False

custom_false = []
for _used in used_list:
    if _used not in docs_configs.custom_files:
        custom_false.append(_used)
if len(custom_false) > 0 and custom_false_export:
    print(f'''\nCustom 文件夹缺少的文件: {custom_false}\n''')
    
# 生成时间
import time
t = time.strftime('%Y-%m-%d %H:%M', time.localtime())
time_cache = f'''
::: info

请注意，本文章截至最后一次更新此资源文件索引的内容的时间为 `{t}` ，此时交错战线的最新版本为 `{docs_configs.game_version}` 。

:::
'''[1:][:-1]
with open(f"{docs_configs.index_dir}/time.md", 'w', encoding='utf-8') as docs_files:
    docs_files.write(time_cache)
