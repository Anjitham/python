# print largest number from 2 number

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    print(f"{num1} is greatest")
elif num2>num1:
    print(f"{num2} is greatest")
else:
    print("Both numbers are same")