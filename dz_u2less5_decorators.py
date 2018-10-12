# Create a function decorator that prints the name of the current running function by using the __name__ attribute.
# Make sure to also decorate some different functions to see that it works properly.


import operator


def deco_func(func):
    def repres_res(*args):
        result = func(*args)
        print("The name of current func is ", func.__name__)
        print(result, "is result of the function")

    return repres_res


@deco_func
def floor_div(a, b):
    return operator.floordiv(a, b)


@deco_func
def math_power(a, b):
    return operator.__pow__(a, b)


@deco_func
def negative(ob):
    return operator.__neg__(ob)


@deco_func
def check_if_contans(a, b):
    return operator.contains(a, b)


floor_div(50, 5)

math_power(50, 10)

negative(586)

check_if_contans('sonata mi major', 'Sonata')
