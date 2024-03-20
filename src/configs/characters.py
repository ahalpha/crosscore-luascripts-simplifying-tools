# 显示 Index 缺少的文件
print_index_false = True

# 显示 Custom 缺少的文件
print_custom_false = False

# 实装角色ID
not_new_cid = [
    "10010", "10020", "10030", "10040", "10110", "10120", "10180", "10190", "10240", "10260",
    "20020", "20040", "20070", "20080", "20090", "20110", "20120", "20140", "20240",
    "30020", "30050", "30080", "30100", "30120", "30180", "30200", "30220", "30230", "30310", "30320", "30400", "30420", "30430", "30431",
    "40010", "40030", "40040", "40050", "40070", "40120", "40140", "40150", "40190", "40210", "40220", "40290", "40310", "40320", "40350",
    "50010", "50011", "50020", "50030", "50040", "50041", "50060", "50080", "50100", "50130", "50140", "50180", "50190",
    "60020", "60030", "60050", "60060", "60070", "60080", "60090", "60110", "60140", "60190",
    "70050", "70051", "70070", "70090", "71010", "71020"
]

# 异变角色ID
variation_cid = [
    "70020", "70040", "70060", "70100", "70120", "70140", "70250", "70270", "70300"
]

# 未实装皮肤角色ID
new_skins_cid = [
    "10010", "10240", "20040", "20070", "20080", "30050", "30100", "30220", "30320", "30400", "30420", "40050", "60191"
]

# 角色附属昵称
ename_configs = [
    ["10250","Sphalerite"], ["30040","Kenai"], ["30170","Miacis"], ["30260","Tyrant"], ["40060","Mist"], ["40080","Cumulonimbus"], ["40120","Hail"], ["40330","Tornado",], ["40390","Fracture"],
    ["50300","Reduvia"], ["50310","Orchid"], ["70310","Atum"], ["70320","Osiris"], ["80010","Steelgiant"], ["80020","Soulless"], ["80030","Sternsauge"], ["80050","Helion"], ["70250","Skadi"],
    ["70270","Thor"], ["85010","Blazers"], ["86010","Steelgiant"], ["86020","Soulless"], ["86030","Sternsauge"], ["86050","Helion"], ["86060","Bloodwarlock"], ["86080","Tx"], ["86090","Tx"],
    ["86110","Dz00e02"], ["90390","Cerberus"], ["90540","Dissocider"], ["90600","Paranoid"], ["90840","Robot"], ["90850","Robot"], ["90860","Robot"], ["90870","Robot"], ["90880","Folie"],
    ["90900","Weaver"], ["90910","Scout"], ["90920","Abandonment"], ["90930","Ambushsnipe"], ["90940","Ambushsnipe"], ["90950","Ambushsnipe"], ["90960","Ambushsnipe"], ["90970","Ambushsnipe"],
    ["90980","Badwolf"], ["90990","Rebel"], ["91130","Variation Zeus"], ["92291","Vidar"], ["92292","Vidar"], ["93010","Tombspearsoldier"], ["93020","Tombspearsoldier"], ["93030","Tombspearsoldier"],
    ["93040","Tombspearsoldier"], ["93050","Oman Soldier"], ["93060","Oman Soldier"], ["93070","Oman Soldier"], ["93080","Oman Soldier"], ["93090","Oman Soldier"], ["93100","Betisvassalr"],
    ["93110","Betisspiritualist"], ["93120","Betiscurse"], ["93130","Betisshaman"], ["93140","Betissupernaturalist"], ["93150","Betis"], ["93160","Benbenstone"], ["93170","Rielbeacon"],
    ["93180","Differentobelisk"], ["93190","Rielstele"], ["93200","Baka"], ["93210","Rielservant"], ["93220","Rielscout"], ["93230","Rielscout"], ["93240","Rielfaithful"], ["93250","Rielacolyte"],
    ["93260","Betisvisionary"], ["93270","Betisoracle"], ["93280","Oman"], ["93290","Riel"], ["99060","Prometheus"], ["99070","Akas"], ["99080","Kadya"], ["99090","Pretender"], ["99100","Operator"],
    ["99110","Greek"], ["99120","Nordics"], ["99130","Mechanical"], ["99140","Core"], ["99150","Core"], ["99160","Karl"], ["99170","Mia"], ["99180","Villagehead"], ["99190","Michelle"],
    ["99200","Flower"], ["99210","Hlokk"], ["99220","Valkyrja"], ["99230","NPCBoy"], ["99240","NPCGirl"], ["99250","NPCGirl"], ["99260","NPCHoward"], ["99270","NPCMan Purgetrooper"],
    ["99280","NPCGirl Purgetrooper"], ["99290","NPCMichellepetit"], ["99310","NPC Amon"], ["99320","NPCMan Egyptian"], ["99330","NPCGirl Egyptian"], ["99340","NPC Amon Matrixleader"],
    ["99350","NPC Mahat"], ["99361","Phalanx"], ["99362","Nestingdoll"], ["99363","Nestingdoll"], ["99364","Weimei"], ["99371","Pretender"], ["99381","Eig"],

    ["30431","核心同调"], ["50011","核心同调"], ["50041","核心同调"], ["60191","核心同调"],

    ["30011","形态切换"], ["70051","形态切换"], ["70321","形态切换"],
    ["90311","形态切换"], ["90321","形态切换"], ["90331","形态切换"], ["90341","形态切换"], ["90351","形态切换"], ["90361","形态切换"], ["90401","形态切换"], ["90841","形态切换"], ["90851","形态切换"],
    ["90861","形态切换"], ["90871","形态切换"], ["90881","形态切换"], ["93281","形态切换"], ["93291","形态切换"], ["98011","形态切换"],
    
    ["71010","男主"], ["71020","女主"],
    
    ["80080",""], ["80090",""], ["80120",""], ["80170",""], ["80180",""], ["80200",""], ["80240",""], ["80260",""], ["86120",""], ["86130",""], ["86140",""], ["86150",""], ["86160",""],
    ["86170",""], ["86180",""], ["86190",""], ["86200",""], ["86210",""], ["86220",""], ["86230",""], ["86240",""], ["86250",""], ["86260",""], ["86270",""], ["86280",""], ["99300",""],
]

