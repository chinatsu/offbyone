import random
import sys

def offbyone(item):
    if isinstance(item, bool):
        return not item
    if isinstance(item, (int, float)):
        return item + random.choice([-1, 1])
    if isinstance(item, list):
        return [x+random.choice([-1, 1]) for x in item]
    if isinstance(item, str):
        c = random.randint(0, len(item))
        newitem = ""
        for i, x in enumerate(item):
            if i == c:
                x = chr(ord(x)+random.choice([-1, 1]))
            newitem += x
        return newitem
    if isinstance(item, tuple):
        a = offbyone(list(item))
        return tuple(a)
    if isinstance(item, dict):
        for x in item.keys():
            item[x] = offbyone(item[x])
        return item
    else:
        return item

def displayhook(obj):
    if obj is not None:
        print(offbyone(obj))

sys.displayhook = displayhook
