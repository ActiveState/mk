from os.path import join
from mklib import Task, File
from mklib.sh import touch

class answer(Task):
    "touch answer.tmp"
    results = ["answer.tmp"]
    def make(self):
        touch(join(self.dir, "answer.tmp"))

class answer_tmp(File):
    path = "answer.tmp"
    deps = ["question.txt"]

