import inspect


def get_kwd_args(func):
    """
    Return a dict of keyword arguments.
    """
    try:
        sig = inspect.signature(func)
    except AttributeError:
        args, _, _, defaults = inspect.getargspec(func)
        if defaults:
            kwonlyargs = args[-len(defaults):]
        else:
            kwonlyargs = []
    else:
        kwonlyargs = {p.name:p.default for p in sig.parameters.values()
                      if p.default is not p.empty}

    return kwonlyargs