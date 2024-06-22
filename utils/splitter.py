def splitDictFoward(dictionary, position):
    items = list(dictionary.items())

    sub_items = items[position:]

    return dict(sub_items)

def splitDictBackward(dictionary, position):
    items = list(dictionary.items())

    sub_items = items[:position]

    return dict(sub_items)