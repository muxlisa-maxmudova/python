from contextlib import nullcontext


def greeting(name=None): # allows to handle missing params
    if name is None:
        print('Hello, everyone!')
    else:
        print(f'Hello, {name}')

greeting()