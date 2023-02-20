import math
#!2.1 - a
# x = 2
#!2.1 - b
# Value of 2 + 2 is 4
#!2.1 - c
# x =
#!2.1 - d
# 5 = 5

#!2.2
#? it will give an error because you can't multiply sequence by non-int of type 'str'

#!2.3
grade = int(input("Input a number between 1 and 10 : "))
if grade>=90:
    print("Congratulations! Your grade of", grade ,"earns you an A in this course")

#!2.4
"""
    Lefties: -5 0 5 7.5
    Righties: 2
"""
"""
    -5/2 = -2.5
    0/2 = 0
    5/2 = 2.5
    7.5/2 = 3.75

    -5+2 = -3
    0+2 = 2
    5+2 = 2.5
    7.5+2 = 3.75

    -5-2 = -7
    0-2 = -2
    5-2 = 3
    7.5-2 = 5.5

    -5*2 = -10
    0*2 = 0
    5*2 = 10
    7.5*2 = 15

    -5//2 = -3
    0//2 = 0
    5//2 = 2
    7.5//2 = 3

    -5**2 = 25
    0**2 = 0
    5**2 = 25
    7.5**2 = 56.25
"""

#!2.5
number=32
if number%2==0:
    print("Number is even")
else:    
    print("Number is odd")

#!2.6
marbles=22
if marbles/4==int(marbles/4):
    print("You can distribute")
else:   
    print("You cant distribute")

#!2.7
print(math.ceil(28/6),"boxes are nedded")
print("2 eggs nedded for the last box")

#!2.8
"""
    Formula : 200*2^n
"""
print("Hour      Number of Bacteria ")
print(0,"       ",200*(2**0))
print(5,"       ",200*(2**5))
print(10,"      ",200*(2**10))
print(15,"      ",200*(2**15))

#!2.9
tom='Tom'
jim='Jim'
if ord(tom[0])>ord(jim[0]):
    print('Tom goes first')
elif ord(tom[0])<ord(jim[0]):
    print('Jim goes first')
else:
    print('Both are same oredered, flip a coin')
