# print even/positive(ternary operator)
num1=12
print("even" if num1%2==0 else "odd")
print("positive" if num1>0 else "negative")

# print largest
num1=12
num2=15
print("num1" if num1>num2 else "num2")

# largest from 2 numbers
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print (num1-num2 if num1>num2 else num2-num1)