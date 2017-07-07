
from functools import wraps

def tags(tag):

    def inner_decorator(fun):

        @wraps(fun)
        def wrapper(*args, **kwargs):

            result = fun(*args, **kwargs)

            return f"<{tag}>{result}</{tag}>"

        return wrapper
    return inner_decorator


@tags("body")
@tags("div")
@tags("span")


def core_string(name, firstname):
    return f"Hello {firstname} {name} "

print(core_string("Marlena", "Filipkiewicz"))