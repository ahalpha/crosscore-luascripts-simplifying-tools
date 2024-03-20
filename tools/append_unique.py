def append_unique(list_, new_item_):
    if isinstance(new_item_, int) or isinstance(new_item_, float) or isinstance(new_item_, str):
        if new_item_ not in list_:
            list_.append(new_item_)
    elif isinstance(new_item_, list):
        for item_ in new_item_:
            append_unique(list_, item_)
    else:
        print(f"[WARN] append_unique: Unknown Type - {type(new_item_)}")
    return list_