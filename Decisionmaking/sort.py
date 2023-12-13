# sort 3 numbers in ascending order
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if (num1>num2 and num1>num3):
    if (num2>num3):
        print(f"number in ascending order is {num1},{num2},{num3}")
    else:
        print(f"number in ascending order is {num1},{num3},{num2}")
elif (num2>num1 and num2>num3):
    if (num1>num3):
        print(f"number in ascending order is {num2},{num1},{num3}")
    else:
        print(f"number in ascending order is {num2},{num3},{num1}")
elif (num3>num1 and num3>num2):
    if (num1>num2):
        print(f"number in ascending order is {num3},{num1},{num2}")
    else:
        print(f"number in ascending order is {num3},{num2},{num1}")
elif (num1==num2 and num2==num3):
    print("All numbers are same")


        