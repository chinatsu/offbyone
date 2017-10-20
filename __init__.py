import random
import sys

def offbyone(item):
    coin = random.choice([-1, 1])
    if isinstance(item, bool):
        return not item
    if isinstance(item, (int, float)):
        return item + coin
    if isinstance(item, list):
        return list(map(offbyone, item))
    if isinstance(item, str):
        c = random.randint(0, len(item)-1)
        return "".join([chr(ord(l)+coin) if i == c else l for i, l in enumerate(item)])
    if isinstance(item, tuple):
        return tuple(offbyone(list(item)))
    if isinstance(item, dict):
        for x in item.keys():
            item[x] = offbyone(item[x])
        return item
    else:
        return item

def print_decorator(func):
    def wrapped_print(*args, **kwargs):
        return func(offbyone(*args), **kwargs)
    return wrapped_print

def displayhook(obj):
    if obj is not None:
        print(obj)

sys.displayhook = displayhook
globals()['__builtins__']['print'] = print_decorator(print)
