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

#!2.10
#TODO Coruse 1
max_c1=float('-inf')
min_c1=float('inf')
total_grades_c1=0
total_students_c1=0
num=int(input("Enter course 1's grades : "))
while False:
    num=int(input("Enter course 1's grades : "))
    if not 100>num>0:
        break
    if num>max_c1:
        max_c1=num
    if num<min_c1:
        min_c1=num
    total_grades_c1+=num
    total_students_c1+=1

#TODO Coruse 2
max_c2=float('-inf')
min_c2=float('inf')
total_grades_c2=0
total_students_c2=0
num=int(input("Enter course 2's grades : "))
while False:
    num=int(input("Enter course 2's grades : "))
    if not 100>num>0:
        break
    if num>max_c2:
        max_c2=num
    if num<min_c2:
        min_c2=num
    total_grades_c2+=num
    total_students_c2+=1


#TODO Coruse 3
max_c3=float('-inf')
min_c3=float('inf')
total_grades_c3=0
total_students_c3=0
num=int(input("Enter course 3's grades : "))
while False:
    num=int(input("Enter course 3's grades : "))
    if not 100>num>0:
        break
    if num>max_c3:
        max_c3=num
    if num<min_c3:
        min_c3=num
    total_grades_c3+=num
    total_students_c3+=1

# print("---Averages---")
# print("Course 1 : ",total_grades_c1/total_students_c1)
# print("Course 2 : ",total_grades_c2/total_students_c2)
# print("Course 3 : ",total_grades_c3/total_students_c3)
      
# print("--Max--Min--")
# print("Max grade out of all of them : ",max(max_c1,max_c2,max_c3))
# print("Min grade out of all of them : ",min(min_c1,min_c2,min_c3))

#!2.11
seconds=int(input("Seconds : "))
hour=seconds//3600
seconds-=hour*3600
minutes=seconds//60
seconds-=minutes*60
print("Hours : ",hour)
print("Minutes : ",minutes)
print("Seconds : ",seconds)

#!2.12
hourly_wage=10
for i in range(5):
    hourly_wage=hourly_wage*1.03
for i in range(2):
    hourly_wage=hourly_wage*0.97
print(hourly_wage)

#!2.13
"""
    It accepts till 2000 at the least
"""
try:
    i=0
    while i<10:
        i+=1
        num=2**i 
        print(num)
except:
    print("Error")

#!2.14
"""
    Formula = 220 - age
"""
age = int(input("Your Age : "))
maximum_heart_rate=220-age
prefered=str(maximum_heart_rate*0.5)+"-"+str(maximum_heart_rate*0.85)
print("Your prefered heart rate per minute is :",prefered)

#!2.15
runner1=int(input("Runner 1 : "))
runner2=int(input("Runner 2 : "))
runner3=int(input("Runner 3 : "))
print("Increasing order")
if runner1>runner2:
    if runner2>runner3:
        print(runner3,runner2,runner1)
    elif runner2<runner3:
        if runner1>runner3:
            print(runner2,runner3,runner1)
        else:
            print(runner2,runner1,runner3)
else:
    if runner3>runner2:
        print(runner1,runner2,runner3)
    else:
        if runner1>runner3:
            print(runner3,runner1,runner2)
        else:
            print(runner1,runner3,runner2)