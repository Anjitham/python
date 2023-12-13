num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

if (num1>num2 and num1>num3):
    print(f"{num1}is greatest")
    if (num2>num3):
        print(f"{num2} is second largest")
    else:
        print(f"{num3} is second largest")
elif (num2>num1 and num2>num3):
    print(f"{num2} is greatest")
    if (num1>num3):
        print(f"{num1} is second largest")
    else:
        print(f"{num3} is second largest")

elif (num3>num1 and num3>num2):
    print(f"{num3}is greatest")
    if (num1>num2):
        print(f"{num1} is second largest")
    else:
        print(f"{num2} is second largest")
elif (num1==num2 and num2==num3):
    print("All numbers are same")