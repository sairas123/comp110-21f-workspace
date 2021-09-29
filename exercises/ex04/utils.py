"""List utility functions."""
__author__ = "730439074"

# TODO: Implement your functions here.

"""Exercise all to practice built-in len function."""


def all(x:list[int], y: int) -> bool:  

    if len(x) == y:
        return True
    return False


"""Exercise on deep equality and comparing two lists."""


__author__ = "730439074"

def is_equal(x:list[int], y: list[int]) -> bool:  

    if x == y: 
        print(True)
    else:
        print(False)