num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

small_num=num1 if num1<num2 else num2

factor=1
i=1
while(i<=small_num):
    if (num1%i==0 and num2%i==0):
        factor=i
    i+=1
print(f"{factor} is the hcf") #gcd



