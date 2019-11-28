from utils.Signatures import get_kwd_args #For function signature

def block_none_or_empty_arguments(func):
    """Protect of overwritting default arguments to set none or empty"""
    default_keyword = get_kwd_args(func) #Store signature keyword arguments

    def wrapper(*args, **kwargs):

        #Check if some of inserted arguments are empty
        for key in kwargs:
            if kwargs[key] == "" or kwargs[key] == None:
                if key in default_keyword:
                    kwargs[key] = default_keyword[key]

        return func(*args, **kwargs)
    return wrapper


def block_argument(*blocked_args):
    """Protect whatever type of argument to overwrite default arguments in function"""
    def block_args(func):
        default_keyword = get_kwd_args(func) #Store signature keyword arguments

        def wrapper(*args, **kwargs):

            #Check if some of inserted arguments are empty
            for key in kwargs:
                if kwargs[key] in blocked_args:
                    if key in default_keyword:
                        kwargs[key] = default_keyword[key]

            return func(*args, **kwargs)
        return wrapper
    return block_args
