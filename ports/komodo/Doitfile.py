
"""Komodo build file."""

import os
import sys
from os.path import abspath, exists, join, dirname, basename
from pprint import pprint
import urllib

from doitlib import Task, File, Configuration
from doitlib.sh import run, run_in_dir, rm, mkdir


class cfg(Configuration):
    prefix = "ko"



class debug(Task):
    def doit(self):
        self.log.info("cfg is %r", self.cfg)

class src(Task):
    results = ["src/src/version.txt"] # just a landmark
    def doit(self):
        self._get_from_p4()
    def _get_from_p4(self):
        # Just get the smaller "util" tree for now.
        p4plat = sys.platform == "win32" and "p4win" or "p4unix"
        url = "http://tl.activestate.com/%s/depot/main/Apps/Komodo-devel/util.tar.gz" % p4plat
        if exists("src"):
            rm("src", self.log)
        mkdir("src", log=self.log)
        self.log.info("download source from p4")
        tarball = join("src", "komodo.tar.gz")
        urllib.urlretrieve(url, tarball)
        run_in_dir("tar xzf %s" % basename(tarball), "src")
        

class build(Task):
    default = True
    deps = ["src"]

