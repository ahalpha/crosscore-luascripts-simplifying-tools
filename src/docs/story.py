import os
import re
from tqdm import tqdm
from tools import *
from src.configs import *
from .story_id import story_id

# 侧栏
configs_text = f'''import type {{ DefaultTheme }} from 'vitepress'

export const story: DefaultTheme.SidebarItem[] = [
__configs__
]
'''

# 索引
index_text =f'''
# 剧情
主线剧情或限时剧情中的场景。

__index__

'''

# 列表
lists_text = f'''
# 剧情
主线剧情或限时剧情等对话收集。

__lists__

'''

# 索引列表
index_lists_text = f'''
## [**剧情**](illvstration_story)
主线剧情或限时剧情中的场景。

__index_lists__

'''

# 导出剧情
def story_main():
    docs_text = {}
    used_list = []

    os.makedirs(f"{configs_general.docs_dir}/story/sid", exist_ok=True)
    os.makedirs(f"./story_text/", exist_ok=True)
    print("> Story Spawn Docs:")
    for a in tqdm(os.listdir("data/story")):
        sid = a.split('.')[0]

        cache = story_id(a)
        write_files(f"{configs_general.docs_dir}/story/sid/{sid}.md", cache[0])
        dist_create(docs_text, "configs", cache[1]+"\n")
        dist_create(docs_text, "index", cache[3]+"\n\n")
        dist_create(docs_text, "lists", cache[4]+" ")
        dist_create(docs_text, "index_lists", cache[5]+" ")
        write_files(f"./story_text/{sid}.txt", cache[2])
        append_unique(used_list, cache[6])

    # 生成文档
    def spawn_docs(docs): # index_list
        cache = {}
        exec(f"text = {docs}_text", globals(), cache)
        cache = cache["text"]
        names = re.findall('__(.*?)__', cache)
        for name in names:
            cache = cache.replace("__" + name + "__", docs_text.get(name, "")[:-1])
        return cache

    # 生成侧栏文档
    if configs_general.enable_export_configs:
        os.makedirs(f"{configs_general.configs_dir}", exist_ok=True)
        write_files(f"{configs_general.configs_dir}/story.mts", spawn_docs("configs"))

    # 生成索引文档
    os.makedirs(f"{configs_general.index_dir}", exist_ok=True)
    write_files(f"{configs_general.index_dir}/illvstration_story.md", spawn_docs("index"))

    # 生成列表文档
    write_files(f"{configs_general.docs_dir}/story/index.md", spawn_docs("lists"))

    # 生成索引列表文档
    write_files(f"{configs_general.index_dir}/_illvstration_story.md", spawn_docs("index_lists"))

    return used_list