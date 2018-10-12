# Create a function that takes in 2 numbers and a mathematical function, that also takes 2 numbers as arguments,
# and then returns the result of the passed argument function given the 2 numbers.


import operator


def take1(a, b, f):
    """

    returns selected operation over two integers
    """
    return f(a, b)


def take_sub(a, b):
    return operator.__sub__(a, b)


def take_pow(a, b):
    return operator.pow(b, a)


print(take1(2, 3, take_sub))

print(take1(4, 3, take_pow))


