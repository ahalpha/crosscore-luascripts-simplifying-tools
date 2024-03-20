def dist_create(dist_, name_, new_item_):
    if not dist_.get(name_, False):
        dist_[name_] = ""
    dist_[name_] += new_item_
    return