import os
from os.path import join, exists
from mklib import include, Task

include("subdir/Makefile.py")

class clean(Task):
    "clean up for test"
    def make(self):
        to_del = ["answer.tmp",
                  join("subdir", "answer.tmp")]
        for path in to_del:
            if exists(path):
                os.remove(path)
