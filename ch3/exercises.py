
#!3.1
find=4
faliures=0
while int(input("Enter number between 0 and 20 : "))!=find:
    faliures+=1
print("Success! You failed "+str(faliures)+" times.")

#!3.2
a = b = 7
print('a =', a, '\nb =', b)

#!3.3
#? >>>>>>>>>>>
#? <<<<<<<<<<<
#? >>>>>>>>>>>
#? <<<<<<<<<<<
#? >>>>>>>>>>>
#? <<<<<<<<<<<
#? >>>>>>>>>>>
#? <<<<<<<<<<<
#? >>>>>>>>>>>
#? <<<<<<<<<<<

#!3.4
for i in range(3):
    for i in range(3):
        print('0', end='')
    print()

#!3.6
answer = input("What is your problem? ")
while answer=='':
    answer = input("Have you had this problem before (yes or no)? ")
    if answer=="yes":
        print("Well, you have it again.")
        break
    elif answer=="no":
        print("Well, you have it now.")
        break

#!3.7
"""
    Formula : 200*2^n
"""
print("Hour      Number of Bacteria ")
for i in range(0,16,5):
    print(f"{i : >4}"," ",f"{200*(2**i) : >21}")
