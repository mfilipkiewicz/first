

def tags(tag):

    def inner_decorator(fun):

        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            return result

        return wrapper



#@tags("div")
#@tags("span")

def print_core_string(name):
    return "Hello"

print_core_string