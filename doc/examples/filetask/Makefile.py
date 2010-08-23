from mklib import Task

class answer(Task):
    default = True
    deps = ["one.txt", "two.txt"]
    results = ["answer.txt"]
    def make(self):
        answer = 0
        for dep in self.deps:
            answer += int(open(dep.path).read().strip())
        self.log.info("answer is %r" % answer)
        open(self.results[0].path, 'w').write(str(answer))

