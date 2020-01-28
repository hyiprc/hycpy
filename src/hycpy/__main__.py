import sys
from . import __version__
  
def help():

    from textwrap import dedent
    print(dedent(f"""
    ---------------------------------------
    HycPy v{__version__}
        Henry's Python modules
    ---------------------------------------
    """))

if __name__ == '__main__':
    help()
