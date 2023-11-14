def deduplicate_input(f):
    """Takes in a function f that takes a variable number of arguments
    possibly with duplicates, returns a decorator that removes duplicates
    in the positional argument."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        no_dupes = set(args)
        new_func = f(*no_dupes, **kwargs)
        return new_func
    return wrapper



