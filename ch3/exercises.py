# !3.1
def threedotone():
    find = 4
    faliures = 0
    while int(input("Enter number between 0 and 20 : ")) != find:
        faliures += 1
    print("Success! You failed " + str(faliures) + " times.")


# !3.2
def threedottwo():
    a = b = 7
    print('a =', a, '\nb =', b)


# !3.3
# ? >>>>>>>>>>>
# ? <<<<<<<<<<<
# ? >>>>>>>>>>>
# ? <<<<<<<<<<<
# ? >>>>>>>>>>>
# ? <<<<<<<<<<<
# ? >>>>>>>>>>>
# ? <<<<<<<<<<<
# ? >>>>>>>>>>>
# ? <<<<<<<<<<<

# !3.4
def threedotfour():
    for i in range(3):
        for j in range(3):
            print('0', end='')
        print()


# !3.6
def threedotsix():
    answer = input("What is your problem? ")
    while answer == '':
        answer = input("Have you had this problem before (yes or no)? ")
        if answer == "yes":
            print("Well, you have it again.")
            break
        elif answer == "no":
            print("Well, you have it now.")
            break


# !3.7
def threedotseven():
    """
        Formula : 200*2^n
    """
    print("Hour      Number of Bacteria ")
    for i in range(0, 16, 5):
        print(f"{i : >4}", " ", f"{200 * (2 ** i) : >21}")


# !3.8
def threedoteight():
    total = 0
    count = 0
    smallest = float('inf')
    biggest = float('-inf')
    while True:
        grade = int(input("Enter grade (-1 to exit) : "))
        if grade == -1:
            break
        total += grade
        count += 1
        if grade > biggest:
            biggest = grade
        if grade < smallest:
            smallest = grade

    average = total / count
    print("Total is :", total)
    print("Average is :", "%.2f" % average)
    print("Biggest is :", biggest)
    print("Smallest is :", smallest)


# !3.10
def threedotten():
    wage = 10
    for i in range(11):
        wage = wage * 1.03
        print(wage, i)


#!3.11
def threedoteleven():
    rabbitst=0
    colonyt=0
    while True:
        colony = int(input("Enter the number of does in the rabbit colony (-1 to end) : "))
        if colony == -1:
            break
        colonyt+=colony
        rabbits = int(input("Number of baby rabbits born in the past month : "))
        rabbitst+=rabbits
    print(rabbitst/colonyt)


#!3.12
def threedottwelve():
    first = int(input("First side : "))
    second = int(input("Second side : "))
    third = int(input("Third side : "))

    if second == first == third:
        print("Equilateral triangle")
    else:
        print("Not equilateral triangle")

