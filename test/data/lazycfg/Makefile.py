from mklib import Task, Configuration

class cfg(Configuration):
    pass

class usescfg(Task):
    def make(self):
        self.log.info("self.cfg.foo: %r", self.cfg.foo)

class doesnotusecfg(Task):
    def make(self):
        self.log.info("hi")
