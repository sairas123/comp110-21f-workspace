"""Which Disney Princess are you?"""
def greet(greeting): 
    name: int = int(input("Hi, what is your name: "))
    return greeting + name 

print("Where would you like to buy a house?")
print(" a) Inside the forest")
print("b) In the city ")
print("c) In the mountains")
answer_1: int = int(input("Enter your answer: "))
print("What do you like to do on the weekend?")
print(" a) Read ")
print("b) Spend time outside ")
print("c) Hanging out with friends")
answer_2: int = int(input("Enter your answer: "))
print("Others are probably envious of: ")
print(" a) My looks ")
print("b) My passion ")
print("c) My voice ")
answer_3: int = int(input("Enter your answer: "))
print("What is your favorite holiday?")
print(" a) Christmas ")
print("b) I love all holidays ")
print("c) My birthday ")
answer_4: int = int(input("Enter your answer: "))
print("If you won a lottery, what is the first thing you would do with it?")
print(" a) Spend some and save the rest")
print("b) Go on a vacation ")
print("c) Buy a big house ")
answer_5: int = int(input("Enter your answer: "))
print("If you had superpowers, what would it be?")
print(" a) The ability to control water")
print("b) Be able to communicate with animals ")
print("c) Strength")
answer_6: int = int(input("Enter your answer: "))
print("What cake do you like?")
print(" a) Tres leche cake")
print("b) Rainbow cake ")
print("c) Red velvet cake")
answer_7: int = int(input("Enter your answer: "))
print("What is your favorite animal?")
print(" a) dolphin ")
print("b) Bear")
print("c) Deer")
answer_8: int = int(input("Enter your answer: "))

all_answer = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8]
a_total = 0
b_total = 0
c_total = 0
for answer in all_answer:
    if answer == " a ":
        a_total += 1
    else: answer == "["b":]"
        b_total += 1
    if answer == "c":
        c_total += 1
        if a_total > 5:
            print(" You are Belle")
        else
            print("You are Ariel")
        if c_total < 5:
            print("You are Snow White")
            