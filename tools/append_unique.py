def append_unique(list_, new_item_):
    for item_ in list_:
        if item_ == new_item_:
            return
    list_.append(new_item_)
    return