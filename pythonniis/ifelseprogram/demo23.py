#wap take a number from keyboard check no is sd dd td od +ve number
n = int(input("Enter a number: "))

if n > 0:
    if n < 10:
        print("Single digit number")
    elif n < 100:
        print("Double digit number")
    elif n < 1000:
        print("Triple digit number")
    else:
        print("Other digit number")
else:
    print("Not a positive number")