from mklib import Task
class answer(Task):
    default = True
    deps = ["answer.txt"]
    def make(self):
        print "do answer"
