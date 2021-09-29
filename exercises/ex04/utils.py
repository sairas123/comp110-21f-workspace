"""List utility functions."""


__author__ = "730439074"

# TODO: Implement your functions here.

"""Exercise all to practice built-in len function."""


def all(x:list[int], y: int) -> bool:  

    while len(x) == y:
        return True
    else:
        return False


"""Exercise on deep equality and comparing two lists."""


def is_equal(a:list[int], b: list[int]) -> bool:  

    while a == b: 
        return True
    else:
        return False


"""Exercise max on our own"""


def max(x:list[int]) -> int:  
    max_number = max(x)
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        print(max_number)