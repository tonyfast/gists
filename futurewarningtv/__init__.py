def load_ipython_extension(shell):
    with __import__('importnb').Notebook(): ...
def unload_ipython_extension(shell):
    with __import__('importnb').Notebook(): ...

with __import__('importnb').Notebook(lazy=True):
    from . import *