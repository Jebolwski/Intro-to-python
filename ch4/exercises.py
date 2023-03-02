# !4.3
import math
import random


def cube(x):
    """Calculate the cube of x."""
    return x ** 3


# !4.4
"""
    Returns the sum of the even numbers in array
"""


def mystery(x):
    y = 0
    for i in x:
        if i % 2 == 0:
            y += i
    return y


# !4.6
def average(arr, *args):
    return sum(arr) / len(arr)


# !4.7
def messi():
    import datetime
    return datetime.datetime.today()


# !4.9
def radian(degrees):
    return (degrees * math.pi) / 180


# !4.10,4.11
def game():
    flag = False
    count = 0
    while not flag:
        randnum = random.randint(0, 9)
        randnum1 = random.randint(0, 9)
        result = input("What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
        if result == 'Q':
            flag = True
        elif int(result) == randnum * randnum1:
            print("True")
            count += 1
        else:
            print("Wrong! You guessed right", count, "time.")
            return


# !4.14
def game_guess():
    flag = False
    count = 0
    while not flag:
        randnum = random.randint(0, 9)
        randnum1 = random.randint(0, 9)
        result = float('inf')
        result = input("What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
        if result == 'Q':
            flag = True
        elif int(result) == randnum * randnum1:
            count += 1
        else:
            while int(result) != randnum * randnum1:
                result = input(
                    "Wrong! What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
                if result == 'Q':
                    flag = True
                elif int(result) == randnum * randnum1:
                    count += 1
                    break
    print("You guessed right", count, "times.")


# !4.16
def game_guess_diff():
    flag = False
    count = 0
    level = input("Enter diff level (Mid or Hard) : ")
    if level == "Mid":
        while not flag:
            randnum = random.randint(0, 9)
            randnum1 = random.randint(0, 9)
            result = float('inf')
            result = input("What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
            if result == 'Q':
                flag = True
            elif int(result) == randnum * randnum1:
                count += 1
            else:
                while int(result) != randnum * randnum1:
                    result = input(
                        "Wrong! What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
                    if result == 'Q':
                        flag = True
                    elif int(result) == randnum * randnum1:
                        count += 1
                        break
        print("You guessed right", count, "times.")
    elif level == "Hard":
        while not flag:
            randnum = random.randint(10, 100)
            randnum1 = random.randint(10, 100)
            result = float('inf')
            result = input("What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
            if result == 'Q':
                flag = True
            elif int(result) == randnum * randnum1:
                count += 1
            else:
                while int(result) != randnum * randnum1:
                    result = input(
                        "Wrong! What is the product of " + str(randnum) + " and " + str(randnum1) + " (to quit 'Q') : ")
                    if result == 'Q':
                        flag = True
                    elif int(result) == randnum * randnum1:
                        count += 1
                        break
        print("You guessed right", count, "times.")
    else:
        print("Wrong diff level.")


game_guess_diff()
