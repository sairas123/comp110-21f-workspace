"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730439074"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Pick a number between 1-4")
fortune_num = (randint(1, 4))


fortune_1 = "I am worth a fortune"
fortune_2 = "The fortune you seek is in another cookie"
fortune_3 = "An alien of some sort will be appearing to you shortly"
fortune_4 = "You can always find happiness at work on Friday"

if (fortune_num == 1): 
    print("your fortune cookie says..." + fortune_1)
else: 
    print(fortune_2)

if (fortune_num == 3):
    print(fortune_3)
else:
    print(fortune_4)



