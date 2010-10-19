
# This is a Makefile for the `mk` tool. (Limited) details for that here:
# <http://github.com/ActiveState/mk>


import os
from os.path import join, dirname, normpath, abspath
import re

from mklib import Task
from mklib.sh import run_in_dir



class test(Task):
    """Run the full test suite."""
    def make(self):
        run_in_dir("python test.py", join(dirname(__file__), "test"))
        #TODO: consider adding Task.top (dir holding Makefile.py)



#---- internal support stuff