# 角色皮肤增加
added_skins_cache = '''
50320 突破动态立绘 50320_break_Salticidae_spine
70110 限定静态立绘 7011_hermes03_draw 皮肤时装
50020 特殊大招立绘 -86817250
40050 特殊大招立绘 352459276
50011 特殊战斗头像 -380712160
50190 特殊大招立绘 -645511593
60210 默认大招立绘 -748755818
70250 特殊大招立绘 953908542
50041 特殊战斗头像 1128014561
80240 默认战斗头像 -1334405166
90380 特殊战斗头像 -1577947897
20110 特殊动态立绘 Arpeggio
20140 特殊静态立绘 2014_capriccio03_draw
50140 核心同调静态立绘 5014_wasp03_draw
50310 特殊静态立绘 5031_orchid01_draw
50310 特殊静态立绘 5031_orchid02_draw
70040 特殊静态立绘 7004_neptune02_draw
70040 特殊表情差分 7004_neptune02_draw_face
70250 特殊静态立绘 7025_skadi02_draw
71010 默认表情差分 7101_lead01_draw_face
80240 默认静态立绘 8011_dz00e01_draw
99080 默认静态立绘 9908_kadya03_draw
99310 默认表情差分 99310_npc_amon_draw_face
99999 默认大招头像 1739341194
99381 默认静态立绘 99381_eig01_draw
40010 特殊静态立绘 4001_hurricane04_draw
60030 特殊静态立绘 6003_durandal04_draw
60250 默认表情差分 6025_fang01_draw_face

91000 默认战斗模型 g91000
91010 默认战斗模型 g91010
91030 默认战斗模型 g91020
91030 默认战斗模型 g91030
91040 默认战斗模型 g91040
91050 默认战斗模型 g91050

91000 默认战斗效果 g91000
91010 默认战斗效果 g91010
91030 默认战斗效果 g91020
91030 默认战斗效果 g91030
91040 默认战斗效果 g91040
91050 默认战斗效果 g91050
'''

added_skins = []
for added_skin_cache in added_skins_cache.split("\n"):
    if len(added_skin_cache.split(" ")) >= 3:
        added_skins.append(added_skin_cache.split(" ")) # 转换成列表

# 角色皮肤移除
removed_skins_cache = '''
70110 默认静态立绘 7011_hermes03_draw
'''

removed_skins = []
for removed_skin_cache in removed_skins_cache.split("\n"):
    if len(removed_skin_cache.split(" ")) >= 3:
        removed_skins.append(removed_skin_cache.split(" ")) # 转换成列表

