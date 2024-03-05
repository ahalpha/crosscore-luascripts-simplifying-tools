from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)

def read_lua_excel(files):
    try:
        excel_dist = {}
        with open(f"./luascripts/{files}", "r", encoding="utf-8") as data_files: # 读取数据
            lua_table = lua.eval(f"function() {data_files.read()} end")
        
        lua_table_names = list(lua_table()["names"].values())
        lua_table_data_tbs = list(lua_table()["data"].values())

        lua_table_names=[v + str(lua_table_names[:i].count(v) + 1) if lua_table_names.count(v) > 1 else v for i, v in enumerate(lua_table_names)]

        for lua_table_data_tb in lua_table_data_tbs:
            lua_table_data = list(lua_table_data_tb.values())
            excel_dist[lua_table_data[0]] = {}
            for i in range(len(lua_table_names)):
                excel_dist[lua_table_data[0]][lua_table_names[i]] = lua_table_data[i]
    
        return excel_dist
    
    except:
        print("[WARN] 未能加载文件: \"{files}\"")
        return False

def read_lua_excel_id(files):
    try:
        excel_dist = {}
        with open(f"./luascripts/{files}", "r", encoding="utf-8") as data_files: # 读取数据
            lua_table = lua.eval(f"function() {data_files.read()} end")
        
        lua_table_names = list(lua_table()["names"].values())
        lua_table_data_tbs = list(lua_table()["data"].values())

        lua_table_names=[v + str(lua_table_names[:i].count(v) + 1) if lua_table_names.count(v) > 1 else v for i, v in enumerate(lua_table_names)]

        for i in range(len(lua_table_data_tbs)):
            lua_table_data = list(lua_table_data_tbs[i].values())
            excel_dist[i] = {}
            for j in range(len(lua_table_names)):
                excel_dist[i][lua_table_names[j]] = lua_table_data[j]
    
        return excel_dist
    
    except:
        print("[WARN] 未能加载文件: \"{files}\"")
        return False