"""wap take emp salary from keyboard if sal>5000 da=30% hra=20% then display basic salary da hra and totalsal""" 
sal = float(input("Enter basic salary: "))
da = sal*0.30 if sal>5000 else 0
hra = sal*0.20 if sal>5000 else 0
print("Basic Salary =", sal)
print("DA =", da)
print("HRA =", hra)
print("Total Salary =", sal+da+hra)