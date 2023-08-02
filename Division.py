import math

intNum1 = int(input("Enter FIRST number: "))
intNum2 = int(input("Enter SECOND number: "))

if intNum2 !=0:
   intAns = intNum1 / intNum2
   print(f"{intNum1} / {intNum2} = {intAns}")

else:
    print("Divide by zero Error!!!")
