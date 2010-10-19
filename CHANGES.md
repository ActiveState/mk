# mk change log

## mk 0.7.2

- Add `mklib.mk` function that allows a task body to call another task with
  `mk(*task_names)`.


## mk 0.7.1

- Always load a Configuration module with cwd switched to the dir of the
  config file.


## mk 0.7.0

- Add support for a 'dir' attribute on a Configuration instance:
    class cfg(Configuration):
        dir = '..'  # will pick up config.py up on dir
  This can be useful for include'd makefiles.
- Add -F|--force option to force rebuilding of targets.
- Add "Alias" support (see tasks.py::Alias docstring for info).
- Change `mk -Tv` output to distinguish whether task dependencies are
  tasks or files. Also output task results.
- Add <File>.relpath attribute for convenience. (Remember that items in
  `deps' and `results' lists are often converted to File instances.)
- Add support for including makefiles: include(<path>[, <ns>]). As part of
  this is the ability to namespace tasks from included makefiles. E.g.:
    -- Makefile.py --------
    from mklib import Task, include
    include('bar/Makefile.py', 'bar')
    class build(Task):
        ...
    -- bar/Makefile.py ----
    from mklib import Task
    class build(Task):
        ...
    -- at the shell -------
    $ mk -Tv
    mk build
    mk bar:build
    -----------------------
- Add mklib.sh.touch() utility method.
- `mk -T FILTER` changes: FILTER is interpreted as a full "task query
  pattern" rather than a substring match against task names, FILTER of the
  form '/regex/flags' can be used to do a pattern match against task names
- Log mk output to stdout (instead of stderr) to allow for easier
  redirection.


(started maintaining this list 5 Oct 2007, mk v0.6)
