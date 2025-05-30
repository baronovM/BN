import sys

import os

INTERP = os.path.expanduser("/var/www/u3117157/data/www/nb-class.ru/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from app import app as application
