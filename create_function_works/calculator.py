num1=int(input("number 1:"))
num2=int(input("number 2:"))


def add(num1,num2):
    res=num1+num2
    return res
print(f"result of addition {add(num1,num2)}")

def sub(num1,num2):
    res=num1-num2 if num1>num2 else num2-num1
    return res
print(f"subtraction result is {sub(num1,num2)}")

def mul(num1,num2):
    res=num1*num2
    return res
print(f"multiplication result is {mul(num1,num2)}")

def div(num1,num2):
    res=num1/num2
    return res
print(f"division result is {div(num1,num2)}")