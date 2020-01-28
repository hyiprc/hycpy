rootname = "hycpy"

from .version import version as __version__

import pathlib, inspect
root = __import__(rootname)
rootdir = pathlib.Path(inspect.getfile(root)
          ).expanduser().resolve().absolute().parent
template = rootdir/'template'
cwd = pathlib.Path.cwd()


import logging, logging.handlers
handler = logging.handlers.WatchedFileHandler(__name__+'.log',delay=True)
formatter = logging.Formatter('\n%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