# 转换描述
rpdesc_text  = [
    ["<color=#FFC432>\n【心流感应（莫纳）】</color>","\n<color=#FFC432>【心流感应（莫纳）】</color>"],

    ["<color=#", "<font color=#"],
    ["</color>", "</font>"],

    ["<skillEff=真实伤害>", "[<Badge type=\"danger\">**真实伤害**</Badge>](##)"],
    ["<skillEff=灼烧>", "[<Badge type=\"danger\">**灼烧**</Badge>](##)"],

    ["<skillEff=相转移>", "[<Badge type=\"warning\">**相转移**</Badge>](##)"],
    ["<skillEff=过热>", "[<Badge type=\"warning\">**过热**</Badge>](##)"],
    ["<skillEff=强制嘲讽>", "[<Badge type=\"warning\">**强制嘲讽**</Badge>](##)"],
    ["<skillEff=能量屏障>", "[<Badge type=\"warning\">**能量屏障**</Badge>](##)"],
    ["<skillEff=物理屏障>", "[<Badge type=\"warning\">**物理屏障**</Badge>](##)"],
    ["<skillEff=重塑>", "[<Badge type=\"warning\">**重塑**</Badge>](##)"],

    ["<skillEff=基础概率>", "[<Badge type=\"info\">**基础概率**</Badge>](##)"],
    ["<skillEff=负面效果>", "[<Badge type=\"info\">**负面效果**</Badge>](##)"],
    ["<skillEff=战败退场>", "[<Badge type=\"info\">**战败退场**</Badge>](##)"],
    ["<skillEff=控制效果>", "[<Badge type=\"info\">**控制效果**</Badge>](##)"],
    ["<skillEff=弱化效果>", "[<Badge type=\"info\">**弱化效果**</Badge>](##)"],
    ["<skillEff=强化效果>", "[<Badge type=\"info\">**强化效果**</Badge>](##)"],

    ["<skillEff=防御弱化>", "[<Badge type=\"tip\">**防御弱化**</Badge>](##)"],
    ["<skillEff=眩晕>", "[<Badge type=\"tip\">**眩晕**</Badge>](##)"],
    ["<skillEff=化解>", "[<Badge type=\"tip\">**化解**</Badge>](##)"],
    ["<skillEff=昏睡>", "[<Badge type=\"tip\">**昏睡**</Badge>](##)"],
    ["<skillEff=残损>", "[<Badge type=\"tip\">**残损**</Badge>](##)"],
    ["<skillEff=劣化>", "[<Badge type=\"tip\">**劣化**</Badge>](##)"],
    ["<skillEff=战术嘲讽>", "[<Badge type=\"tip\">**战术嘲讽**</Badge>](##)"],
    ["<skillEff=恩赐>", "[<Badge type=\"tip\">**恩赐**</Badge>](##)"],
    ["<skillEff=短路>", "[<Badge type=\"tip\">**短路**</Badge>](##)"],
    ["<skillEff=沉默>", "[<Badge type=\"tip\">**沉默**</Badge>](##)"],

    ["<font color=#FFC432>47％<font color=#FFC432>", "<font color=#FFC432>47％</font>"],
    ["并使目标<font color=#FFC432>攻击-30%、防御-30%（持续2回合）", "并使目标<font color=#FFC432>攻击-30%、防御-30%（持续2回合）</font>"],

    ["#FFC432", "#bf6b14"],
    ["#FF3300", "#f55385"],
    ["#33CCFF", "#89cdc5"]
]

