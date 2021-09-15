"""An exercise in remainders and boolean logic."""

__author__ = "730439074"


# Begin your solution here...
# if x is evely divisible by 2
# if x is evenly divisble by 7
# if x is evenly divisble by both 2 and 7
x: int = int(input("Enter an int: "))
a = (x % 2)
b = (x % 7)

if a == 0:
    print("TAR")
else:
    if b == 0:
        print("HEELS")
    else:
        if (a == 0) and (b == 0):
            print("TAR HEELS") 
        else:
            print("CAROLINA")