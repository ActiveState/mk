Note: There is a bug here that lazy cfg doesn't work: at least you
currently can't have a top-level `cfg` like this:

    from mklib import Configuration
    class cfg(Configuration):
        pass

without yet having "config.py".

