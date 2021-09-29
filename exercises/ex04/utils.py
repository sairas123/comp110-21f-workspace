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


__author__ = "730439074"

def is_equal(a:list[int], b: list[int]) -> bool:  

    while a == b: 
        print(True)
    else:
        print(False)