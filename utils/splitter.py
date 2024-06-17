def splitDictFoward(dict, position):
    items = list(dict.items())

    sub_items = items[position:]

    return dict(sub_items)

def splitDictBackward(dict, position):
    items = list(dict.items())

    sub_items = items[:position]

    return dict(sub_items)