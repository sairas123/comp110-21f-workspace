"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730439074"
"""Tests for the only evens function. """

from exercises.ex05.utils import only_evens

def test_only_evens_empty() -> None:
    x:list[int] = []
    assert only_evens(x) == 0
def test_only_evens_one() -> None:
    x:list[int] = [1, 2, 3, 4 ]
    assert only_evens(x) == 2

def test_only_evens_two() -> None:
    x:list[int] = []
    assert only_evens(x) == 2
 




"""Tests for the sub function"""


def test_sub_empty() -> None:
    x:list[int] = []
    assert sub(x) == 0

def test_sub_one() -> None:
    x:list[int] = [10,20,30 ]
    assert sub(x) == 10,30

def test_sub_two() -> None:
    x:list[int] = []
    assert sub(-10, 10, -20, 20) == 0






"""Tests for the Concat Function."""


def test_concat_empty() -> None:
    xs:list[int] = []
    ys:list[int] = []
    assert concat(xs, ys) == 0

def test_concat_one() -> None:
    xs:list[int] = [1,2,2,3,4]
    ys:list[int] = [1,2,3,3,4]
    assert concat(xs,ys) == 2,3

def test_concat_two() -> None:
    xs:list[int] = [-1,-1,-2,2]
    ys:list[int] = [-2,-2,3,4]
    assert concat(xs,ys) == -1,-2
