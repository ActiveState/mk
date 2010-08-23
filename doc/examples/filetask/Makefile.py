from os.path import exists, dirname
import os
from mklib import Task

class answer(Task):
    default = True
    deps = ["one.txt", "two.txt"]
    results = ["tmp/answer.txt"]
    def make(self):
        answer = 0
        for dep in self.deps:
            answer += int(open(dep.path).read().strip())
        self.log.info("answer is %r" % answer)

        result = self.results[0].path
        if not exists(dirname(result)):
            os.mkdir(dirname(result))
        open(result, 'w').write(str(answer))

