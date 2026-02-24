#wap take 3 number on keyboard display biggest number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a>=b and a>=c:
    print("Biggest number =", a)
elif b>=a and b>=c:
    print("Biggest number =", b)
else:
    print("Biggest number =", c)