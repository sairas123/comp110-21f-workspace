"""Finding duplicate letters in a word."""

__author__ = "730439074"

word: str = input("Enter a word: ")

dup: bool = False

i: int = 0
while i < len(word):
    char =
    j: int = i + 1
    while j < len(word):