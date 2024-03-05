import os
import docs_configs

# 索引列表缓存
ic_index_list = {}
uc_index_list = {}
for tid in ["10000", "20000", "30000", "40000", "50000", "60000", "70000", "71000"]: 
    ic_index_list[tid] = ""
    uc_index_list[tid] = ""
kishins_index_list = ""
monster_index_list = ""
npc_index_list = ""

# 索引缓存
ic_index = ""
uc_index = ""
kishins_index = ""
monster_index = ""
npc_index = ""

# 列表缓存
ic_list = {}
uc_list = {}
for tid in ["10000", "20000", "30000", "40000", "50000", "60000", "70000", "71000"]: 
    ic_list[tid] = ""
    uc_list[tid] = ""
kishins_list = ""
monster_list = ""
npc_list = ""

# 配置缓存
ic_configs = ""
uc_configs = ""
kishins_configs = ""
monster_configs = ""
npc_configs = ""

# 导出索引
os.makedirs(f"{docs_configs.index_dir}", exist_ok=True)

# 索引 - 0
def index_spawn():
    index_cache = f'''
# 角色
游戏内的所有角色，包括实装角色，未实装角色，机神，敌对生物，无战斗型角色等。

## [**实装角色**](characters_index)
目前可以通过游戏正常方式获得的角色，仅供参考。

### `10000` 山脉
{ic_index_list["10000"][:-1]}

### `20000` 乐团
{ic_index_list["20000"][:-1]}

### `30000` 不朽
{ic_index_list["30000"][:-1]}

### `40000` 气象
{ic_index_list["40000"][:-1]}

### `50000` 虫洞
{ic_index_list["50000"][:-1]}

### `60000` 灭刃
{ic_index_list["60000"][:-1]}

### `70000` 碎星
{ic_index_list["70000"][:-1]}

### `71000` 总队长
{ic_index_list["71000"][:-1]}

### `00000` 未实装
[<Badge type="danger"><b>`00000` > 未实装角色索引</b></Badge>](characters_uc)

## [**机神**](kishins_index)
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

{kishins_index_list[:-1]}

## [**敌对生物**](monster_index)
由 AI 操控的一些敌对型战斗实体，仅供参考。

{monster_index_list[:-1]}

## [**无战斗型角色**](npc_index)
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

{npc_index_list[:-1]}

'''
    with open(f"{docs_configs.index_dir}/characters.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(index_cache)

# 索引 - 1
def ic_index_spawn():
    ic_index_cache =f'''
# 实装角色
目前可以通过游戏正常方式获得的角色，仅供参考。

{ic_index}
'''
    with open(f"{docs_configs.index_dir}/characters_ic.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(ic_index_cache)

# 索引 - 2
def uc_index_spawn():
    uc_index_cache =f'''
# 未实装角色
对于一些未实装但存在的角色，仅供参考，以正式上线为准。

### `10000` 山脉
{uc_index_list["10000"][:-1]}

### `20000` 乐团
{uc_index_list["20000"][:-1]}

### `30000` 不朽
{uc_index_list["30000"][:-1]}

### `40000` 气象
{uc_index_list["40000"][:-1]}

### `50000` 虫洞
{uc_index_list["50000"][:-1]}

### `60000` 灭刃
{uc_index_list["60000"][:-1]}

### `70000` 碎星
{uc_index_list["70000"][:-1]}

### `71000` 总队长
{uc_index_list["71000"][:-1]}

{uc_index}
'''
    with open(f"{docs_configs.index_dir}/characters_uc.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(uc_index_cache)

# 索引 - 3
def kishins_index_spawn():
    kishins_index_cache =f'''
# 机神
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

{kishins_index}
'''
    with open(f"{docs_configs.index_dir}/characters_kishins.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(kishins_index_cache)

# 索引 - 4
def monster_index_spawn():
    monster_index_cache =f'''
# 敌对生物
由 AI 操控的一些敌对型战斗实体，仅供参考。

{monster_index}
'''
    with open(f"{docs_configs.index_dir}/characters_monster.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(monster_index_cache)

# 索引 - 5
def npc_index_spawn():
    npc_index_cache =f'''
# 无战斗型角色
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

{npc_index}
'''
    with open(f"{docs_configs.index_dir}/characters_npc.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(npc_index_cache)

# 导出角色
os.makedirs(f"{docs_configs.docs_dir}/characters/cid", exist_ok=True)
def characters_spawn(cid, data):
    with open(f"{docs_configs.docs_dir}/characters/cid/{cid}.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(data)

# 导出列表

# 列表 - 1
def ic_list_spawn():
    ic_list_cache = f'''
# 实装角色
目前可以通过游戏正常方式获得的角色，仅供参考。

### `10000` 山脉
{ic_list["10000"][:-1]}

### `20000` 乐团
{ic_list["20000"][:-1]}

### `30000` 不朽
{ic_list["30000"][:-1]}

### `40000` 气象
{ic_list["40000"][:-1]}

### `50000` 虫洞
{ic_list["50000"][:-1]}

### `60000` 灭刃
{ic_list["60000"][:-1]}

### `70000` 碎星
{ic_list["70000"][:-1]}

### `71000` 总队长
{ic_list["71000"][:-1]}

### `00000` 未实装
[<Badge type="danger"><b>`00000` > 未实装角色索引</b></Badge>](characters_uit_index)

'''
    with open(f"{docs_configs.docs_dir}/characters/ic.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(ic_list_cache)

# 列表 - 2
def uc_list_spawn():
    uc_list_cache = f'''
# 未实装角色
对于一些未实装但存在的角色，仅供参考，以正式上线为准。

### `10000` 山脉
{uc_list["10000"][:-1]}

### `20000` 乐团
{uc_list["20000"][:-1]}

### `30000` 不朽
{uc_list["30000"][:-1]}

### `40000` 气象
{uc_list["40000"][:-1]}

### `50000` 虫洞
{uc_list["50000"][:-1]}

### `60000` 灭刃
{uc_list["60000"][:-1]}

### `70000` 碎星
{uc_list["70000"][:-1]}

### `71000` 总队长
{uc_list["71000"][:-1]}

'''
    with open(f"{docs_configs.docs_dir}/characters/uc.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(uc_list_cache)

# 列表 - 3
def kishins_list_spawn():
    kishins_list_cache = f'''
# 机神
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

{kishins_list[:-1]}

'''
    with open(f"{docs_configs.docs_dir}/characters/kishins.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(kishins_list_cache)

# 列表 - 4
def monster_list_spawn():
    monster_list_cache = f'''
# 敌对生物
由 AI 操控的一些敌对型战斗实体，仅供参考。

{monster_list[:-1]}

'''
    with open(f"{docs_configs.docs_dir}/characters/monster.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(monster_list_cache)

# 列表 - 5
def npc_list_spawn():
    npc_list_cache = f'''
# 无战斗型角色
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

{npc_list[:-1]}

'''
    with open(f"{docs_configs.docs_dir}/characters/npc.md", 'w', encoding='utf-8') as docs_files:
        docs_files.write(npc_list_cache)

# 导出配置
os.makedirs(f"{docs_configs.configs_dir}", exist_ok=True)

# 配置
def ic_configs_spawn():
    ic_configs_cache = f'''import type {{ DefaultTheme }} from 'vitepress'

export const characters_ic: DefaultTheme.SidebarItem[] = [
{ic_configs}]
'''
    with open(f"{docs_configs.configs_dir}/characters_ic.mts", 'w', encoding='utf-8') as docs_files:
        docs_files.write(ic_configs_cache)

# 配置 - 2
def uc_configs_spawn():
    uc_configs_cache = f'''import type {{ DefaultTheme }} from 'vitepress'

export const characters_uc: DefaultTheme.SidebarItem[] = [
{uc_configs}]
'''
    with open(f"{docs_configs.configs_dir}/characters_uc.mts", 'w', encoding='utf-8') as docs_files:
        docs_files.write(uc_configs_cache)

# 配置 - 3
def kishins_configs_spawn():
    kishins_configs_cache = f'''import type {{ DefaultTheme }} from 'vitepress'

export const characters_kishins: DefaultTheme.SidebarItem[] = [
{kishins_configs}]
'''
    with open(f"{docs_configs.configs_dir}/characters_kishins.mts", 'w', encoding='utf-8') as docs_files:
        docs_files.write(kishins_configs_cache)

# 配置 - 4
def monster_configs_spawn():
    monster_configs_cache = f'''import type {{ DefaultTheme }} from 'vitepress'

export const characters_monster: DefaultTheme.SidebarItem[] = [
{monster_configs}]
'''
    with open(f"{docs_configs.configs_dir}/characters_monster.mts", 'w', encoding='utf-8') as docs_files:
        docs_files.write(monster_configs_cache)

# 配置 - 5
def npc_configs_spawn():
    npc_configs_cache = f'''import type {{ DefaultTheme }} from 'vitepress'

export const characters_npc: DefaultTheme.SidebarItem[] = [
{npc_configs}]
'''
    with open(f"{docs_configs.configs_dir}/characters_npc.mts", 'w', encoding='utf-8') as docs_files:
        docs_files.write(npc_configs_cache)