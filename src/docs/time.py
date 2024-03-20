import time
from tools import *
from src.configs import *

def time_main():
    t = time.strftime('%Y-%m-%d %H:%M', time.localtime())
    cache = f'''
::: info

请注意，本文章截至最后一次更新此资源文件索引的内容的时间为 `{t}` ，此时交错战线的最新版本为 `{configs_general.game_version}` 。

:::
'''
    write_files(f"{configs_general.index_dir}/time.md", cache[1:][:-1])