# 禁用索引列表
disabled_index = [
    "prefabs_spine_cg_seashore", # 插画
    "prefabs_spine_cg02", # 插画
    "prefabs_spine_cg03_fireworksloient", # 插画
    "prefabs_spine_cg04_summerrendezvous", # 插画
    "prefabs_spine_cg05_shimmeringfeast_spine", # 插画
    "prefabs_spine_cg06_trytomoveforward_spine", # 插画
    "prefabs_spine_xingyun", # 插画
    "textures_bigs_character_device_draw", # 设备动画
    "textures_bigs_character_99381_eig01_draw", # 无效
    "1739341194", # 无效

    "prefabs_effects_cardpool_10010", # 卡池
    "prefabs_effects_cardpool_20110",
    "prefabs_effects_cardpool_30050",
    "prefabs_effects_cardpool_30400",
    "prefabs_effects_cardpool_30420",
    "prefabs_effects_cardpool_30430",
    "prefabs_effects_cardpool_40310",
    "prefabs_effects_cardpool_40400",
    "prefabs_effects_cardpool_50010",
    "prefabs_effects_cardpool_50320",
    "prefabs_effects_cardpool_60020",
    "prefabs_effects_cardpool_60050",
    "prefabs_effects_cardpool_70030",
    "prefabs_effects_cardpool_70050",
    "prefabs_effects_cardpool_70090",
    "prefabs_effects_cardpool_60090",

    "prefabs_characters_combo", # 其他杂项
    "prefabs_dormitory_body",
    "prefabs_dormitory_prop",
    "prefabs_effects_battle",
    "prefabs_effects_buff",
    "prefabs_effects_camera_effs",
    "prefabs_effects_common",
    "prefabs_effects_common_hit",
    "prefabs_effects_device",
    "prefabs_effects_dormitory",
    "prefabs_effects_emoji",
    "prefabs_effects_heihua",
    "prefabs_effects_hero",
    "prefabs_effects_menu",
    "prefabs_effects_openbox",
    "prefabs_effects_overload",
    "prefabs_effects_pifuzhuanshi",
    "prefabs_effects_plot",
    "prefabs_effects_resurrection",
    "prefabs_effects_rolelist",
    "prefabs_effects_shandianxiaoguo",
    "prefabs_effects_shanguangxiaoguo",
    "prefabs_effects_summoneffs",
    "prefabs_effects_texiao_yvaine_jijianhecheng",
    "prefabs_effects_ui_structure",
    "prefabs_effects_uieff",
    "prefabs_effects_videos"
]

