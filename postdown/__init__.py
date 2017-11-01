import sys

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')

from .ctor import MDDoc
from .parser import parse

__author__ = 'Titor'
__version__ = '1.0.11'

