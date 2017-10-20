import random
import sys
import builtins

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

def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins._ = None
    text = repr(offbyone(value))
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins._ = value

builtins.print = print_decorator(print)
sys.displayhook = displayhook