# 角色皮肤增加
numfiles_configs_cache = '''
10010_Break_Alps_F->-733843653
10010_Common_Alps_F->-1772925851
1001_Alps01_ohead->1190954965
10020_Break_Kunlun_F->1891117790
10020_Common_Kunlun_F->-1266596156
1002_Kunlun01_ohead->799201786
10030_Break_Wolframite_F->-638346933
10030_Common_Wolframite_F->2004984190
10030_Skin102_Wolframite_F->684737680
10030_Skin102_Wolframite_O->733770882
1003_Rocky01_ohead->-2138485020
10040_Andes01_ohead->-979963122
10040_Break_Andes_F->2077212777
10040_Common_Andes_F->1375206019
10110_Break_Granite_F->-1222049471
10110_Common_Granite_F->524606169
1011_ElCapitan01_ohead->-1876758513
10120_Break_Jadeite_F->994878662
10120_Common_Jadeite_F->-591598813
10120_Jadeite01_ohead->-349978113
10180_Break_Kailas_F->-1532155654
10180_Common_Kailas_F->-1159058049
1018_Kailas01_ohead->-218576562
10190_Break_Ljen_F->204634499
10190_Common_Ljen_F->551823666
10190_Common_Ljen_O->868630444
10240_Break_Pyroxene_F->415709756
10240_Common_Pyroxene_F->-129702955
10240_Pyroxene01_ohead->-1667696252
10260_Break_Ruby_F->44447013
10260_Common_Ruby_F->-976794542
10260_Common_Ruby_O->-689612084
20020_Break_March_F->242505603
20020_Common_March_F->2024367471
2002_March01_ohead->940775985
20040_Break_Fugue_F->-1167641902
20040_Common_Fugue_F->-1096509395
2004_Fugue01_ohead->-1930804927
20070_Break_Anthem_F->-497630042
20070_Common_Anthem_F->-1925789918
20070_Common_Anthem_O->245948775
20080_Break_Melody_F->-2025089573
20080_Common_Melody_F->2024014129
2008_Melody01_ohead->-1284810877
20090_Break_Echo_F->1038707825
20090_Common_Echo_F->-1541468059
2009_Chords01_ohead->1986323145
20110_Arpeggio01_ohead->713649493
20110_Break_Arpeggio_F->1839674813
20110_Common_Arpeggio_F->-770145493
20120_Break_Elegy_F->1406208208
20120_Common_Elegy_F->-1375806110
20120_Elegy01_ohead->1055436727
20140_Break_Capriccio_F->-1853980377
20140_Common_Capriccio_F->1052256621
2014_Capriccio01_ohead->2130680168
20150_Common_Fantasia_O->919198383
20240_Break_Uillean_F->158344727
20240_Common_Uillean_F->-1728410954
2024_Uillean01_ohead->148569193
30020_Break_Lokotunjailurus_F->166513186
30020_Common_Lokotunjailurus_F->606439568
3002_Lokotunjailurus01_ohead->1432677514
30050_Break_Acheron_F->1496006879
30050_Common_Acheron_F->851528469
3005_Sarcosuchus01_ohead->636869463
30080_Break_Talbot_F->-353055022
30080_Common_Talbot_F->833990417
30080_Skin107_Talbot_F->-1588114444
30080_Skin107_Talbot_O->-1921166476
3008_Talbothound01_ohead->-951286238
30100_Break_Pongo_F->-1331597269
30100_Common_Pongo_F->2060606875
3010_BNeotoma01_ohead->65021983
30120_Break_Siva_F->1673628590
30120_Common_Siva_F->341098786
3012_Sivapanthera01_ohead->-1124232145
30180_Break_Machairodus_F->905702261
30180_Common_Machairodus_F->1685714023
30180_Skin107_Machairodus_F->1690681418
30180_Skin107_Machairodus_O->-1117720949
3018_Machairodus01_ohead->-796524290
30200_Break_Direwolf_F->865030426
30200_Common_Direwolf_F->1912916690
30200_Skin101_Direwolf_F->-556675033
30200_Skin101_Direwolf_O->1857477554
3020_CanisRufus01_ohead->-1644459541
30220_Break_REX_F->2087629725
30220_Common_REX_F->-487890177
3022_REX01_ohead->-947874680
30230_Break_Sturnus_F->1795271809
30230_Common_Sturnus_F->-1417834409
30230_Sturnus01_ohead->-2078989623
30310_Break_Megaloceros_F->1210505276
30310_Common_Megaloceros_F->-638759562
3031_Megaloceros01_ohead->1973836677
30320_Break_Pelorovis_F->-19778064
30320_Common_Pelorovis_F->1625761826
30320_Common_Pelorovis_O->-796908617
30400_Break_Badlands_F->1658036280
30400_Common_Badlands_F->-121764602
30400_Common_Badlands_O->1060478855
30420_Break_Lynx_F->1865822246
30420_Common_Lynx_F->-1106629232
3042_Lynx01_ohead->-1785076742
30430_Break_Lepus_F->-620288754
30430_Common_Lepus_F->57259890
30430_Common_Lepus_O->1053956254
30431_Common_Lepus_F->1712229428
30431_Common_Lepus_O->1538597848
40010_Break_Hurricane_F->561670533
40010_Common_Hurricane_F->-1009089198
40010_Skin103_Hurricane_F->-1506379898
40010_Skin103_Hurricane_O->217859327
4001_Hurricane01_ohead->676125398
40030_Break_Frost_F->-399785561
40030_Common_Frost_F->968649657
40030_Frost01_ohead->-476227397
40040_Break_Prominence_F->558255103
40040_Common_Prominence_F->-1431550248
4004_Prominence01_ohead->-2023251270
40050_Break_Vortex_F->2108505715
40050_Common_Vortex_F->62901244
40050_Common_Vortex_O->-2145260103
4005_Vortex01_ohead->352459276
40060_Common_Mist_O->-459723901
40070_Break_Thunder_F->309815170
40070_Common_Thunder_F->-1396117073
40070_Thunder01_ohead->507004280
40120_ Hail01_ohead->1177828632
40120_Break_Hail_F->-1497223250
40120_Common_Hail_F->-1036532788
40140_Break_Rays_F->-423630704
40140_Common_Rays_F->-1682599372
4014_Rays01_ohead->1701897839
40150_Break_Rainbow_F->-1911112333
40150_Common_Rainbow_F->-382091580
40150_Common_Rainbow_O->-988567996
40190_Aurora01_ohead->-587486597
40190_Break_Aurora_F->-1006964031
40190_Common_Aurora_F->-480628329
40210_Break_Desert_F->-1506822171
40210_Common_Desert_F->1436798904
40210_Desert01_ohead->1402277785
40220_Break_Rapids_F->-54706003
40220_Common_Rapids_F->1297553235
40220_Rapids01_ohead->-194894148
40290_Break_Rain_F->76544320
40290_Common_Rain_F->742971999
40290_Skin114_Rain_F->1621558060
40290_Skin114_Rain_O->1562160320
4029_Rain01_ohead->-1609280027
40310_Break_Noctilucent_F->-1790703153
40310_Common_Noctilucent_F->1137392640
40310_Noctilucent01_ohead->574288946
40310_Skin116_Noctilucent_F->152506480
40310_Skin116_Noctilucent_O->-793624911
40320_Break_Bubble_F->-1891171439
40320_Common_Bubble_F->-1292445061
40320_Common_Bubble_O->828963902
40350_Break_Meteor_F->1491462070
40350_Common_Meteor_F->1768588868
40350_Common_Meteor_O->-353067007
40350_Skin105_Meteor_F->1238526006
40350_Skin105_Meteor_O->1710780598
50010_Break_Queenbee_F->-26824736
50010_Common_Queenbee_F->1868681727
50010_Common_QueenBee_O->-1461040258
50011_Break_Queenbee_F->-380712160
50011_Common_Queenbee_F->-200131797
50011_Synchro_QueenBee_O->-1638747010
50020_Beethorn01_ohead->479112602
50020_Break_Beethorn_F->-1056454301
50020_Common_Beethorn_F->2130388841
5002Beethorn01_ohead->-86817250
50030_Break_Stinger_F->39692384
50030_Common_Stinger_F->-1568064953
5003_Stinger01_ohead->-768019358
50040_Break_Silver_Feather_F->1309251073
50040_Common_Silver_Feather_F->1659323970
50040_Silver Feather01_ohead->-1148638473
50041_Common_Silver_Feather_F->31498086
50041_Common_SilverFeather_F->1128014561
50041_Silver Feather01_ohead->-1170417686
50060_Break_Atrophaneura_F->463711251
50060_Common_Atrophaneura_F->1394814528
5006_EdgeButterfly01_ohead->-42680192
50080_Break_Sandfly_F->586639124
50080_Common_Sandfly_F->1950614632
50080_Skin101_Sandfly_F->97101055
50080_Skin101_Sandfly_O->-1035846018
5008_Sandfly01_ohead->1657282404
50100_Break_Heliconius_F->-1019341696
50100_Common_Heliconius_F->1927175277
5010_Heliconius01_ohead->-1887753279
50130_Break_Morphidae_F->493154508
50130_Common_Morphidae_F->-1690950004
5013_Morphidae01_ohead->-1967106528
50140_Break_Wasp_F->-1214889663
50140_Common_Wasp_F->1187493361
5014_Wasp01_ohead->-284291406
50180_Break_Odonata_F->1178091270
50180_Common_Odonata_F->182309769
5018_Odonata01_ohead->829036726
50190_Break_Psilica_F->-1694389234
50190_Common_Psilica_F->1539296917
50190_Psilica01_ohead->-645511593
5019_Psilica01_ohead->-578639664
60020_Break_Joyeuse_F->-1576185836
60020_Common_Joyeuse_F->1228412812
60020_Skin101_Joyeuse_F->-1620109474
60020_Skin101_Joyeuse_O->1491373535
6002_Joyeuse01_ohead->-35447757
60030_Break_Durandal_F->-1457027422
60030_Common_Durandal_F->1296967520
60030_Skin103_Durandal_F->-2041900078
60030_Skin103_Durandal_O->908859463
6003_Durandal01_ohead->-312740488
60050_Break_Naglering_F->1789937366
60050_Common_Naglering_F->-992431587
60050_Common_Naglering_O->1958721928
60060_Break_Kusanagi_F->569988627
60060_Common_Kusanagi_F->-1231271954
6006_Murakumo01_ohead->1318161182
60070_Altachiara01_ohead->-1641979311
60070_Break_Altachiara_F->-956856062
60070_Common_Altachiara_F->1338218492
60080_Break_Clausolas_F->-1106550759
60080_Common_Clausolas_F->1483741782
6008_ClaimhSolais01_ohead->-8910736
60090_Break_Curtana_F->1243392551
60090_Common_Curtana_F->1464736996
6009_Courtain01_ohead->581486028
60110_Break_Burtgang_F->-1890436224
60110_Common_Burtgang_F->2067296397
60110_Skin102_Burtgang_F->362678629
60110_Skin102_Burtgang_O->-1510407440
6011_Burtgang01_ohead->1610974472
60140_Break_Geiboruga_F->-422366251
60140_Common_Geiboruga_F->780338350
60140_Common_Geiboruga_O->-1629221061
60190_Break_Fragarach_F->374435448
60190_Common_Fragarach_F->-1777150073
6019_Fragarach01_ohead->-1428853389
60210_Common_Longxian_O->-748755818
70010_Break_Zeus_F->-1648429157
70010_Common_Zeus_F->1083505727
70010_Common_Zeus_ohead->1615679475
70020_Variation_Zeus_F->1520212599
70020_Variation_Zeus_ohead->-2081730222
70030_Break_Poseidon_F->-188124111
70030_Common_Poseidon_F->-1724815323
70030_Poseidon01_ohead->-732560633
70040_Poseidon01_ohead->-1561355351
70040_Variation_Poseidon_F->-619557409
70050_Break_Hades_F->2032462941
70050_Common_Hades_F->-195670459
70050_Hades01_ohead->-1570285099
70050_Hades02_ohead->998588372
70051_Break_Hades_F->-1362727931
70051_Common_Hades_F->-1859029757
70051_Hades01_ohead->1971706253
70060_Hades01_ohead->231609375
70060_Variation_Hades_F->-139192987
70070_Athena01_ohead->-25627515
70070_Break_Athena_F->272323458
70070_Common_Athena_F->-917606005
70090_Break_Ares_F->-11825518
70090_Common_Ares_F->-1239724543
70090_Common_Ares_O->-1522968417
70100_Variation_Ares_F->1568360501
70100_Variation_Ares_O->1901154485
70110_Break_Hermes_F->629158294
70110_Common_Hermes_F->-194854195
70110_Common_Hermes_O->2013062280
70120_Variation_Hermes_F->343774694
70120_Variation_Hermes_O->-1541759373
70130_Break_Hera_F->1437736711
70130_Common_Hera_F->-866132986
70130_Hera01_ohead->1129662702
70140_Hera01_ohead->158057381
70140_Variation_Hera_F->-273917951
70220_Break_Loki_F->-517497834
70220_Common_Loki_F->519580448
7022_Loki01_ohead->-1860782371
70240_Break_Skadi_F->669090673
70240_Common_Skadi_F->-1699065524
70240_Common_Skadi_O->-1493041504
70250_Common_Skadi_O->953908542
70250_Variation_Skadi_F->-525676793
70250_Variation_Skadi_O->656496006
70260_Break_Thor_F->-1178272785
70260_Common_Thor_F->-509695390
7026_Thor01_ohead->-555132558
70280_Break_Gondul_F->1257757690
70280_Common_Gondul_F->-1060408076
7028_Gondul01_ohead->-404206559
70290_Break_Brynhild_F->1229892981
70290_Common_Brynhild_F->-1947059379
70290_Common_Brynhild_O->1283039692
70300_Variation_Brynhild_F->824091705
70300_Variation_Brynhild_O->846369835
71010_Break_Leader01_F->1998386003
71010_Common_Leader01_F->1826604600
7101_lead01_ohead->-1739091461
71020_Break_Leader02_F->806473971
71020_Common_Leader02_F->86603149
7102_ladylead01_ohead->216702803
80040_Common_Ripper_F->-704947917
8004_Ripper01_ohead->-341867049
80060_Common_Warlock_F->-203981377
8006_BloodWarlock01_ohead->1092684730
80110_Break_Schwarzritter_F->-1334405166
80110_Common_Schwarzritter_F->-900206315
8011_Dz00e02_ohead->1403190133
80130_Common_Legions_F->1336481132
8013_ForLegion01_ohead->-1665783612
80140_Common_LordThunder_F->-442661033
8014_KingThunder01_ohead->2143458327
80150_Common_Aegypius_F->927374428
8015_Aegypius01_ohead->-1776566123
80160_Common_Streptopelia_F->614812241
8016_Streptopelia01_ohead->-1373519744
80190_Common_OKA_F->-573746864
8019_OKA01_ohead->-358886791
80210_Common_Nidhogg_F->1703492014
8021_Nidhogg01_ohead->486741130
80240_Common_Schwarzritter_O->2084178761
80250_Common_Nebula_F->217601346
8025_Nebula01_ohead->954557069
80270_Common_Cordillera_F->1065157201
80270_Common_Cordillera_O->-1783156440
86130_Common_Legions_F->611482058
86130_Variation_Legions_O->-1755831881
86140_Common_LordThunder_F->1962694606
90010_Variation_SDLMα_F->-413650539
90020_Variation_SDLMβ_F->-480404133
90030_Variation_SDHMα_F->2127935410
90040_Variation_SDHMβ_F->-2123542137
90050_Common_TrapBomb_F->2112023374
90060_Common_DeclineBomb_F->1199660612
90070_Common_NarcoticBomb_F->-771684318
90080_Common_StunBomb_F->1903845595
90090_Common_SleepingBomb_F->734795855
90100_Common_SilentBomb_F->-59336541
90110_Common_FreezeBomb_F->-743188795
90120_Common_GravastarBomb_F->1260809651
90130_Common_AugmentationDevice_F->585728988
90140_Common_DeflectionDevice_F->-1782704800
90150_Common_DefenseDevice_F->-1780273982
90160_Common_BarrierDevice_F->354237344
90170_Common_ShieldingDevice_F->-742851407
90180_Common_RepairDevice_F->1973123056
90190_Common_SphericalRepairDevice_F->-1419688365
90200_Common_SlowTrap_F->1045445757
90210_Common_InterferenceTrap_F->73532939
90220_Common_TraumaTrap_F->1188339474
90230_Common_IncrementMatrix_F->-42086201
90240_Common_ImprisoningMatrix_F->1543409399
90250_Common_Trainer_F->-1892167537
90260_Common_Sentry_F->855343459
90300_Common_Guard_F->17825959
90350_Common_EagleGuardα_F->-791337538
90360_Common_EagleGuardβ_F->-471648252
90370_Common_WhiteComet_F->-2081867925
90380_Common_Inspector_F->-1853741370
90380_Common_Inspector_N->-1577947897
90400_Common_Chimera_F->-1706357500
90400_Common_Chimera_O->-1235151484
90410_Common_Puppet01_F->208455122
90420_Common_Puppet01_F->1416785146
90430_Common_Puppet01_F->-715716131
90440_Common_Puppet01_F->-464568662
90450_Common_Puppet01_F->1701469069
90460_Common_Puppet01_F->1031074469
90610_Common_Drasoul_F->1053268547
90610_Drasoul_ohead->898884248
90620_Common_Predator_F->-1006809170
90630_Common_Boundary_F->1029643758
90640_Common_Floater_F->880749162
90650_Common_Signa_F->-298724316
90660_Common_Wandering_F->1959016050
90670_Common_Aircraft_F->-2075692415
90700_Variation_Hades_F->-150851376
90710_Common_Thanatos01_F->-1568456945
90710_Thanatos01_ohead->1012634275
90720_Common_Hypnos01_F->554521541
90720_Hypnos01_ohead->-1667535559
90730_Common_ShapingBody01_F->1070888741
90760_Common_ShapingBody02_F->978703949
90770_Common_Frostguard01_F->-802271037
90780_Auditor01_ohead->-843233784
90780_Common_Censor_F->-274315631
90790_Common_BladeWolf01_F->899649197
90800_Common_TauntingDevice_F->-117252782
90840_Common_SDLMα_F->1245131263
90850_Common_SDLMβ_F->1828147106
90860_Common_SDHMα_F->1837914117
90870_Common_SDHMβ_F->1263281752
92010_Common_Thurses_F->444661015
92050_Common_Troll_F->520746612
92100_Common_Cruise_F->-1978385544
92150_Common_Gluttonous_F->-1924974263
92160_Common_Pestle_F->-240879270
92170_Common_Funnel_F->-902427390
92180_Common_Spider_F->-1286384232
92190_Common_Core_F->-1041706594
92200_Common_Annihilator_F->-629251534
92210_Common_Protector_F->1911272533
92220_Common_Sweeper_F->1121916379
92230_Common_Strike_F->1822865757
92240_Common_Concealment_F->1551976226
92250_Common_LuxiFire_F->-1903080540
92260_Common_LuxiCool_F->832188779
92280_Common_Ymir_F->1111744161
92280_Common_Ymir_O->1365362751
92291_Common_Vidar_F->-895048130
92291_Common_Vidar_O->-149091886
test_F->1739341194
60090_Skin101_Curtana_O->-1159894726
91130_Variation_Zeus_O->-1550029561
91130_Variation_Zeus_F->-1883867769
60090_Skin101_Curtana_F->2102850491
'''

numfiles_configs = []
for numfiles_config_cache in numfiles_configs_cache.split("\n"):
    if len(numfiles_config_cache.split("->")) >= 2:
        numfiles_configs.append(numfiles_config_cache.split("->")) # 转换成列表

# 获取 Custom 文件列表

with open(f'custom', 'r', encoding='utf-8') as custom_file: # 读取数据
    custom_cache = custom_file.read()

from tools.append_unique import append_unique
from tools.is_number import is_number

custom_files = []
for file in custom_cache.split("\n"):
    if file != "":
        if is_number(file):
            append_unique(custom_files, file)
        elif file[:14] == "prefabs_spine_":
            append_unique(custom_files, file)
        elif file[:24] == "textures_bigs_character_":
            append_unique(custom_files, file)
        elif file[:19] == "prefabs_characters_":
            append_unique(custom_files, file)
        elif file[:16] == "prefabs_effects_":
            append_unique(custom_files, file)
        elif file[:18] == "prefabs_dormitory_":
            append_unique(custom_files, file)