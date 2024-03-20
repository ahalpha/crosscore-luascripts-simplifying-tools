# 索引列表
index_list_text = '''
# 角色
游戏内的所有角色，包括实装角色，未实装角色，机神，敌对生物，无战斗型角色等。

## [**实装角色**](characters_index)
目前可以通过游戏正常方式获得的角色，仅供参考。

### `10000` 山脉
__ic_index_list1__

### `20000` 乐团
__ic_index_list2__

### `30000` 不朽
__ic_index_list3__

### `40000` 气象
__ic_index_list4__

### `50000` 虫洞
__ic_index_list5__

### `60000` 灭刃
__ic_index_list6__

### `70000` 碎星
__ic_index_list7__

### `71000` 总队长
__ic_index_list8__

### `00000` 未实装
[<Badge type="danger"><b>`00000` > 未实装角色索引</b></Badge>](characters_uc)

## [**机神**](kishins_index)
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

__kishins_index_list__

## [**敌对生物**](monster_index)
由 AI 操控的一些敌对型战斗实体，仅供参考。

__monster_index_list__

## [**无战斗型角色**](npc_index)
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

__npc_index_list__

'''

# 索引 - 实装角色
ic_index_text ='''
# 实装角色
目前可以通过游戏正常方式获得的角色，仅供参考。

__ic_index__

'''

# 索引 - 未实装角色
uc_index_text ='''
# 未实装角色
对于一些未实装但存在的角色，仅供参考，以正式上线为准。

### `10000` 山脉
__uc_index_list1__

### `20000` 乐团
__uc_index_list2__

### `30000` 不朽
__uc_index_list3__

### `40000` 气象
__uc_index_list4__

### `50000` 虫洞
__uc_index_list5__

### `60000` 灭刃
__uc_index_list6__

### `70000` 碎星
__uc_index_list7__

### `71000` 总队长
__uc_index_list8__

__uc_index__

'''

# 索引 - 机神
kishins_index_text ='''
# 机神
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

__kishins_index__
'''

# 索引 - 敌对生物
monster_index_text ='''
# 敌对生物
由 AI 操控的一些敌对型战斗实体，仅供参考。

__monster_index__

'''

# 索引 - 无战斗型角色
npc_index_text ='''
# 无战斗型角色
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

__npc_index__

'''

# 数据库列表 - 实装角色
ic_list_text = '''
# 实装角色
目前可以通过游戏正常方式获得的角色，仅供参考。

### `10000` 山脉
__ic_list1__

### `20000` 乐团
__ic_list2__

### `30000` 不朽
__ic_list3__

### `40000` 气象
__ic_list4__

### `50000` 虫洞
__ic_list5__

### `60000` 灭刃
__ic_list6__

### `70000` 碎星
__ic_list7__

### `71000` 总队长
__ic_list8__

### `00000` 未实装
[<Badge type="danger"><b>`00000` > 未实装角色索引</b></Badge>](characters_uit_index)

'''

# 数据库列表 - 未实装角色
uc_list_text = '''
# 未实装角色
对于一些未实装但存在的角色，仅供参考，以正式上线为准。

### `10000` 山脉
__uc_list1__

### `20000` 乐团
__uc_list2__

### `30000` 不朽
__uc_list3__

### `40000` 气象
__uc_list4__

### `50000` 虫洞
__uc_list5__

### `60000` 灭刃
__uc_list6__

### `70000` 碎星
__uc_list7__

### `71000` 总队长
__uc_list8__

'''

# 数据库列表 - 机神
kishins_list_text = '''
# 机神
由一些角色使用特殊技能召唤的额外战斗实体，仅供参考。

__kishins_list__

'''

# 数据库列表 - 敌对生物
monster_list_text = '''
# 敌对生物
由 AI 操控的一些敌对型战斗实体，仅供参考。

__monster_list__

'''

# 数据库列表 - 无战斗型角色
npc_list_text = '''
# 无战斗型角色
不属于战斗实体但拥有立绘的角色，多为剧情中出现，仅供参考。

__npc_list__

'''

# 数据库侧栏 - 实装角色
ic_configs_text = '''import type {{ DefaultTheme }} from 'vitepress'

export const characters_ic: DefaultTheme.SidebarItem[] = [
__ic_configs__
]
'''

# 数据库侧栏 - 未实装角色
uc_configs_text = '''import type {{ DefaultTheme }} from 'vitepress'

export const characters_uc: DefaultTheme.SidebarItem[] = [
__uc_configs__
]
'''

# 数据库侧栏 - 机神
kishins_configs_text = '''import type {{ DefaultTheme }} from 'vitepress'

export const characters_kishins: DefaultTheme.SidebarItem[] = [
__kishins_configs__
]
'''

# 数据库侧栏 - 敌对生物
monster_configs_text = '''import type {{ DefaultTheme }} from 'vitepress'

export const characters_monster: DefaultTheme.SidebarItem[] = [
__monster_configs__
]
'''

# 数据库侧栏 - 无战斗型角色
npc_configs_text = '''import type {{ DefaultTheme }} from 'vitepress'

export const characters_npc: DefaultTheme.SidebarItem[] = [
__npc_configs__
]
'''