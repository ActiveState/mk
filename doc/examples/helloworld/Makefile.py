
"""Hello, World for 'do'."""

from mklib import Task

class default(Task):
    default = True
    deps = ["hello", "bye"]

class hello(Task):
    "say hi"
    def make(self):
        print "Hello, World!"

class bye(Task):
    "say bye"
    def make(self):
        print "Bye bye."
